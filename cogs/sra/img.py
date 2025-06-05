from discord.ext import commands

class export:
  @commands.command(aliases=["image"])
  async def img(self, ctx, of: str = ""):
    opts=['fox', 'cat', 'bird', 'panda', 'red_panda', 'pikachu', 'racoon', 'koala', 'kangaroo', 'whale', 'dog', 'bird']
    of=of.lower()
    if (not of) or of not in opts:
      return await ctx.send(
        "Available types:\n```\n"+"\n".join(opts)+"\n```"
      )

    return await ctx.send(
      await self.fetch(of)
    )


exports = {"img": export.img}
