import random
import discord
from discord.ext import commands
from youtube_dl import YoutubeDL

config = {
          'token': 'MTA4NzMyNjQ5MzE1MzE2OTQ3OA.GOcjj1.MHaDCWINjYY6JvE35NQQDsTIB4u2pRjFooLRY4',
          'prefix': '$',
         }
YDL_OPTIONS={'format': 'worstaudio/best', 'noplaylist': 'False', 'simulate': 'True', 'key': 'FFmpegExtractAudio' }
FFMPEG_OPTIONS={'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
bot = commands.Bot(command_prefix=config['prefix'], intents=discord.Intents.all())



@bot.event
async def on_new_members(ctx: commands.Context):
          if len(ctx.author.roles)==0:
              role_to_new = 1088005959777013780
              ch = ctx.guild.system_channel
              embed= discord.Embed(
                  title="Новый пчел",
                  description=f"{ctx.author.name}#{ctx.author.discriminator}",
                  colour=(0,204,0)
              )
              await ctx.author.add_roles(role_to_new)
              await ch.send(embed=embed)

@bot.command()
async def amogus(ctx):
    await ctx.send("⣿⣿⣿⠟⢹⣶⣶⣝⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n ⣿⣿⡟⢰⡌⠿⢿⣿⡾⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n ⣿⣿⣿⢸⣿⣤⣒⣶⣾⣳⡻⣿⣿⣿⣿⡿⢛⣯⣭⣭⣭⣽⣻⣿⣿⣿\n ⣿⣿⣿⢸⣿⣿⣿⣿⢿⡇⣶⡽⣿⠟⣡⣶⣾⣯⣭⣽⣟⡻⣿⣷⡽⣿\n ⣿⣿⣿⠸⣿⣿⣿⣿⢇⠃⣟⣷⠃⢸⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽\n ⣿⣿⣿⣇⢻⣿⣿⣯⣕⠧⢿⢿⣇⢯⣝⣒⣛⣯⣭⣛⣛⣣⣿⣿⣿⡇\n ⣿⣿⣿⣿⣌⢿⣿⣿⣿⣿⡘⣞⣿⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\n ⣿⣿⣿⣿⣿⣦⠻⠿⣿⣿⣷⠈⢞⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\n ⣿⣿⣿⣿⣿⣿⣗⠄⢿⣿⣿⡆⡈⣽⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢻\n ⣿⣿⣿⣿⡿⣻⣽⣿⣆⠹⣿⡇⠁⣿⡼⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣾\n ⣿⠿⣛⣽⣾⣿⣿⠿⠋⠄⢻⣷⣾⣿⣧⠟⣡⣾⣿⣿⣿⣿⣿⣿⡇⣿\n ⢼⡟⢿⣿⡿⠋⠁⣀⡀⠄⠘⠊⣨⣽⠁⠰⣿⣿⣿⣿⣿⣿⣿⡍⠗⣿\n ⡼⣿⠄⠄⠄⠄⣼⣿⡗⢠⣶⣿⣿⡇⠄⠄⣿⣿⣿⣿⣿⣿⣿⣇⢠⣿\n ⣷⣝⠄⠄⢀⠄⢻⡟⠄⣿⣿⣿⣿⠃⠄⠄⢹⣿⣿⣿⣿⣿⣿⣿⢹⣿\n ⣿⣿⣿⣿⣿⣧⣄⣁⡀⠙⢿⡿⠋⠄⣸⡆⠄⠻⣿⡿⠟⢛⣩⣝⣚⣿\n ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣤⣤⣤⣾⣿⣿⣄⠄⠄⠄⣴⣿⣿⣿⣇⣿\n ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⡀⠛⠿⣿⣫⣾⣿")


@bot.command()
@commands.has_role(789155394781052969)
@commands.
async  def time_out_user(ctx: commands.Context, user: discord.Member, time, res='Причина не известна'):
    await  user.timeout()

@bot.command()
@commands.has_role(789155394781052969)
async def kick_user(ctx: commands.Context, user: discord.User, res='Причина не известна'):
        await ctx.guild.kick(user, reason=res)
        await ctx.send( f'был кикнут {user.name}, по причине: {res}')

@bot.command()
@commands.has_role(789155394781052969)
async def ban_user(ctx: commands.Context, user: discord.User, time, res='Причина не известна'):
        await ctx.guild.ban(user, res, time)
        await ctx.send( f'был забанен {user.name}, по причине: {res}')




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