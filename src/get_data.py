import os
import yaml
import pandas as pd
import argparse
# This code defines a function named read_params that takes a 
# single argument config_path, which is expected to be a file path
#  pointing to a YAML (YAML Ain't Markup Language) file. 
# The function reads the content of the specified YAML file and 
# returns the parsed content as a Python dictionary.
def read_params(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

def get_data(config_path):
    config = read_params(config_path)
    
    data_path = config["data_source"]["s3_source"]
    df = pd.read_csv(data_path,sep = ",",encoding = 'utf-8')
    return df

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config",default="params.yaml")
    parsed_args = args.parse_args()
    data = get_data(config_path=parsed_args.config)