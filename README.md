# Meow_Bot-Public_Version-

這些為需要安裝的套件 有部分是`lonnstyle/DiscordBotMods`內所需要的

+ pip install flask
+ pip install mwclient
+ pip install chinese_converter
+ pip install discord
+ pip install discord.py
+ pip install loguru
+ pip install discord-webhook

此版本直接把一堆不該有的東西清理過了 為乾淨版本(可能會漏刪)

若要用上新的help選單 請把 @bot.command() 或者是 在模組內的 @commands.command() 的括號內

弄成像是這種格式：

`@bot.command(name="NAME" , aliases=['指令別名'] ,description="指令說明", brief="指令分類的類別")`

`async def NAME(ctx, options:str="all"):`

`   '''code'''`

舊的目前命名為help.pydis要使用的話把main內那個刪除 和 把 help.pydis內的dis去掉慢慢填上去即可
