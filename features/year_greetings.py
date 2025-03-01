import random
import datetime

year_now = datetime.datetime.now().year

year_greeting = [
    f'С Новым годом, друг! Пусть каждый день {year_now} года будет наполнен радостью и успехом!',
    f'Желаю тебе в этом году только удачи, здоровья и исполнения всех заветных желаний!',
    f'Пусть этот год принесет больше приключений, ярких моментов и счастливых дней!',
    f'С Новым годом! Пусть все твои начинания в {year_now} году увенчаются успехом!',
    f'Желаю тебе крепкого здоровья, большого счастья и неиссякаемой энергии!',
    f'Пусть этот год подарит тебе больше поводов для смеха и радости!',
    f'С новым счастьем! Пусть {year_now} станет для тебя лучшим годом в жизни!',
    f'Пусть в этом году сбудутся все твои мечты и задуманные планы!',
    f'С Новым годом! Пусть вокруг тебя всегда будут только добрые и искренние люди!',
    f'Желаю тебе в этом году бесконечных возможностей и удачи во всех делах!',
    f'Пусть {year_now} год будет полон неожиданных радостей и приятных сюрпризов!',
    f'Счастья, любви и тепла в новом году, дорогой друг!',
    f'Пусть в {year_now} году все неприятности останутся в прошлом, а впереди будет только светлое будущее!',
    f'С Новым годом! Пусть твой дом будет полон смеха, любви и уюта!',
    f'Желаю в этом году достичь новых вершин и насладиться каждым моментом!',
    f'Пусть {year_now} год станет годом больших свершений и исполненных желаний!',
    f'С Новым годом! Пусть в твоей жизни будет больше добрых чудес!',
    f'Желаю в этом году встретить только радостные события и добрых людей!',
    f'Счастья, здоровья и удачи в новом году! Пусть он принесет много хорошего!',
    f'Пусть все мечты, загаданные под бой курантов, сбудутся в этом году!',
    f'С Новым годом! Пусть каждый день будет наполнен улыбками и радостью!',
    f'Желаю, чтобы {year_now} год стал для тебя годом побед и новых открытий!',
    f'С новым счастьем, друг! Пусть этот год будет щедрым на добрые моменты!',
    f'Пусть твоя жизнь в {year_now} году станет еще ярче и лучше!',
    f'С Новым годом! Желаю в этом году наслаждаться каждым днем!',
    f'Пусть код в твоей жизни всегда компилится с первого раза!',
    f'С Новым годом! Пусть твой баг-репорт станет списком новых возможностей!',
    f'Желаю, чтобы {year_now} год принес тебе больше оперативной памяти и меньше зависаний!',
    f'Пусть твои апдейты всегда проходят без ошибок и с радостью!',
    f'С Новым годом! Пусть этот год будет полон инноваций и апгрейдов!',
    f'Желаю тебе в этом году идеального баланса между работой и отдыхом!',
    f'Пусть твой жизненный проект будет успешным на всех стадиях!',
    f'С новым счастьем! Пусть твои pull requests всегда принимаются без конфликтов!',
    f'Пусть в {year_now} году ты найдешь больше возможностей для креативного кодинга!',
    f'С Новым годом! Пусть твои алгоритмы всегда находят самое оптимальное решение!',
    f'Желаю в этом году больше времени на кофе и меньше на дебаг!',
    f'Пусть в {year_now} году каждое твое приложение будет загружаться мгновенно!',
    f'С Новым годом! Пусть твой жизненный сервер всегда работает без сбоев!',
    f'Желаю, чтобы в этом году твой чат-бот стал еще умнее!',
    f'Пусть твой год будет таким же светлым, как темная тема IDE!',
    f'С Новым годом! Пусть твой код будет лаконичным, а жизнь насыщенной!',
    f'Желаю, чтобы {year_now} год принес тебе идеальные логические условия и полный синтаксический порядок!',
    f'Пусть твоя сеть связей становится только шире, а потери пакетов — меньше!',
    f'С Новым годом! Пусть каждый день будет как успешно выполненный тест!',
    f'Желаю тебе в этом году больше свободного места на диске и меньше ошибок в коде!',
    f'Пусть {year_now} год принесет тебе больше времени на творчество и меньше на исправления!',
    f'С Новым годом! Пусть твоих «404» будет как можно меньше!',
    f'Желаю, чтобы в этом году твоя жизнь работала на максимальной частоте!',
    f'Пусть в {year_now} году тебя ждет только стабильное соединение с удачей!',
    f'С Новым годом! Пусть каждый твой жизненный цикл завершится успехом!',
    f'Пусть твои запросы к вселенной всегда возвращают только положительные ответы!',
    f'С Новым годом! Желаю в этом году больше вдохновения и меньше дедлайнов!',
    f'Пусть твои жизненные логи всегда будут полны хороших событий!',
    f'С новым счастьем, друг! Пусть ни один важный момент не уйдет в sleep mode!',
    f'Пусть {year_now} год будет таким же плавным, как бесконечный скролл радости!',
    f'С Новым годом! Пусть все твои действия будут выполнены с высоким приоритетом!',
    f'Желаю в этом году больше светлых идей и меньше сбойных транзакций!',
    f'С Новым годом! Пусть в твоей жизни всегда будет место для успешного бэкапа!',
    f'Пусть твои API-запросы к счастью всегда возвращают статус 200!',
    f'С новым счастьем! Пусть {year_now} год подарит тебе еще больше положительных эмоций!',
    f'Желаю в этом году только правильных решений и минимальных багов!',
    f'Пусть твои проекты всегда deploy-ятся без ошибок!',
    f'С Новым годом! Пусть {year_now} принесет тебе больше времени для отдыха и развлечений!',
    f'Пусть в этом году твой жизненный код будет работать без исключений!',
    f'С Новым годом! Пусть каждый commit в твоей жизни будет удачным!',
    f'С Новым годом! Пусть в {year_now} году ты всегда находил решение для самых сложных задач!',
    f'Желаю, чтобы твои пароли от счастья были всегда надежными и не терялись!',
    f'С новым счастьем! Пусть твой жизненный репозиторий пополняется яркими моментами!',
    f'Пусть твой процессор легко справляется с любыми задачами, а память никогда не подводит!',
    f'С Новым годом! Пусть твои идеи всегда находят поддержку и признание!',
    f'Желаю тебе в этом году меньше багов и больше фич в жизни!',
    f'Пусть твоя операционная система счастья обновится до самой стабильной версии!',
    f'С Новым годом! Пусть твоя производительность остается на высоком уровне весь год!',
    f'Пусть твои жизненные переменные всегда хранят только положительные значения!',
    f'С Новым годом! Пусть твои ресурсы восстанавливаются быстрее, чем расходуются!',
    f'Желаю тебе в {year_now} году, чтобы все твои задачи завершались с успехом!',
    f'Пусть в этом году тебя ждет успешный выход из всех дедлайнов!',
    f'С Новым годом! Пусть твой путь к успеху будет быстрым, как SSD!',
    f'Желаю в этом году больше времени на отдых и меньше на дебаг!',
    f'С Новым годом! Пусть {year_now} год будет таким же успешным, как запуск стабильного релиза!',
    f'Пусть твой код жизни будет написан без ошибок и с отличной логикой!',
    f'С Новым годом! Желаю тебе гармоничного user experience в каждом дне!',
    f'Пусть твои главные проекты в жизни всегда получают нужное финансирование!',
    f'С Новым годом! Пусть в твоей жизни будет больше happy flow и меньше исключений!',
    f'Желаю, чтобы {year_now} год принес только приятные уведомления и ни одного алерта!',
    f'С Новым годом! Пусть все твои жизненные запросы возвращают положительный результат!',
    f'Пусть твоя база данных радости будет всегда полна!',
    f'С новым счастьем! Пусть твоя жизнь проходит на высокой скорости и с минимальной задержкой!',
    f'Желаю в {year_now} году только стабильных подключений к счастью и удаче!',
    f'С Новым годом! Пусть твои лайфхаки всегда работают на 100%!',
    f'Пусть твоя карьера в этом году идет по экспоненте вверх!',
    f'С Новым годом! Пусть твои жизненные апдейты всегда приносят только улучшения!',
    f'Желаю, чтобы каждый твой день начинался с успешной загрузки!',
    f'С Новым годом! Пусть твои идеи всегда находят правильные реализации!',
    f'Пусть твой жизненный код будет написан на языке, который понимают все близкие!',
    f'С новым счастьем! Пусть твои друзья будут самыми надежными в сети и вне ее!',
    f'Пусть в этом году у тебя будет больше времени на любимые проекты!',
    f'С Новым годом! Желаю, чтобы твой firewall защищал от всего ненужного!',
    f'Пусть в твоей жизни будет больше Wi-Fi счастья и меньше лагов!',
    f'С Новым годом! Пусть {year_now} год принесет тебе новые инсайты и вдохновение!',
    f'Желаю, чтобы в твоем проекте жизни не было ни одной уязвимости!',
    f'С Новым годом! Пусть твой мониторинг всегда показывает только зеленую зону!',
    f'Пусть твои ресурсы восполняются быстрее, чем ты их тратишь!',
    f'С Новым годом! Пусть каждый твой день будет как успешный релиз!',
    f'Желаю в {year_now} году оптимального баланса между работой и отдыхом!',
    f'С Новым годом! Пусть твоя жизнь будет защищена антивирусом от стресса!',
    f'Пусть в твоей жизни будет как можно меньше ошибок 404!',
    f'С Новым годом! Пусть в {year_now} году сбываются все твои самые смелые мечты!',
    f'Желаю, чтобы каждый твой жизненный проект достигал цели с первого раза!',
    f'С Новым годом! Пусть твой год пройдет в режиме низкого энергопотребления!',
    f'Пусть твоя сеть знакомств в {year_now} году растет и укрепляется!',
    f'С Новым годом! Пусть в твоей жизни будет больше апгрейдов и меньше даунтайма!',
    f'Желаю в этом году меньше обновлений по ночам и больше сна!',
    f'С Новым годом! Пусть твоя кривая роста счастья всегда идет вверх!',
    f'Пусть твои проекты в этом году выйдут на новый уровень!',
    f'С Новым годом! Пусть в {year_now} году тебя ждет только стабильный аптайм!',
    f'Желаю тебе в новом году быстрого доступа к самым радостным моментам!',
    f'С Новым годом! Пусть твои файлы жизни всегда сохраняются и никогда не теряются!',
    f'Пусть в твоей жизни будет больше лайков от судьбы!',
    f'С Новым годом! Пусть твоя лента событий будет наполнена только хорошими новостями!',
    f'Пусть твоя жизнь в {year_now} году будет работать на процессоре счастья!',
    f'С Новым годом! Пусть все твои жизненные запросы будут успешными!',
    f'Желаю, чтобы в {year_now} году у тебя было больше свободного времени!',
    f'Пусть твой жизненный проект всегда проходит ревью без замечаний!',
    f'С Новым годом! Пусть твои ежедневные таски будут легкими и интересными!',
    f'Пусть в {year_now} году тебя ждут только яркие и запоминающиеся события!',
    f'С Новым годом! Пусть твоей энергией всегда можно заряжаться!',
    f'Пусть в {year_now} году у тебя будет больше времени для личных проектов!',
    f'С Новым годом! Пусть твоя продуктивность будет вдохновением для других!',
    f'Желаю в этом году только зеленых индикаторов и никаких тревог!',
    f'С Новым годом! Пусть твои фреймворки счастья работают без сбоев!',
    f'Пусть все ошибки из прошлого года останутся в логах истории!',
    f'С Новым годом! Пусть твой жизненный алгоритм будет максимально оптимизирован!',
    f'Желаю, чтобы {year_now} год принес только успехи и новые достижения!',
    f'С Новым годом! Пусть все твои задачи всегда выполняются в срок!',
    f'Пусть в этом году твои цели будут достигнуты без переработок!',
    f'С Новым годом! Пусть твоя жизнь всегда будет на высоте!',
    f'Пусть все твои запросы счастья возвращают статус 200!',
    f'С Новым годом! Пусть каждая итерация твоего дня будет лучше предыдущей!',
    f'Желаю, чтобы в {year_now} году твоя кривая успеха росла!',
    f'С Новым годом! Пусть каждый день приносит новые впечатления и радости!',
    f'Пусть в этом году твой код жизни будет чистым и понятным!',
    f'С Новым годом! Пусть твоя производительность будет на пике весь год!',
    f'Желаю, чтобы {year_now} год был полон приятных инсайтов и счастливых событий!',
    f'С Новым годом! Пусть твои жизненные баги останутся в прошлом году!'
]


def get_random_year_message(messages):
    return random.choice(messages)
