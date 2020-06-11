import json

# 创建一个读取数据的函数方法
def read_build(file_name,intreface_name):
    # 定义个空列表
    data_list = []

    # 读取数据
    with open(file_name,'r',encoding='utf-8') as file:
        # 加载成json数据
        jsonData = json.load(file)
        # 获取数据驱动的值
        json_values = jsonData.get(intreface_name)
        # 转换列表格式添加到列表当中
        data_list.append(list(json_values.values()))
    # 把列表返回出去
    return data_list

