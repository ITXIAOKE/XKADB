# -*- coding: utf-8 -*-
# @Time    : 2018/5/22 19:21
# @Author  : xiaoke
# @Email   : 976249817@qq.com
# @File    : app_adb_time.py

import os
from utils.operate_system_search import get_system_use_search
from utils.operate_log_util import logger

find = get_system_use_search()


# com.a1chemic.owner.android/net.sourceforge.simcpux.activity.user.YeZhu_Activity_welcome
# com.a1chemic.owner.android/net.sourceforge.simcpux.activity.mine.YeZhu_Activity_Guidance

@logger('获取启动耗时')
def collect_time(packagename, packagename_activicy):
    cmd = 'adb shell am start -W -n %s' % packagename_activicy
    # print(cmd)
    # print("===============")
    # print(os.popen(cmd).read())
    # print("-----------------")
    # print(os.popen(cmd).read().split('\n'))
    # print("**********")
    me = os.popen(cmd).read().split('\n')[-7].split(': ')
    # 强制停止app
    cmd2 = 'adb shell am force-stop %s' % packagename
    os.system(cmd2)
    return me


if __name__ == '__main__':
    print(collect_time("com.a1chemic.owner.android",
                         "com.a1chemic.owner.android/net.sourceforge.simcpux.activity.user.YeZhu_Activity_welcome"))
