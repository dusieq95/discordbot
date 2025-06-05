exts = ["ai", "sra"]
async def setup(bot: commands.Bot):
  """Function to load the cog"""
  for ext in exts:
    ext="cogs."+ext
    await bot.load_extension(ext)

async def teardown(bot: commands.Bot):
  """Function to unload the cog"""
  for ext in exts:
    ext="cogs."+ext
    await bot.unload_extension(ext)
