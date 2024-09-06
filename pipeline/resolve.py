import os
from git import Repo
from docx import Document

def repo_check(repo_url, repo_dir):
    # 克隆 GitHub 仓库（如果本地不存在）
    if not os.path.exists(repo_dir):
        print(f"Cloning repository from {repo_url}...")
        Repo.clone_from(repo_url, repo_dir)
    else:
        print(f"Repository already cloned in {repo_dir}")