from exprsVisitor import exprsVisitor

#Faciliten la llegibilitat del codi
AritDICT = {'+': lambda x,y: x+y, '-': lambda a,b: a-b, '*': lambda x,y: x*y, '/': lambda x,y: x/y, '^': lambda x,y: x**y}
LogicDICT = {'<': lambda a,b: a < b, '<=': lambda a,b: a < b, '>': lambda x,y: x > y, '>=': lambda a,b: a >= b, '<>': lambda a,b: a != b, "=": lambda x,y: x == y}

class EvalVisitor(exprsVisitor):

    def __init__(self):
        self.mem = {}

#EXPRESIONS

    def visitOpArit(self,ctx):
        l = list(ctx.getChildren())
        expr1 = self.visit(l[0])
        operador = l[1].getText()
        expr2 = self.visit(l[2])
        return int(AritDICT[operador] ((int(expr1)),(int(expr2))))

    def visitOpLogic(self, ctx):
        l = list(ctx.getChildren())
        expr1 = self.visit(l[0])
        cmp = l[1].getText()
        expr2 = self.visit(l[2])
        return int(bool(LogicDICT[cmp] ((int(expr1)),(int(expr2)))))

    def visitNumero(self, ctx):
        numero = ctx.getText()
        return int(numero)

    def visitVariable(self,ctx):
        variable = ctx.getText()
        return self.mem[str(variable)]

#STATEMENTS

    def visitAsignar(self, ctx):
        [variable, operador, expressio] = list(ctx.getChildren())
        self.mem[str(variable)] = self.visit(expressio) 

    def visitImprimir(self, ctx):
        [instr, expr] = list(ctx.getChildren())
        print(self.visit(expr))

    def visitCondicional(self,ctx): # 'if' cond cosIf
        l = list(ctx.getChildren())
        cond = int(self.visit(l[1]))
        cosIf = l[2]
        if cond != 0:
            return self.visit(cosIf)

    def visitCondwhile(self,ctx):
        l = list(ctx.getChildren())
        value = None
        condition = self.visit(l[1]) 
        while condition != 0:
            value = self.visit(l[2])
            if value != None: break
            condition = self.visit(l[1])
        return value