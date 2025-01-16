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
        [_,nom,_,paramList,_,statements,_] = list(ctx.getChildren())
        funcName = nom.getText()

        FunctionTable[funcName] = {
            "params": self.visit(paramList),
            "statements": statements
        }


    def visitFuncCall(self, ctx):
        funcName = ctx.VAR().getText()
        if funcName not in FunctionTable:
            raise Exception(f"Execution Error: Function {funcName} is not defined")

        funcData = FunctionTable[funcName]
        paramList = funcData["params"]
        statements = funcData["statements"]
        
        # Comprovem que els arguments siguin vàlids
        args = [self.visit(arg) for arg in ctx.expr()]  # Visitem cada argument


        # Assignem arguments a paràmetres en un nou entorn
        newScope = {param: arg for param, arg in zip(paramList, args)}
        SymbolTable.append(newScope)

        result = None
        # Executem els statements
        result = self.visit(statements)
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
        for statement in ctx.statement():
            result = self.visit(statement)
            if result is not None:  # Si trobem un valor de retorn, sortim
                return result
        return None  # Si no hi ha retorn, simplement retornem `None`
    
#CADA STATEMENT

    def visitAsignar(self, ctx):
        l = list(ctx.getChildren())
        nomVariable = l[0].getText()
        value = l[2]
        SymbolTable[-1][nomVariable] = int(self.visit(value))  # Últim conjunt de variables de la pila
        return None  # No hi ha retorn, continuem

    def visitWrite(self, ctx):
        expr = ctx.expr()
        value = int(self.visit(expr))
        print(value)
        return None  # No hi ha retorn, continuem

    def visitCondicional(self, ctx):  # 'if' cond cosIf
        l = list(ctx.getChildren())
        cond = int(self.visit(l[1]))  # Avaluem la condició
        cosIf = l[2]
        if cond != 0:
            return self.visit(cosIf)  # Si la condició és certa, executem el cos
        return None  # Si no s'executa el cos, retornem `None`

    def visitCosIf(self, ctx: exprsParser.CosIfContext):
        return self.visit(ctx.statements()) 

    def visitCondwhile(self, ctx):  # 'while' cond cosWhile
        l = list(ctx.getChildren())
        value = None
        condition = self.visit(l[1])
        while condition != 0:  # Si la condició és certa, repetim el cos
            value = self.visit(l[2])
            if value is not None:  # Si trobem un `return`, sortim
                break
            condition = self.visit(l[1])  # Tornem a comprovar la condició
        return value  # Retornem el valor del cos del `while` si en trobem

    def visitCosWhile(self, ctx: exprsParser.CosWhileContext):
        return self.visit(ctx.statements()) 

    def visitParamListBuida(self, ctx):
        return []

    def visitParamListPlena(self, ctx):
        return [x.getText() for x in ctx.VAR()]

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
        # Comprovem si és una variable coneguda
        ID = ctx.getText()  # Obtenim el nom de la variable directament
        if ID in SymbolTable[-1]:
            return int(SymbolTable[-1][ID])  # Retorna el valor de la variable
        else:
            raise Exception(f"Execution Error: Variable {ID} is not defined")


