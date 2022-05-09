import os
from yaml import load, dump, CLoader as Loader, CDumper as Dumper
with open('config.yml', 'r') as config:
    cfg = load(config, Loader=Loader)
from discord import Bot, Intents
from discord.utils import get
bot = Bot(intents=Intents.all())

async def rr(member):
    try:
        guild = member.guild
        mrs = []
        for role in member.roles:
            mrs.append(str(role.id))
        check = False
        for role in cfg['roles']:
            if role in mrs:
                if check:
                    dr = get(guild.roles, id=int(role))
                    await member.remove_roles(dr)
                check = True
    except Exception as e:
        print(e)

@bot.event
async def on_ready():
    print(cfg)
    for guild in bot.guilds:
        for member in guild.members:
            await rr(member)
    print('Ready!')

@bot.event
async def on_guild_join(guild):
    for member in guild.members:
        await rr(member)

@bot.event
async def on_member_update(before, after):
    if len(before.roles) < len(after.roles):
        await rr(after)

bot.run(os.getenv("TOKEN"))
