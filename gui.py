import tkinter as tk
from tkinter import messagebox
import urllib.request
import json
import datetime
import random
import string
import time
import os

def genString(stringLength):
    try:
        letters = string.ascii_letters + string.digits
        return ''.join(random.choice(letters) for i in range(stringLength))
    except Exception as error:
        print(error)

def digitString(stringLength):
    try:
        digit = string.digits
        return ''.join((random.choice(digit) for i in range(stringLength)))
    except Exception as error:
        print(error)

def run(referrer):
    try:
        url = f'https://api.cloudflareclient.com/v0a{digitString(3)}/reg'
        install_id = genString(22)
        body = {"key": "{}=".format(genString(43)),
                "install_id": install_id,
                "fcm_token": "{}:APA91b{}".format(install_id, genString(134)),
                "referrer": referrer,
                "warp_enabled": False,
                "tos": datetime.datetime.now().isoformat()[:-3] + "+02:00",
                "type": "Android",
                "locale": "es_ES"}
        data = json.dumps(body).encode('utf8')
        headers = {'Content-Type': 'application/json; charset=UTF-8',
                    'Host': 'api.cloudflareclient.com',
                    'Connection': 'Keep-Alive',
                    'Accept-Encoding': 'gzip',
                    'User-Agent': 'okhttp/3.12.1'}
        req = urllib.request.Request(url, data, headers)
        response = urllib.request.urlopen(req)
        status_code = response.getcode()
        return status_code
    except Exception as error:
        print(error)

def start_process():
    global g, b
    referrer = referrer_entry.get()
    if referrer:
        messagebox.showinfo("提示", "请稍后，正在处理您的ID")
        while True:
            result = run(referrer)
            if result == 200:
                g = g + 1

                # 这里添加更新UI的代码
                # 例如：progress_label.config(text="发送请求...")
                # 你需要自己根据需要更新UI
            else:
                b = b + 1
                # 这里添加更新UI的代码
                # 例如：messagebox.showerror("错误", "无法连接到服务器")
                # 你需要自己根据需要更新UI
    else:
        messagebox.showerror("错误", "请输入您的设备ID")

# 创建主窗口
root = tk.Tk()
root.title("Warp+ 流量添加")

# 标签和输入框
referrer_label = tk.Label(root, text="设备ID:")
referrer_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
referrer_entry = tk.Entry(root)
referrer_entry.grid(row=0, column=1, padx=10, pady=5)

# 开始按钮
start_button = tk.Button(root, text="开始", command=start_process)
start_button.grid(row=1, columnspan=2, padx=10, pady=5)

# 运行主循环
root.mainloop()
