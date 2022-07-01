from config import DISCORD_BOT_TOKEN
from discord.ext.commands import Bot

bot = Bot(command_prefix='!')

@bot.command()
async def test(context, message_link):
    message_link_components = message_link.split('/')
    channel_id = message_link_components[-2]
    message_id = message_link_components[-1]
    channel = await bot.fetch_channel(channel_id)
    message = await channel.fetch_message(message_id)
    for reaction in message.reactions:
        if reaction.emoji == '👍':
            users = await reaction.users().flatten()
            print('Users:', [user.name for user in users])

bot.run(DISCORD_BOT_TOKEN)