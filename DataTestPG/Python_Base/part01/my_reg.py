'''
2019年12月11日22:58:14
11位手机号码匹配：
移动： 139 138 137 136 135 134
150 151 152 157 158 159
联通： 130 131 132 185 186 145
电信： 133 153 180 199

'''
import re
def  checkCellphone(cellphone):
    reqex = '^(13[0-9]|(14[5|7])|(15([0-3]|[5-9]))|(18[0,5-9]))\d{8}$'
    result = re.findall(reqex,cellphone)
    if result:
        print('成功')
        return True
    else:
        print('失败')
        return False

cellphone = '13301473825'
print(checkCellphone(cellphone))