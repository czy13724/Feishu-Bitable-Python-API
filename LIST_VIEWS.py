import requests
import configparser
import json
import argparse

# 此函数用于获取数据表的所有视图，接收四个可选参数
def LIST_VIEWS(app_token=None, table_id=None, user_access_token=None, page_token=None, page_size=None):
    # 读取配置文件
    config = configparser.ConfigParser()
    config.read('feishu-config.ini')

    # 如果参数为空，则使用配置文件中的默认值
    if not app_token:
        app_token = config.get('TOKEN', 'app_token')
    if not table_id:
        table_id = config.get('ID', 'table_id')
    if not user_access_token:
        user_access_token = config.get('TOKEN', 'user_access_token')
    if not page_token:
        page_token = config.get('LIST_VIEWS', 'page_token', fallback=None)
    if not page_size:
        page_size = config.get('LIST_VIEWS', 'page_size', fallback=100)

    # 构造请求URL和头部
    url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{table_id}/views"
    headers = {
        'Authorization': f'Bearer {user_access_token}',
        'Content-Type': 'application/json; charset=utf-8'
    }

    # 如果存在page_token，则添加到请求参数中
    params = {'page_size': page_size}
    if page_token:
        params['page_token'] = page_token

    # 发起请求，并返回响应体的json形式
    response = requests.get(url, headers=headers, params=params)
    return response.json()

if __name__ == "__main__":
    # 解析命令行参数
    parser = argparse.ArgumentParser()
    parser.add_argument('--app_token', help='app token')
    parser.add_argument('--table_id', help='table id')
    parser.add_argument('--user_access_token', help='user access token')
    parser.add_argument('--page_token', help='page token')
    parser.add_argument('--page_size', type=int, help='page size')
    args = parser.parse_args()

    # 调用封装的函数，使用命令行参数或默认值
    response_body = LIST_VIEWS(args.app_token, args.table_id, args.user_access_token, args.page_token, args.page_size)
    print(json.dumps(response_body, indent=4))
