
import json
import os
import pandas as pd

# make a list of files in a directory
def make_file_list(path):
    file_list = []
    for file in os.listdir(path):
        if file.endswith(".json"):
            file_list.append(f"{path}/{file}")
    return file_list

def read_json(infile):
    df = [json.loads(line)
        for line in open(infile, 'r', encoding='utf-8')]
    df = pd.DataFrame(df)
    return df

# connect two dataframes with two keys
def connect_df(df1, df2, key1, key2):
    df = pd.merge(df1, df2, how="outer", on = [key1, key2])
    return df


def main():
    directjson_list = make_file_list("associationByOverallDirect")
    for infile in directjson_list:
        if infile == directjson_list[0]:
            df_direct = read_json(infile)
        else:
            df_direct = pd.concat([df_direct,read_json(infile)])


    indirectjson_list = make_file_list("associationByOverallIndirect")
    for infile in indirectjson_list:
        if infile == indirectjson_list[0]:
            df_indirect = read_json(infile)
        else:
            df_indirect = pd.concat([df_indirect,read_json(infile)])


    df_merged = connect_df(df_direct, df_indirect, "diseaseId","targetId")
    df_merged.to_csv("associations_combined2.tsv", sep="\t", index=False)

if __name__ == "__main__":
    main()
