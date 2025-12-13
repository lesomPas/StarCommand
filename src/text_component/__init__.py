"""
Minecraft Rawtext JSON Processor
用于处理Minecraft基岩版原始JSON文本格式

主要功能：
- 创建和操作Minecraft原始JSON文本组件
- 序列化和反序列化JSON格式
- 验证和解析Rawtext数据
"""

__version__ = "2.0.0"
__author__ = "lesomras"
__description__ = "Minecraft Rawtext JSON Processor"

# 组件系统
from .components import (
    TextComponent,  # 所有文本组件的基类
    Rawtext,        # Rawtext容器
    Text,           # 纯文本组件
    Score,          # 计分板组件
    Selector,       # 选择器组件
    Translate,      # 翻译组件
)

# 构建器
from .builder import TranslateBuilder  # 翻译构建器

# 解析器
from .parser import (
    Parser,         # 主要解析器
    parse_file,     # 快捷函数：从文件解析
    parse_string,   # 快捷函数：从字符串解析
    to_json_dict,   # 快捷函数：转换为JSON字典
    validate_rawtext_file,    # 快捷函数：验证文件
    validate_rawtext_string,  # 快捷函数：验证字符串
    extract_components,      # 快捷函数：提取组件
    extract_strings,         # 快捷函数：提取字符串
)

# 序列化器
# from ..core.serializer import (
    # JSONSerializer,      # 普通JSON序列化器
    # CompactSerializer,   # 紧凑JSON序列化器
    # load_json,           # 快捷函数：加载JSON
    # loads_json,          # 快捷函数：从字符串加载JSON
    # dump_json,           # 快捷函数：保存JSON
    # dumps_json,          # 快捷函数：序列化为JSON字符串
    # dump_json_compact,   # 快捷函数：保存紧凑JSON
    # dumps_json_compact,  # 快捷函数：序列化为紧凑JSON字符串
# )

# 异常系统
from ..core.exceptions import (
    CommandException,    # 命令异常基类
    MissingArgument,     # 参数缺失异常
    UnsupportedArgument, # 参数类型异常
    MalformedArgument,   # 参数格式异常
)


# 导出列表
__all__ = [
    # 版本信息
    "__version__", "__author__", "__description__",

    # 组件类
    "TextComponent",
    "Rawtext",
    "Text",
    "Score",
    "Selector",
    "Translate",

    # 构建器类
    "TranslateBuilder",

    # 解析器
    "Parser",
    "parse_file",
    "parse_string",
    "to_json_dict",
    "validate_rawtext_file",
    "validate_rawtext_string",
    "extract_components",
    "extract_strings",

    # 序列化器
    # "JSONSerializer",
    # "CompactSerializer",
    # "load_json",
    # "loads_json",
    # "dump_json",
    # "dumps_json",
    # "dump_json_compact",
    # "dumps_json_compact",

    # 异常
    "CommandException",
    "MissingArgument",
    "UnsupportedArgument",
    "MalformedArgument",
]

# 包级配置
CONFIG = {
    "default_indent": 4,          # 默认缩进
    "ensure_ascii": False,        # 默认不强制ASCII编码
    "default_encoding": "utf-8",  # 默认编码
}
