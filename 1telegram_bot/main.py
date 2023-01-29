import openai
import telegram
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Set the OpenAI API key
openai.api_key = "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"

# Initialize the Telegram bot
updater = Updater(token='5965750764:AAHcEVzjjcWDsipsPI-rmXEJIUtIbAGPuVM')
dispatcher = updater.dispatcher

# Function to handle Telegram bot commands
def generate_response(bot, update: Update):
    user_input = update.message.text
    response = openai.Completion.create(engine="text-davinci-002", prompt=user_input)
    context.bot.send_message(chat_id=update.message.chat_id, text=response.choices[0].text)

# Register the command handler
dispatcher.add_handler(CommandHandler('generate_response', generate_response))

# Start the bot
updater.start_polling()
