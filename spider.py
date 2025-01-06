import requests
from bs4 import BeautifulSoup
import os
import re
from urllib.parse import quote

def download_images(keyword, num_images=10):
    # 创建保存图片的文件夹
    if not os.path.exists('images'):
        os.makedirs('images')
    
    # 对关键词进行URL编码
    encoded_keyword = quote(keyword)
    
    # 构建百度图片搜索URL
    url = f"https://image.baidu.com/search/flip?tn=baiduimage&word={encoded_keyword}"
    
    # 设置请求头，模拟浏览器访问
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        # 发送请求获取页面内容
        response = requests.get(url, headers=headers)
        response.encoding = 'utf-8'
        
        # 使用正则表达式提取图片URL
        img_urls = re.findall('"objURL":"(.*?)",', response.text)
        
        # 下载指定数量的图片
        count = 0
        for img_url in img_urls:
            if count >= num_images:
                break
                
            try:
                img_response = requests.get(img_url, headers=headers, timeout=10)
                
                # 确保请求成功
                if img_response.status_code == 200:
                    # 保存图片
                    file_name = f'images/{keyword}_{count+1}.jpg'
                    with open(file_name, 'wb') as f:
                        f.write(img_response.content)
                    print(f'成功下载第 {count+1} 张图片')
                    count += 1
                    
            except Exception as e:
                print(f'下载图片失败: {str(e)}')
                continue
                
        print(f'\n总共成功下载 {count} 张图片')
        
    except Exception as e:
        print(f'发生错误: {str(e)}')

if __name__ == "__main__":
    keyword = "王鹤棣"
    download_images(keyword) 