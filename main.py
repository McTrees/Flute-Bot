#Import libraries
import discord #The Discord API
import asyncio #Used for await and async
from discord.ext import commands #Used to define commands and some other things

#Import other dependencies created by Ben
import credentials #The Bot's Secret Key
import sys
import os
import flutes
import botobject

bot = botobject.bot #import the bot object
   
bot.run(credentials.BotSecret) #run bot