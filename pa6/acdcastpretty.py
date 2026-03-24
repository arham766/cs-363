from acdcast import *


def _label(node: ASTNode) -> str:
    if isinstance(node, AssignNode):
        return f"Assign(varname={node.varname!r})"
    if isinstance(node, PrintNode):
        return f"Print(varname={node.varname!r})"
    if isinstance(node, IntDclNode):
        return f"IntDcl(varname={node.varname!r})"
    if isinstance(node, FloatDclNode):
        return f"FloatDcl(varname={node.varname!r})"
    if isinstance(node, StrDclNode):
        return f"StrDcl(varname={node.varname!r})"
    if isinstance(node, BinOpNode):
        op = getattr(node.optype, "name", str(node.optype))
        return f"BinOp(op={op})"
    if isinstance(node, IntLitNode):
        return f"IntLit(value={node.value})"
    if isinstance(node, FloatLitNode):
        return f"FloatLit(value={node.value})"
    if isinstance(node, VarRefNode):
        return f"VarRef(varname={node.varname!r})"
    if isinstance(node, StrLitNode):
        return f"StrLit(value={node.value!r})"
    return type(node).__name__


def _children(node: ASTNode) -> list:
    if isinstance(node, AssignNode):
        return [node.expr]
    if isinstance(node, BinOpNode):
        return [node.left, node.right]
    return []


def _pretty_lines(node: ASTNode, prefix: str = "", is_last: bool = True) -> list:
    lines = []
    if prefix == "" and is_last:
        lines.append(_label(node))
    else:
        connector = "└─ " if is_last else "├─ "
        lines.append(prefix + connector + _label(node))

    kids = _children(node)
    if not kids:
        return lines

    child_prefix = prefix + ("   " if is_last else "│  ")

    for i, child in enumerate(kids):
        child_is_last = (i == len(kids) - 1)
        lines.extend(_pretty_lines(child, child_prefix, child_is_last))

    return lines


def pretty_str(node: ASTNode) -> str:
    if node is None:
        return "<None>"
    return "\n".join(_pretty_lines(node))


def pretty_print(node: ASTNode) -> None:
    print(pretty_str(node))