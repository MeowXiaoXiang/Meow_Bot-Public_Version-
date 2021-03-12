import json
from discord.ext import commands
from core.classes import Cog_Extension

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class wf(Cog_Extension):
    tag = "Warframe"
     #近戰有塞急進猛突12x下的暴擊機率計算器
    @commands.command(name='ccc', aliases=['急進猛突' , '急進' , '極盡'], brief="計算塞急進猛突後暴率", description=f"計算放入急進猛突MOD後的暴率 可以自定義連擊和額外加乘\n使用方法：{jdata['command_prefix']}ccc 基礎近戰暴率 連擊數 額外暴率加成\n[請用空格隔開]")
    async def ccc(self,ctx,*,num='CCC'):
      try:
        i1, i2, i3 = num.split(' ')
        if int(i2) <= 13:
          sum= float(i1) * ( 100 + 60 * ( float(i2) - 1 ) + float(i3) )  / 100
          #總暴率=基礎暴率× (1 + 急進猛突的加成 × (連擊倍率-1)+其他暴擊加成)
          await ctx.send('近戰總爆擊機率：' + str(sum) + '%')
        else:
          await ctx.send('連擊最高只有到13x啦！')
      except:
        await ctx.send(jdata['command_prefix']+'ccc 基礎近戰暴率 連擊數 額外暴率加成')
    #----------------------------------
    #近戰有塞創口潰爛12x下的觸發機率計算器    
    @commands.command(name= 'wws', aliases=['創口潰爛' , '創口'], brief="計算塞創口潰爛後觸發", description=f"計算放入急進猛突MOD後的觸發率 可以自定義連擊和額外加成\n使用方法：{jdata['command_prefix']}wws [基礎近戰觸發] [連擊數] [額外觸發加成]")
    async def wws(self,ctx,*,num='WWS'):
      try:
        i1, i2, i3 = num.split(' ')
        if int(i2) <= 13:
          sum= float(i1) * ( 100 + 40 * ( float(i2) - 1 ) + float(i3) )  / 100
          #總觸發=基礎觸發× (1 + 觸發加成 × (連擊倍率-1)+其他觸發加成)
          await ctx.send('近戰總觸發機率：' + str(sum) + '%')
        else:
          await ctx.send('連擊最高只有到13x啦！')
      except:
        await ctx.send(jdata['command_prefix']+'wws 基礎近戰觸發 連擊數 額外觸發加成')

    #環形裝置
    @commands.command(name='toroid',aliases=['環形裝置'], brief="顯示環形裝置出處", description='顯示環形裝置出處')
    async def toroid(self,ctx):
      await ctx.send('```維加環形裝置→太空站          & 微蟎蛛型機\n告達環形裝置→昇華實驗室      & 賽托蛛型機(瓦內蜘蛛)\n索拉環形裝置→潤盈寺          & 凱塔蛛型機\n聖油環形裝置→利潤收割者圓蛛\n天藍環形裝置→剝削者圓蛛```')

    

def setup(bot):
    bot.add_cog(wf(bot))