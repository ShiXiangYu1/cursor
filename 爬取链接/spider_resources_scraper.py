import requests
from bs4 import BeautifulSoup
import json

def scrape_spider_resources():
    # 预定义一些优质的中文爬虫学习资源
    resources = [
        {
            "title": "Python爬虫入门教程",
            "url": "https://www.runoob.com/python3/python3-spider.html",
            "source": "菜鸟教程",
            "difficulty": "入门"
        },
        {
            "title": "Python3网络爬虫实战",
            "url": "https://www.bilibili.com/video/BV1Yh411o7Sz",
            "source": "Bilibili",
            "difficulty": "入门到中级"
        },
        {
            "title": "Python爬虫教程",
            "url": "https://www.w3school.com.cn/python/python_spider.asp",
            "source": "W3School中文",
            "difficulty": "入门"
        },
        {
            "title": "Python网络爬虫从入门到实践",
            "url": "https://www.bilibili.com/video/BV1rv4y1H7o6",
            "source": "Bilibili",
            "difficulty": "实战"
        }
    ]
    
    # 保存为文本文件
    with open('spider_learning_resources.txt', 'w', encoding='utf-8') as f:
        for r in resources:
            f.write(f"课程名称: {r['title']}\n")
            f.write(f"难度: {r['difficulty']}\n")
            f.write(f"来源: {r['source']}\n")
            f.write(f"链接: {r['url']}\n\n")
    
    return resources

if __name__ == "__main__":
    results = scrape_spider_resources()
    print("推荐的爬虫学习资源：")
    for idx, resource in enumerate(results, 1):
        print(f"\n{idx}. {resource['title']}")
        print(f"难度: {resource['difficulty']}")
        print(f"来源: {resource['source']}")
        print(f"链接: {resource['url']}") 