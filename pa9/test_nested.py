class CondNode:
  class OpType:
    EQ = 1
    NE = 2

  def getOpFromString(self, op: str):
    if op == '==':
      return OpType.EQ 

c = CondNode()
print(c.getOpFromString('=='))
