# -*- coding: utf-8 -*-
# @Time    : 2018/5/23 15:12
# @Author  : xiaoke
# @Email   : 976249817@qq.com
# @File    : app_adb_state.py
import os
from utils.operate_log_util import logger
from utils.operate_system_search import get_system_use_search

find = get_system_use_search()


@logger('获取设备状态')
def collect_state():
    cmd1 = 'adb get-state'
    devices_status = os.popen(cmd1).read().split()[0]
    return devices_status


if __name__ == '__main__':
    print(collect_state())
