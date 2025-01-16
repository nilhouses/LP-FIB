from schemeVisitor import schemeVisitor
from schemeParser import schemeParser
from fractions import Fraction
from ex import ex

# Diccionari per emmagatzemar constants i funcions
GlobalSymbols = {} 

# Pila de diccionaris per les variables locals
LocalSymbols = [{}]

# Operacions 
OpDICT = {
    #1 aritmètiques
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
    'mod': lambda x, y: x % y,
    #2 relacionals
    '<': lambda a, b: a < b,
    '<=': lambda a, b: a <= b,
    '>': lambda a, b: a > b,
    '>=': lambda a, b: a >= b ,
    '<>': lambda a, b: a != b,
    "=": lambda a, b: a == b ,
    #3 lògiques
    'not': lambda a: not a,
    'and': lambda a, b: a and b,
    'or': lambda a, b: a or b
}

prohibitedID = [ #noms que no poden tenir les variables i/o funcions
    'define', 'if', 'cond', 'display', 'read', 'newline', 'let',
    'car', 'cdr', 'conds', 'null?', 'and', 'or', 'not'
]

class EvalVisitor(schemeVisitor):

    def visitRoot(self, ctx):
        for expr in ctx.expr():
            self.visit(expr)

    def visitNumber(self, ctx): #Number
        num = ctx.getText()
        if '/' in num:
            return Fraction(num) 
        else:
            return int(num) 

    def visitBoolean(self, ctx): #Boolean
        return ctx.getText()

    def visitString(self, ctx): #String
        return ctx.getText()
    
    def visitList(self, ctx):#List
        #'\'' '(' expr* ')'
        value = []
        for e in ctx.expr():
            v = self.visit(e)
            value.append(v)
        return value
    
    def visitID(self, ctx): # ID (IDENTIFICADOR D'UNA VARIABLE, UNA FUNCIÓ O UNA LLISTA)
        ID = ctx.getText()
        # 1) ID ES LOCAL
        if ID in LocalSymbols[-1]: # Variable local, llista
            return LocalSymbols[-1][ID]

        # 2) ID ES GLOBAL (variable, llista o funcio)
        elif ID in GlobalSymbols:
            if isinstance(GlobalSymbols[ID],dict):
                return ID
            return GlobalSymbols[ID]
        else:
            raise ex(f"\nERROR: '{ID}' is not defined")
    
    # Evaluar les expressions
    def visitEvaluate(self, ctx):
        # '(' expr* ')' 
        first_child = ctx.getChild(1).getText()
        #################################################### OPERACIONS
        if first_child in OpDICT:  
            # '(' OP expr1 expr2 ')'
            operador = first_child
            expr1 = self.visit(ctx.getChild(2)) 
            if operador == 'not':  # '(' not expr ')'
                    if expr1 in ['#t', '#f']: 
                        return '#t' if OpDICT[operador](expr1 == '#t') else '#f'
                    else:
                        raise ex(f"\nERROR: Unable to execute not over expression {ctx.getChild(2)} with value {expr1}, it is not boolean")
            else : # Altres operadors '(' operador expr1 expr2 ')'
                expr2 = self.visit(ctx.getChild(3))
                if operador in ['+', '-', '/', '*', 'mod']:
                    if isinstance(expr1, (Fraction, int)) and isinstance(expr2, (Fraction, int)):
                        # Passo els operands en forma de Fraction
                        if isinstance(expr1, int):
                            expr1 = Fraction(expr1, 1)
                        if isinstance(expr2, int):
                            expr2 = Fraction(expr2, 1)
                        #Opero
                        return OpDICT[operador](expr1, expr2)
                elif operador in ['<', '<=', '>=', '>', '=', '<>'] and isinstance(expr1, (Fraction, int)) and isinstance(expr2, (Fraction, int)):
                        # Passo els operands en forma de Fraction
                        if isinstance(expr1, int):
                            expr1 = Fraction(expr1, 1)
                        if isinstance(expr2, int):
                            expr2 = Fraction(expr2, 1)
                        #Opero
                        return '#t' if OpDICT[operador](expr1, expr2) else '#f'
                elif operador in ['and', 'or', '=', '<>'] and expr1 in ['#t', '#f'] and expr2 in ['#t', '#f']:
                    return '#t' if OpDICT[operador](expr1 == '#t', expr2 == '#t') else '#f'
            
            raise ex(f"\nERROR: unable to operate expressions {expr1}, {expr2} with operator {operador}")

        #################################################### IF
        elif first_child == "if":
            # '(' 'if' condicio expr expr ')'
            [_, _, condicio, expr1, expr2, _] = list(ctx.getChildren())
            
            cond = self.visit(condicio)
            if cond is None:
                raise ex(f"\nERROR: If condition is not written properly")
            
            if cond == '#f':  # La condició és falsa
                return self.visit(expr2)
            else: # Si la condició és diferent de #f es considera #t
                return self.visit(expr1)
        #################################################### COND
        elif first_child == "cond":
            # '(' 'cond' (condicio expr)* expr expr ')'
            # Elimino els parèntesis i "cond"
            children = [child for child in ctx.getChildren() if child.getText() not in ["cond", "(", ")"]]

            # Comprovo que cada fill té exactament dos elements (condició i expressió)
            for child in children:
                grandchildren = [gchild for gchild in child.getChildren() if gchild.getText() not in ["(", ")"]]

                # Comprovo si el nombre de nets és diferent de 2
                if len(grandchildren) != 2:
                    raise ex(f"\nCond error: The condition {condicio} misses either a condition or an expression return value")

            # Si tots els fills són correctes, itero sobre ells per processar-los
            for child in children:
                grandchildren = [gchild for gchild in child.getChildren() if gchild.getText() not in ["(", ")"]]
                cosCond = grandchildren[0]  # condició
                expr = grandchildren[1]  # expressió

                if cosCond.getText() == "else":  # Tracto el cas especial "else"
                    return self.visit(expr)
                
                condicio = self.visit(cosCond)
                
                if condicio != '#f': # Si la condició és diferent de #f l'executo la seva expressió
                    return self.visit(expr)
                
            raise ex(f"\nERROR: Bad cond definition {ctx.getChildren()} no evaluation returned #t")
        ##################################################### DISPLAY (ESCRIURE)
        elif first_child == "display":
            # '(' 'display' expr ')'
            valor = self.visit(ctx.getChild(2))
            if isinstance(valor, str):
                valor = valor.strip('"')  #String
            if valor is not None:
                if isinstance(valor,list): #Llista, els seus elements poden ser més llistes
                    print("( ", end="")
                    parsePrint(valor)
                    print(")", end="")
                else:  
                    print(valor, end="")  # Altres tipus
        ##################################################### NEWLINE
        elif first_child == "newline":
            print('')  # \n
        ##################################################### READ
        elif first_child == "read":
            # '(' 'read' ')'
            return parseRead(input())
        ##################################################### LLISTES
        elif first_child == "car": # retorna el primer element d'una llista
            # '(' 'car' expr ')'
            llista = self.visit(ctx.getChild(2))
            if (isinstance(llista, list)):
                return llista[0]
            raise ex(f"\nCan't execute car over expression {ctx.getChild(2).getText()} with value {llista}, it is not a list")
        elif first_child == "cdr": # retorna la cua de la llista 
            # '(' 'cdr' expr ')'
            llista = self.visit(ctx.getChild(2))
            if (isinstance(llista, list)):
                return llista[1:]
            raise ex(f"\nCan't execute cdr over expression {ctx.getChild(2).getText()} with value {llista}, it is not a list")
        elif first_child == "cons": # afegeix un element al principi d'una llista
            # '(' 'cons' expr expr ')'
            [_, _, element, llista, _] = list(ctx.getChildren())
            element = self.visit(element)
            llista = self.visit(llista)
            if (isinstance(llista, list)):
                return [element] + llista
            raise ex(f"\nCan't execute cons overexpression {ctx.getChild(3).getText()} with value {llista}, it is not a list")
        elif first_child == "null?": # comprova si una llista és buida 
            # '(' 'null?' expr ')'
            llista = self.visit(ctx.getChild(2))
            if (isinstance(llista, list)):
                return '#t' if llista == [] else '#f'   
            raise ex(f"\nCan't exectue null? over expression {ctx.getChild(2).getText()} with value {llista}, it is not a list")
        ##################################################### LLISTES
        elif first_child == "let":
                # '(' 'let' (assignations)+ body ')'
                assignations = ctx.expr(1) #exemple ((x 3) (y 4))
                body = ctx.expr()[2:]  # body
                LocalSymbols.append(LocalSymbols[-1].copy())
                # ASSIGNATIONS
                for a in assignations.expr(): # exemple (x 3)
                    name = a.expr(0).getText() # x 
                    value = self.visit(a.expr(1)) # 3
                    LocalSymbols[-1][name] = value 
                # BODY
                result = None
                for expr in body:
                    result = self.visit(expr)
                LocalSymbols.pop()
                return result

        ##################################################### DEFINICIO DE CONSTANTS
        elif first_child == "define":                           

            if ctx.getChild(2).getText().startswith('('):# FUNCIONS 
                # '(' 'define' '(' expr+ ')' expr* ')'
                funcName = ctx.getChild(2).getChild(1).getText()

                if funcName in GlobalSymbols:
                    raise ex(f"\nERROR: Function {funcName} already defined")
                elif funcName in prohibitedID:
                    raise ex(f"\nERROR: Can't define a function with the type name: {funcName}")

                if (funcName == "main"):
                    if "main" in GlobalSymbols:
                        raise ex("'main' is already defined")
                    #Executo directament el main
                    for expr in list(ctx.getChildren())[3:-1]:
                        self.visit(expr)
             
                # Paràmetres
                paramList = [param.getText() for param in list(ctx.getChild(2).getChildren())[2:-1]]
                expressions = list(ctx.getChildren())[3:-1]  # A partir del fill 3 fins a l'últim (no inclòs) ')'
                GlobalSymbols[funcName] = {"params": paramList, "exprs": expressions}

            elif ctx.getChild(3).getText().startswith("'("): #LLISTA
                # '(' 'define' ID '\' '(' expr+ ')' ')'
                listName = ctx.getChild(2).getText()
                
                if listName in GlobalSymbols:
                    raise ex(f"\nERROR: List {listName} already defined")
                elif (ctx.getChild(2).getText() in prohibitedID):
                    raise ex(f"\nERROR: Can't define a list with the type name: {listName}")
                
                value = [self.visit(expr) for expr in ctx.getChild(3).getChildren() if self.visit(expr) is not None]
                GlobalSymbols[listName] = value
                
            else: #VARIABLE
                #  '(' 'define' ID expr ')'
                name = ctx.getChild(2).getText()     
                if name in GlobalSymbols:
                    raise ex(f"\nERROR: Variable {name} already defined")           
                elif (name in prohibitedID):
                    raise ex(f"\nCan't define a variable with the type name: {name}")
                value = self.visit(ctx.getChild(3))
                GlobalSymbols[name] = value
    
        ################################################### ACCES A FUNCIONS CONSTANTS o VARIABLES LOCALS
        elif first_child in GlobalSymbols or first_child in LocalSymbols[-1]:
            # '(' ID expr* ')'
            if first_child in LocalSymbols[-1] and LocalSymbols[-1][first_child] in GlobalSymbols: #Tinc una funció com a paràmetre
                first_child = LocalSymbols[-1][first_child]
            if first_child in GlobalSymbols:
                valor = GlobalSymbols[first_child]
                # FUNCIO
                if isinstance(valor, dict) and "params" in valor and "exprs" in valor:

                    # Només selecciono els fills que representen arguments (excloc el nom de la funció)
                    arguments = [self.visit(argument) for argument in ctx.expr()[1:]]  # Saltar el primer fill
                    funcParams = valor["params"]

                    # Valido el nombre d'arguments
                    if len(funcParams) != len(arguments):
                        raise ex(f"\nExpected {len(funcParams)} arguments but got {len(arguments)}")

                    # Relaciono els arguments amb els seus paràmetres
                    LocalSymbols.append(LocalSymbols[-1].copy())
                    for param, arg in zip(funcParams, arguments):
                        LocalSymbols[-1][param] = arg

                    result = None
                    for expr in valor["exprs"]:
                        result = self.visit(expr)

                    LocalSymbols.pop()
                    return result
                # VARIABLE
                else: 
                    raise ex(f"\nUnable to execute ({first_child} {ctx.getChild(2).getText()}),  {first_child} value can't change, it is a constant variable")

            # ID LOCAL (variable O LLISTA)
            elif first_child in LocalSymbols[-1]:
                return LocalSymbols[-1][first_child]
            else:
                raise ex(f"\nExpression '{first_child}' is not valid")
  
        ##################################################### ERROR DE LECTURA
        else:
            raise ex(f"\nUnknown expression ( {ctx.getChild(1).getText()} )")

