import sys
from .AbstractASTVisitor import AbstractASTVisitor
from ...compiler.Scope import Scope
from ...ast.BinaryOpNode import BinaryOpNode
from ...ast.AssignNode import AssignNode
from ...ast.CondNode import CondNode
from ...ast.CallNode import CallNode
from ...ast.ReturnNode import ReturnNode
from typing import Any

class TypeCheckVisitor(AbstractASTVisitor):

    def _type_error(self):
        print("TYPE ERROR", file=sys.stderr)
        sys.exit(7)

    def postprocessBinaryOpNode(self, node: BinaryOpNode, left: Any, right: Any) -> Any:
        if node.getLeft().getType() != node.getRight().getType():
            self._type_error()
        node.setType(node.getLeft().getType())
        return None

    def postprocessAssignNode(self, node: AssignNode, left: Any, right: Any) -> Any:
        if node.getLeft().getType() != node.getRight().getType():
            self._type_error()
        return None

    def postprocessCondNode(self, node: CondNode, left: Any, right: Any) -> Any:
        if node.getLeft().getType() != node.getRight().getType():
            self._type_error()
        return None

    def postprocessCallNode(self, node: CallNode, args: Any) -> Any:
        ste = node.ste
        ste_arg_types = ste.getArgTypes()
        node_args = node.getArgs()
        
        if len(ste_arg_types) != len(node_args):
            self._type_error()

        for st_type, as_node in zip(ste_arg_types, node_args):
            if st_type != as_node.getType():
                self._type_error()
        
        return None

    def postprocessReturnNode(self, node: ReturnNode, retExpr: Any) -> Any:
        funcSymbol = node.getFuncSymbol()
        if node.getRetExpr() is not None:
            if node.getRetExpr().getType() != funcSymbol.getReturnType():
                self._type_error()
        return None
