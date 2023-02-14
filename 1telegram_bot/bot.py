import openai
import aiogram.utils
import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, executor, types

OPENAI_API_KEY = "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"

# Initialize bot and dispatcher
bot = Bot(token="5965750764:AAHcEVzjjcWDsipsPI-rmXEJIUtIbAGPuVM")
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def cmd_start(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await bot.send_message(
        chat_id=message.chat.id,
        text="Hi there! I am a GPT-3 powered Telegram bot. How can I help you today?",
    )

@dp.message_handler()
async def chat_handler(message: types.Message):
    """
    This handler will process any text messages sent to the bot.
    """
    # Use OpenAI's GPT-3 API to generate a response to the user's message
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"{message.text}\n",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    ).get("choices")[0].text

    # Send the response to the user
    await bot.send_message(
        chat_id=message.chat.id,
        text=response,
    )

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
