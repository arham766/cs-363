from acdcast import *

def semanticanalysis(program: list[ASTNode]) -> None:
    declared = set()

    def visit(node: ASTNode):
        if isinstance(node, IntDclNode):
            if node.varname in declared:
                raise Exception(f"Variable {node.varname} already declared")
            declared.add(node.varname)
        elif isinstance(node, PrintNode):
            if node.varname not in declared:
                raise Exception(f"Variable {node.varname} not declared")
        elif isinstance(node, AssignNode):
            if node.varname not in declared:
                raise Exception(f"Variable {node.varname} not declared")
            visit(node.expr)
        elif isinstance(node, VarRefNode):
            if node.varname not in declared:
                raise Exception(f"Variable {node.varname} not declared")
        elif isinstance(node, BinOpNode):
            visit(node.left)
            visit(node.right)
        elif isinstance(node, IntLitNode):
            pass

    for stmt in program:
        visit(stmt)