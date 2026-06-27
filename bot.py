import discord
import random 
# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    if message.content.startswith('$name'):
        await message.channel.send("Hola, mi nombre es Geto Bot y puedo responder comandos de mensaje.")
    if message.content.startswith('$kaoemoji'):
        def gen_kaoemoji():
            kaoemoji = ["(╥﹏╥)", "(˶˃ ᵕ ˂˶)", "(,,>ヮ<,,)", "(,,>﹏<,,)"]
            return random.choice(gen_kaoemoji)
    elif message.content.startswith('$password'):
        def gen_pass(pass_length):
            elements = "+-/*!&$#?=@<>"
            password = ""

            for i in range(pass_length):
                password += random.choice(elements)

            return password
        
        password = gen_pass(10)
        await message.channel.send(password)
    else:
        await message.channel.send(message.content)

client.run("")