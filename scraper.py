import asyncio
import csv
from argparse import ArgumentParser

from telethon import TelegramClient, types

from arg_parser import add_parsing_arguments
from config import Configuration


async def get_group_id_by_name(client: TelegramClient, group_name: str) -> int:
    dialogs = await client.get_dialogs()
    for dialog in dialogs:
        if isinstance(
                dialog.entity,
                (types.Chat, types.Channel)
                ) and dialog.entity.title == group_name:
            return dialog.entity.id
    raise NameError('The desired group was not found.')


async def scrap_group(client: TelegramClient, config: Configuration):
    group_id = config.group_id
    if not group_id:
        group_id = await get_group_id_by_name(client, config.group_name)

    users = await client.get_participants(group_id)
    with open('group_members.csv', 'w', encoding='UTF-8') as f:
        writer = csv.writer(f,delimiter=",",lineterminator="\n")
        writer.writerow(['id', 'bot',
                         'first_name', 'last_name',
                         'username', 'phone'])
        for user in users:
            writer.writerow([user.id, user.bot, user.first_name,
                             user.last_name, user.username, user.phone])


async def main():
    parser = ArgumentParser()
    add_parsing_arguments(parser)
    args = parser.parse_args()
    config = Configuration.from_args(args)
    client = TelegramClient('scraper', config.api_id, config.api_hash)
    await client.start()
    await scrap_group(client, config)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
