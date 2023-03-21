import random
import discord
from discord.ext import commands
from youtube_dl import YoutubeDL

config = {
          'token': '',
          'prefix': '$',
         }
YDL_OPTIONS={'format': 'worstaudio/best', 'noplaylist': 'False', 'simulate': 'True', 'key': 'FFmpegExtractAudio' }
FFMPEG_OPTIONS={'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
bot = commands.Bot(command_prefix=config['prefix'], intents=discord.Intents.all())

@bot.command()
async def ping(ctx):
     await ctx.send('pong')

@bot.command()
async def play(ctx, url):
    vc = await ctx.message.author.voice.channel.connect()


    with YoutubeDL(YDL_OPTIONS) as ydl:
        if 'https://' in url:
            info = ydl.extract_info(url, download=False)
        else:
            info = ydl.extract_info(f'ytsearch:{url}', download=False)['entries'][0]

    link = info['formats'][0]['url']

    vc.play(discord.FFmpegPCMAudio(executable="ffmpeg\\ffmpeg.exe", source=link, **FFMPEG_OPTIONS))





bot.run(config['token'])