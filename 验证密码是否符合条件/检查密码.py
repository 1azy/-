"""
# 给定一个字符串，用以下规则检查合法性，完全符合返回True，否则返回False
1.第一位是字母
2.只能包含字母、数字、下划线
3.只能是数字或字母结尾
4.最小长度为2
5.最长长度为10
"""

def valid_password(pwd):
    pword = pwd[1:-2]
    if len(pwd) <= 10 and len(pwd) >= 2:
        if pwd[0].isalpha() == True:
            if pwd[-1].isalpha() == True or pwd[-1].isdigit() == True:
                if len(pwd) > 2:
                    i = 0
                    while i < len(pword):
                        if pword[i].isalpha() == True or pword[i].isdigit() == True or pword[i] == '_':
                             pass
                        else:
                            return False
                        i = i + 1
                    return True
                else:
                    return True
            else:
                return False
        else:
            return False
    else:
        return False
























    #     if ord(pwd[0]) in (97, 122) or ord(pwd[0]) in (65, 90):
    #         if ord(pwd[-1]) in (97, 122) or ord(pwd[-1]) in (65, 90) or ord(pwd[-1]) in (48, 57):
    #         if (ord(pwd[-1])>=97 and ord(pwd[-1])<=122) or (ord(pwd[-1])>=65 and ord(pwd[-1])<=90) or
    #             for x in pwd:
    #                 if ord(x) in (97, 122) or ord(x) in (65, 90) or ord(x) in (48, 57) or ord(x) == 95:
    #                     print('Ture')
    #                     break
    #                 else:
    #                     print('False')
    #         else:
    #             print('False')
    #     else:
    #         print('False')
    # else:
    #     print('False')





pwd = input('请输入密码：')
print(valid_password(pwd))


