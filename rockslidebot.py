import os
import random

import discord

token = os.getenv('DISCORD_TOKEN')

class RockSlideClient(discord.Client):
  async def on_message(self, message):
      if self.user.id == message.author.id:
          return
      if "dynamax" in [role.name.lower() for role in message.author.roles]:
          print('The flinch was blocked by the power of Dynamax!')
          return
      if random.randrange(10) >= 3:
          return
      await message.delete()
      await message.channel.send(message.author.mention + ' flinched and couldn\'t post!')

if __name__ == '__main__':
    client = RockSlideClient()
    client.run(token)

