import aiogram.dispatcher
import aiogram.types
import aiogram.utils
import requests
from aiogram.types import Message
from aiogram.utils import executor

API_KEY = "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"
API_ENDPOINT = "https://api.openai.com/v1/engines/davinci/jobs"

# Create the bot instance
bot = aiogram.Bot(token="5965750764:AAHcEVzjjcWDsipsPI-rmXEJIUtIbAGPuVM")

# Set up the dispatcher
dp = aiogram.dispatcher.Dispatcher(bot)

# Message handler for incoming messages
@dp.message_handler(commands='help')
async def cmd_help(message: Message):
    input_text = message.text

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    data = {
        "prompt": input_text,
        "max_tokens": 100,
        "temperature": 0.5,
    }
    response = requests.post(API_ENDPOINT, headers=headers, json=data)

    response_text = response.json()["choices"][0]["text"]

    await bot.send_message(chat_id=message.chat.id, text=response_text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
