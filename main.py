from telethon import TelegramClient, events, functions, types
import logging
import os
from dotenv import load_dotenv

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

load_dotenv(override=True)

client = TelegramClient(os.getenv('STRING_SESSION'),
                        os.getenv('API_ID'), os.getenv('API_HASH'))


@client.on(events.NewMessage)
async def handler(event):
    if (str(event.chat_id) == os.getenv('TARGET')):
        await client(functions.messages.SendReactionRequest(
            peer=event.message.peer_id,
            msg_id=event.message.id,
            big=True,
            reaction=[types.ReactionEmoji(
                emoticon=os.getenv('EMOJI')
            )]
        ))


client.start()
client.run_until_disconnected()
