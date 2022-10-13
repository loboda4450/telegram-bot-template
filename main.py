import asyncio
import logging

import yaml

from telethon import TelegramClient
from telethon.events import NewMessage


async def main(config):
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=config['log_level'])
    logger = logging.getLogger(__name__)
    client = TelegramClient(**config['telethon_settings'])
    print("Starting")

    if not config['bot_token']:
        raise Exception('No bot token provided')

    await client.start(bot_token=config['bot_token'])
    print("Started")

    @client.on(NewMessage(pattern='/start'))
    async def status(event):
        await event.reply("Hello world!")

    async with client:
        print("Good morning!")
        await client.run_until_disconnected()


if __name__ == '__main__':
    with open("config.yml", 'r') as f:
        config = yaml.safe_load(f)
        asyncio.get_event_loop().run_until_complete(main(config=config))
