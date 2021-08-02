# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------------
# Name:         DownloadObj
# Description:  
# Author:       guohuanyang
# Date:         2021/8/2
# Email         guohuanyang@datagrand.com
# -------------------------------------------------------------------------------
from utils import download_pdf


class UrlInfo:
    def __init__(self, url, name):
        self.url = url
        self.name = name


class Downloader:

    def __init__(self, url_info: UrlInfo, save_dir_name: str = "files"):
        self.url_info = url_info
        self.save_dir_name = save_dir_name

