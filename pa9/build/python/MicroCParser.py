# Generated from python/MicroC.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO



from MicroCCompiler.compiler.SymbolTable import SymbolTable
from MicroCCompiler.compiler.Scope import Scope
from MicroCCompiler.ast.IntLitNode import IntLitNode
from MicroCCompiler.ast.FloatLitNode import FloatLitNode
from MicroCCompiler.ast.AssignNode import AssignNode
from MicroCCompiler.ast.VarNode import VarNode
from MicroCCompiler.ast.WriteNode import WriteNode
from MicroCCompiler.ast.ReadNode import ReadNode
from MicroCCompiler.ast.ReturnNode import ReturnNode
from MicroCCompiler.ast.CondNode import CondNode
from MicroCCompiler.ast.StatementListNode import StatementListNode
from MicroCCompiler.ast.ASTNode import ASTNode
from MicroCCompiler.ast.BinaryOpNode import BinaryOpNode
from MicroCCompiler.ast.UnaryOpNode import UnaryOpNode
from MicroCCompiler.ast.IfStatementNode import IfStatementNode
from MicroCCompiler.ast.WhileNode import WhileNode

def serializedATN():
    return [
        4,1,32,246,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,1,0,1,0,1,0,1,0,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,3,1,62,8,1,1,2,1,2,1,2,1,2,3,2,68,8,2,1,
        3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,
        6,1,6,3,6,88,8,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,
        1,8,1,8,3,8,104,8,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,
        116,8,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,
        10,3,10,130,8,10,1,11,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,
        12,1,12,1,12,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,15,1,
        15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,
        15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,3,15,175,8,15,1,16,1,16,1,
        16,1,16,1,16,1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,17,1,
        17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,3,17,201,8,17,1,18,1,
        18,1,18,1,18,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,5,19,216,
        8,19,10,19,12,19,219,9,19,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,
        1,20,5,20,230,8,20,10,20,12,20,233,9,20,1,21,1,21,1,21,1,21,1,21,
        1,22,1,22,1,23,1,23,1,24,1,24,1,24,0,2,38,40,25,0,2,4,6,8,10,12,
        14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,0,3,1,0,18,
        23,1,0,24,25,2,0,17,17,26,26,237,0,50,1,0,0,0,2,61,1,0,0,0,4,67,
        1,0,0,0,6,69,1,0,0,0,8,71,1,0,0,0,10,76,1,0,0,0,12,87,1,0,0,0,14,
        89,1,0,0,0,16,103,1,0,0,0,18,115,1,0,0,0,20,129,1,0,0,0,22,131,1,
        0,0,0,24,137,1,0,0,0,26,143,1,0,0,0,28,147,1,0,0,0,30,174,1,0,0,
        0,32,176,1,0,0,0,34,200,1,0,0,0,36,202,1,0,0,0,38,206,1,0,0,0,40,
        220,1,0,0,0,42,234,1,0,0,0,44,239,1,0,0,0,46,241,1,0,0,0,48,243,
        1,0,0,0,50,51,3,2,1,0,51,52,3,14,7,0,52,53,6,0,-1,0,53,1,1,0,0,0,
        54,55,3,8,4,0,55,56,3,2,1,0,56,62,1,0,0,0,57,58,3,10,5,0,58,59,3,
        2,1,0,59,62,1,0,0,0,60,62,1,0,0,0,61,54,1,0,0,0,61,57,1,0,0,0,61,
        60,1,0,0,0,62,3,1,0,0,0,63,64,3,8,4,0,64,65,3,4,2,0,65,68,1,0,0,
        0,66,68,1,0,0,0,67,63,1,0,0,0,67,66,1,0,0,0,68,5,1,0,0,0,69,70,5,
        27,0,0,70,7,1,0,0,0,71,72,3,12,6,0,72,73,3,6,3,0,73,74,5,1,0,0,74,
        75,6,4,-1,0,75,9,1,0,0,0,76,77,5,2,0,0,77,78,3,6,3,0,78,79,5,3,0,
        0,79,80,5,30,0,0,80,81,5,1,0,0,81,82,6,5,-1,0,82,11,1,0,0,0,83,84,
        5,4,0,0,84,88,6,6,-1,0,85,86,5,5,0,0,86,88,6,6,-1,0,87,83,1,0,0,
        0,87,85,1,0,0,0,88,13,1,0,0,0,89,90,5,4,0,0,90,91,5,6,0,0,91,92,
        5,7,0,0,92,93,5,8,0,0,93,94,5,9,0,0,94,95,3,16,8,0,95,96,5,10,0,
        0,96,97,6,7,-1,0,97,15,1,0,0,0,98,99,3,18,9,0,99,100,3,16,8,0,100,
        101,6,8,-1,0,101,104,1,0,0,0,102,104,6,8,-1,0,103,98,1,0,0,0,103,
        102,1,0,0,0,104,17,1,0,0,0,105,106,3,20,10,0,106,107,5,1,0,0,107,
        108,6,9,-1,0,108,116,1,0,0,0,109,110,3,30,15,0,110,111,6,9,-1,0,
        111,116,1,0,0,0,112,113,3,32,16,0,113,114,6,9,-1,0,114,116,1,0,0,
        0,115,105,1,0,0,0,115,109,1,0,0,0,115,112,1,0,0,0,116,19,1,0,0,0,
        117,118,3,28,14,0,118,119,6,10,-1,0,119,130,1,0,0,0,120,121,3,22,
        11,0,121,122,6,10,-1,0,122,130,1,0,0,0,123,124,3,24,12,0,124,125,
        6,10,-1,0,125,130,1,0,0,0,126,127,3,26,13,0,127,128,6,10,-1,0,128,
        130,1,0,0,0,129,117,1,0,0,0,129,120,1,0,0,0,129,123,1,0,0,0,129,
        126,1,0,0,0,130,21,1,0,0,0,131,132,5,11,0,0,132,133,5,7,0,0,133,
        134,3,6,3,0,134,135,5,8,0,0,135,136,6,11,-1,0,136,23,1,0,0,0,137,
        138,5,12,0,0,138,139,5,7,0,0,139,140,3,38,19,0,140,141,5,8,0,0,141,
        142,6,12,-1,0,142,25,1,0,0,0,143,144,5,13,0,0,144,145,3,38,19,0,
        145,146,6,13,-1,0,146,27,1,0,0,0,147,148,3,6,3,0,148,149,5,3,0,0,
        149,150,3,38,19,0,150,151,6,14,-1,0,151,29,1,0,0,0,152,153,5,14,
        0,0,153,154,5,7,0,0,154,155,3,42,21,0,155,156,5,8,0,0,156,157,5,
        9,0,0,157,158,3,16,8,0,158,159,5,10,0,0,159,160,6,15,-1,0,160,175,
        1,0,0,0,161,162,5,14,0,0,162,163,5,7,0,0,163,164,3,42,21,0,164,165,
        5,8,0,0,165,166,5,9,0,0,166,167,3,16,8,0,167,168,5,10,0,0,168,169,
        5,15,0,0,169,170,5,9,0,0,170,171,3,16,8,0,171,172,5,10,0,0,172,173,
        6,15,-1,0,173,175,1,0,0,0,174,152,1,0,0,0,174,161,1,0,0,0,175,31,
        1,0,0,0,176,177,5,16,0,0,177,178,5,7,0,0,178,179,3,42,21,0,179,180,
        5,8,0,0,180,181,5,9,0,0,181,182,3,16,8,0,182,183,5,10,0,0,183,184,
        6,16,-1,0,184,33,1,0,0,0,185,186,3,6,3,0,186,187,6,17,-1,0,187,201,
        1,0,0,0,188,189,5,7,0,0,189,190,3,38,19,0,190,191,5,8,0,0,191,192,
        6,17,-1,0,192,201,1,0,0,0,193,194,3,36,18,0,194,195,6,17,-1,0,195,
        201,1,0,0,0,196,197,5,28,0,0,197,201,6,17,-1,0,198,199,5,29,0,0,
        199,201,6,17,-1,0,200,185,1,0,0,0,200,188,1,0,0,0,200,193,1,0,0,
        0,200,196,1,0,0,0,200,198,1,0,0,0,201,35,1,0,0,0,202,203,5,17,0,
        0,203,204,3,38,19,0,204,205,6,18,-1,0,205,37,1,0,0,0,206,207,6,19,
        -1,0,207,208,3,40,20,0,208,209,6,19,-1,0,209,217,1,0,0,0,210,211,
        10,1,0,0,211,212,3,48,24,0,212,213,3,40,20,0,213,214,6,19,-1,0,214,
        216,1,0,0,0,215,210,1,0,0,0,216,219,1,0,0,0,217,215,1,0,0,0,217,
        218,1,0,0,0,218,39,1,0,0,0,219,217,1,0,0,0,220,221,6,20,-1,0,221,
        222,3,34,17,0,222,223,6,20,-1,0,223,231,1,0,0,0,224,225,10,1,0,0,
        225,226,3,46,23,0,226,227,3,34,17,0,227,228,6,20,-1,0,228,230,1,
        0,0,0,229,224,1,0,0,0,230,233,1,0,0,0,231,229,1,0,0,0,231,232,1,
        0,0,0,232,41,1,0,0,0,233,231,1,0,0,0,234,235,3,38,19,0,235,236,3,
        44,22,0,236,237,3,38,19,0,237,238,6,21,-1,0,238,43,1,0,0,0,239,240,
        7,0,0,0,240,45,1,0,0,0,241,242,7,1,0,0,242,47,1,0,0,0,243,244,7,
        2,0,0,244,49,1,0,0,0,10,61,67,87,103,115,129,174,200,217,231
    ]

