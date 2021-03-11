# -*- coding: utf-8 -*-
# @Time    : 2018/5/23 15:10
# @Author  : xiaoke
# @Email   : 976249817@qq.com
# @File    : app_adb_monkey.py

import os
from utils.operate_log_util import logger
from utils.operate_system_search import get_system_use_search

find = get_system_use_search()


@logger('执行monkey测试')
def collect_monkey(packagename, s_num, throttle, pct_touch, pct_motion, pct_trackball, pct_nav, pct_syskeys, pct_appswitch,
               num, logfilepath):
    cmd_monkey = 'adb shell monkey -p %s -s %s --throttle %s --pct-touch %s --pct-motion %s  --pct-trackball  %s  --pct-trackball %s  --pct-syskeys  %s  --pct-appswitch  %s   -v -v -v %s >%s' % (
        packagename, s_num, throttle, pct_touch, pct_motion, pct_trackball, pct_nav, pct_syskeys, pct_appswitch, num,
        logfilepath)
    os.popen(cmd_monkey)
