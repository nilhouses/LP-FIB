from exprsVisitor import exprsVisitor
from exprsParser import exprsParser


FunctionTable = {}  #Llista de funcions
                    # cada funcio esta identificada per un nom i els noms de 
                    # les seves variables internes (tipus de retorn es sempre int)

SymbolTable = [{}] # Pila de diccionaris de variables 

#Faciliten la llegibilitat del codi
AritDICT = {'+': lambda x,y: x+y, '-': lambda a,b: a-b, '*': lambda x,y: x*y, '/': lambda x,y: x/y, '^': lambda x,y: x**y}
LogicDICT = {'<': lambda a,b: a < b, '<=': lambda a,b: a < b, '>': lambda x,y: x > y, '>=': lambda a,b: a >= b, '<>': lambda a,b: a != b, "=": lambda x,y: x == y}

class EvalVisitor(exprsVisitor):

    def visitRoot(self, ctx):
        for funcDecl in ctx.functionDeclaration():
            self.visit(funcDecl)
        return self.visit(ctx.main())
#DATA

    # FUNCIONS
    def visitFunctionDeclaration(self, ctx):
        funcName = ctx.VAR().getText()
        paramList = [param.getText() for param in ctx.paramList().VAR()] if ctx.paramList() else []
        statements = ctx.statements().statement()

        # Hi ha d'haver almenys 1 return, sino peta
        returns = [stmt for stmt in statements if isinstance(stmt, exprsParser.ReturnContext)]

        if len(returns) < 1:
            raise Exception(f"Syntax Error: Function '{funcName}' misses at least one return statement.")

        FunctionTable[funcName] = {
            "params": paramList, 
            "statements": statements, 
            "returns": returns
        }


    def visitFuncCall(self, ctx):
        funcName = ctx.VAR().getText()
        if funcName not in FunctionTable:
            raise Exception(f"Execution Error: Function {funcName} is not defined")
        
        funcData = FunctionTable[funcName]
        paramList = funcData["params"]
        statements = funcData["statements"]
        returns = funcData["returns"]
        
        # Comprovem que els arguments siguin vàlids
        args = [self.visit(arg) for arg in ctx.expr()]  # Visitem cada argument
        if len(args) != len(paramList):
            raise Exception(f"Execution Error: Function {funcName} expects {len(paramList)} arguments, got {len(args)}")

        # Assignem arguments a paràmetres en un nou entorn
        newScope = {param: arg for param, arg in zip(paramList, args)}
        SymbolTable.append(newScope)

        result = None
        # Executem els statements
        for statement in statements:
            result = self.visit(statement)
            if result is not None:  # Si hi ha un resultat, retornem i sortim de la funció
                SymbolTable.pop() #buido la pila
                return result

        SymbolTable.pop() #buido la pila
        return None

#MAIN
    def visitMain(self, ctx):
        for statement in ctx.statements().statement():
            result = self.visit(statement)
            if result is not None:
                break

#STATEMENTS

    def visitStatements(self, ctx):
        for statement in list(ctx.statement()):
            result = self.visit(statement)
            if result != None:
                return result
        return None
    
#CADA STATEMENT

    def visitAsignar(self, ctx):
        l = list(ctx.getChildren())
        nomVariable = l[0].getText()
        value = l[2]
        SymbolTable[-1][nomVariable] = int(self.visit(value))  # Últim conjunt de variables de la pila
        return None

    def visitWrite(self, ctx):
        value = int(self.visit(ctx.expr()))
        print(value)
        return None  # No hi ha retorn, continuem

    def visitCondicional(self, ctx):  # 'if' cond cosIf
        l = list(ctx.getChildren())
        cond = int(self.visit(l[1]))  # Avaluem la condició
        cosIf = l[2]
        if cond != 0:
            return self.visit(cosIf) 
        return None  

    def visitCosIf(self, ctx: exprsParser.CosIfContext):
        return self.visit(ctx.statements()) 

    def visitCondwhile(self, ctx):  # 'while' cond cosWhile
        l = list(ctx.getChildren())
        value = None
        condition = self.visit(l[1])
        while condition != 0:  
            value = self.visit(l[2])
            if value is not None:  
                break
            condition = self.visit(l[1])  
        return value 

    def visitCosWhile(self, ctx: exprsParser.CosWhileContext):
        return self.visit(ctx.statements()) 

    def visitReturn(self,ctx):
        return self.visit(ctx.expr())
    
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

    def visitVariable(self, ctx):
        ID = ctx.getText()  
        if ID in SymbolTable[-1]:
            return int(SymbolTable[-1][ID])  
        else:
            raise Exception(f"Execution Error: Variable {ID} is not defined")


