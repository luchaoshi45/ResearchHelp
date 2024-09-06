import os
from git import Repo
from docx import Document

from pipeline.resolve import repo_check
from package.common import out_dir_check
from package.docx import add_file_to_doc
from core.markdown_core import markdwon_core

# 配置 GitHub 仓库的 URL 和本地存储路径
input_url = 'https://github.com/luchaoshi45/TigerBalm.git'
input_dir = 'input/TigerBalm'

# 创建输出目录
out_dir = "output/"
out_type = "docx"
assert out_type in ["docx"], "Output type not supported"

# 检查 GitHub 仓库和输出目录
repo_check(input_url, input_dir)
out_dir_check(out_dir)


if out_type == "docx":
    # 创建一个新的 Word 文档
    doc = Document()
    doc.add_heading('GitHub Repository Content', level=1)
    
    markdwon_core(input_dir, add_file_to_doc, doc)
    
    # 保存 Word 文档
    doc.save(out_dir + input_dir.split("/")[-1] + '.docx')
    print("Word document created: " 
          + out_dir + input_dir.split("/")[-1] + '.docx')