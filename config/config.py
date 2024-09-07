# 配置 GitHub 仓库的 URL 和本地存储路径
input_url = 'https://github.com/luchaoshi45/TigerBalm.git'
input_dir = 'input/TigerBalm'
# input_url = 'https://github.com/ultralytics/yolov3.git'
# input_dir = 'input/yolov3'
# input_url = 'https://github.com/luchaoshi45/cloud_storage.git'
# input_dir = 'input/cloud_storage'

# 创建输出目录
out_dir = "output/"
out_type = "docx"
assert out_type in ["docx"], "Output type not supported"

# 创建核心类型
core_type = "ai"