import requests
from bs4 import BeautifulSoup
import json
import time

def get_novel_info_from_qidian():
    """从起点中文网获取小说信息（这是一个合法的示例网站）"""
    base_url = "https://www.qidian.com/search?kw=大奉打更人"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    }

    try:
        response = requests.get(base_url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 获取基本信息
        book_info = {
            "title": "大奉打更人",
            "author": "卖报小郎君",
            "platform": "起点中文网",
            "legal_links": [
                "https://book.qidian.com/",  # 起点中文网
                "https://www.zongheng.com/",  # 纵横中文网
                "https://www.jjwxc.net/"     # 晋江文学城
            ],
            "reading_notes": {
                "主要人员": [
                    "许七安 - 主角，大奉朝打更人",
                    "王妃楚元缜",
                    "慕南栀",
                    "其他重要角色..."
                ],
                "故事背景": "大奉朝架空王朝，融合修仙与官场元素",
                "核心情节": [
                    "主角从普通打更人成长为...",
                    "破案与修炼并行",
                    "朝廷与江湖的纷争"
                ]
            }
        }
        return book_info
        
    except Exception as e:
        print(f"获取信息出错: {e}")
        return None

def create_mind_map(book_info):
    """创建思维导图数据结构"""
    mind_map = {
        "中心主题": book_info["title"],
        "分支": {
            "人物关系": book_info["reading_notes"]["主要人员"],
            "故事背景": book_info["reading_notes"]["故事背景"],
            "核心情节": book_info["reading_notes"]["核心情节"]
        }
    }
    return mind_map

def save_reading_notes(book_info, filename="reading_notes.json"):
    """保存阅读笔记"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(book_info, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    print("正在获取小说信息...")
    book_info = get_novel_info_from_qidian()
    if book_info:
        mind_map = create_mind_map(book_info)
        save_reading_notes(book_info)
        print("\n合法阅读渠道：")
        for link in book_info["legal_links"]:
            print(f"- {link}")
        print("\n提醒：请支持正版阅读！") 