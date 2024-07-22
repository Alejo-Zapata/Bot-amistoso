import discord
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
        await message.channel.send("See you next time")
    elif message.content.startswith('$do you want to be my friend?'):
        await message.channel.send("Of course")
    elif message.content.startswith('$which days are you avaible?'):
        await message.channel.send("All days you need me")
    elif message.content.startswith('$how are you today?'):
        await message.channel.send("Happy to be talking with you")
    elif message.content.startswith('$dime una adivinanza'):
        await message.channel.send("¿Qué se encuentra una vez en un minuto, dos veces en un momento pero ninguno en cien años?")
    elif message.content.startswith("$meme"):
        await message.channel.send(file=discord.File("M1L2/Bot/meme.jpg"))
    elif message.content.startswith("$discord leave"):
        await message.channel.send(file=discord.File("M1L2\Bot\discord-leave.mp3"))
    elif message.content.startswith('$dime una problematica'):
        await message.channel.send("contaminacion del aire, que se refiere a la presencia en los diversos estratos de aire que integran la atmósfera terrestre, de materiales y formas de energía que no forman parte de su composición natural y que representan una potencial fuente de daños y molestias para la vida, al acarrear reacciones químicas impredecibles e inconvenientes.")
    elif message.content.startswith('$por que es malo?'):
        await message.channel.send("Este tipo de contaminación es una de las más graves para el planeta, por las implicaciones que tiene, ya que deteriora la calidad del aire que respiramos, degrada la capa de ozono, es parte responsable del calentamiento global.")
    elif message.content.startswith('$dime una solucion'):
        await message.channel.send("Ser sostenibles, por ejemplo usar mas la bicicleta que el carro, usar energias renovables como solar y eolica, prevenir la deforestacion y plantar mas arboles que ayudan a reducir el dioxido de carbono")
    elif message.content.startswith("$bicicleta"):
        await message.channel.send(file=discord.File("M1L2/Bot/bicicleta.jpg"))
    elif message.content.startswith("$energias renovables"):
        await message.channel.send(file=discord.File("M1L2\Bot\energias-renovables.jpg"))
    elif message.content.startswith("$arbol"):
        await message.channel.send(file=discord.File("M1L2/Bot/arbol.jpg"))
    else:
        await message.channel.send(message.content)
client.run("")
