import os
import logging
from flask import Flask, render_template, request, json
from telegram import Bot

token = os.getenv('TELEGRAM_TOKEN')
chat = os.getenv('CHAT_ID')
app = Flask(__name__)
bot = Bot(token = token)

@app.route('/', methods=['POST'])
def home_post():

    data = request.get_json()

    resp = None

    if data['type'] == 'REMOVED_FROM_SPACE':
        logging.info('Bot removed from a space')

    else:
        resp_dict = format_response(data)
        resp = json.jsonify(resp_dict)

    bot.sendMessage(chat, f"{resp_dict['sender']}{os.linesep}{resp_dict['text']}")
    return resp

def format_response(event):

    text = ""

    if event['type'] == 'ADDED_TO_SPACE' and event['space']['type'] == 'ROOM':
        text = 'Thanks for adding me to "%s"!' % event['space']['displayName']

    elif event['type'] == 'ADDED_TO_SPACE' and event['space']['type'] == 'DM':
        text = 'Thanks for adding me to a DM, %s!' % event['user']['displayName']

    elif event['type'] == 'MESSAGE':
        text = event['message']['text']
        sender = event['message']['sender']['displayName']
        # if '//save' in event['message']['text']:
        #     text = 'Your message SAVED!'

    return {'sender': sender, 'text': text}

@app.route('/', methods=['GET'])
def home_get():

    return render_template('home.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=False)
