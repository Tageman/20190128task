# -*- coding:utf-8 -*-

import time


def write_file(request_result):
    with open(".\\result\\result-{0}.txt".format(time.strftime("%Y-%m-%d", time.localtime())), "a+") as file:
        file.write(request_result + "\n")