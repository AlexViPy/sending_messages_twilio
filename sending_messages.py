import os
import time
import requests
from twilio.rest import Client
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')
number_from = os.getenv('NUMBER_FROM')
number_to = os.getenv('NUMBER_TO')
access_token = os.getenv('ACCESS_TOKEN')

def get_status(user_id):
    params = {
        'user_id':user_id,
        'fields': 'online',
        'v':5.92,
        'access_token':ACCESS_TOKEN
    }
    user_status = requests.post('https://api.vk.com/method/users.get', data = params)
    return user_status.json()['response'][0]['online']


def sms_sender(sms_text):
    client = Client(account_sid, auth_token)
    message = client.messages.create (
        body ='Time to start tracking!',
        from_= number_from,
        to = number_to
                         )
    return message.sid


if __name__ == "__main__":
    vk_id = input("Введите id ")
    while True:
        if get_status(vk_id) == 1:
            sms_sender(f'{vk_id} сейчас онлайн!')
            break
        time.sleep(5)
