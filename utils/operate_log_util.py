# -*- coding: utf-8 -*-
# @Time    : 2018/5/21 9:52
# @Author  : xiaoke
# @Email   : 976249817@qq.com
# @File    : operate_log_util.py
import os
from functools import wraps
import logbook
# 将日志文件打印到屏幕中
from logbook.more import ColorizedStderrHandler

check_path = '.'
LOG_DIR = os.path.join(check_path, 'log')
# print(LOG_DIR)
file_stream = False
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)
    file_stream = True


def get_logger(name='monkey小工具各流程日志输出', file_log=file_stream, level=''):
    '''获取日志工厂功能'''
    '''
     py:attr:`LogRecord.time` will be a datetime in local time zone
     (but not time zone aware)
    '''
    logbook.set_datetime_format('local')
    ColorizedStderrHandler(bubble=False, level=level).push_thread()
    # # 日志打印到文件中
    logbook.TimedRotatingFileHandler(os.path.join(LOG_DIR, '%s.log' % name),
                                     date_format='%Y-%m-%d-%H',
                                     bubble=True,
                                     encoding='utf-8').push_thread()
    return logbook.Logger(name)


# 通过工厂的方法创建log
LOG = get_logger(file_log=file_stream, level='INFO')


# print(LOG)


def logger(param=None):
    def wrap(function):
        @wraps(function)
        def _wrap(*args, **kwargs):
            LOG.info("当前模块：{}".format(param))
            LOG.info("全部args参数信息：{}".format(str(args)))
            LOG.info("全部kwargs参数信息：{}".format(str(kwargs)))
            return function(*args, **kwargs)

        return _wrap

    return wrap
