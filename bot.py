# Проект: ТГ-бот для поиска адвоката, ближайшего к доверителю
# 09.02.2023    IgorLytkin  настроил SSH-ключ на GitHub
#
import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, types

# Данные об ОС
print(os.name)

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=os.getenv("BOT_TOKEN"))
# Диспетчер
dp = Dispatcher()


# Хэндлер на команду /start
@dp.message(commands=["start"])
async def cmd_start(message: types.Message):
    await message.answer("Hello!")


# Хэндлер на команду /test1
@dp.message(commands=["test1"])
async def cmd_test1(message: types.Message):
    await message.reply("Test 1")


# Хэндлер на команду /test2
async def cmd_test2(message: types.Message):
    await message.reply("Test 2")


@dp.message(commands=["answer"])
async def cmd_answer(message: types.Message):
    await message.answer("Это простой ответ")


@dp.message(commands=["reply"])
async def cmd_reply(message: types.Message):
    await message.reply('Это ответ с "ответом"')


@dp.message(commands=["dice"])
async def cmd_dice(message: types.Message, bot: Bot):
    await bot.send_dice(os.getenv("LAWCHANNEL_BOT_ID"), emoji="🎲")


@dp.message(commands=["add_to_list"])
async def cmd_add_to_list(message: types.Message, mylist: list[int]):
    mylist.append(7)
    await message.answer("Добавлено число 7")


@dp.message(commands=["show_list"])
async def cmd_show_list(message: types.Message, mylist: list[int]):
    await message.answer(f"Ваш список: {mylist}")


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
