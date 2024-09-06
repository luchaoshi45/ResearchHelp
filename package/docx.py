import os

# 函数：将文件内容添加到 Word 文档
def add_file_to_doc(file_path, doc):
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                doc.add_heading(os.path.basename(file_path), level=2)
                doc.add_paragraph(content)
        except UnicodeDecodeError as e:
            print(f"Error reading file {file_path}: {e}")
    else:
        print(f"File {file_path} not found")