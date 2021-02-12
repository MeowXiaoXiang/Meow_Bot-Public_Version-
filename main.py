import discord
from discord.ext import commands
import os
import json
import keep_alive
from core.time import time_info #時間戳記 時間 UTC+8
import asyncio
import requests

#os.system('pip install --upgrade pip')
#os.system('pip install --upgrade discord.py')

intents = discord.Intents.all()

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix=jdata["command_prefix"],intents = intents)

@bot.event
async def on_ready():
    print(">> Bot is online <<")
    while(1):
        await asyncio.sleep(60)
        requests.get("http://127.0.0.1:8080/")
#------------------------------------------------------------------------------
bot.remove_command('help') #移除原有的help選單 help選單放在common.py內
#------------------------------help清單-----------------------------------------
#help 使用description來提供描述功能 然後把 brief當作類型(例如當作admin或game或common來分辨)
@bot.command(name="help" , aliases=['幫助' , '機器人功能' , 'HELP'] ,description="機器人功能選單", brief="common")
async def help(ctx, options:str="all"):
  if options == "all":
    helptext="本機器人能夠使用的功能如下（格式：指令 指令說明）：\n普通功能：\n```css\n"
    for command in bot.commands:
      if command.brief == "common":         
        helptext+='{0:12}   {1}\n'.format(jdata['command_prefix'] + str(command), command.description)
    helptext+="```WARFRAME 查詢功能：\n```css\n"
    for command in bot.commands:
      if command.brief == "warframe":         
        helptext+='{0:12}   {1}\n'.format(jdata['command_prefix'] + str(command), command.description)
    helptext+=f"```\n```若要瞭解這些功能的詳細功用 請輸入{jdata['command_prefix']}help [你要查詢的指令]\n管理員指令請打{jdata['command_prefix']}help admin 來查詢\n查詢指令別名{jdata['command_prefix']}help alias```"
    await ctx.send(helptext)
  elif options == "admin":
    helptext="僅限管理員功能：\n```css\n"
    for command in bot.commands:
      if command.brief == "admin":         
        helptext+='{0:12}   {1}\n'.format(jdata['command_prefix'] + str(command), command.description)
    helptext+="```"
    await ctx.send(helptext)
  elif options == "alias":
    helptext="本機器人能夠使用的功能如下（格式：指令 別名）：\n普通功能：\n```css\n"
    for command in bot.commands:
      if command.brief == "common":         
        helptext+='{0:12}   {1}\n'.format(jdata['command_prefix'] + str(command), command.aliases)
    helptext+="```WARFRAME 查詢功能：\n```css\n"
    for command in bot.commands:
      if command.brief == "warframe":         
        helptext+='{0:12}   {1}\n'.format(jdata['command_prefix'] + str(command), command.aliases)
    helptext+="```管理員指令：\n```css\n"
    for command in bot.commands:
      if command.brief == "admin":         
        helptext+='{0:12}   {1}\n'.format(jdata['command_prefix'] + str(command), command.aliases)
    helptext+="```"
    await ctx.send(helptext)


#-----------------以下為機器人基本模組載入卸載列出下載功能區域建議不要隨意更改------------
#列出所有此機器人的Python模組 cmds 內的
@bot.command(name= 'listmod', aliases=['列出所有模組' , '列出模組'], brief="admin", description = "此功能可以列出機器人的所有模組")
async def listmodel(ctx):
  modlist = []
  modindex = 0
  for modname in os.listdir('./cmds'):
      if modname.endswith('.py'):
          modlist.append(modindex)
          modlist.append(modname)
          modindex += 1
  modindex = 0
  msg = ''
  dou = 0
  for i in modlist:
      if dou == 0:
          dou+=1
      else:
          msg = msg + '[' + str(i)[:-3] +']'
          dou = 0
  await ctx.send(f'```ini\n此機器人目前擁有的所有模組：\n{msg}```')
#把模組的原始Python檔案下載
@bot.command(name= 'downloadmod', aliases=['下載模組' , '模組下載' , '下載mod' , 'mod下載'], brief="admin", description = f"此功能可以下載機器人的模組\n用法為：{jdata['command_prefix']}downloadmod [模組名稱]")
async def downloadmod(ctx, *args):
    if ctx.author.id == jdata['owner']:
        mod = ' '.join(args)
        if mod == ():
            await ctx.send(NullMod())
        else:
            try:
                fileurl = 'cmds/' + mod + '.py'
                print(fileurl+'\n')
                await asyncio.sleep(0.5)
                upfile = discord.File(F'{fileurl}')
                await ctx.send(file = upfile)
            except:
                await ctx.send('錯誤：無法下載模組')

