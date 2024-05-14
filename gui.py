import tkinter as tk
from tkinter import ttk, messagebox
import urllib.request
import json
import datetime
import random
import string
import threading
import time

# 全局变量
g = 0
b = 0

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

def run(referrer, progress):
    try:
        url = f'https://api.cloudflareclient.com/v0a{digitString(3)}/reg'
        install_id = genString(22)
        body = {"key": "{}=".format(genString(43)),
                "install_id": install_id,
                "fcm_token": "{}:APA91b{}".format(install_id, genString(134)),
                "referrer": referrer,
                "warp_enabled": False,
                "tos": datetime.datetime.now().isoformat()[:-3] + "-05:00",
                "type": "Android",
                "locale": "en_US"}
        data = json.dumps(body).encode('utf8')
        headers = {'Content-Type': 'application/json; charset=UTF-8',
                    'Host': 'api.cloudflareclient.com',
                    'Connection': 'Keep-Alive',
                    'Accept-Encoding': 'gzip',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'}
        req = urllib.request.Request(url, data, headers)
        response = urllib.request.urlopen(req)
        status_code = response.getcode()
        # 更新进度条
        for i in range(100):
            time.sleep(0.01)  # 每次循环暂停0.01秒
            progress['value'] = i + 1
            progress.update()
        return status_code
    except Exception as error:
        print(error)

def start_process():
    referrer = referrer_entry.get()
    if referrer:
        threading.Thread(target=process_request, args=(referrer,)).start()
    else:
        messagebox.showerror("错误", "请输入您的设备ID")

def process_request(referrer):
    global g, b
    first_request = True
    while True:
        if not first_request:
            progress_bar['value'] = 0  # 重置进度条
            for _ in range(18):
                time.sleep(1)  # 每次等待1秒
                progress_bar['value'] += (100 / 18)  # 更新进度条
                progress_bar.update()
        result = run(referrer, progress_bar)
        if first_request:
            first_request = False
        if result == 200:
            g = g + 1
            success_label.config(text=f"成功: {g} GB")
        else:
            b = b + 1
            fail_label.config(text=f"失败: {b} GB")

# 创建主窗口
root = tk.Tk()
root.title("Warp+")

# 标签和输入框
referrer_label = tk.Label(root, text="设备ID:")
referrer_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
referrer_entry = tk.Entry(root)
referrer_entry.grid(row=0, column=1, padx=10, pady=5)

# 进度条
progress_bar = ttk.Progressbar(root, orient='horizontal', mode='determinate', length=200)
progress_bar.grid(row=1, columnspan=2, padx=10, pady=5)

# 成功和失败次数标签
success_label = tk.Label(root, text="成功: 0 GB")
success_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
fail_label = tk.Label(root, text="失败: 0 GB")
fail_label.grid(row=2, column=1, padx=10, pady=5, sticky="e")

# 开始按钮
start_button = tk.Button(root, text="开始", command=start_process)
start_button.grid(row=3, columnspan=2, padx=10, pady=5)

# 运行主循环
root.mainloop()
