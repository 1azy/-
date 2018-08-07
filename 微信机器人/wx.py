# coding=utf-8
# author=veficos

import wxpy
import weather
import re

from wxpy import *
# 初始化机器人，扫码登陆
bot = Bot()

#my_friend = bot.friends().search('乔')[0]

@bot.register()
def print_others(msg):
    if msg.sender.remark_name in ['张鑫']:
        msg.reply_image('picture.jpg')
        return '请扫码改需求'
    if msg.sender.name in ['乔']:
        msg.reply_image('picture.jpg')
        return '请扫码吹水'

    if '需求' in msg.text:
        msg.reply_image('picture.jpg')
        return '请扫码改需求'

    elif 'BUG' in msg.text.upper():
        msg.reply_image('picture.jpg')
        return '请扫码修BUG'
    elif '99' in msg.text.upper():
        msg.reply_image('picture.jpg')
        return '请扫码测试'
    elif '测试' in msg.text.upper():
        msg.reply_image('picture.jpg')
        return '请扫码测试'


    elif '天气' in msg.text.upper():
        result = re.split(r'[|]', msg.text)
        if result and len(result) >= 2:
            city = result[0]
            b = weather.Weather.Format_Weather(weather.Weather.Get_Weather(city))
            return b
        else:
            return '城市有误'







#@bot.register(my_friend)
#def reply_my_friend(msg):
#    if '需求' in msg.text:
#        my_friend.send_image('picture.jpg')
#        return '请扫码改需求'
#    elif 'BUG' in msg.text.upper():
#        my_friend.send_image('picture.jpg')
#        return '请扫码修BUG'
#    #my_friend.send_image('picture.jpg')
#    #return '请扫码聊天'
#    return None



bot.join()
