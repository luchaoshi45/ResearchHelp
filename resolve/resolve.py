import os
from git import Repo
from abc import ABC

class Resolve(ABC):
    def __init__(self, repo_url, repo_dir):
        self.repo_url = repo_url
        self.repo_dir = repo_dir
        self.IGNORE_DIRS = [
            '.git', '.github', '.dev_scripts', '.circleci',
            '.idea', '.vscode',  '.venv'
        ]
        # self.SUPPORT_FILES = [
        #     '.py', '.cpp', '.h', '.c', '.java', '.go', '.php', '.rb', '.sh',
        #     '.js', '.html', '.css', '.md', '.txt', '.json', '.xml', '.yml',
        #     '.ts', '.jsx', '.tsx', '.cs', '.bat', '.ini', '.yaml', '.sql', 
        #     '.swift', '.kt', '.rs', '.m', '.pl', '.erl', '.ex', '.exs'
        # ]
        self.SUPPORT_FILES = [
            '.py', '.sh' # only supprot for python project
        ]
        
        
        self.repo_check()
        self.build_tree()
        
    def repo_check(self):
        # 克隆 GitHub 仓库（如果本地不存在）
        if not os.path.exists(self.repo_dir):
            print(f"Cloning repository from {self.repo_url}...")
            Repo.clone_from(self.repo_url, self.repo_dir)
        else:
            print(f"Repository already cloned in {self.repo_dir}")
            
    def build_tree(self):
        self.tree = dict()
        
        for root, dirs, files in os.walk(self.repo_dir):
            for dir in self.IGNORE_DIRS:
                if dir in dirs:
                    dirs.remove(dir)
                 
            for file in files:
                type = file.split('.')[-1]
                if '.'+type in self.SUPPORT_FILES:
                    file_path = os.path.join(root, file)
                    self.tree[file_path] = ""

if __name__ == "__main__":
    import sys
    sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
    from config.config import input_url, input_dir
    resolve = Resolve(input_url, input_dir)
    print(resolve.tree)