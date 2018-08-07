# coding=utf-8
from urllib import request
from urllib.parse import quote
import json
'''
 对接天气机器人，在微信中输入地点，返回对应的天气预报
 
'''
class Weather():
    @staticmethod
    def Get_Weather(city):
        # 传入的城市为utf-8，而网址中输入的格式为ascii格式，使用quote对城市进行转换
        req = request.Request(url=('https://www.sojson.com/open/api/weather/json.shtml?city=%s' % quote(city)))

        with request.urlopen(req) as f:
            data = f.read()

            # 请求接口失败
            if f.code != 200:
                return ''
            print('请求登陆接口返回的数据：', data)
            response = json.loads(data.decode('utf-8'))

        return response

    @staticmethod
    def Format_Weather(response):
        a = response
        city = a['city']
        date = a['date']
        wendu = a['data']['wendu']

        return "日期 :" +date + " \n城市:" + city + "\n温度:" + wendu




# weather = Weather()
# weather.Get_Weather('广州')

#
# a =  Weather.Get_Weather('广州')
# Weather.format(a)
# # print(a['data'])
