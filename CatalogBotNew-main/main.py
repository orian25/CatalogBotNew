import os
import asyncio
from telethon import TelegramClient
import requests

# הגדרות
api_id = 28047447
api_hash = '3255fe0eaa699b285c51da76a2ffcd9b'
bot_token = 'nfp_jSttTPJcvPP6dsFxCEYjbZzJJuhL1VTtee02'

categories = {
    'אריחים 120/60': 'downloads_120x60',
    'אריחים 120/120': 'downloads_120x120',
    'אריחים 80/80': 'downloads_80x80',
    'אריחים 100/100': 'downloads_100x100',
    'פלטות': 'downloads_plates',
    'מיוחדים': 'downloads_special',
}

async def main():
    client = TelegramClient('session', api_id, api_hash)
    await client.start(bot_token=bot_token)
    
    for dialog in await client.get_dialogs():
        for category_name, folder_name in categories.items():
            if category_name in dialog.name:
                os.makedirs(folder_name, exist_ok=True)
                messages = await client.get_messages(dialog.id, limit=50)
                for msg in messages:
                    if msg.photo:
                        path = os.path.join(folder_name, f"{msg.id}.jpg")
                        if not os.path.exists(path):
                            await client.download_media(msg, file=path)
    
    await client.disconnect()

if __name__ == '__main__':
    asyncio.run(main())
