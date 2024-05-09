import discord

intents = discord.Intents.default()

intents.message_content = True

client = discord.Client(intents=intents)


import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$merhaba'):
        await message.channel.send("Selam!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\\U0001f642")
    elif message.content.startswith("$şifre"):
        await message.channel.send(gen_pass(8))
    elif message.content.startswith("$coinflip"):
        await message.channel.send(yazi_tura())
    else:
        await message.channel.send(message.content)

def yazi_tura():
    para = random.randint(0, 2)
    if para == 0:
        return "YAZI"
    else:
        return "TURA"

client.run("")
