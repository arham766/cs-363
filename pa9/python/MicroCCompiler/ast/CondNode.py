from .ASTNode import ASTNode
from enum import Enum
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
  from .visitor import ASTVisitor

class CondNode(ASTNode):
  class OpType(Enum):
    EQ = 1
    NE = 2
    LT = 3
    LE = 4
    GT = 5
    GE = 6

  def getOpFromString(self, op: str):
    if op == '==':
      return CondNode.OpType.EQ
    elif op == '!=':
      return CondNode.OpType.NE
    elif op == '<':
      return CondNode.OpType.LT
    elif op == '<=':
      return CondNode.OpType.LE
    elif op == '>':
      return CondNode.OpType.GT
    elif op == '>=':
      return CondNode.OpType.GE
    else:
      raise Exception("invalid op in CondNode")

  def __init__(self, left: ASTNode, right: ASTNode, op: str):
    self.setLeft(left)
    self.setRight(right)
    self.setOp(self.getOpFromString(op))

  def accept(self, visitor: 'ASTVisitor') -> Any:
    return visitor.visitCondNode(self)

  def getLeft(self) -> ASTNode:
    return self.left

  def setLeft(self, left: ASTNode):
    self.left = left

  def getRight(self) -> ASTNode:
    return self.right

  def setRight(self, right: ASTNode):
    self.right = right  

  def getOp(self) -> OpType:
    return self.oc

  def setOp(self, op: OpType):
    self.oc = op
 
  def getReversedOp(self, op: OpType) -> OpType:
    if op == CondNode.OpType.LE:
      return CondNode.OpType.GT
    elif op == CondNode.OpType.LT:
      return CondNode.OpType.GE
    elif op == CondNode.OpType.GE:
      return CondNode.OpType.LT
    elif op == CondNode.OpType.GT:
      return CondNode.OpType.LE
    elif op == CondNode.OpType.EQ:
      return CondNode.OpType.NE
    elif op == CondNode.OpType.NE:
      return CondNode.OpType.EQ
    else:
      raise Exception("Bad op type")

