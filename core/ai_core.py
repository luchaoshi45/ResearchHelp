from core.common_core import CommonCore
from package.common_file import CommonFile
from resolve.resolve import Resolve
from core.ai_interface import AI_INTERFACE
from tqdm import tqdm
from core.database.redis import table_files

class AiCore(CommonCore):
    def __init__(self, resolve: Resolve, package: CommonFile, ai):
        super().__init__(resolve, package)
        self.ai = AI_INTERFACE[ai]
        self.USER_PROMPT_CMD = "请为我的工程生成专业的文档, 下面是工程的字典，" + \
            "它的键值是各个文件的路径，它的值是各个文件的内容。\n"
        
    def run(self):
        # 打印信息
        self.info()
        
        # 构造提示词
        self.construct()
        
        # 生成文档
        print("\033[92mAI Reasoning...\033[00m")
        user_prompt = self.USER_PROMPT_CMD + str(table_files)
        res = self.ai(user_prompt)
        
        # 写入文档
        self.package.add_paragraph(res)
        self.package.save()

    # 构造提示词
    def construct(self):
        print("\033[92mCollect File...\033[00m")
        for key, val in tqdm(self.resolve.tree.items()):
            print(key + ': ' + val)
            table_files[key] = self.read_file(key)
    
    # 读取文件
    def read_file(self, dir):
        with open(dir, 'r', encoding='utf-8') as f:
            return f.read()
        
if __name__ == '__main__':
    ai_core = AiCore()
    print(ai_core.ai)