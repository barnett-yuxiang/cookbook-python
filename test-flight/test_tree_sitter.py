from tree_sitter_languages import get_parser

# 尝试获取一个 Python 的 parser
parser = get_parser('python')

# 测试解析一小段简单代码
source_code = b'''
def hello():
    print("Hello, World!")
'''

tree = parser.parse(source_code)
root_node = tree.root_node

# 打印根节点信息
print(f"Root node type: {root_node.type}")
print(f"Root node start_byte: {root_node.start_byte}")
print(f"Root node end_byte: {root_node.end_byte}")
