import yaml
import os
import pandas as pd
import numpy as np

def datasets_update(file_name:str,password:str):
    '''
    更新數據集資料
    '''
    config_yaml_path = "./datasets/config.yaml"
    if not os.path.exists(config_yaml_path):
        config_yaml = {
            "datasets":{}
        }
        with open(config_yaml_path, 'w', encoding='utf-8') as f:
            yaml.dump(config_yaml, f, allow_unicode=True)
    config_yaml = yaml.load(open(config_yaml_path, 'r', encoding='utf-8'), Loader=yaml.FullLoader)
    config_yaml["datasets"][file_name] = password
    with open(config_yaml_path, 'w', encoding='utf-8') as f:
        yaml.dump(config_yaml, f, allow_unicode=True)
    return True

def datasets_read(file_name:str,password:str):
    '''
    讀取數據集資料
    '''
    config_yaml_path = "./datasets/config.yaml"
    if not os.path.exists(config_yaml_path):
        config_yaml = {
            "datasets":{}
        }
        with open(config_yaml_path, 'w', encoding='utf-8') as f:
            yaml.dump(config_yaml, f, allow_unicode=True)
    config_yaml = yaml.load(open(config_yaml_path, 'r', encoding='utf-8'), Loader=yaml.FullLoader)
    if file_name in config_yaml["datasets"] and config_yaml["datasets"][file_name] == password:
        return pd.read_csv("./datasets/"+file_name)
    else:
        return None