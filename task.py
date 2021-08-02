# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------------
# Name:         task
# Description:  
# Author:       guohuanyang
# Date:         2021/8/2
# Email         guohuanyang@datagrand.com
# -------------------------------------------------------------------------------
from concurrent.futures import ThreadPoolExecutor
from DownloadObj import Downloader, UrlInfo
from utils import split_txt, download_pdf
from config import host, upload_dir


executor= ThreadPoolExecutor(max_workers=8)
NUM_LIMIT = 200
START = 1


lines = split_txt(filepath='file_info.txt')
lines = lines[START:START+NUM_LIMIT]

lines = [[file_id, file_name, "{}.{}".format(unique_name, file_name.rsplit(".")[-1]), y] for file_id, file_name, unique_name, *y in lines]

url_info_list = [UrlInfo("{}/{}/{}".format(
    host, upload_dir, unique_name
), file_name) for file_id, file_name, unique_name, *y in lines]

for url_info in url_info_list:
    downloader = Downloader(url_info, save_dir_name="./files")
    executor.submit(
        download_pdf, downloader.url_info.url, downloader.save_dir_name, downloader.url_info.name
    )

print("down")
