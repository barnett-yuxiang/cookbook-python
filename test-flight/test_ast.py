import ast

# Step 1: Read the existing Python file
with open('./test-flight/test_abc.py', 'r', encoding='utf-8') as file:
    source_code = file.read()

# Step 2: Parse the source code into an AST
tree = ast.parse(source_code)

# Step 3: Define a Visitor class to traverse the AST
class Analyzer(ast.NodeVisitor):
    def visit_FunctionDef(self, node):
        print(f"Found a function: {node.name} at line {node.lineno}")
        self.generic_visit(node)  # Continue visiting inside the function

    def visit_ClassDef(self, node):
        print(f"Found a class: {node.name} at line {node.lineno}")
        self.generic_visit(node)

    def visit_Assign(self, node):
        # Simple example: find assignments
        targets = [target.id for target in node.targets if isinstance(target, ast.Name)]
        print(f"Found assignment to: {targets} at line {node.lineno}")
        self.generic_visit(node)

    def visit_Call(self, node):
        if isinstance(node.func, ast.Name) and node.func.id == 'print':
            print(f"Found a print statement at line {node.lineno}")
        self.generic_visit(node)

# Step 4: Use the Visitor to traverse the AST
analyzer = Analyzer()
analyzer.visit(tree)

print(ast.dump(tree, indent=4))
