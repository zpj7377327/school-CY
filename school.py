import requests
import socket
import tkinter
import re
from os import path, mkdir, chdir
from getpass import getuser



# 获取本机地址

def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip


# 检测初始化用户文件夹和切换工作区


def test_user(id, pas):
    # 检测文件夹和文件
    my_path = 'C:\\Users\\' + getuser() + '\\Documents\\school'
    my_ts = 'C:\\Users\\' + getuser() + '\\Documents\\school\\my_user.txt'
    he_exists = path.exists(my_path)
    ts_exists = path.exists(my_ts)

    if not (he_exists and ts_exists):
        try:
            mkdir(my_path)
        except(FileExistsError):
            chdir(my_path)

        chdir(my_path)
        print("第一次初始化\n")
        a = id
        a = 'XYGY_S' + a + '@SCITC'
        b = pas
        with open('my_user.txt', 'a+') as f:
            f.write(a + '\n')
            f.write(b)
        return 111

    else:
        print('欢迎回来')
        chdir(my_path)
        return 222


# 手动获取路由器ip/滑稽
def get_rout_ip():
    print('请将路由器设为静态ip:172.25.33.196\n')
    input('下一步请按任意键')
    return 'http://10.10.11.14/webauth.do?wlanuserip=172.25.33.196&wlanacname=XF_BRAS'


# 获取用户账号密码
def get_user():
    with open('my_user.txt', 'r') as f:
        user = f.readlines()
    return user


def inter(e1, e2):
    headrs = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Length': '320',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': '10.10.11.14',
        'Origin': 'http://10.10.11.14',
        'Referer': 'http://10.10.11.14/webauth.do?wlanuserip=172.25.33.99&wlanacname=XF_BRAS&vlan=0&rand=fd501de91c262',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36}'}

    url = 'http://10.10.11.14/webauth.do?wlanuserip=' + get_host_ip() + '&wlanacname=XF_BRAS'
    Date = {
        'pageid': '1',
        'userId': '',
        'passwd': ''}

    test_user(e1, e2)
    user_list = get_user()

    Date['userId'] = user_list[0]
    Date['passwd'] = user_list[1]
    my_ip = get_host_ip()

    if not re.match(r'192.168', my_ip):
        now = requests.post(url, Date, headrs)
    else:

        now = requests.post(get_rout_ip(), Date, headrs)

    baidu = requests.get('https://baidu.com')
    if baidu.status_code == 200:
        print('网络成功连接')
        print('您的IP:' + get_host_ip())

    else:
        print('无网络请检查插口或无线调制器')
