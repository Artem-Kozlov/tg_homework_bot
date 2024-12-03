from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
import asyncio

TOKEN = "7169731413:AAEyPHs1ZJY4CaoDeNbGc3Auwxc1r_Hta6w"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(F.text)
async def echo_handler(message: Message):
    await message.reply(message.text)

async def main():
    print("Бот запущен и готов к работе...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())



    