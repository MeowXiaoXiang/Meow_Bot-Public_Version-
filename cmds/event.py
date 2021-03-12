from discord.ext import commands
from core.classes import Cog_Extension
from core.time import time_info
from datetime import datetime,timedelta
import json

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)


class event(Cog_Extension):
  @commands.Cog.listener()
  async def on_message(self,msg):
    tag = "common"
    if str(msg.channel.type) == 'private' and msg.author != self.bot.user:
        print(time_info.UTC_8() + str(msg.author) + '說:' + msg.content)
        '''
        下面那兩行是當有人密機器人訊息 機器人就會轉寄訊息給owner 怕給太多人困擾預設關閉 要使用的把註解"#"拔掉
        '''
        #own = self.bot.get_user(int(jdata['owner']))
        #await own.send(time_info.UTC_8_CH() + '\n' + str(msg.author) + '說：' + msg.content+'\n')
        fp = open('./log/' + 'Private.log', 'a',encoding='utf8')
        fp.write(time_info.UTC_8() + str(msg.author) + '說：' + msg.content+'\n')
        fp.close()
    else:
        if str(msg.channel.type) == 'text' and msg.author != self.bot.user:
            print(time_info.UTC_8_CH() + str(msg.author) + '說:' + msg.content)
            a = str(msg.guild)
            b = str(msg.channel)
            fp = open('./log/' + a + '-' + b + '.log', 'a',encoding='utf8')
            fp.write(time_info.UTC_8() + str(msg.author) + '說:' + msg.content+'\n')
            fp.close()
    pass

def setup(bot):
    bot.add_cog(event(bot))