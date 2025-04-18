import asyncio
from aiogram import Bot, Dispatcher # aiogram 3
from app.handlers import router




async def main():
    bot = Bot(token = '7448768558:AAHbrdffYW4Zw33u6F42YUNFNYzk7yrADQM') # API-token
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot, skip_updates = True)




if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Ctrl + C: Бот выключен.')



















# Запуск бота

r"""start

Visual Studio Code

Для запуска бота нужно ввести в терминал (Ctrl + `):

set-ExecutionPolicy RemoteSigned -Scope CurrentUser 

Get-ExecutionPolicy

Get-ExecutionPolicy -list

.venv\Scripts\activate

python main.py

end"""




# Перезапуск бота

r"""start

Visual Studio Code

Для перезапуска бота нужно ввести в терминал (Ctrl + `):

.venv\Scripts\activate

python main.py

end"""




# Создание бота

r"""start

Visual Studio Code

Для создания своего бота (и отделения бота от других проектов) нужно ввести в терминал (Ctrl + `):

python -m venv .venv 

.venv\Scripts\activate

pip list

python.exe -m pip install --upgrade pip

pip install aiogram

pip install dotenv

pip list

end"""