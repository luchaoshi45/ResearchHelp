from core.common_core import CommonCore
from package.common_file import CommonFile
from resolve.resolve import Resolve
from tqdm import tqdm
import time

class MarkdownCore(CommonCore):
    def __init__(self, resolve: Resolve, package: CommonFile):
        super().__init__(resolve, package)
        self.TYPE = '.md'
        self.md_file = dict()

    def run(self):
        self.info()
        
        # 收集 Markdown
        print("\033[92mCollect Markdown File...\033[00m")
        for key, val in tqdm(self.resolve.tree.items()):
            print(key + ': ' + val)
            
            if key.endswith(self.TYPE):
                print("\033[91mFound Markdown file: {}\033[00m".format(key))
                
                # 读取文件内容
                with open(key, 'r', encoding='utf-8') as file:
                    content = file.read()
                    self.md_file[key] = content


        # 写入 Word
        print("\033[92mWrite Markdown File to Docx...\033[00m")
        # 添加文件内容到 Word 文档
        for key, val in tqdm(self.md_file.items()):
            self.package.add_heading(key, level=2)
            self.package.add_paragraph(val)
            
        # 保存文件
        self.package.save()