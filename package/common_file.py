import os
from abc import ABC, abstractmethod

class CommonFile(ABC):
    def __init__(self, out_dir):
        self.out_dir = out_dir
        self.out_dir_check()
        self.COMMON_FILE_HEADER = "GitHub Repository Content"
        
    # 函数：检查输出目录是否存在，不存在则创建
    def out_dir_check(self):
        if not os.path.exists(self.out_dir):
            os.makedirs(self.out_dir)
