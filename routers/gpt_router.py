import os

from aiogram import F
from aiogram import Router
from aiogram.types import Message
from openai import AsyncOpenAI

# Create a separate Router for description
gpt_router = Router()

client = AsyncOpenAI(api_key=os.getenv('OPENAI_APIKEY'))


async def get_gpt_response(user_question: str) -> str:
    """
    Accesses the OpenAI API and receives a response from the model.
    """
    try:
        response = await client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_question}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error when requesting OpenAI API: {e}"


@gpt_router.message(F.text.startswith('/gpt'))
async def handle_gpt_command(message: Message):
    """
    Processes the /gpt command and responds to the user.
    """
    # Extracting the question from the command
    user_question = message.text.lstrip('/gpt').strip()
    if not user_question:
        await message.answer("Please write a question after the command /gpt.")
        return

    await message.answer("Thinking about the answer....")
    gpt_response = await get_gpt_response(user_question)
    await message.answer(gpt_response)
