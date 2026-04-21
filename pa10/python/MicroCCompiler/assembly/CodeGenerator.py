import sys
import os
from typing import List

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
    self.loopLabel = 0
    self.elseLabel = 0
    self.outLabel = 0
    self.currFunc = None
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
    if left.lval: left = self.rvalify(left)
    if right.lval: right = self.rvalify(right)
    co.code.extend(left.code)
    co.code.extend(right.code)

    op = node.getOp()
    if left.type == Scope.Type.INT and right.type == Scope.Type.INT:
      temp = self.generateTemp(Scope.Type.INT)
      op_map = {BinaryOpNode.OpType.ADD: Add, BinaryOpNode.OpType.SUB: Sub, BinaryOpNode.OpType.MUL: Mul, BinaryOpNode.OpType.DIV: Div}
      co.code.append(op_map[op](left.temp, right.temp, temp))
      co.type = Scope.Type.INT
    else:
      temp = self.generateTemp(Scope.Type.FLOAT)
      op_map = {BinaryOpNode.OpType.ADD: FAdd, BinaryOpNode.OpType.SUB: FSub, BinaryOpNode.OpType.MUL: FMul, BinaryOpNode.OpType.DIV: FDiv}
      co.code.append(op_map[op](left.temp, right.temp, temp))
      co.type = Scope.Type.FLOAT

    co.temp = temp
    co.lval = False
    return co

  def postprocessUnaryOpNode(self, node: UnaryOpNode, expr: CodeObject) -> CodeObject:
    co = CodeObject()
    if expr.lval: expr = self.rvalify(expr)
    co.code.extend(expr.code)

    if expr.type == Scope.Type.INT:
      temp = self.generateTemp(Scope.Type.INT)
      co.code.append(Neg(expr.temp, temp))
    else:
      temp = self.generateTemp(Scope.Type.FLOAT)
      co.code.append(FNeg(expr.temp, temp))

    co.type = expr.type
    co.temp = temp
    co.lval = False 
    return co

  def postprocessAssignNode(self, node: AssignNode, left: CodeObject, right: CodeObject) -> CodeObject:
    co = CodeObject()
    if right.lval: right = self.rvalify(right)
    co.code.extend(left.code)
    co.code.extend(right.code)

    address = self.generateAddrFromVariable(left)
    temp1 = self.generateTemp(Scope.Type.INT)
    
    if left.getSTE().isLocal():
        co.code.append(Addi("fp", address, temp1))
    else:
        co.code.append(La(temp1, address))

    if left.type == Scope.Type.INT:
      co.code.append(Sw(right.temp, temp1, '0'))
    else:
      co.code.append(Fsw(right.temp, temp1, '0'))
      
    co.type = left.type
    co.lval = False
    co.temp = right.temp
    return co

  def postprocessStatementListNode(self, node: StatementListNode, statements: list) -> CodeObject:
    co = CodeObject()
    for subcode in statements:
      if subcode is not None: co.code.extend(subcode.code)
    co.type = None
    return co
	
  def postprocessReadNode(self, node: ReadNode, var: CodeObject) -> CodeObject:
    co = CodeObject()
    if var.type is Scope.Type.INT:
      temp = self.generateTemp(Scope.Type.INT)
      co.code.append(GetI(temp))
      address = self.generateAddrFromVariable(var)
      temp2 = self.generateTemp(Scope.Type.INT)
      if var.getSTE().isLocal(): co.code.append(Addi("fp", address, temp2))
      else: co.code.append(La(temp2, address))
      co.code.append(Sw(temp, temp2, '0'))
    else:
      temp = self.generateTemp(Scope.Type.FLOAT)
      co.code.append(GetF(temp))
      address = self.generateAddrFromVariable(var)
      temp2 = self.generateTemp(Scope.Type.INT)
      if var.getSTE().isLocal(): co.code.append(Addi("fp", address, temp2))
      else: co.code.append(La(temp2, address))
      co.code.append(Fsw(temp, temp2, '0'))
    return co

  def postprocessWriteNode(self, node: WriteNode, expr: CodeObject) -> CodeObject:
    co = CodeObject()
    if expr.type == Scope.Type.STRING:
      address = self.generateAddrFromVariable(expr)
      temp = self.generateTemp(Scope.Type.INT)
      co.code.append(La(temp, address))
      co.code.append(PutS(temp))
    else:
      if expr.lval: expr = self.rvalify(expr)
      co.code.extend(expr.code)
      if expr.type == Scope.Type.INT:
        co.code.append(PutI(expr.temp))
      else:
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
        ops = {CondNode.OpType.EQ: Beq, CondNode.OpType.NE: Bne, CondNode.OpType.LT: Blt,
               CondNode.OpType.LE: Ble, CondNode.OpType.GT: Bgt, CondNode.OpType.GE: Bge}
        co.code.append(ops[cond.cmptype](cond.temp, cond.temp2, target_label))
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
    if tlist is not None: co.code.extend(tlist.code)
    co.code.append(J(done_label))
    co.code.append(Label(else_label))
    if elist is not None: co.code.extend(elist.code)
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
    if wlist is not None: co.code.extend(wlist.code)
    co.code.append(J(loop_label))
    co.code.append(Label(done_label))
    return co

  def postprocessReturnNode(self, node: ReturnNode, retExpr: CodeObject) -> CodeObject:
    co = CodeObject()
    if retExpr is not None:
        if retExpr.lval is True: retExpr = self.rvalify(retExpr)
        co.code.extend(retExpr.code)
        
        temp = self.generateTemp(Scope.Type.INT)
        co.code.append(Addi("fp", "8", temp))
        if retExpr.type == Scope.Type.INT:
            co.code.append(Sw(retExpr.temp, temp, "0"))
        elif retExpr.type == Scope.Type.FLOAT:
            co.code.append(Fsw(retExpr.temp, temp, "0"))
            
    co.code.append(J(self._generateFunctionRetLabel()))
    co.type = None
    return co

  def preprocessFunctionNode(self, node: FunctionNode):
    self.currFunc = node.getFuncName()
    self.intRegCount = 0
    self.floatRegCount = 0

  def postprocessFunctionNode(self, node: FunctionNode, body: CodeObject) -> CodeObject:
    co = CodeObject()
    co.code.append(Label(self._generateFunctionEntryLabel()))
    co.code.append(Addi("sp", "-4", "sp"))
    co.code.append(Sw("fp", "sp", "0"))
    co.code.append(Mv("sp", "fp"))

    if self.intRegCount > 0:
        co.code.append(Addi("sp", str(-4 * self.intRegCount), "sp"))
        for i in range(self.intRegCount):
            co.code.append(Sw(self.intTempPrefix + str(i), "sp", str(4 * i)))
            
    if self.floatRegCount > 0:
        co.code.append(Addi("sp", str(-4 * self.floatRegCount), "sp"))
        for i in range(self.floatRegCount):
            co.code.append(Fsw(self.floatTempPrefix + str(i), "sp", str(4 * i)))

    numLocals = node.getScope().getNumLocals()
    if numLocals > 0:
        co.code.append(Addi("sp", str(-4 * numLocals), "sp"))

    co.code.append(Label(self._generateFunctionCodeLabel()))
    if body is not None:
        co.code.extend(body.code)
    
    co.code.append(Label(self._generateFunctionRetLabel()))

    if numLocals > 0:
        co.code.append(Addi("sp", str(4 * numLocals), "sp"))

    if self.floatRegCount > 0:
        for i in reversed(range(self.floatRegCount)):
            co.code.append(Flw(self.floatTempPrefix + str(i), "sp", str(4 * i)))
        co.code.append(Addi("sp", str(4 * self.floatRegCount), "sp"))
        
    if self.intRegCount > 0:
        for i in reversed(range(self.intRegCount)):
            co.code.append(Lw(self.intTempPrefix + str(i), "sp", str(4 * i)))
        co.code.append(Addi("sp", str(4 * self.intRegCount), "sp"))

    co.code.append(Mv("fp", "sp"))
    co.code.append(Lw("fp", "sp", "0"))
    co.code.append(Addi("sp", "4", "sp"))
    co.code.append(Ret())
    return co

  def postprocessFunctionListNode(self, node: FunctionListNode, functions: List[CodeObject]) -> CodeObject:
    co = CodeObject()
    co.code.append(Mv("sp", "fp"))
    co.code.append(Jr(self._generateFunctionEntryLabel("main")))
    co.code.append(Halt())
    co.code.append(Blank())
    for c in functions:
        if c is not None:
            co.code.extend(c.code)
            co.code.append(Blank())
    return co

  def postprocessCallNode(self, node: CallNode, args: List[CodeObject]) -> CodeObject:
    co = CodeObject()
    numArgs = len(args)
    for c in reversed(args):
        if c.lval: c = self.rvalify(c)
        co.code.extend(c.code)
        co.code.append(Addi("sp", "-4", "sp"))
        if c.type == Scope.Type.INT:
            co.code.append(Sw(c.temp, "sp", "0"))
        else:
            co.code.append(Fsw(c.temp, "sp", "0"))
            
    co.code.append(Addi("sp", "-4", "sp"))
    co.code.append(Addi("sp", "-4", "sp"))
    co.code.append(Sw("ra", "sp", "0"))
    
    co.code.append(Jr(self._generateFunctionEntryLabel(node.getFuncName())))
    
    co.code.append(Lw("ra", "sp", "0"))
    co.code.append(Addi("sp", "4", "sp"))
    
    rt = node.ste.getReturnType()
    if rt == Scope.Type.INT:
        temp = self.generateTemp(Scope.Type.INT)
        co.code.append(Lw(temp, "sp", "0"))
        co.temp = temp
    elif rt == Scope.Type.FLOAT:
        temp = self.generateTemp(Scope.Type.FLOAT)
        co.code.append(Flw(temp, "sp", "0"))
        co.temp = temp
        
    co.code.append(Addi("sp", "4", "sp"))
    
    if numArgs > 0:
        co.code.append(Addi("sp", str(4 * numArgs), "sp"))
        
    co.type = rt
    co.lval = False
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
    co = CodeObject()
    address = self.generateAddrFromVariable(lco)
    temp1 = self.generateTemp(Scope.Type.INT) 
    if lco.getSTE().isLocal():
        co.code.append(Addi("fp", address, temp1))
    else:
        co.code.append(La(temp1, address)) 

    if lco.type is Scope.Type.INT:
      temp2 = self.generateTemp(Scope.Type.INT)
      co.code.append(Lw(temp2, temp1, '0'))
    elif lco.type is Scope.Type.FLOAT:
      temp2 = self.generateTemp(Scope.Type.FLOAT)
      co.code.append(Flw(temp2, temp1, '0'))

    co.type = lco.type
    co.lval = False
    co.temp = temp2
    return co

  def generateAddrFromVariable(self, lco: CodeObject) -> str:
    symbol = lco.getSTE()
    return symbol.addressToString()

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
  def _generateFunctionEntryLabel(self, func = None) -> str:
    if func is None: return "func_entry_" + self.currFunc
    else: return "func_entry_" + func
  def _generateFunctionCodeLabel(self, func = None) -> str:
    if func is None: return "func_code_" + self.currFunc
    else: return "func_code_" + func  
  def _generateFunctionRetLabel(self) -> str:
    return "func_ret_" + self.currFunc