import requests


def download_image(url):
    try:
        # 发送GET请求
        response = requests.get(url)

        # 检查请求是否成功
        if response.status_code == 200:
            # 检查响应内容类型
            content_type = response.headers.get('Content-Type')

            # 根据Content-Type确定文件扩展名
            if 'image/jpeg' in content_type:
                file_extension = '.jpg'
            elif 'image/png' in content_type:
                file_extension = '.png'
            elif 'image/gif' in content_type:
                file_extension = '.gif'
            else:
                print("未知的图片格式")
                return  # 如果格式未知，退出函数

            # 保存图片到文件
            with open(f'downloaded_image{file_extension}', 'wb') as file:
                file.write(response.content)
            print(f"图片已保存为 downloaded_image{file_extension}")
        else:
            print(f"请求失败，状态码：{response.status_code}")
    except Exception as e:
        print(f"发生错误：{e}")


# API的URL
url = "https://api.03c3.cn/api/zb"

# 调用函数
download_image(url)