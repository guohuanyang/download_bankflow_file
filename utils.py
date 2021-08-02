# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------------
# Name:         utils
# Description:  
# Author:       guohuanyang
# Date:         2021/8/2
# Email         guohuanyang@datagrand.com
# -------------------------------------------------------------------------------
import requests
import os


def download_pdf(url, dir_name='./files', new_pdf_name='test.pdf'):
    print(url)
    try:
        response_info = requests.get(url, stream=True)
        response_info.encoding = response_info.apparent_encoding
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)
        pdf_path = os.path.join(dir_name, new_pdf_name)
        with open(pdf_path, "wb") as f:
            for chunk in response_info.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
    except Exception as e:
        print(e)


def split_txt(filepath='file_info.txt'):
    with open(filepath, 'r') as f:
        lines = f.readlines()
    lines = list(map(lambda x: x.split(r"	"), lines))
    lines = [[file_id, file_name, unique_name.replace("\n", ""), y] for file_id, file_name, unique_name, *y in lines]
    return lines
