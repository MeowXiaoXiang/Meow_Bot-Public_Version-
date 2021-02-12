import discord
from discord.ext import commands
from core.classes import Cog_Extension
import requests
import json
from opencc import OpenCC
from datetime import datetime
from operator import itemgetter

cc = OpenCC('s2twp') #簡體中文 -> 繁體中文 (台灣, 包含慣用詞轉換)

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class worldstate(Cog_Extension):
  @commands.command(name='poe',aliases=['夜靈平原時間' , '夜靈平原' , '希圖斯時間' , '希圖斯' , 'POE' , 'cetus' , 'Cetus'], brief="warframe", description="查詢夜靈平野(希圖斯)的時間")
  async def eidolontime(self,ctx):
    try:
      html = requests.get('https://api.warframestat.us/pc/cetusCycle',headers={'Accept-Language':'tc','Cache-Control': 'no-cache'}).text
      data = json.loads(html)
      h = int(data["expiry"][11:13]) + 8
      m = data["expiry"][14:16]
      m = ("0" if len(m) == 1 else "") + m
      s = data["expiry"][17:19]
      s = ("0" if len(s) == 1 else "") + s
      timeLeft = data['timeLeft'].replace("h","小時").replace("m","分鐘").replace("s","秒")
      if (data["state"]=="day"):
        poeEmbed = discord.Embed(title="夜靈平原-早上☀", description=F"夜靈平原晚上將於 {h}:{m} 開始\n距離夜靈平原晚上還有：{timeLeft}", color=0xf6c10c)
        poeIcon = "https://i.imgur.com/HFjX0xz.png"
      elif (data["state"]=="night"):
        poeEmbed = discord.Embed(title="夜靈平原-晚上🌙", description=F"夜靈平原早上將於 {h}:{m} 開始\n距離夜靈平原早上還有：{timeLeft}", color=0x2e91ec)
        poeIcon = "https://i.imgur.com/XUgoXKq.png"
        
      poeEmbed.set_footer(text=F"Requested by {ctx.author.name}",icon_url=ctx.author.avatar_url)
      poeEmbed.set_thumbnail(url=poeIcon)
      await ctx.send(embed=poeEmbed)
    except:
      await ctx.send(worldstate.FunctionFail())

  @commands.command(name='earth',aliases=['地球時間' , '地球' , 'Earth'], brief="warframe", description="查詢地球的時間")
  async def earthtime(self,ctx):
    try:
      html = requests.get('https://api.warframestat.us/pc/tc/earthCycle',headers={'Accept-Language':'tc','Cache-Control': 'no-cache'}).text
      data = json.loads(html)
      h = int(data["expiry"][11:13]) + 8
      m = data["expiry"][14:16]
      m = ("0" if len(m) == 1 else "") + m
      s = data["expiry"][17:19]
      s = ("0" if len(s) == 1 else "") + s
      timeLeft = data['timeLeft'].replace("h","小時").replace("m","分鐘").replace("s","秒")
      if (data["state"]=="day"):
        earthEmbed = discord.Embed(title="地球-早上☀", description=F"地球晚上將於 {h}:{m} 開始\n距離地球晚上還有：{timeLeft}", color=0xf6c10c)
        earthIcon = "https://i.imgur.com/wixFlzS.jpg"
      elif (data["state"]=="night"):
        earthEmbed = discord.Embed(title="地球-晚上🌙", description=F"地球早上將於 {h}:{m} 開始\n距離地球早上還有：{timeLeft}", color=0x2e91ec)
        earthIcon = "https://i.imgur.com/otNlXLG.jpg"

      earthEmbed.set_footer(text=F"Requested by {ctx.author.name}",icon_url=ctx.author.avatar_url)
      earthEmbed.set_thumbnail(url=earthIcon)
      await ctx.send(embed=earthEmbed)
    except:
      await ctx.send(worldstate.FunctionFail())

  @commands.command(name='Deimos',aliases=['魔裔禁地時間' , '火衛二' , '火衛二時間' , 'deimos'], brief="warframe", description="查詢魔裔禁地(火衛二)的時間")
  async def deimostime(self,ctx):
    try:
      html = requests.get('https://api.warframestat.us/pc/cetusCycle',headers={'Accept-Language':'tc','Cache-Control': 'no-cache'}).text
      data = json.loads(html)
      h = int(data["expiry"][11:13]) + 8
      m = data["expiry"][14:16]
      m = ("0" if len(m) == 1 else "") + m
      s = data["expiry"][17:19]
      s = ("0" if len(s) == 1 else "") + s
      timeLeft = data['timeLeft'].replace("h","小時").replace("m","分鐘").replace("s","秒")
      if (data["state"]=="day"):
        deimosEmbed = discord.Embed(title="魔裔禁地-Fass", description=F"魔裔禁地Vome將於 {h}:{m} 開始\n距離魔裔禁地Vome還有：{timeLeft}", color=0xf6c10c)
        deimosIcon = "https://i.imgur.com/BBmvDM5.png"
      elif (data["state"]=="night"):
        deimosEmbed = discord.Embed(title="魔裔禁地-Vome", description=F"魔裔禁地Fass將於 {h}:{m} 開始\n距離魔裔禁地Fass還有：{timeLeft}", color=0x2e91ec)
        deimosIcon = "https://i.imgur.com/iHmnpR2.png"
        
      deimosEmbed.set_footer(text=F"Requested by {ctx.author.name}",icon_url=ctx.author.avatar_url)
      deimosEmbed.set_thumbnail(url=deimosIcon)
      await ctx.send(embed=deimosEmbed)
    except:
      await ctx.send(worldstate.FunctionFail())

  @commands.command(name='Orb',aliases=['奧布山谷時間' , '奧布山谷' , '福爾圖娜' , '福爾圖娜時間' , 'orb' , 'fortuna' , 'Fortuna'], brief="warframe", description="查詢奧布山谷(福爾圖娜)的時間")
  async def orbtime(self,ctx):
    try:
      html = requests.get('https://api.warframestat.us/pc/vallisCycle',headers={'Accept-Language':'tc','Cache-Control': 'no-cache'}).text
      data = json.loads(html)
      h = int(data["expiry"][11:13]) + 8
      m = data["expiry"][14:16]
      m = ("0" if len(m) == 1 else "") + m
      s = data["expiry"][17:19]
      s = ("0" if len(s) == 1 else "") + s
      timeLeft = data['timeLeft'].replace("h","小時").replace("m","分鐘").replace("s","秒")
      if (data["state"]=="cold"):
        orbEmbed = discord.Embed(title="奧布山谷-寒冷:snowflake: ", description=F"奧布山谷溫暖將於 {h}:{m} 開始\n距離奧布山谷溫暖還有：{timeLeft}", color=0xf6c10c)
        orbIcon = "https://i.imgur.com/8Ne96ou.jpg"
      elif (data["state"]=="warm"):
        orbEmbed = discord.Embed(title="奧布山谷-溫暖:sunny: ", description=F"奧布山谷寒冷將於 {h}:{m} 開始\n距離奧布山谷寒冷還有：{timeLeft}", color=0x2e91ec)
        orbIcon = "https://i.imgur.com/I4ipQ0b.jpg"
        
      orbEmbed.set_footer(text=F"Requested by {ctx.author.name}",icon_url=ctx.author.avatar_url)
      orbEmbed.set_thumbnail(url=orbIcon)
      await ctx.send(embed=orbEmbed)
    except:
      await ctx.send(worldstate.FunctionFail())

  #突擊
  @commands.command(name='sortie', aliases=['突擊' , '突襲' , 'Sortie'], brief="warframe", description="查詢每日突擊")
  async def sortie(self,ctx):
    try:
      count = 1
      raw = requests.get('https://api.warframestat.us/pc/zh/sortie',headers={'Accept-Language':'tc'})
      text = cc.convert(raw.text)
      data = json.loads(text)
      sortieIcon="https://i.imgur.com/WC9F8pE.png"
      sortie_embed=discord.Embed(title="突擊", description=F"突擊剩餘時間：{data['eta']}\n{data['boss']} 的部隊，{data['faction']}陣營", color=0xff9500)
      for missions in data['variants']:
        node = missions['node']
        missionType= missions['missionType']
        modifier = missions['modifier']
        sortie_embed.add_field(name=F"突擊 [{count}]", value=F"節點：{node} 等級：[{35+15*count} ~ {40+20*count}]\n任務：**{missionType}**\n狀態：**{modifier}**", inline=False)
        count += 1
      sortie_embed.set_footer(text=F"Requested by {ctx.author.name}",icon_url=ctx.author.avatar_url)
      sortie_embed.set_thumbnail(url=sortieIcon)
      await ctx.send(embed=sortie_embed)
    except:
      await ctx.send(worldstate.FunctionFail())

  #仲裁
  @commands.command(name="arbitration",aliases=['仲裁'], brief="warframe", description="查詢仲裁任務(API不穩定)")
  async def arbitration(self,ctx):
    try:
      raw = requests.get("https://api.warframestat.us/pc/tc/arbitration",headers={'Accept-Language':'zh'})
      text = raw.text
      text = cc.convert(raw.text)
      data = json.loads(text)
      expiry = data['expiry']
      timeLeft = datetime.strptime(expiry,'%Y-%m-%dT%X.000Z')
      now = datetime.now()
      timeLeft = timeLeft-now
      minutes = int((timeLeft.seconds - timeLeft.seconds%60)/60)
      seconds = timeLeft.seconds%60
      await ctx.send(f"```\n當前仲裁任務(API並不穩定，僅供參考):\n任務:{data['type']}\n節點:{data['node']}\n敵人:{data['enemy']}\n剩餘時間:{minutes}分鐘{seconds}秒```")
    except:
      await ctx.send(worldstate.FunctionFail())

  #午夜電波
  @commands.command(name='nightwave', aliases=['午夜電波' , '電波' ], brief="warframe", description="查詢午夜電波")
  async def nightwave(self,ctx):
    try:
      raw = requests.get('https://api.warframestat.us/pc/tc/nightwave',headers={'Accept-Language':'zh'})
      text = cc.convert(raw.text)
      data = json.loads(text)
      nightwaveIcon="https://i.imgur.com/vQgZfYO.png"
      Night_embed=discord.Embed(title="午夜電波", color=0x042f66)
      if data['active'] == True:
        for nightwaveChallenge in data['activeChallenges']:
          if nightwaveChallenge['active'] == True:
            missionType = ""
            reputation = int(nightwaveChallenge['reputation'])
            title = nightwaveChallenge['title']
            desc = nightwaveChallenge['desc']
            if "isDaily" in nightwaveChallenge:
              missionType = "每日"
            elif reputation == 4500:
              missionType = "每週"
            else:
              missionType = "每週菁英"
            Night_embed.add_field(name=F"{title}({missionType})", value=F"{desc}\n聲望：{reputation:,}", inline=False)
          elif nightwaveChallenge['active'] == False:
            continue
      elif data['active'] == False:
        Night_embed.add_field(name="狀態", value="目前關閉中...", inline=False)
      Night_embed.set_footer(text=F"Requested by {ctx.author.name}",icon_url=ctx.author.avatar_url)
      Night_embed.set_thumbnail(url=nightwaveIcon)
      await ctx.send(embed=Night_embed)
    except:
      await ctx.send(worldstate.FunctionFail())

  @commands.command(name='fissure', aliases=['虛空裂縫' , '裂縫' , '遺物'], brief="warframe", description="查詢現在可以打的裂縫(開遺物)任務列表")
  async def fissurelist(self,ctx):
    try:
      raw = requests.get('https://api.warframestat.us/pc/fissures',headers={'Accept-Language':'zh','Cache-Control': 'no-cache'})
      text = raw.text
      text = cc.convert(text)
      fissuresNotSort = json.loads(text)
      fissurePic = "https://i.imgur.com/erITsjd.png"
      fissures = sorted(fissuresNotSort, key=itemgetter('tierNum'))
      #https://blog.csdn.net/qq_23564667/article/details/106287575

      Fissure_embed=discord.Embed(title="遺物", description="目前可以打的任務列表", color=0xb59954)

      for fissure in fissures:
        if fissure['expired'] == True:
          pass
        
        node = fissure['node']
        missionType = fissure['missionType']
        tier = fissure['tier']
        tier = tier.replace("安魂","鎮魂")

        eta = fissure['eta']
        eta = eta.replace("h","小時")
        eta = eta.replace("m","分鐘")
        eta = eta.replace("s","秒")
        description=F"階級：**{tier}**\n任務：**{missionType}**\n剩餘時間：{eta}"
        Fissure_embed.add_field(name=node, value=description, inline=False)

      Fissure_embed.set_footer(text=F"Requested by {ctx.author.name}",icon_url=ctx.author.avatar_url)
      Fissure_embed.set_thumbnail(url=fissurePic)
      await ctx.send(embed=Fissure_embed)
    except:
      await ctx.send(worldstate.FunctionFail())


  class FunctionFail(Exception):
    def __str__(self):
      return '該功能目前無法使用'

def setup(bot):
    bot.add_cog(worldstate(bot))
