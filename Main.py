import discord
import asyncio
from discord.ext import commands
from os import path, system


# Prefix 
PREFIX = ">"
TOKEN = "**TOKEN**"


# ถ้าอยากให้คนอื่นใช้คำสั่งได้ปรับ self_bot=True จาก True เป็น False
bot = commands.Bot(command_prefix=PREFIX, description='''Selfbot by Larina''', self_bot=True)

#################
# C O N S O L E #
#################

system("cls")
system('title [Discord Ezmoney v.3] - Ready ^| Make By potteryyy Aka Larina')



###################
# C O M M A N D S #
###################

# list
@bot.command(pass_context=True)
async def list(ctx, *args):
    await ctx.send('''    
    > **command**
        sendmsg
        sendmsgwithaliases
        msginputint
        msginputstr
        msginputstrandint
        msginputmultiple
    ''')
    

@bot.command(pass_context=True) #, aliases=['']
async def sendmsg(ctx):
    await ctx.send('Hello world')


@bot.command(pass_context=True, aliases=['s', 'msg'])
async def sendmsgwithaliases(ctx):
    await ctx.send('send msg with aliases')


@bot.command(pass_context=True)
async def msginputint(ctx, arg1: int):
    await ctx.send(f'input int only = **{arg1}**')


@bot.command(pass_context=True)
async def msginputstr(ctx, arg1: str):
    await ctx.send(f'input str only = **{arg1}**')

@bot.command(pass_context=True)
async def msginputstrandint(ctx, arg1):
    await ctx.send(f'input str and int = **{arg1}**')

@bot.command(pass_context=True)
async def msginputmultiple(ctx, *, arg1):
    await ctx.send(f'input multiple values = **{arg1}**')

    

print("[INFO] Login Successfully")
# login token
bot.run(TOKEN, bot=False)