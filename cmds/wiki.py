import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
from mwclient import Site
from opencc import OpenCC

cc = OpenCC('t2s') #繁體中文 -> 簡體中文

subpage = {"Main":"概述","Prime":"Prime","Abilities":"技能","Equip":"可替換裝備","Patch_History":"更新歷史","Media":"影音資料"}

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class wiki(Cog_Extension):
  @commands.command(name='wiki',aliases=['維基'], brief="warframe", description=f"查詢warframe wiki 使用方法：{jdata['command_prefix']}wiki [你要查詢的東西(可用繁體)]")
  async def wiki(self,ctx,*args):
    try:
      zh = Site('warframe.huijiwiki.com', scheme='https')
      tc = Site('warframe.fandom.com', path='/zh-tw/', scheme='https')
      en = Site('warframe.fandom.com', path='/', scheme='https')
      raw = " ".join(args)
      name = cc.convert(raw)
      page = zh.pages[name]
      if page.exists == False:
        page = tc.pages[name]
        if page.exists == False:
          page = en.pages[name]
          if page.exists == False:
            await ctx.send("頁面不存在，Ordis在等待指揮官為Wiki作出貢獻呢")
            return
          else: 
            page = page.resolve_redirect()
            name = page.name
            url = "https://warframe.fandom.com/wiki/"+name
            footer="英文Fandom"
            host = en
        else:
          page = page.resolve_redirect()
          name = page.name
          url = "https://warframe.fandom.com/zh-tw/wiki/"+name
          footer="繁中Fandom"
          host = tc
      else:
        page = page.resolve_redirect()
        name = page.name
        url = "https://warframe.huijiwiki.com/wiki/"+name
        footer="灰機Wiki"
        host = zh
      url = url.replace(" ","_")
      found = 0
      desc = "以下為嵌入頁面鏈接:\n"
      for items in subpage:
        sub = host.pages[f"{name}/{items}"]
        if sub.exists == True:
          linkURL = url.replace(name,"")+items
          desc += f"[{subpage[items]}]({linkURL})\n"
      if desc == "以下為嵌入頁面鏈接:\n":
        desc = ""
      desc += "以下為相關頁面鏈接:\n"
      for link in page.links():
        if name in link.name:
          linkURL = url.replace(name,"")+link.name.replace(" ","_")
          if found <=5:
            desc += f"[{link.name}]({linkURL})\n"
          found += 1
      if found == 0:
        desc = ""
      embed = discord.Embed(title=name,url=url,description=desc)
      embed.set_footer(text=footer)
      await ctx.send(embed=embed)
    except:
      await ctx.send("目前wiki異常 請稍後再試")


def setup(bot):
    bot.add_cog(wiki(bot))