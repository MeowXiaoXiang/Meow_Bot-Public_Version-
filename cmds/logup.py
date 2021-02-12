import discord
from discord.ext import commands
from core.classes import Cog_Extension
import os
import json
import asyncio

with open('setting.json','r',encoding='utf8') as jset:
    jdata = json.load(jset)

loglist = []
logindex = 0
for logname in os.listdir('./log'):
    if logname.endswith('.log'):
        loglist.append(logindex)
        loglist.append(logname)
        logindex += 1
logindex = 0

class logup(Cog_Extension):
    @commands.command(name= 'loglist', aliases=['列出log' , 'log列表'], brief="admin", description="列出所有機器人攔截到的對話紀錄log檔案清單")
    async def loglist(self,ctx):
        if ctx.author.id == jdata['owner']:
            await ctx.send(f'Log列表\n指令：{jdata["command_prefix"]}downloadlog [編號] ,{ jdata["command_prefix"]}reloadlog')
            msg = ''
            dou = 0
            for i in loglist:
                if dou == 0:
                    msg = msg +" "+ str(i)+ ', '
                    dou+=1
                else:
                    msg = msg + str(i)[:-4] +'\n'
                    dou = 0
            print(msg)
            await ctx.send('```'+msg+'```')

    @commands.command(name= 'reloadlog', aliases=['重載log' , '重新載入log'], brief="admin", description="重新載入log紀錄檔案清單")
    async def reloadlog(self,ctx):
        if ctx.author.id == jdata['owner']:
            global loglist,logindex
            loglist = []
            for logname in os.listdir('./log'):
                if logname.endswith('.log'):
                    loglist.append(logindex)
                    loglist.append(logname)
                    logindex += 1
            await ctx.send('已重新加載')
            logindex = 0

    @commands.command(name= 'downloadlog', aliases=['下載log' , 'log下載'], brief="admin", description="下載log對話紀錄檔案")
    async def downloadlog(self,ctx,index):
        if ctx.author.id == jdata['owner']:
            a = 0
            for i in loglist:
                if i == int(index):
                    print(loglist[a+1]+'\n')
                    fileurl = 'log/'+loglist[a+1]
                    print(fileurl+'\n')
                    await asyncio. sleep(1)
                    upfile = discord.File(F'{fileurl}')
                    await ctx.send(file = upfile)
                a+=1




def setup(bot):
    bot.add_cog(logup(bot))