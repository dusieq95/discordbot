from discord.ext import commands
import discord


class export:
  @commands.command(aliases=["image"])
  async def img(self, ctx, of: str = ""):
    opts=['fox', 'cat', 'birb', 'panda', 'red_panda', 'pikachu', 'racoon', 'koala', 'kangaroo', 'whale', 'dog', 'bird']
    of=of.lower()
    if (not of) or of not in opts:
      return await ctx.reply(
        "Available types:\n```\n"+"\n".join(opts)+"\n```"
      )

    return await ctx.reply(
      (await self.fetch("img/"+of))["link"]
    )
    
  @commands.command(name="filter")
  async def filter_cmd(self, ctx, filter: str = "", user: discord.User = None):
    opts="blue blurple pixelate blur blurple2 green greyscale invert red invertgreyscale sepia".split(" ")
    filter=filter.lower().replace("gray", "grey")
    if (not filter) or filter not in opts:
      return await ctx.reply(
        "Available types:\n```\n"+"\n".join(opts)+"\n```"
      )
    im=""
    if user and user.avatar:
      im=user.avatar.url
    if im:...
    elif ctx.message.attachments:
      for m in ctx.message.attachments:
        if m.content_type=="image/png":
          im=m.url
          break
      if not im:
        return await ctx.reply("Only pmg format is supported!")
    elif ctx.author.avatar and ctx.author.avatar.url:
      im=ctx.author.avatar.url
      
    if not im:
      return await ctx.reply('Couldnt find an image!')
      
    return await ctx.reply("https://api.some-random-api.com/canvas/filter/"+filter+"?"+self.urlfmt(dict(avatar=im)))
    
  @commands.command(name="mask")
  async def mask_cmd(self, ctx, mask: str = "", user: discord.User = None):
    opts="circle heart horny lied lolice simpcard tonikawa".split(" ")
    mask=mask.lower()
    if (not mask) or mask not in opts:
      return await ctx.reply(
        "Available types:\n```\n"+"\n".join(opts)+"\n```"
      )
    im=""
    if user and user.avatar:
      im=user.avatar.url
    if im:...
    elif ctx.message.attachments:
      for m in ctx.message.attachments:
        if m.content_type=="image/png":
          im=m.url
          break
      if not im:
        return await ctx.reply("Only pmg format is supported!")
    elif ctx.author.avatar and ctx.author.avatar.url:
      im=ctx.author.avatar.url
      
    if not im:
      return await ctx.reply('Couldnt find an image!')
      
    return await ctx.reply("https://api.some-random-api.com/canvas/misc/"+mask+"?"+self.urlfmt(dict(avatar=im)))
    
  @commands.command()
  async def tweet(self, ctx, *tweet: str):
    tweet=" ".join(tweet)
    return await ctx.reply("https://api.some-random-api.com/canvas/misc/tweet?"+self.urlfmt(dict(
      displayname=ctx.author.display_name,
      username=ctx.author.name,
      comment=tweet,
      avatar=ctx.author.avatar.url,
      theme="dark"
    )))
    
  @commands.command()
  async def comment(self, ctx, *comment: str):
    comment=" ".join(comment)
    return await ctx.reply("https://api.some-random-api.com/canvas/misc/youtube-comment?"+self.urlfmt(dict(
      username=ctx.author.name,
      comment=comment,
      avatar=ctx.author.avatar.url,
      theme="dark"
    )))
    
img_cmd=export.img
mask_cmd=export.mask_cmd
filter_cmd = export.filter_cmd
tweet_cmd = export.tweet
comment_cmd = export.comment
# exports = {"img": img}
