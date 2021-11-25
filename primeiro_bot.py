import datetime

import discord
from discord import channel 
from discord.ext import commands, tasks

bot = commands.Bot("!")

@bot.event
async def on_ready():
     print(f"Estou pronto! Estou conectado como {bot.user}")
     #current_time.start()


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

        if "palavrão" in message.content:
            await message.channel.send(
                f"Por Favor, {message.author.name}, não ofenda os demais usuários!"
            )

            await message.delete()

            await bot.process_commands(message)


#  !calcular 2+2*3/4
@bot.command(name="oi")
async def send_hello(ctx):
    name = ctx.author.name

    response = "Olá, " + name 

    await ctx.send(response)


@bot.comand(name='calcular')
async def calculate_expression(ctx, expression):
    response = eval(expression)

    await ctx.send('A resposta é: '+ str(response))

@tasks.loop(seconds=60)
async def current_time():
    now = datetime.datetime.now()

    now = now.strftime("%d/%m/%Y as %H:%M:%S")

    channel = bot.get_channel(889198164521926676)

    await channel.send("Data atual: " + now)


current_time.start()
bot.run("ODg5ODU0MTUyOTA4MzQ1MzU0.YUnTQg.7W0UUK68AV8CF_aa8iPlPTSMsI4")
