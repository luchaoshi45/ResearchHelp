from config.config import input_url, input_dir, out_dir, out_type, core_type, core_interface
from resolve.resolve import Resolve
from package.docx_file import DocxFile
from core.markdown_core import MarkdownCore
from core.ai_core import AiCore

# 创建 Resolve 对象
resolve = Resolve(input_url, input_dir)

# 运行核心
if out_type == "docx":
    docx_file = DocxFile(out_dir, input_dir.split("/")[-1] + '.' + out_type)

# 创建核心对象
if core_type == "markdown":
    core = MarkdownCore(resolve, docx_file)
elif core_type == "ai":
    core = AiCore(resolve, docx_file, core_interface)
    
    
core.run()  # 运行核心