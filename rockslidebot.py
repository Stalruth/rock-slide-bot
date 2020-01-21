import os
import random

import discord

token = os.getenv('DISCORD_TOKEN')

class CustomClient(discord.Client):
  async def on_message(self, message):
      if self.user.id != message.author.id:
          if random.randrange(10) < 3:
              await message.delete()
              await message.channel.send(message.author.mention + ' flinched and couldn\'t post!')

client = CustomClient()
client.run(token)

