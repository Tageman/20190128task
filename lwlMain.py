# -*- coding:utf-8 -*-

import json
import smtplib
import threading
import xlrd
import time
from common.api_method import *
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def read_excel(line_num):
    excel_list = table.row_values(line_num)
    url = excel_list[0]
    params = json.loads(excel_list[1])
    code = excel_list[3]

    if excel_list[2] == 'GET':
        get_method(url, params, code)
    elif excel_list[2] == 'PUT':
        put_method(url, params, code)
    elif excel_list[2] == 'POST':
        post_method(url, params, code)
    else:
        delete_method(url, params, code)


if __name__ == '__main__':

    excel_address = "lwl_api.xlsx"
    data = xlrd.open_workbook(excel_address)
    table = data.sheets()[0]
    nrows = table.nrows

    # 根据数据行数进行启动线程数
    threads = []
    for i in range(nrows-1):
        t = threading.Thread(target=read_excel, args=(i+1,))
        threads.append(t)
    for i in range(nrows-1):
        threads[i].start()
    for i in range(nrows-1):
        threads[i].join()

    sender = '15026905296@139.com'
    password = 'qn123456'
    receivers = '825817056@qq.com'

    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receivers
    msg['Subject'] = 'API_Test_Result'

    msg.attach(MIMEText('当前接口测试结果（结果全部显示在附件中）', 'plain', 'utf-8'))
    att1 = MIMEText(open(".\\result\\result-{0}.txt".format(time.strftime("%Y-%m-%d", time.localtime())), 'rb').read(),
                    "base64", "utf-8")
    att1['Content-Type'] = 'application/octet-stream'
    att1['Content-Disposition'] = 'attahment; filename="result-{0}.txt"'.format(
        time.strftime("%Y-%m-%d-%H", time.localtime()))
    msg.attach(att1)

    smtpobj = smtplib.SMTP("smtp.139.com", 25)
    smtpobj.login(sender, password)
    smtpobj.sendmail(sender, receivers, msg.as_string())
    smtpobj.quit()

    print('执行完毕')

