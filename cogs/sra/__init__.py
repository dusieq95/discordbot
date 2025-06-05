from discord.ext import commands

from shapesinc import AsyncRoute as Rt
from urllib.parse import urlencode as ufmt

from .img import img_cmd, filter_cmd, tweet_cmd, comment_cmd, mask_cmd



BASE=Rt.__class__("https://api.some-random-api.com/")

class SRA(commands.Cog):
  def __init__(self, bot): self.bot = bot

  async def fetch(self, p: str, params: dict = {}, json=True):
    p=p.lstrip("/") or "/"
    if params: p=p+"?"+ufmt(params)
    return await (BASE/p).request("GET",is_json=json)
    
  urlfmt=staticmethod(ufmt)
    
    
  img=img_cmd
  filter=filter_cmd
  tweet=tweet_cmd
  comment=comment_cmd
  mask=mask_cmd

async def setup(bot: commands.Bot):
  await bot.add_cog(SRA(bot))
  
async def teardown(bot: commands.Bot):
  await bot.remove_cog("SRA")
