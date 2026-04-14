import sys
import os

from .CodeObject import CodeObject
from .InstructionList import InstructionList
from .instructions import *
from ..compiler import *
from ..ast import *
from ..ast.visitor.AbstractASTVisitor import AbstractASTVisitor

class CodeGenerator(AbstractASTVisitor):

  def __init__(self):
    self.intRegCount = 1 
    self.floatRegCount = 1 
    self.intTempPrefix = 't'
    self.floatTempPrefix = 'f'
    self.numCtrlStructs = 0

  def getIntRegCount(self):
    return self.intRegCount

  def getFloatRegCount(self):
    return self.floatRegCount

  def postprocessVarNode(self, node: VarNode) -> CodeObject:
    sym = node.getSymbol()
    co = CodeObject(sym)
    co.lval = True
    co.type = node.getType()
    return co
  
  def postprocessIntLitNode(self, node: IntLitNode) -> CodeObject:
    co = CodeObject()
    temp = self.generateTemp(Scope.Type.INT)
    val = node.getVal()
    co.code.append(Li(temp, val))
    co.temp = temp
    co.lval = False
    co.type = node.getType()
    return co

  def postprocessFloatLitNode(self, node: FloatLitNode) -> CodeObject:
    co = CodeObject()
    temp = self.generateTemp(Scope.Type.FLOAT)
    val = node.getVal()
    co.code.append(FImm(temp, val))
    co.temp = temp
    co.lval = False
    co.type = node.getType()
    return co

  def postprocessBinaryOpNode(self, node: BinaryOpNode, left: CodeObject, right: CodeObject) -> CodeObject:
    co = CodeObject()

    if left.lval:
      left = self.rvalify(left)
    if right.lval:
      right = self.rvalify(right)

    co.code.extend(left.code)
    co.code.extend(right.code)

    op = node.getOp()
    if left.type == Scope.Type.INT and right.type == Scope.Type.INT:
      temp = self.generateTemp(Scope.Type.INT)
      if op == BinaryOpNode.OpType.ADD:
        co.code.append(Add(left.temp, right.temp, temp))
      elif op == BinaryOpNode.OpType.SUB:
        co.code.append(Sub(left.temp, right.temp, temp))
      elif op == BinaryOpNode.OpType.MUL:
        co.code.append(Mul(left.temp, right.temp, temp))
      elif op == BinaryOpNode.OpType.DIV:
        co.code.append(Div(left.temp, right.temp, temp))
      else:
        raise Exception("Unknown operator: " + str(op))
      co.type = Scope.Type.INT
    elif left.type == Scope.Type.FLOAT and right.type == Scope.Type.FLOAT:
      temp = self.generateTemp(Scope.Type.FLOAT)
      if op == BinaryOpNode.OpType.ADD:
        co.code.append(FAdd(left.temp, right.temp, temp))
      elif op == BinaryOpNode.OpType.SUB:
        co.code.append(FSub(left.temp, right.temp, temp))
      elif op == BinaryOpNode.OpType.MUL:
        co.code.append(FMul(left.temp, right.temp, temp))
      elif op == BinaryOpNode.OpType.DIV:
        co.code.append(FDiv(left.temp, right.temp, temp))
      else:
        raise Exception("Unknown operator: " + str(op))
      co.type = Scope.Type.FLOAT
    else:
      raise Exception("Mismatched types in BinaryOpNode")

    co.temp = temp
    co.lval = False

    return co

  def postprocessUnaryOpNode(self, node: UnaryOpNode, expr: CodeObject) -> CodeObject:
    co = CodeObject()

    if expr.lval:
      expr = self.rvalify(expr)

    co.code.extend(expr.code)

    if expr.type == Scope.Type.INT:
      temp = self.generateTemp(Scope.Type.INT)
      co.code.append(Neg(expr.temp, temp))

    elif expr.type == Scope.Type.FLOAT:
      temp = self.generateTemp(Scope.Type.FLOAT)
      co.code.append(FNeg(expr.temp, temp))

    else:
      raise Exception("Non int/float type in unary op!")

    co.type = expr.type
    co.temp = temp
    co.lval = False 

    return co

  def postprocessAssignNode(self, node: AssignNode, left: CodeObject, right: CodeObject) -> CodeObject:
    co = CodeObject()

    if right.lval:
      right = self.rvalify(right)

    co.code.extend(left.code)
    co.code.extend(right.code)

    address = self.generateAddrFromVariable(left)
    temp1 = self.generateTemp(Scope.Type.INT)
    co.code.append(La(temp1, address))

    if left.type == Scope.Type.INT:
      co.code.append(Sw(right.temp, temp1, '0'))
    elif left.type == Scope.Type.FLOAT:
      co.code.append(Fsw(right.temp, temp1, '0'))
    else:
      raise Exception("Mismatched or unknown type in AssignNode")
      
    co.type = left.type
    co.lval = False
    co.temp = right.temp

    return co

  def postprocessStatementListNode(self, node: StatementListNode, statements: list) -> CodeObject:
    co = CodeObject()

    for subcode in statements:
      if subcode is not None:
        co.code.extend(subcode.code)

    co.type = None
    return co
	
  def postprocessReadNode(self, node: ReadNode, var: CodeObject) -> CodeObject:
    co = CodeObject()

    assert(var.isVar())

    if var.type is Scope.Type.INT:
      temp = self.generateTemp(Scope.Type.INT)
      co.code.append(GetI(temp))
      address = self.generateAddrFromVariable(var)
      temp2 = self.generateTemp(Scope.Type.INT)
      co.code.append(La(temp2, address))
      co.code.append(Sw(temp, temp2, '0'))

    elif var.type is Scope.Type.FLOAT:
      temp = self.generateTemp(Scope.Type.FLOAT)
      co.code.append(GetF(temp))
      address = self.generateAddrFromVariable(var)
      temp2 = self.generateTemp(Scope.Type.INT)
      co.code.append(La(temp2, address))
      co.code.append(Fsw(temp, temp2, '0'))

    else:
      raise Exception("Bad type in read node")

    return co

  def postprocessWriteNode(self, node: WriteNode, expr: CodeObject) -> CodeObject:
    co = CodeObject()

    if expr.type == Scope.Type.STRING:
      address = self.generateAddrFromVariable(expr)
      temp = self.generateTemp(Scope.Type.INT)
      co.code.append(La(temp, address))
      co.code.append(PutS(temp))
    else:
      if expr.lval:
        expr = self.rvalify(expr)
      co.code.extend(expr.code)
      if expr.type == Scope.Type.INT:
        co.code.append(PutI(expr.temp))
      elif expr.type == Scope.Type.FLOAT:
        co.code.append(PutF(expr.temp))

    return co

  def postprocessCondNode(self, node: CondNode, left: CodeObject, right: CodeObject) -> CodeObject:
    node.setOp(node.getReversedOp(node.getOp())) 
    co = CodeObject()
    
    if left.lval: left = self.rvalify(left)
    if right.lval: right = self.rvalify(right)
    
    co.code.extend(left.code)
    co.code.extend(right.code)
    
    co.temp = left.temp
    co.temp2 = right.temp
    co.cmptype = node.getOp()
    co.type = left.type
    return co

  def _generateBranch(self, co: CodeObject, cond: CodeObject, target_label: str):
    if cond.type == Scope.Type.INT:
        if cond.cmptype == CondNode.OpType.EQ:
            co.code.append(Beq(cond.temp, cond.temp2, target_label))
        elif cond.cmptype == CondNode.OpType.NE:
            co.code.append(Bne(cond.temp, cond.temp2, target_label))
        elif cond.cmptype == CondNode.OpType.LT:
            co.code.append(Blt(cond.temp, cond.temp2, target_label))
        elif cond.cmptype == CondNode.OpType.LE:
            co.code.append(Ble(cond.temp, cond.temp2, target_label))
        elif cond.cmptype == CondNode.OpType.GT:
            co.code.append(Bgt(cond.temp, cond.temp2, target_label))
        elif cond.cmptype == CondNode.OpType.GE:
            co.code.append(Bge(cond.temp, cond.temp2, target_label))
    elif cond.type == Scope.Type.FLOAT:
        temp = self.generateTemp(Scope.Type.INT)
        if cond.cmptype == CondNode.OpType.EQ:
            co.code.append(Feq(cond.temp, cond.temp2, temp))
            co.code.append(Bne(temp, 'x0', target_label))
        elif cond.cmptype == CondNode.OpType.NE:
            co.code.append(Feq(cond.temp, cond.temp2, temp))
            co.code.append(Beq(temp, 'x0', target_label))
        elif cond.cmptype == CondNode.OpType.LT:
            co.code.append(Flt(cond.temp, cond.temp2, temp))
            co.code.append(Bne(temp, 'x0', target_label))
        elif cond.cmptype == CondNode.OpType.LE:
            co.code.append(Fle(cond.temp, cond.temp2, temp))
            co.code.append(Bne(temp, 'x0', target_label))
        elif cond.cmptype == CondNode.OpType.GT:
            co.code.append(Flt(cond.temp2, cond.temp, temp)) 
            co.code.append(Bne(temp, 'x0', target_label))
        elif cond.cmptype == CondNode.OpType.GE:
            co.code.append(Fle(cond.temp2, cond.temp, temp))
            co.code.append(Bne(temp, 'x0', target_label))

  def postprocessIfStatementNode(self, node: IfStatementNode, cond: CodeObject, tlist: CodeObject, elist: CodeObject) -> CodeObject:
    self._incrnumCtrlStruct()
    labelnum = self._getnumCtrlStruct()
    
    co = CodeObject()
    co.code.extend(cond.code)
    
    else_label = self._generateElseLabel(labelnum)
    done_label = self._generateDoneLabel(labelnum)
    
    self._generateBranch(co, cond, else_label)
    
    if tlist is not None:
        co.code.extend(tlist.code)
        
    co.code.append(J(done_label))
    co.code.append(Label(else_label))
    
    if elist is not None:
        co.code.extend(elist.code)
        
    co.code.append(Label(done_label))
    
    return co

  def postprocessWhileNode(self, node: WhileNode, cond: CodeObject, wlist: CodeObject) -> CodeObject:
    self._incrnumCtrlStruct()
    labelnum = self._getnumCtrlStruct()
    
    co = CodeObject()
    loop_label = self._generateLoopLabel(labelnum)
    done_label = self._generateDoneLabel(labelnum)
    
    co.code.append(Label(loop_label))
    co.code.extend(cond.code)
    
    self._generateBranch(co, cond, done_label)
    
    if wlist is not None:
        co.code.extend(wlist.code)
        
    co.code.append(J(loop_label))
    co.code.append(Label(done_label))
    
    return co

  def postprocessReturnNode(self, node: ReturnNode, retExpr: CodeObject) -> CodeObject:
    co = CodeObject()

    if retExpr.lval is True:
      retExpr = self.rvalify(retExpr)

    co.code.extend(retExpr.code)
    co.code.append(Halt())
    co.type = None
    return co

  def generateTemp(self, t: Scope.Type) -> str:
    if t == Scope.Type.INT:
      s = self.intTempPrefix + str(self.intRegCount)
      self.intRegCount += 1
      return s
    elif t == Scope.Type.FLOAT:
      s = self.floatTempPrefix + str(self.floatRegCount)
      self.floatRegCount += 1
      return s
    else:
      raise Exception("Generating temp for bad type")

  def rvalify(self, lco : CodeObject) -> CodeObject:
    assert(lco.lval is True)
    assert(lco.isVar() is True)
    
    co = CodeObject()

    address = self.generateAddrFromVariable(lco)
    temp1 = self.generateTemp(Scope.Type.INT) 
    co.code.append(La(temp1, address)) 

    if lco.type is Scope.Type.INT:
      temp2 = self.generateTemp(Scope.Type.INT)
      co.code.append(Lw(temp2, temp1, '0'))

    elif lco.type is Scope.Type.FLOAT:
      temp2 = self.generateTemp(Scope.Type.FLOAT)
      co.code.append(Flw(temp2, temp1, '0'))

    else:
      raise Exception("Bad type in rvalify!")

    co.type = lco.type
    co.lval = False
    co.temp = temp2

    return co
    
  def generateAddrFromVariable(self, lco: CodeObject) -> str:
    assert(lco.isVar() is True)
    symbol = lco.getSTE()   
    address = str(symbol.getAddress()) 
    return address

  def _incrnumCtrlStruct(self):
    self.numCtrlStructs += 1

  def _getnumCtrlStruct(self) -> int:
    return self.numCtrlStructs
  
  def _generateThenLabel(self, num: int) -> str:
    return "then"+str(num)

  def _generateElseLabel(self, num: int) -> str:
    return "else"+str(num)

  def _generateLoopLabel(self, num: int) -> str:
    return "loop"+str(num)

  def _generateDoneLabel(self, num: int) -> str:
    return "done"+str(num)