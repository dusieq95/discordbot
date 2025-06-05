from discord.ext import commands
path="cogs.sra."
exts =["img"]
from shapesinc import AsyncRoute as Rt
from urllib.parse import urlencode as ufmt

BASE=Rt.__class__("https://api.some-random-api.com/")

class SRA(commands.Cog):
  def __init__(self, bot): self.bot = bot

  async def fetch(self, p: str, params: dict = {}, json=True):
    p=p.lstrip("/") or "/"
    if params: p=p+"?"+ufmt(params)
    return await (BASE/p).request("GET",is_json=json)
    
async def setup(bot: commands.Bot):
  for ext in exts:
    for k, v in __import__(path+ext).exports.items():
      setattr(SRA,k,v)

  await bot.add_cog(SRA(bot))
  
async def teardown(bot: commands.Bot):...
  await bot.remove_cog("SRA")