class MicroCParser ( Parser ):

    grammarFileName = "MicroC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'string'", "'='", "'int'", "'float'", 
                     "'main'", "'('", "')'", "'{'", "'}'", "'read'", "'print'", 
                     "'return'", "'if'", "'else'", "'while'", "'-'", "'<'", 
                     "'<='", "'>='", "'=='", "'!='", "'>'", "'*'", "'/'", 
                     "'+'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "IDENTIFIER", 
                      "INT_LITERAL", "FLOAT_LITERAL", "STR_LITERAL", "COMMENT", 
                      "WS" ]

    RULE_program = 0
    RULE_decls = 1
    RULE_var_decls = 2
    RULE_ident = 3
    RULE_var_decl = 4
    RULE_str_decl = 5
    RULE_base_type = 6
    RULE_function = 7
    RULE_statements = 8
    RULE_statement = 9
    RULE_base_stmt = 10
    RULE_read_stmt = 11
    RULE_print_stmt = 12
    RULE_return_stmt = 13
    RULE_assign_stmt = 14
    RULE_if_stmt = 15
    RULE_while_stmt = 16
    RULE_primary = 17
    RULE_unaryminus_expr = 18
    RULE_expr = 19
    RULE_term = 20
    RULE_cond = 21
    RULE_cmpop = 22
    RULE_mulop = 23
    RULE_addop = 24

    ruleNames =  [ "program", "decls", "var_decls", "ident", "var_decl", 
                   "str_decl", "base_type", "function", "statements", "statement", 
                   "base_stmt", "read_stmt", "print_stmt", "return_stmt", 
                   "assign_stmt", "if_stmt", "while_stmt", "primary", "unaryminus_expr", 
                   "expr", "term", "cond", "cmpop", "mulop", "addop" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    IDENTIFIER=27
    INT_LITERAL=28
    FLOAT_LITERAL=29
    STR_LITERAL=30
    COMMENT=31
    WS=32

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    def setSymbolTable(self, st: SymbolTable):
      self.st = st

    def getSymbolTable(self) -> SymbolTable:
      return self.st

    def setAST(self, node: ASTNode):
      self.ast = node

    def getAST(self) -> ASTNode:
      return self.ast



    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._function = None # FunctionContext

        def decls(self):
            return self.getTypedRuleContext(MicroCParser.DeclsContext,0)


        def function(self):
            return self.getTypedRuleContext(MicroCParser.FunctionContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = MicroCParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.decls()
            self.state = 51
            localctx._function = self.function()
            self.setAST(localctx._function.node);
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(MicroCParser.Var_declContext,0)


        def decls(self):
            return self.getTypedRuleContext(MicroCParser.DeclsContext,0)


        def str_decl(self):
            return self.getTypedRuleContext(MicroCParser.Str_declContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_decls

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecls" ):
                listener.enterDecls(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecls" ):
                listener.exitDecls(self)




    def decls(self):

        localctx = MicroCParser.DeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decls)
        try:
            self.state = 61
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 54
                self.var_decl()
                self.state = 55
                self.decls()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 57
                self.str_decl()
                self.state = 58
                self.decls()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(MicroCParser.Var_declContext,0)


        def var_decls(self):
            return self.getTypedRuleContext(MicroCParser.Var_declsContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_var_decls

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_decls" ):
                listener.enterVar_decls(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_decls" ):
                listener.exitVar_decls(self)




    def var_decls(self):

        localctx = MicroCParser.Var_declsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_var_decls)
        try:
            self.state = 67
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                self.var_decl()
                self.state = 64
                self.var_decls()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MicroCParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return MicroCParser.RULE_ident

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdent" ):
                listener.enterIdent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdent" ):
                listener.exitIdent(self)




    def ident(self):

        localctx = MicroCParser.IdentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_ident)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(MicroCParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._base_type = None # Base_typeContext
            self._ident = None # IdentContext

        def base_type(self):
            return self.getTypedRuleContext(MicroCParser.Base_typeContext,0)


        def ident(self):
            return self.getTypedRuleContext(MicroCParser.IdentContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_var_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_decl" ):
                listener.enterVar_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_decl" ):
                listener.exitVar_decl(self)




    def var_decl(self):

        localctx = MicroCParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_var_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            localctx._base_type = self.base_type()
            self.state = 72
            localctx._ident = self.ident()
            self.state = 73
            self.match(MicroCParser.T__0)
            self.st.addVariable(localctx._base_type.t, (None if localctx._ident is None else self._input.getText(localctx._ident.start,localctx._ident.stop)));
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Str_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ident = None # IdentContext
            self.val = None # Token

        def ident(self):
            return self.getTypedRuleContext(MicroCParser.IdentContext,0)


        def STR_LITERAL(self):
            return self.getToken(MicroCParser.STR_LITERAL, 0)

        def getRuleIndex(self):
            return MicroCParser.RULE_str_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStr_decl" ):
                listener.enterStr_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStr_decl" ):
                listener.exitStr_decl(self)




    def str_decl(self):

        localctx = MicroCParser.Str_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_str_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(MicroCParser.T__1)
            self.state = 77
            localctx._ident = self.ident()
            self.state = 78
            self.match(MicroCParser.T__2)
            self.state = 79
            localctx.val = self.match(MicroCParser.STR_LITERAL)
            self.state = 80
            self.match(MicroCParser.T__0)
            self.st.addVariable(Scope.Type.STRING, (None if localctx._ident is None else self._input.getText(localctx._ident.start,localctx._ident.stop)), (None if localctx.val is None else localctx.val.text));
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Base_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.t = None


        def getRuleIndex(self):
            return MicroCParser.RULE_base_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBase_type" ):
                listener.enterBase_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBase_type" ):
                listener.exitBase_type(self)




    def base_type(self):

        localctx = MicroCParser.Base_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_base_type)
        try:
            self.state = 87
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 83
                self.match(MicroCParser.T__3)
                localctx.t =  Scope.Type.INT
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 85
                self.match(MicroCParser.T__4)
                localctx.t =  Scope.Type.FLOAT
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._statements = None # StatementsContext

        def statements(self):
            return self.getTypedRuleContext(MicroCParser.StatementsContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)




    def function(self):

        localctx = MicroCParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(MicroCParser.T__3)
            self.state = 90
            self.match(MicroCParser.T__5)
            self.state = 91
            self.match(MicroCParser.T__6)
            self.state = 92
            self.match(MicroCParser.T__7)
            self.state = 93
            self.match(MicroCParser.T__8)
            self.state = 94
            localctx._statements = self.statements()
            self.state = 95
            self.match(MicroCParser.T__9)
            localctx.node =  localctx._statements.node
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._statement = None # StatementContext
            self.s = None # StatementsContext

        def statement(self):
            return self.getTypedRuleContext(MicroCParser.StatementContext,0)


        def statements(self):
            return self.getTypedRuleContext(MicroCParser.StatementsContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_statements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatements" ):
                listener.enterStatements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatements" ):
                listener.exitStatements(self)




    def statements(self):

        localctx = MicroCParser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_statements)
        try:
            self.state = 103
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11, 12, 13, 14, 16, 27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 98
                localctx._statement = self.statement()
                self.state = 99
                localctx.s = self.statements()
                localctx.node =  StatementListNode(localctx._statement.node, localctx.s.node.getStatements())
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                localctx.node =  StatementListNode()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._base_stmt = None # Base_stmtContext
            self._if_stmt = None # If_stmtContext
            self._while_stmt = None # While_stmtContext

        def base_stmt(self):
            return self.getTypedRuleContext(MicroCParser.Base_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(MicroCParser.If_stmtContext,0)


        def while_stmt(self):
            return self.getTypedRuleContext(MicroCParser.While_stmtContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = MicroCParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_statement)
        try:
            self.state = 115
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11, 12, 13, 27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 105
                localctx._base_stmt = self.base_stmt()
                self.state = 106
                self.match(MicroCParser.T__0)
                localctx.node =  localctx._base_stmt.node
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 2)
                self.state = 109
                localctx._if_stmt = self.if_stmt()
                localctx.node =  localctx._if_stmt.node
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 3)
                self.state = 112
                localctx._while_stmt = self.while_stmt()
                localctx.node =  localctx._while_stmt.node
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Base_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._assign_stmt = None # Assign_stmtContext
            self._read_stmt = None # Read_stmtContext
            self._print_stmt = None # Print_stmtContext
            self._return_stmt = None # Return_stmtContext

        def assign_stmt(self):
            return self.getTypedRuleContext(MicroCParser.Assign_stmtContext,0)


        def read_stmt(self):
            return self.getTypedRuleContext(MicroCParser.Read_stmtContext,0)


        def print_stmt(self):
            return self.getTypedRuleContext(MicroCParser.Print_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(MicroCParser.Return_stmtContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_base_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBase_stmt" ):
                listener.enterBase_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBase_stmt" ):
                listener.exitBase_stmt(self)




    def base_stmt(self):

        localctx = MicroCParser.Base_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_base_stmt)
        try:
            self.state = 129
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 117
                localctx._assign_stmt = self.assign_stmt()
                localctx.node =  localctx._assign_stmt.node
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 120
                localctx._read_stmt = self.read_stmt()
                localctx.node =  localctx._read_stmt.node
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 3)
                self.state = 123
                localctx._print_stmt = self.print_stmt()
                localctx.node =  localctx._print_stmt.node
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 4)
                self.state = 126
                localctx._return_stmt = self.return_stmt()
                localctx.node =  localctx._return_stmt.node
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Read_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._ident = None # IdentContext

        def ident(self):
            return self.getTypedRuleContext(MicroCParser.IdentContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_read_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRead_stmt" ):
                listener.enterRead_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRead_stmt" ):
                listener.exitRead_stmt(self)




    def read_stmt(self):

        localctx = MicroCParser.Read_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_read_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.match(MicroCParser.T__10)
            self.state = 132
            self.match(MicroCParser.T__6)
            self.state = 133
            localctx._ident = self.ident()
            self.state = 134
            self.match(MicroCParser.T__7)
            localctx.node =  ReadNode(VarNode((None if localctx._ident is None else self._input.getText(localctx._ident.start,localctx._ident.stop))))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Print_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._expr = None # ExprContext

        def expr(self):
            return self.getTypedRuleContext(MicroCParser.ExprContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_print_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint_stmt" ):
                listener.enterPrint_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint_stmt" ):
                listener.exitPrint_stmt(self)




    def print_stmt(self):

        localctx = MicroCParser.Print_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_print_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(MicroCParser.T__11)
            self.state = 138
            self.match(MicroCParser.T__6)
            self.state = 139
            localctx._expr = self.expr(0)
            self.state = 140
            self.match(MicroCParser.T__7)
            localctx.node =  WriteNode(localctx._expr.node)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._expr = None # ExprContext

        def expr(self):
            return self.getTypedRuleContext(MicroCParser.ExprContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_return_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn_stmt" ):
                listener.enterReturn_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn_stmt" ):
                listener.exitReturn_stmt(self)




    def return_stmt(self):

        localctx = MicroCParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_return_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.match(MicroCParser.T__12)
            self.state = 144
            localctx._expr = self.expr(0)
            localctx.node =  ReturnNode(localctx._expr.node)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._ident = None # IdentContext
            self._expr = None # ExprContext

        def ident(self):
            return self.getTypedRuleContext(MicroCParser.IdentContext,0)


        def expr(self):
            return self.getTypedRuleContext(MicroCParser.ExprContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_assign_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign_stmt" ):
                listener.enterAssign_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign_stmt" ):
                listener.exitAssign_stmt(self)




    def assign_stmt(self):

        localctx = MicroCParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            localctx._ident = self.ident()
            self.state = 148
            self.match(MicroCParser.T__2)
            self.state = 149
            localctx._expr = self.expr(0)
            localctx.node =  AssignNode(VarNode((None if localctx._ident is None else self._input.getText(localctx._ident.start,localctx._ident.stop))), localctx._expr.node)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._cond = None # CondContext
            self._statements = None # StatementsContext
            self.ts = None # StatementsContext
            self.es = None # StatementsContext

        def cond(self):
            return self.getTypedRuleContext(MicroCParser.CondContext,0)


        def statements(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MicroCParser.StatementsContext)
            else:
                return self.getTypedRuleContext(MicroCParser.StatementsContext,i)


        def getRuleIndex(self):
            return MicroCParser.RULE_if_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_stmt" ):
                listener.enterIf_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_stmt" ):
                listener.exitIf_stmt(self)




    def if_stmt(self):

        localctx = MicroCParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_if_stmt)
        try:
            self.state = 174
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 152
                self.match(MicroCParser.T__13)
                self.state = 153
                self.match(MicroCParser.T__6)
                self.state = 154
                localctx._cond = self.cond()
                self.state = 155
                self.match(MicroCParser.T__7)
                self.state = 156
                self.match(MicroCParser.T__8)
                self.state = 157
                localctx._statements = self.statements()
                self.state = 158
                self.match(MicroCParser.T__9)
                localctx.node =  IfStatementNode(localctx._cond.node, localctx._statements.node, None)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 161
                self.match(MicroCParser.T__13)
                self.state = 162
                self.match(MicroCParser.T__6)
                self.state = 163
                localctx._cond = self.cond()
                self.state = 164
                self.match(MicroCParser.T__7)
                self.state = 165
                self.match(MicroCParser.T__8)
                self.state = 166
                localctx.ts = self.statements()
                self.state = 167
                self.match(MicroCParser.T__9)
                self.state = 168
                self.match(MicroCParser.T__14)
                self.state = 169
                self.match(MicroCParser.T__8)
                self.state = 170
                localctx.es = self.statements()
                self.state = 171
                self.match(MicroCParser.T__9)
                localctx.node =  IfStatementNode(localctx._cond.node, localctx.ts.node, localctx.es.node)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._cond = None # CondContext
            self._statements = None # StatementsContext

        def cond(self):
            return self.getTypedRuleContext(MicroCParser.CondContext,0)


        def statements(self):
            return self.getTypedRuleContext(MicroCParser.StatementsContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_while_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_stmt" ):
                listener.enterWhile_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_stmt" ):
                listener.exitWhile_stmt(self)




    def while_stmt(self):

        localctx = MicroCParser.While_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.match(MicroCParser.T__15)
            self.state = 177
            self.match(MicroCParser.T__6)
            self.state = 178
            localctx._cond = self.cond()
            self.state = 179
            self.match(MicroCParser.T__7)
            self.state = 180
            self.match(MicroCParser.T__8)
            self.state = 181
            localctx._statements = self.statements()
            self.state = 182
            self.match(MicroCParser.T__9)
            localctx.node =  WhileNode(localctx._cond.node, localctx._statements.node)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._ident = None # IdentContext
            self._expr = None # ExprContext
            self._unaryminus_expr = None # Unaryminus_exprContext
            self.il = None # Token
            self.fl = None # Token

        def ident(self):
            return self.getTypedRuleContext(MicroCParser.IdentContext,0)


        def expr(self):
            return self.getTypedRuleContext(MicroCParser.ExprContext,0)


        def unaryminus_expr(self):
            return self.getTypedRuleContext(MicroCParser.Unaryminus_exprContext,0)


        def INT_LITERAL(self):
            return self.getToken(MicroCParser.INT_LITERAL, 0)

        def FLOAT_LITERAL(self):
            return self.getToken(MicroCParser.FLOAT_LITERAL, 0)

        def getRuleIndex(self):
            return MicroCParser.RULE_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary" ):
                listener.enterPrimary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary" ):
                listener.exitPrimary(self)




    def primary(self):

        localctx = MicroCParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_primary)
        try:
            self.state = 200
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 185
                localctx._ident = self.ident()
                localctx.node =  VarNode((None if localctx._ident is None else self._input.getText(localctx._ident.start,localctx._ident.stop)))
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 188
                self.match(MicroCParser.T__6)
                self.state = 189
                localctx._expr = self.expr(0)
                self.state = 190
                self.match(MicroCParser.T__7)
                localctx.node =  localctx._expr.node
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 3)
                self.state = 193
                localctx._unaryminus_expr = self.unaryminus_expr()
                localctx.node =  localctx._unaryminus_expr.node
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 4)
                self.state = 196
                localctx.il = self.match(MicroCParser.INT_LITERAL)
                localctx.node =  IntLitNode((None if localctx.il is None else localctx.il.text))
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 5)
                self.state = 198
                localctx.fl = self.match(MicroCParser.FLOAT_LITERAL)
                localctx.node =  FloatLitNode((None if localctx.fl is None else localctx.fl.text))
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Unaryminus_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._expr = None # ExprContext

        def expr(self):
            return self.getTypedRuleContext(MicroCParser.ExprContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_unaryminus_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryminus_expr" ):
                listener.enterUnaryminus_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryminus_expr" ):
                listener.exitUnaryminus_expr(self)




    def unaryminus_expr(self):

        localctx = MicroCParser.Unaryminus_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_unaryminus_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.match(MicroCParser.T__16)
            self.state = 203
            localctx._expr = self.expr(0)
            localctx.node =  UnaryOpNode(localctx._expr.node, '-')
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self.e1 = None # ExprContext
            self._term = None # TermContext
            self._addop = None # AddopContext

        def term(self):
            return self.getTypedRuleContext(MicroCParser.TermContext,0)


        def addop(self):
            return self.getTypedRuleContext(MicroCParser.AddopContext,0)


        def expr(self):
            return self.getTypedRuleContext(MicroCParser.ExprContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MicroCParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            localctx._term = self.term(0)
            localctx.node =  localctx._term.node
            self._ctx.stop = self._input.LT(-1)
            self.state = 217
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MicroCParser.ExprContext(self, _parentctx, _parentState)
                    localctx.e1 = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 210
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 211
                    localctx._addop = self.addop()
                    self.state = 212
                    localctx._term = self.term(0)
                    localctx.node =  BinaryOpNode(localctx.e1.node, localctx._term.node, (None if localctx._addop is None else self._input.getText(localctx._addop.start,localctx._addop.stop))) 
                self.state = 219
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self.t1 = None # TermContext
            self._primary = None # PrimaryContext
            self._mulop = None # MulopContext

        def primary(self):
            return self.getTypedRuleContext(MicroCParser.PrimaryContext,0)


        def mulop(self):
            return self.getTypedRuleContext(MicroCParser.MulopContext,0)


        def term(self):
            return self.getTypedRuleContext(MicroCParser.TermContext,0)


        def getRuleIndex(self):
            return MicroCParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)



    def term(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MicroCParser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_term, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            localctx._primary = self.primary()
            localctx.node =  localctx._primary.node
            self._ctx.stop = self._input.LT(-1)
            self.state = 231
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MicroCParser.TermContext(self, _parentctx, _parentState)
                    localctx.t1 = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                    self.state = 224
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 225
                    localctx._mulop = self.mulop()
                    self.state = 226
                    localctx._primary = self.primary()
                    localctx.node =  BinaryOpNode(localctx.t1.node, localctx._primary.node, (None if localctx._mulop is None else self._input.getText(localctx._mulop.start,localctx._mulop.stop))) 
                self.state = 233
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class CondContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self.e1 = None # ExprContext
            self._cmpop = None # CmpopContext
            self.e2 = None # ExprContext

        def cmpop(self):
            return self.getTypedRuleContext(MicroCParser.CmpopContext,0)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MicroCParser.ExprContext)
            else:
                return self.getTypedRuleContext(MicroCParser.ExprContext,i)


        def getRuleIndex(self):
            return MicroCParser.RULE_cond

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCond" ):
                listener.enterCond(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCond" ):
                listener.exitCond(self)




    def cond(self):

        localctx = MicroCParser.CondContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_cond)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            localctx.e1 = self.expr(0)
            self.state = 235
            localctx._cmpop = self.cmpop()
            self.state = 236
            localctx.e2 = self.expr(0)
            localctx.node =  CondNode(localctx.e1.node, localctx.e2.node, (None if localctx._cmpop is None else self._input.getText(localctx._cmpop.start,localctx._cmpop.stop)))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmpopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MicroCParser.RULE_cmpop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmpop" ):
                listener.enterCmpop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmpop" ):
                listener.exitCmpop(self)




    def cmpop(self):

        localctx = MicroCParser.CmpopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_cmpop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 16515072) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MulopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MicroCParser.RULE_mulop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulop" ):
                listener.enterMulop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulop" ):
                listener.exitMulop(self)




    def mulop(self):

        localctx = MicroCParser.MulopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_mulop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            _la = self._input.LA(1)
            if not(_la==24 or _la==25):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MicroCParser.RULE_addop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddop" ):
                listener.enterAddop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddop" ):
                listener.exitAddop(self)




    def addop(self):

        localctx = MicroCParser.AddopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_addop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            _la = self._input.LA(1)
            if not(_la==17 or _la==26):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[19] = self.expr_sempred
        self._predicates[20] = self.term_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         

    def term_sempred(self, localctx:TermContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         




