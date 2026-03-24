from acdcast import *

class SemanticError(Exception):
    pass

def semanticanalysis(program: list[ASTNode]) -> None:
    declared: dict[str, str] = {}

    def typeof_expr(node: ASTNode) -> str:
        if isinstance(node, IntLitNode):
            return "int"
        elif isinstance(node, FloatLitNode):
            return "float"
        elif isinstance(node, StrLitNode):
            return "str"
        elif isinstance(node, VarRefNode):
            if node.varname not in declared:
                raise SemanticError(f"Variable {node.varname} not declared")
            return declared[node.varname]
        elif isinstance(node, BinOpNode):
            left_type = typeof_expr(node.left)
            right_type = typeof_expr(node.right)
            if left_type == "str" or right_type == "str":
                raise SemanticError(
                    f"Cannot use string in arithmetic operation"
                )
            if left_type != right_type:
                raise SemanticError(
                    f"Type mismatch: cannot mix {left_type} and {right_type} in expression"
                )
            return left_type
        else:
            raise SemanticError(f"Unknown expression node: {type(node).__name__}")

    def visit(node: ASTNode):
        if isinstance(node, IntDclNode):
            if node.varname in declared:
                raise SemanticError(f"Variable {node.varname} already declared")
            declared[node.varname] = "int"

        elif isinstance(node, FloatDclNode):
            if node.varname in declared:
                raise SemanticError(f"Variable {node.varname} already declared")
            declared[node.varname] = "float"

        elif isinstance(node, StrDclNode):
            if node.varname in declared:
                raise SemanticError(f"Variable {node.varname} already declared")
            declared[node.varname] = "str"

        elif isinstance(node, PrintNode):
            if node.varname not in declared:
                raise SemanticError(f"Variable {node.varname} not declared")

        elif isinstance(node, AssignNode):
            if node.varname not in declared:
                raise SemanticError(f"Variable {node.varname} not declared")
            var_type = declared[node.varname]
            expr_type = typeof_expr(node.expr)
            if var_type != expr_type:
                raise SemanticError(
                    f"Type mismatch: cannot assign {expr_type} to {var_type} variable {node.varname}"
                )
        else:
            raise SemanticError(f"Unknown statement node: {type(node).__name__}")

    for stmt in program:
        visit(stmt)