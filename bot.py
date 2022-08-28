import discord
import random
from discord.ext import commands
from random import random


Token = 'MTAxMDkyMzUwMTE2ODg5ODA2OA.GSQotT.CLZU6DCR_IKiob0eUS9ERegUHkRc_aC_bPnDHw'

client = commands.Bot(command_prefix = '!', intents = discord.Intents.all())


@client.event
async def on_ready():
    print('We have logged in as {0 user}'.format(client))

@client.command()
async def hello(ctx):
    await ctx.reply("Hello!")

@client.command()
async def yash(ctx):
    await ctx.reply('khargosh ke saath busy hai wo....')

@client.command()
async def random(ctx):
    await ctx.reply ({random.randrange(1000000)})

@client.command()
async def beg(ctx):
    await ctx.send('pls work')

@client.command()
async def mihika(ctx):
    await ctx.reply('loves sarthak')

@client.command()
async def manku(ctx):
    await ctx.reply('mayank-uddin sheikh mulla')

@client.command()
async def ping(ctx):
    await ctx.reply('pong')

@client.command()
async def who(ctx):
    await ctx.reply('mujhe modi ji ne parliament se nikal diya isiliye berozgaari ki wajah se yaha baitha hu aur mere jaise anya berozgaaro ki madad kar rha hu')

#embed for about

@client.command(aliases=['user','info'])
@commands.has_permissions(kick_members=True)
async def about(ctx, member: discord.Member):
    embed = discord.Embed(title = member.name , description = member.mention , color = discord.Colour.red())
    embed.add_field(name = "ID", value = member.id , inline = True)
    embed.set_thumbnail(url = member.avatar.url)
    embed.set_footer(icon_url = ctx.author.avatar, text = f"Requested by {ctx.author.name}")
    await ctx.send(embed=embed)

#custom help command

client.remove_command("help")

@client.group(invoke_without_command=True)
async def commands(ctx):
    em = discord.Embed(title = "Commands", description = "Use !command for all commands.", color = ctx.author.color)

    await ctx.send (embed = em)

client.run (Token)