
import plotly.offline as pyo
import numpy as np 
import pandas as pd
from pandas_datareader import data as pdr 
import yfinance as yf
import datetime as dt 
import plotly.graph_objs as go 
from random import choice, randint
import os
from discord import Client,Intents,Message
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')
yf.pdr_override() 


intents: Intents = Intents.default()
intents.message_content = True  
client: Client = Client(intents=intents)
#Time
Date =dt.datetime.now().today()
Time =dt.datetime.now().time()
print(Date)
print(Time)
#Stock LIVE PRice
# STEP 2: MESSAGE FUNCTIONALITY
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('(Message was empty because intents were not enabled probably)')
        return

    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    try:
        response: str = get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')


@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)


# STEP 5: MAIN ENTRY POINT
def main() -> None:
    client.run(token=TOKEN)

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()


    if lowered == '':
        return 'Well, you\'re awfully silent...'
    elif 'hello' in lowered:
        return 'Hello there!'
    elif 'how are you' in lowered:
        return 'I am fine !'
    elif lowered.startswith('/'):
        stock = lowered[1:].strip()
        df = yf.download(tickers=stock,period='1m')
        print(df)
        return df
    elif 'bye' in lowered:
        return 'See you!'
    elif 'time'in lowered:
        return f'Time Right Now is {Time}'
    elif 'roll dice' in lowered:
        return f'You rolled: {randint(1, 6)}'
    else:
        return choice(['I do not understand...',
                       'What are you talking about?',
                       'Do you mind rephrasing that?'])


if __name__ == '__main__':
    main()