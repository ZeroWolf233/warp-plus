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
url = f'https://api.cloudflareclient.com/v0a{digitString(3)}/reg'
def run():
	try:
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
					'User-Agent': 'okhttp/3.12.1'
					}
		req         = urllib.request.Request(url, data, headers)
		response    = urllib.request.urlopen(req)
		status_code = response.getcode()	
		return status_code
	except Exception as error:
		print(error)	

g = 0
b = 0
animation = [
	"[□□□□□□□□□□] 0%",
	"[■□□□□□□□□□] 10%",
	"[■■□□□□□□□□] 20%",
	"[■■■□□□□□□□] 30%",
	"[■■■■□□□□□□] 40%",
	"[■■■■■□□□□□] 50%",
	"[■■■■■■□□□□] 60%",
	"[■■■■■■■□□□] 70%",
	"[■■■■■■■■□□] 80%",
	"[■■■■■■■■■□] 90%",
	"[■■■■■■■■■■] 100%"]

referrer = input("请输入您的 设备ID 大抵可以在 设置-高级-诊断 中找到:")
print("好的，请稍后，我们正在处理您的ID")

while True:
	os.system('cls' if os.name == 'nt' else 'clear')
	print('\r试图发送请求ing...')
	result = run()
	if result == 200:
		g = g + 1
		os.system('cls' if os.name == 'nt' else 'clear')
		for i in range(len(animation)):
			time.sleep(1.63)
			os.system('cls' if os.name == 'nt' else 'clear')
			print('\r试图发送请求ing...')
			print("发送请求成功")
			print(f"使用ID: {referrer}")
			print(f"{g} GB的WARP+流量已经添加到您的账户")
			print("\n18秒后会再次发送一个请求")
			print('{冷却}'+animation[i % len(animation)])
			print(f"\n共计: {g} GB成功 {b} GB失败\n")
	else:
		b = b + 1
		os.system('cls' if os.name == 'nt' else 'clear')
		print("错误!无法连接到服务器")
		print(f"总计: {g} GB成功 {b} GB失败")
		print('软件将在20秒后重试')
		time.sleep(20)