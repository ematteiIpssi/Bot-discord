import discord,riot,logging,logging.handlers,redirection,os
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', description='LoLAPI', intents=intents)
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
logging.getLogger('discord.http').setLevel(logging.INFO)

handler = logging.handlers.RotatingFileHandler(
    filename='discord.log',
    encoding='utf-8',
    maxBytes=32 * 1024 * 1024,  # 32 MiB
    backupCount=5,  # Rotate through 5 files
)

dt_fmt = '%Y-%m-%d %H:%M:%S'
formatter = logging.Formatter('[{asctime}] [{levelname:<8}] {name}: {message}', dt_fmt, style='{')
handler.setFormatter(formatter)
logger.addHandler(handler)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def l(ctx,message):
    rep = redirection.parse(message)
    if type(rep) is list:
        await ctx.send(embeds=rep)
    else:
        await ctx.send(embed=rep)

bot.run(DISCORD_TOKEN)