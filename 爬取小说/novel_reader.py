import requests
from bs4 import BeautifulSoup
import json
import os
from datetime import datetime
from typing import Dict, Optional

class NovelReader:
    def __init__(self, novel_name: str = "大奉打更人"):
        self.novel_name = novel_name
        self.reading_progress = 0
        self.notes_dir = "reading_notes"
        self.template_path = "templates/blog_template.md"
        self.reading_data = self._load_reading_data()
        self.create_notes_directory()

    def _load_reading_data(self) -> Dict:
        """加载阅读进度数据"""
        data_file = os.path.join(self.notes_dir, "reading_progress.json")
        if os.path.exists(data_file):
            with open(data_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {
            "current_chapter": 0,
            "total_chapters": 1000,  # 预设章节数
            "last_read_date": None
        }

    def create_notes_directory(self) -> None:
        """创建必要的目录结构"""
        directories = [
            self.notes_dir,
            os.path.join(self.notes_dir, "blogs"),
            os.path.join(self.notes_dir, "highlights"),
            "templates"
        ]
        for directory in directories:
            os.makedirs(directory, exist_ok=True)
        
        # 如果模板文件不存在，创建默认模板
        if not os.path.exists(self.template_path):
            self._create_default_template()

    def _create_default_template(self) -> None:
        """创建默认博客模板"""
        template_content = """# {书名} - 第{章节}章读书笔记

日期：{日期}

## 阅读进度
- 当前章节：{章节号}
- 总体进度：{进度百分比}%

## 章节概要
{在这里写下本章主要内容}

## 人物分析
{记录本章出现的重要人物及其发展}

## 情节梳理
{记录重要情节发展}

## 精彩片段
> {引用本章精彩段落}

## 个人感想
{写下你的读后感}

## 疑问与思考
{记录阅读过程中的疑问}

---
标签：#{书名} #读书笔记 #{自定义标签}
"""
        with open(self.template_path, 'w', encoding='utf-8') as f:
            f.write(template_content)

    def create_reading_blog(self, chapter_num: int, content: Dict) -> str:
        """创建阅读博客"""
        try:
            blog_file = os.path.join(self.notes_dir, "blogs", f"chapter_{chapter_num:04d}.md")
            progress = (chapter_num / self.reading_data["total_chapters"]) * 100
            
            template_vars = {
                "书名": self.novel_name,
                "章节": chapter_num,
                "日期": datetime.now().strftime("%Y-%m-%d"),
                "章节号": chapter_num,
                "进度百分比": f"{progress:.1f}",
                **content
            }

            with open(self.template_path, 'r', encoding='utf-8') as f:
                template = f.read()

            blog_content = template
            for key, value in template_vars.items():
                blog_content = blog_content.replace(f"{{{key}}}", str(value))

            with open(blog_file, "w", encoding='utf-8') as f:
                f.write(blog_content)

            # 更新阅读进度
            self._update_reading_progress(chapter_num)
            
            return blog_file
        except Exception as e:
            print(f"创建博客时出错: {e}")
            return ""

    def _update_reading_progress(self, chapter_num: int) -> None:
        """更新阅读进度"""
        self.reading_data["current_chapter"] = chapter_num
        self.reading_data["last_read_date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        with open(os.path.join(self.notes_dir, "reading_progress.json"), 'w', encoding='utf-8') as f:
            json.dump(self.reading_data, f, ensure_ascii=False, indent=4)

    def get_reading_progress(self) -> str:
        """获取阅读进度信息"""
        progress = (self.reading_data["current_chapter"] / self.reading_data["total_chapters"]) * 100
        return f"""当前阅读进度：
- 最新章节：第 {self.reading_data["current_chapter"]} 章
- 总进度：{progress:.1f}%
- 最后阅读时间：{self.reading_data["last_read_date"] or "尚未开始阅读"}"""

def main():
    reader = NovelReader()
    
    # 示例：创建一篇读书笔记
    chapter_content = {
        "summary": "许七安初次展露才华，破获一桩离奇案件",
        "characters": "- 许七安：展现缜密推理能力\n- 慕南栀：初次出场",
        "thoughts": "本章展现了主角的聪明才智，为后续剧情埋下伏笔",
        "highlights": "> 「正义，不应被门第所限」"
    }
    
    blog_file = reader.create_reading_blog(1, chapter_content)
    if blog_file:
        print(f"读书笔记已保存到: {blog_file}")
        print("\n" + reader.get_reading_progress())
        
    print("\n推荐阅读渠道：")
    print("1. 起点中文网会员购买：https://book.qidian.com/")
    print("2. 掌阅正版：https://www.zhangyue.com/")
    print("3. 微信读书：https://weread.qq.com/")

if __name__ == "__main__":
    main() 