import discord
import asyncio
import random

memecount = 0
memes = []
client = discord.Client()

@asyncio.coroutine
@client.event
async def on_message(message):
	if message.content == '!corby help':
		await client.send_message(message.channel, content=helpContent())
	elif message.content.startswith('!corby nc'):
		test = message.content
		serv = message.server
		whatevs, command, name, change = test.split(" ")
		await client.change_nickname(serv.get_member_named(name), change)
	elif message.content == '!corby rock':
		x = random.randint(1,3)
		if x == 1:
			await client.send_message(message.channel, content='Bot chose rock: Tie')
		elif x == 2:
			await client.send_message(message.channel, content='Bot chose paper: You Lose')
		elif x == 3:
			await client.send_message(message.channel, content='Bot chose scissors: You Win')
	elif message.content == '!corby paper':
		x = random.randint(1,3)
		if x == 1:
			await client.send_message(message.channel, content='Bot chose rock: You Win')
		elif x == 2:
			await client.send_message(message.channel, content='Bot chose paper: Tie')
		elif x == 3:
			await client.send_message(message.channel, content='Bot chose scissors: You Lose')
	elif message.content == '!corby scissors':
		x = random.randint(1,3)
		if x == 1:
			await client.send_message(message.channel, content='Bot chose rock: You Lose')
		elif x == 2:
			await client.send_message(message.channel, content='Bot chose paper: You Win')
		elif x == 3:
			await client.send_message(message.channel, content='Bot chose scissors: Tie')
	elif message.content.startswith('!corby tts'):
		test = message.content
		author = message.author
		whatevs, command, texttospeech = test.split(" ", 2)
		vc = await client.join_voice_channel(author.voice_channel)
		await client.send_message(message.channel, content=texttospeech, tts=True)
		await vc.disconnect()
	elif message.content == '!corby what game?' or message.content == '!corby what game? tts':
		ts = False
		if message.content == '!corby what game? tts':
			ts = True
		game = gameChoose()
		await client.send_message(message.channel, content=game, tts=ts)
	elif message.content == '!corby meme':
		await client.send_message(message.channel, content=generateMeme())
	elif message.content.startswith('!corby addmeme'):
		test = message.content
		whatevs, command, memeToAdd = test.split(" ", 2)
		addMeme(memeToAdd)
	#	player = await vc.create_ffmpeg_player('vent.wav', after=lambda: player.disconnect())
	#	player.start()
		
def gameChoose():
		x = random.randint(1, 9)
		if x == 1:
			return "PUBG"
		elif x == 2:
			return "Counter Strike"
		elif x == 3:
			return "Overwatch"
		elif x == 4:
			return "Golf with friends"
		elif x == 5:
			return "Hand Simulator"
		elif x == 6:
			return "GTA V"
		elif x == 7:
			return "Garrys mod"
		elif x == 8:
			return "Civilization V"
		elif x == 9:
			return "Warframe"
			
def addMeme(memeToAdd):
	global memecount
	global memes
	memes.append(memeToAdd)
	memecount += 1
	
def generateMeme():
	global memes
	global memecount
	if memecount > 0:
		x = random.randint(1, memecount)
		return memes[x - 1]
	else:
		return 'no memes available'
			
def helpContent():
	x = 'Try these commands:\n'
	x += '1. !corby nc "nickname to change" "nickname to be changed to"\n'
	x += '2. !corby "rock" or "paper" or "scissors"\n'
	x += '3. !corby tts "your message" (for a text to speech message)\n'
	x += '4. !corby what game? or !corby what game? tts\n'
	x += '5. !corby addmeme (link meme here)\n'
	x += '6. !corby meme (to generate meme)'
	return x
		

