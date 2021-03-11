# -*- coding: utf-8 -*-
# @Time    : 2018/5/22 20:37
# @Author  : xiaoke
# @Email   : 976249817@qq.com
# @File    : operate_devices_list.py
import subprocess

from utils.operate_log_util import logger


@logger("获取设备列表")
def get_device_list():
    devices = []
    # 如果stdin设置为PIPE，此时的stdin其实是个file对象，用来提供输入到新创建的子进程；
    # 如果stdout设置为PIPE，此时stdout其实是个file对象，用来保存新创建的子进程的输出；
    # 如果stderr设置为PIPE，此时的stderr其实是个file对象，用来保存新创建的子进程的错误输出。
    result = subprocess.Popen("adb devices", shell=True, stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE, encoding="utf-8").stdout.readlines()
    result.reverse()
    for line in result[1:]:
        # strip()是去除换行
        # split()是以空格为分割点，切分
        flag = line.split()[1]
        if flag == "device":
            devices.append(line.split()[0])
        else:
            break

    return devices


if __name__ == '__main__':
    print(get_device_list())
