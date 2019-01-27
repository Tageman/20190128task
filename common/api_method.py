# -*- coding：utf-8 -*-
import requests
from common import save_result

header = {"AUTH-1-1": "hahaha"}


def get_method(url, payload, code):
    response = requests.get(url, params=payload, headers=header)
    if response.status_code == int(code):
        request_result = url + " success"
        save_result.write_file(request_result)
    else:
        request_result = url + " error"
        save_result.write_file(request_result)


def put_method(url, payload, code):
    response = requests.put(url, data=payload, headers=header)
    if response.status_code == int(code):
        request_result = url + " success"
        save_result.write_file(request_result)
    else:
        request_result = url + " error"
        save_result.write_file(request_result)


def post_method(url, payload, code):
    response = requests.post(url, data=payload, headers=header)
    if response.status_code == int(code):
        request_result = url + " success"
        save_result.write_file(request_result)
    else:
        request_result = url + " error"
        save_result.write_file(request_result)


def delete_method(url, payload, code):
    response = requests.delete(url, params=payload, headers=header)
    if response.status_code == int(code):
        request_result = url + " success"
        save_result.write_file(request_result)
    else:
        request_result = url + " error"
        save_result.write_file(request_result)



