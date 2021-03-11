# -*- coding: utf-8 -*-
# @Time    : 2018/5/23 14:31
# @Author  : xiaoke
# @Email   : 976249817@qq.com
# @File    : app_adb_flow.py
import os
from utils.operate_system_search import get_system_use_search
from utils.operate_log_util import logger

find = get_system_use_search()


@logger("获取app的流量")
def collect_flow(packagename):
    # 执行获取进程的命令
    result = os.popen("adb shell ps | %s %s" % (find, packagename))
    # 获取进程ID,注意app一定是打开的状态才能采集这些数据
    pid = result.readlines()[0].split()[1]
    # 获取进程ID使用的流量
    traffic = os.popen("adb shell cat /proc/" + pid + "/net/dev")
    for line in traffic:
        if "wlan0" in line:
            # 将所有空行换成#
            line = "#".join(line.split())
            # 按#号拆分,获取收到和发出的流量
            receive = line.split("#")[1]
            transmit = line.split("#")[9]
        elif "eth1" in line:
            line = "#".join(line.split())
            receive2 = line.split("#")[1]
            transmit2 = line.split("#")[9]

    # 计算所有流量的之和
    alltraffic = (int(receive2) + int(transmit2)) - (int(receive) + int(transmit))
    # 按MB计算所有的流量数据值（wlan0+eth1）
    # all_traffic = '%.4f' % (alltraffic / 1024 / 1024)
    # 接收的流量数据差值
    # flow_rcv = '%.4f' % ((int(receive2) - int(receive)) / 1024 / 1024)
    # 发送的流量数据差值
    # flow_snd = '%.4f' % ((int(transmit2) - int(transmit)) / 1024 / 1024)
    flow_rcv = int(receive2) - int(receive)
    flow_snd = int(transmit2) - int(transmit)
    return flow_rcv, flow_snd, alltraffic


if __name__ == '__main__':
    print(collect_flow("com.a1chemic.owner.android"))
