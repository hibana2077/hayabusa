import yaml
import os
import pandas as pd
import numpy as np

def dataset_df_config(dataset_name:str, config_file_path:str,data_file_path:str , data_case:str, df:pd.DataFrame):
    if os.path.isfile(config_file_path):
        with open(config_file_path, 'r') as f:
            config = yaml.load(f, Loader=yaml.FullLoader)
            #set values from config.yaml
            #check if yaml is empty
            if config is not None:
                config[dataset_name] = {
                    "type": data_case,
                    "path": f"datasets/{dataset_name}.csv"
                }
            else:
                config = {
                    dataset_name: {
                        "type": data_case,
                        "path": f"datasets/{dataset_name}.csv"
                    }
                }
    else:
        config = {
            dataset_name: {
                "type": data_case,
                "path": f"datasets/{dataset_name}.csv"
            }
        }
    with open(config_file_path, 'w') as f:
        yaml.dump(config, f)

    df.to_csv(data_file_path)

def dataset_np_config(dataset_name:str, config_file_path:str,data_file_path:str , data_case:str, x_train:np.ndarray, y_train:np.ndarray, x_test:np.ndarray, y_test:np.ndarray):
    if os.path.isfile(config_file_path):
        with open(config_file_path, 'r') as f:
            config = yaml.load(f, Loader=yaml.FullLoader)
            #set values from config.yaml
            #check if yaml is empty
            if config is not None:
                config[dataset_name] = {
                    "type": data_case,
                    "path": f"datasets/{dataset_name}.npz"
                }
            else:
                config = {
                    dataset_name: {
                        "type": data_case,
                        "path": f"datasets/{dataset_name}.npz"
                    }
                }
    else:
        config = {
            dataset_name: {
                "type": data_case,
                "path": f"datasets/{dataset_name}.npz"
            }
        }
    with open(config_file_path, 'w') as f:
        yaml.dump(config, f)

    np.savez(data_file_path, x_train=x_train, y_train=y_train, x_test=x_test, y_test=y_test)