#encoding:utf-8
import re

"""
获取城市代码
返回一个键为城市名称的 字典
"""
def get_code_name():
    city_code_dict = {}
    with open('city.txt','r') as f:
        lines = f.readlines()
        for line in lines:                                                                   # {'display':"湛江",'data':"Zhanjiang|湛江|547",'group':"Z"}
            single_city = re.findall(r"'data':(.*),'.*",line)[0].replace('"','').split('|')  # ['Beijing', '北京', '1']
            city_code_dict[single_city[1]] = single_city

    return city_code_dict



# 反回用于url的城市代号
def get_str(citys):
    dict_code = {}
    for city in citys:
        city_code_dict = get_code_name()
        single_city_code = city_code_dict[city]
        str_code = single_city_code[0] + single_city_code[2]                         # 用于url的城市代号  beijing1
        dict_code[city] = str_code
        print(str(city) + '的代号是： ' + str_code)
    return dict_code

# citys = ['长沙', '株洲', '湘潭', '衡阳', '邵阳', '岳阳', '常德', '张家界', '益阳', '娄底', '郴州', '永州', '怀化', '湘西']
# get_str(citys)
    # return dict_code







