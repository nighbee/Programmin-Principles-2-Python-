import aiohttp
import aiogram.utils
import aiogram.utils.markdown as md
# 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
from aiogram import Bot, Dispatcher, executor, types, utils
API_TOKEN='5965750764:AAHcEVzjjcWDsipsPI-rmXEJIUtIbAGPuVM'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
@dp.message_handler(commands=['start'])
async def send_welcome(message:types.Message):
    await message.reply("hello there, send me request!")
@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

# connecting ChatGPT
# chatgpt_url= 'https://api.openai.com/v1/engines/chatbot/jobs'
# async def chatgpt_response(message):
#     headers ={
#         'Content-Type': 'application/json',
#         'Authorization':f'bearer {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}'
#     }
#     data = {
#         'engine': 'text-davinci-002',
#         'prompt': message,
#         'temperature': 0.5,
#         'max_tokens': 100,
#         'top_p': 1,
#         'frequency_penalty': 0,
#         'presence_penalty': 0
#     }
# async with aiohttp.ClientSession() as session:
#     async with session.post(chatgpt_url) as resp:
#         response_text= await resp.json()
#         return response_text['choices'][0]['text']
# @dp.message_handler(commands='start')
# async def cmd_start(message: Message):
#     await bot.send_message(chat_id=message.chat.id, text='hi! i am chatgpt powered bot, how i can help?')
# if __name__ == '__main__'
#     executor.start_polling(dp, skip_updates=True)