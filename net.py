import re
import json
import requests
import argparse

class schoolNet:

    user = ''
    passwd = ''
    userInfo = dict()
    queryString = ''
    serverPreFix = ''

    def __init__(self):
        self.serverPreFix = 'http://222.198.127.170'
        self.get_queryString()

    def set_user(self, user=None, passwd=None):
        if user is not None:
            self.user = user
        if passwd is not None:
            self.passwd = passwd

    def get_queryString(self):
        try:
            response = requests.get(self.serverPreFix)
            match = re.search(r"href='.*\?(.+?)'", response.text)  # 使用正则表达式匹配 href 值
            if match:
                queryString = match.group(1)
                self.queryString = queryString
        except Exception as e:
            print(e)

    def get_user_info(self):
        params = {
            'method': 'getOnlineUserInfo',
        }
        response = requests.post(f'{self.serverPreFix}/eportal/InterFace.do', params=params, verify=False)
        text = response.text.encode(response.encoding).decode('utf-8')
        self.userInfo = json.loads(text)

    def do_mac(self, regist=None):
        if regist is None:
            return
        params = {
            'method': 'registerMac' if regist else 'cancelMac',
        }
        self.get_user_info()
        if len(self.userInfo) == 0:
            print('无法获取用户信息!')
            return
        data = {
            'mac': '',
            'userIndex': self.userInfo['userIndex'],
        }
        response = requests.post(f'{self.serverPreFix}/eportal/InterFace.do', params=params, data=data, verify=False)
        print(response.text.encode(response.encoding).decode('utf-8'))


    def login(self):
        params = {
            'method': 'login',
        }
        if self.queryString == '':
            self.get_queryString()
        if self.queryString is None:
            print('无法获取queryString!')
            return
        if self.user == '' or self.passwd == '':
            print('未设置用户名或密码!')
            return
        data = {
            'userId': self.user,
            'password': self.passwd,
            'service': '%E9%BB%98%E8%AE%A4',    # 默认
            'queryString': self.queryString,
            'operatorPwd': '',
            'operatorUserId': '',
            'validcode': '',
        }
        response = requests.post(f'{self.serverPreFix}/eportal/InterFace.do', params=params, data=data, verify=False)
        text = response.text.encode(response.encoding).decode('utf-8')
        print(text)

    def logout(self):
        params = {
            'method': 'logout',
        }
        response = requests.post(f'{self.serverPreFix}/eportal/InterFace.do', params=params, verify=False)
        print(response.text.encode(response.encoding).decode('utf-8'))

def get_args():
    parser = argparse.ArgumentParser()
    # optional args
    parser.add_argument("-u", "--user", dest="user", type=str, help='user name')
    parser.add_argument("-p", "--passwd", dest="passwd", type=str, help='password')
    # mutex args
    group0 = parser.add_mutually_exclusive_group()
    group0.add_argument('--login', action='store_true', help='login')
    group0.add_argument('--logout', action='store_true', help='logout')
    group1 = parser.add_mutually_exclusive_group()
    group1.add_argument("-r", "--regist", dest="regist", action='store_true', help='regist mac address')
    group1.add_argument("-c", "--cancel", dest="cancel", action='store_true', help='cancel mac address')
    return parser.parse_args()

def do_action(args):
    if args.regist:
        regist = True
    elif args.cancel:
        regist = False
    else:
        regist = None

    net = schoolNet()
    if args.login is True:
        if args.user is None or args.passwd is None:
            print('username或password空!')
            return
        net.set_user(args.user, args.passwd)
        net.login()
        net.do_mac(regist)
    elif args.logout is True:
        net.do_mac(regist)
        net.logout()
    elif regist is not None:
        net.do_mac(regist)

if __name__ == '__main__':
    args = get_args()
    do_action(args)
