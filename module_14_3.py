"""
Задача "Витамины для всех!":
Подготовка:
Подготовьте Telegram-бота из последнего домашнего задания 13 модуля сохранив код с ним в файл module_14_3.py.
Если вы не решали новые задания из предыдущего модуля рекомендуется выполнить их.

Дополните ранее написанный код для Telegram-бота:
Создайте и дополните клавиатуры:
В главную (обычную) клавиатуру меню добавьте кнопку "Купить".
Создайте Inline меню из 4 кнопок с надписями "Product1", "Product2", "Product3", "Product4". У всех кнопок назначьте callback_data="product_buying"
Создайте хэндлеры и функции к ним:
Message хэндлер, который реагирует на текст "Купить" и оборачивает функцию get_buying_list(message).
Функция get_buying_list должна выводить надписи 'Название: Product<number> | Описание: описание <number> | Цена: <number * 100>' 4 раза. После каждой надписи выводите картинки к продуктам. В конце выведите ранее созданное Inline меню с надписью "Выберите продукт для покупки:".
Callback хэндлер, который реагирует на текст "product_buying" и оборачивает функцию send_confirm_message(call).
Функция send_confirm_message, присылает сообщение "Вы успешно приобрели продукт!"

"""

from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor

# Инициализация бота и диспетчера
API_TOKEN = '###'
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


# Определение группы состояний
class UserState(StatesGroup):
    gender = State()
    age = State()
    growth = State()
    weight = State()


# Функция для начала цепочки
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton('Рассчитать'), types.KeyboardButton('Информация'), types.KeyboardButton('Купить'))
    await message.answer('Выберите действие:', reply_markup=keyboard)


# Функция для отправки Inline-клавиатуры
@dp.message_handler(lambda message: message.text == 'Рассчитать')
async def main_menu(message: types.Message):
    inline_keyboard = types.InlineKeyboardMarkup()
    inline_keyboard.add(types.InlineKeyboardButton('Рассчитать норму калорий', callback_data='calories'))
    inline_keyboard.add(types.InlineKeyboardButton('Формулы расчёта', callback_data='formulas'))
    await message.answer('Выберите опцию:', reply_markup=inline_keyboard)


# Функция для отправки информации о боте
@dp.message_handler(lambda message: message.text == 'Информация')
async def bot_info(message: types.Message):
    info = (
        "Этот бот помогает рассчитать вашу суточную норму калорий по формуле Миффлина-Сан Жеора.\n\n"
        "Для расчета нормы калорий нажмите кнопку 'Рассчитать' и следуйте инструкциям.\n\n"
        "Разработчик: Sergant13"
    )
    await message.answer(info)


# Функция для отправки формул расчета калорий
@dp.callback_query_handler(lambda call: call.data == 'formulas')
async def get_formulas(call: types.CallbackQuery):
    formulas = (
        "Формула Миффлина-Сан Жеора для мужчин:\n"
        "10 * вес (кг) + 6.25 * рост (см) - 5 * возраст (лет) + 5\n\n"
        "Формула Миффлина-Сан Жеора для женщин:\n"
        "10 * вес (кг) + 6.25 * рост (см) - 5 * возраст (лет) - 161"
    )
    await call.message.answer(formulas)
    await call.answer()


# Функция для начала цепочки расчета калорий
@dp.callback_query_handler(lambda call: call.data == 'calories')
async def set_gender(call: types.CallbackQuery):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("Мужской", "Женский")
    await call.message.answer('Выберите пол:', reply_markup=keyboard)
    await UserState.gender.set()


# Функция для обработки пола
@dp.message_handler(state=UserState.gender)
async def set_age(message: types.Message, state: FSMContext):
    gender = message.text
    await state.update_data(gender=gender)
    await message.answer('Введите свой возраст:', reply_markup=types.ReplyKeyboardRemove())
    await UserState.age.set()


# Функция для обработки возраста
@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=int(message.text))
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


# Функция для обработки роста
@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=int(message.text))
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


# Функция для обработки веса и вычисления нормы калорий
@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=int(message.text))
    data = await state.get_data()

    age = data['age']
    growth = data['growth']
    weight = data['weight']
    gender = data['gender']

    if gender == "Мужской":
        # Формула Миффлина - Сан Жеора для мужчин
        calories = 10 * weight + 6.25 * growth - 5 * age + 5
    elif gender == "Женский":
        # Формула Миффлина - Сан Жеора для женщин
        calories = 10 * weight + 6.25 * growth - 5 * age - 161
    else:
        await message.answer("Неверный пол. Пожалуйста, начните снова.")
        await state.finish()
        return

    await message.answer(f'Ваша норма калорий: {calories:.2f} ккал в день.')
    await state.finish()


# Функция для отображения списка продуктов
@dp.message_handler(lambda message: message.text == 'Купить')
async def get_buying_list(message: types.Message):
    products = [
        {"name": "Витамины", "description": "B 12", "price": 100, "image": "https://via.placeholder.com/150"},
        {"name": "Минералы", "description": "Кальций, Магний", "price": 200, "image": "https://via.placeholder.com/150"},
        {"name": "Слабительное", "description": "Помощь при запоре", "price": 300, "image": "https://via.placeholder.com/150"},
        {"name": "Активированный уголь", "description": "Помощь при отравлении", "price": 400, "image": "https://via.placeholder.com/150"}
    ]

    for product in products:
        await message.answer(f'Название: {product["name"]} | Описание: {product["description"]} | Цена: {product["price"]}')
        await message.answer_photo(product["image"])

    inline_keyboard = types.InlineKeyboardMarkup()
    for i in range(1, 5):
        inline_keyboard.add(types.InlineKeyboardButton(f'Product{i}', callback_data='product_buying'))

    await message.answer('Выберите продукт для покупки:', reply_markup=inline_keyboard)


# Функция для подтверждения покупки
@dp.callback_query_handler(lambda call: call.data == 'product_buying')
async def send_confirm_message(call: types.CallbackQuery):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()


# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)