@bot.command(name= 'load', aliases=['載入' , '載入模組' , '啟用'], brief="admin", description = f"此功能為載入機器人模組使用\n用法為：{jdata['command_prefix']}load [模組名稱]")
async def load(ctx, extension:str ='Null'):
  if ctx.author.id == jdata['owner']:
    if extension == 'Null':
      await ctx.send(NullMod())
    else:
      bot.load_extension(F'cmds.{extension}')
      await ctx.send(f'\n已加載：{extension}')
      print('\n---------------------------------\n' + time_info.time_converter() + f'\n已加載 {extension}\n---------------------------------\n')
  else:
      await ctx.send(InsufficientPermissions())

@bot.command(name= 'unload', aliases=['卸載' , '卸載模組' , '停用'], brief="admin", description = f"此功能為停用機器人模組使用\n用法為：{jdata['command_prefix']}unload [模組名稱]")
async def unload(ctx, extension:str='Null'):
  if ctx.author.id == jdata['owner']:
    if extension == 'Null':
      await ctx.send(NullMod())
    else:
      try:
        bot.unload_extension(F'cmds.{extension}')
        await ctx.send(f'\n已卸載：{extension}')
        print('\n---------------------------------\n' + time_info.UTC_8() + f'\n已卸載 {extension}\n---------------------------------\n')
      except:
        await ctx.send("錯誤：組件卸載失敗")
  else:
      await ctx.send(InsufficientPermissions())


@bot.command(name= 'reload', aliases=['重載' , '重載模組' , '重新載入模組', '重新加載', '重啟' , '重新載入'], brief="admin", description = f"此功能為重啟機器人模組使用\n用法為：{jdata['command_prefix']}reload [模組名稱]")
async def reload(ctx, extension:str ='Null'):
  if ctx.author.id == jdata['owner']:
    if extension == 'Null':
      await ctx.send(NullMod())
    else:
      bot.reload_extension(F'cmds.{extension}')
      await ctx.send(f'\n已重新載入：{extension}')
      print('\n---------------------------------\n' + time_info.UTC_8() + f'\n已重新載入 {extension}\n---------------------------------\n')
  else:
      await ctx.send(InsufficientPermissions())



#機器人關閉系統--------------------------------------------   

@bot.command(name= 'disconnect', aliases=['disable' , 'shutdown' , '關閉機器人' , '關機' , '關閉'], brief="admin", description = "此功能為關閉機器人")
async def turn_off_bot(ctx):
  if ctx.message.author.id == jdata['owner']:
    print(f"-----------------------------------------\n{time_info.UTC_8()}\n機器人已關閉" + "\n-----------------------------------------")
    await ctx.send(time_info.UTC_8() + '\n機器人已關閉') #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    await bot.close()
  else:
    await ctx.send(InsufficientPermissions())

@bot.event
async def on_disconnect():
    requests.get("http://127.0.0.1:8080/")
    fp = open('./log/' + 'System.log', 'a',encoding='utf8')
    fp.write(f"{time_info.UTC_8()}\n------機器人已關閉------\n")
    print(f"-----------------------------------------\n{time_info.UTC_8()}\n機器人已關閉" + "\n-----------------------------------------")
    fp.close()
#---------------------------------------------------------

class InsufficientPermissions(Exception):
  def __str__(self):
    return '權限不足 本指令只提供給機器人擁有者 \n擁有者為 <@' + jdata["owner"] + '>'
class NullMod(Exception):
  def __str__(self):
    return '此處不可為空 請輸入組件名稱'

#系統錯誤紀錄
@bot.event
async def on_command_error(ctx, error):
    fp = open('./log/' + 'System.log', 'a',encoding='utf8')
    fp.write(f"{time_info.UTC_8()}\n錯誤（ERROR）：\n" + str(error) + "\n")
    print(f"-----------------------------------------\n{time_info.UTC_8()}錯誤（ERROR）：\n" + str(error) + "\n-----------------------------------------")
    fp.close()
    
#------------把cmd內的所有模組做載入--------------
for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')
       
if __name__ == "__main__":
    keep_alive.keep_alive()
    bot.run(jdata['TOKEN'])
