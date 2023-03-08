from nextcord import Intents
from nextcord.ext import commands
import os
 
intents = Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="'", intents=intents)

@bot.command(name="hi")
async def SendMessage(ctx):
    await ctx.send('Gabagool')

@bot.event
async def on_ready():
    print("Logged in as : {bot.user.name}")
    
if __name__ == '__main__':
    bot.run(os.environ["DISCORD_TOKEN"])