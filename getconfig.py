import os
import json


def getConfig():
    '''
    获取基础配置信息
    :return:
    '''
    if os.path.exists("config.json"):
        with open(os.path.join("config.json"), 'r', encoding='utf8') as f:
            config = json.loads(f.read())
        f.close()
    else:
        config_path = input("请输入 config.json 文件的路径:\n")
        print("输入的 config.json 的文件路径为：{}".format(config_path))
        with open(os.path.join(config_path, "config.json"), 'r', encoding='utf8') as f:
            config = json.loads(f.read())
        f.close()
    return config


