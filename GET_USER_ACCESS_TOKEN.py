import requests
import configparser
import argparse
import json

def GET_USER_ACCESS_TOKEN(config_path='feishu-config.ini'):
    # 读取配置文件
    config = configparser.ConfigParser()
    config.read(config_path, encoding='utf-8')

    # 从配置文件获取参数
    app_access_token = config.get('TOKEN', 'app_access_token')
    login_code = config.get('TOKEN', 'login_code')

    # 构建请求URL和请求头
    url = "https://open.feishu.cn/open-apis/authen/v1/access_token"
    headers = {
        'Authorization': f'Bearer {app_access_token}',
        'Content-Type': 'application/json; charset=utf-8',
    }

    # 构建请求体
    payload = {
        "grant_type": "authorization_code",
        "code": login_code
    }

    # 发起请求
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    response_json = response.json()

    # 更新配置文件
    if 'data' in response_json and 'access_token' in response_json['data']:
        config.set('TOKEN', 'user_access_token', response_json['data']['access_token'])
        with open(config_path, 'w', encoding='utf-8') as configfile:
            config.write(configfile)

    return response_json.get('data', {}).get('access_token')

def GET_USER_ACCESS_TOKEN_CMD():
    # 解析命令行参数
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', default='feishu-config.ini', help='配置文件路径')
    args = parser.parse_args()

    # 调用 GET_USER_ACCESS_TOKEN 函数，获取 user_access_token
    user_access_token = GET_USER_ACCESS_TOKEN(args.config)
    
    # 打印结果
    print(f'user_access_token: {user_access_token}')

# 主函数
if __name__ == "__main__":
    GET_USER_ACCESS_TOKEN_CMD()