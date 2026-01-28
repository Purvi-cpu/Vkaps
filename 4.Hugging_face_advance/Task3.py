# from config import *
# import telebot 
# import openai

# bot = telebot.TeleBot(BOT_KEY)
# char_str=""
# def ChatModel(prompt):
#     global char_str
#     openai.api_key = API_KEY
#     char_str += f"You: {prompt}\nGamer: "
#     response = openai.completions.create(
#         model="davinci-002",
#         prompt="",
#         temperature=1,
#         max_tokens=256,
#         top_p=1,
#         frequency_penalty=0,
#         presence_penalty=0
#         )
#     char_str += f"{response['choices'][0]['text']}"
#     return response['choices'][0]['text']

# @bot.message_handler(['start'])
# def start(message):
    
#     bot.reply_to(message,"Hello!, Game starts now..")

# @bot.message_handler()
# def chat(message):
#     try:
#         reply = ChatModel(message.text)
#         bot.reply_to(message, reply)
#     except Exception as e:
#         print(e)
#         bot.reply_to(message, e)


# print("Bot Started..")
# bot.polling()

from config import *
import telebot
import google.generativeai as genai

# Configure Gemini
genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel("gemini2.5-pro")

bot = telebot.TeleBot(BOT_KEY)

chat_str = ""

def ChatModel(prompt):
    global chat_str

    chat_str += f"You: {prompt}\nAI: "
    response = model.generate_content(chat_str)

    reply = response.text
    chat_str += reply + "\n"

    return reply


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, " Game Started!!!!")


@bot.message_handler(func=lambda message: True)
def chat(message):
    try:
        reply = ChatModel(message.text)
        bot.reply_to(message, reply)
    except Exception as e:
        print(e)
        bot.reply_to(message, e)


print("🚀 Bot Started...")
bot.polling()