def parsePrint(valor): #Funció usada al display per mostrar les llistes recursivament
    for v in valor:
        if(isinstance(v,str)):
            v = v.strip('"')
        if (isinstance(v, list)):            
            print("'( ", end="")
            parsePrint(v)
            print(") ", end="")
        else:
            print(f"{v} ", end="")

def parseRead(text): #Funció usada al read per parsejar els tipus Bool, Enter, Fracció, Llista i String
    # Bool
    if text in ['#t', '#f']:
        return text
    # Enter
    try: 
        return int(text)
    except ValueError:
        pass
    # Fracció
    if '/' in text:
        try:
            return Fraction(text)
        except ValueError:
            pass 
    # Llista, si cal tractaré llistes dins de la propia llista 
    if text.startswith("'(") and text.endswith(")"):
        text = text[2:-1].strip()  # Elimino "'(" i ")"
        elements = []
        element = ""
        parens_count = 0
        i = 0
        while i < len(text):
            char = text[i]
            if char == '(' and text[i-1] == "'":
                parens_count += 1
                element += char
            elif char == ')':
                parens_count -= 1
                element += char
            elif char == ' ' and parens_count == 0:
                if element:
                    elements.append(parseRead(element))
                    element = ""
            else:
                element += char
            i += 1

        if element:
            elements.append(parseRead(element))

        return elements
    #String
    return text.strip('"') 