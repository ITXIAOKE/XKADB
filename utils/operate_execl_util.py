# -*- coding: utf-8 -*-
# @Time    : 2018/5/21 19:26
# @Author  : xiaoke
# @Email   : 976249817@qq.com
# @File    : operate_execl_util.py
import xlsxwriter
from utils.operate_log_util import logger, LOG

path_time = "E:\\pycharmproject\\adbproject\\xh_adb\\word\\启动时间测试结果.xlsx"
path_cpu = "E:\\pycharmproject\\adbproject\\xh_adb\\word\\cpu_liu_men_report.xlsx"


@logger('保存启动时间测试结果')
def qidongceshi(cishu, start, path_time):
    try:
        workbook = xlsxwriter.Workbook(path_time)
        worksheet = workbook.add_worksheet('time')
        bold = workbook.add_format({'bold': 1})
        headings = ['启动次数', '启动时间']
        data = [cishu, start]
        worksheet.write_row('A1', headings, bold)
        worksheet.write_column('A2', data[0])
        worksheet.write_column('B2', data[1])
        chart1 = workbook.add_chart({'type': 'scatter',
                                     'subtype': 'straight_with_markers'})
        chart1.add_series({
            'name': '=time!$B$1',
            'categories': '=time!$A$2:$A$%s' % (len(start) + 1),
            'values': '=time!$B$2:$B$%s' % (len(start) + 1),
        })
        chart1.set_title({'name': '启动监测'})
        chart1.set_x_axis({'name': "启动次数"})
        chart1.set_y_axis({'name': '花费时间:ms'})
        chart1.set_style(11)
        worksheet.insert_chart('D2', chart1, {'x_offset': 25, 'y_offset': 10})
        workbook.close()
        LOG.info('保存启动时间成功')
    except:
        LOG.info('保存启动时间失败，原因:%s' % Exception)


@logger('保存cpu，流量，内存')
def getcpu(cishu, start_cpu, recv_list, send_list, total_list, pass_list):
    try:
        workbook = xlsxwriter.Workbook(path_cpu)
        worksheet = workbook.add_worksheet('cpu')
        worksheet_liulang = workbook.add_worksheet('liulang')
        worksheet_men = workbook.add_worksheet('men')
        bold = workbook.add_format({'bold': 1})
        headings = ['时间', 'cpu占用率']
        headings_liuliang = ['时间', '上传流量', '下载流量', '总计']
        headings_men = ['时间', '内存占百分比']
        data_cpu = [cishu, start_cpu]
        data_liuliang = [cishu, recv_list, send_list, total_list]
        data_men = [cishu, pass_list]
        worksheet_liulang.write_row('A1', headings_liuliang, bold)
        worksheet_liulang.write_column('A2', data_liuliang[0])
        worksheet_liulang.write_column('B2', data_liuliang[2])
        worksheet_liulang.write_column('C2', data_liuliang[1])
        worksheet_liulang.write_column('D2', data_liuliang[3])
        worksheet_men.write_row('A1', headings_men, bold)
        worksheet_men.write_column('A2', data_men[0])
        worksheet_men.write_column('B2', data_men[1])
        worksheet.write_row('A1', headings, bold)
        worksheet.write_column('A2', data_cpu[0])
        worksheet.write_column('B2', data_cpu[1])
        chart1 = workbook.add_chart({'type': 'scatter',
                                     'subtype': 'straight_with_markers'})
        chart2 = workbook.add_chart({'type': 'scatter',
                                     'subtype': 'straight_with_markers'})
        chart3 = workbook.add_chart({'type': 'scatter',
                                     'subtype': 'straight_with_markers'})
        chart3.add_series({
            'name': '=men!$B$1',
            'categories': '=men!$A$2:$A$%s' % (len(cishu) + 1),
            'values': '=men!$B$2:$B$%s' % (len(cishu) + 1),
        })
        chart2.add_series({
            'name': '=liulang!$B$1',
            'categories': '=liulang!$A$2:$A$%s' % (len(cishu) + 1),
            'values': '=liulang!$B$2:$B$%s' % (len(cishu) + 1),

        })
        chart1.add_series({
            'name': '=cpu!$B$1',
            'categories': '=cpu!$A$2:$A$%s' % (len(cishu) + 1),
            'values': '=cpu!$B$2:$B$%s' % (len(cishu) + 1),
        })
        chart2.add_series({
            'name': '=liulang!$C$1',
            'categories': '=liulang!$A$2:$A$%s' % (len(cishu)),
            'values': '=liulang!$C$2:$C$%s' % (len(cishu)),
        })
        chart2.add_series({
            'name': '=liulang!$D$1',
            'categories': '=liulang!$A$2:$A$%s' % (len(cishu)),
            'values': '=liulang!$D$2:$D$%s' % (len(cishu)),
        })
        chart2.set_title({'name': '流量统计图'})
        chart2.set_x_axis({'name': '时间(秒)'})
        chart2.set_y_axis({'name': '流量：k'})
        chart2.set_style(11)
        chart3.set_title({'name': '内存占有率统计图'})
        chart3.set_x_axis({'name': '时间(秒)'})
        chart3.set_y_axis({'name': '内存值：k'})
        chart3.set_style(11)
        worksheet_men.insert_chart('F2', chart3, {'x_offset': 60, 'y_offset': 60})
        worksheet_liulang.insert_chart('F2', chart2, {'x_offset': 60, 'y_offset': 60})
        chart1.set_title({'name': 'cpu占用率'})
        chart1.set_x_axis({'name': "时间(秒)"})
        chart1.set_y_axis({'name': '占用:%'})
        chart1.set_style(11)
        worksheet.insert_chart('D2', chart1, {'x_offset': 60, 'y_offset': 60})
        workbook.close()
        LOG.info('保存流量，内存等采集数据，成功')
    except:
        LOG.info('保存流量，内存等采集数据，失败:%s' % Exception)


if __name__ == '__main__':
    pass
