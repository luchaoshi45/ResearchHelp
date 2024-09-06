import os

def markdwon_core(input_dir, add_file_fun, output_file):
    # 添加 README 文件内容到 Word 文档
    readme_path = os.path.join(input_dir, 'README.md')
    add_file_fun(readme_path, output_file)
    # 添加其他文件（如 .md 文件、文档文件等）
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.endswith('.md') and file != 'README.md':
                file_path = os.path.join(root, file)
                add_file_fun(file_path, output_file)
