import os
from typing import Tuple

from openai import AsyncOpenAI

# Config
DEFAULT_PROVIDER = (os.getenv("DEFAULT_PROVIDER") or "OPENAI").upper()  # OPENAI | DEEPSEEK
INSTRUCTIONS = os.getenv("INSTRUCTIONS")

# OpenAI
OPENAI_APIKEY = os.getenv("OPENAI_APIKEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL") or "gpt-4o-mini"

# DeepSeek
DEEPSEEK_APIKEY = os.getenv("DEEPSEEK_APIKEY")
DEEPSEEK_MODEL = os.getenv("DEEPSEEK_MODEL") or "deepseek-chat"
DEEPSEEK_BASE_URL = os.getenv("DEEPSEEK_BASE_URL") or "https://api.deepseek.com"

client = AsyncOpenAI(api_key=os.getenv('DEEPSEEK_APIKEY'), base_url="https://api.deepseek.com")

_openai_client: AsyncOpenAI | None = None
_deepseek_client: AsyncOpenAI | None = None


def _get_openai() -> Tuple[AsyncOpenAI, str]:
    global _openai_client
    if not OPENAI_APIKEY:
        raise RuntimeError("OPENAI_APIKEY не задан в окружении.")
    if _openai_client is None:
        _openai_client = AsyncOpenAI(api_key=OPENAI_APIKEY)
    return _openai_client, OPENAI_MODEL


def _get_deepseek() -> Tuple[AsyncOpenAI, str]:
    global _deepseek_client
    if not DEEPSEEK_APIKEY:
        raise RuntimeError("DEEPSEEK_APIKEY не задан в окружении.")
    if _deepseek_client is None:
        _deepseek_client = AsyncOpenAI(api_key=DEEPSEEK_APIKEY, base_url=DEEPSEEK_BASE_URL)
    return _deepseek_client, DEEPSEEK_MODEL


async def _ask(provider: str, user_question: str) -> str:
    messages = [
        {"role": "system", "content": INSTRUCTIONS},
        {"role": "user", "content": user_question},
    ]

    if provider == "OPENAI":
        client, model = _get_openai()
    elif provider == "DEEPSEEK":
        client, model = _get_deepseek()
    else:
        raise ValueError(f"Неизвестный провайдер: {provider}")

    resp = await client.chat.completions.create(
        model=model,
        messages=messages,
        stream=False,
        temperature=0.3,
    )
    return resp.choices[0].message.content or ""


async def get_ai_response(user_question: str) -> Tuple[str, str]:
    primary = "OPENAI" if DEFAULT_PROVIDER != "DEEPSEEK" else "DEEPSEEK"
    secondary = "DEEPSEEK" if primary == "OPENAI" else "OPENAI"

    try:
        text = await _ask(primary, user_question)
        return text, primary
    except Exception as e_primary:
        try:
            text = await _ask(secondary, user_question)
            return text, secondary
        except Exception as e_secondary:
            raise RuntimeError(
                f"Оба провайдера недоступны или произошла ошибка. "
                f"{primary}: {e_primary}; {secondary}: {e_secondary}"
            )
