from exprsVisitor import exprsVisitor

class EvalVisitor(exprsVisitor):
    def __init__(self):
        self.mem = {}
    def visitSuma(self, ctx):
        [expressio1, operador, expressio2] = list(ctx.getChildren())
        return self.visit(expressio1) + self.visit(expressio2)
    def visitNumero(self, ctx):
        [numero] = list(ctx.getChildren())
        return int(numero.getText())
    def visitResta(self, ctx): 
        [expressio1, operador, expressio2] = list(ctx.getChildren())
        return self.visit(expressio1) - self.visit(expressio2)
    def visitMultiplicacio(self, ctx): 
        [expressio1, operador, expressio2] = list(ctx.getChildren())
        return self.visit(expressio1) * self.visit(expressio2)
    def visitDivisio(self, ctx):
        [expressio1, operador, expressio2] = list(ctx.getChildren())
        if expressio2 == 0:
            raise ZeroDivisionError("No es pot dividir per zero.")
        return self.visit(expressio1) / self.visit(expressio2)
    def visitPotencia(self, ctx):
        [expressio1, operador, expressio2] = list(ctx.getChildren())
        return self.visit(expressio1) ** self.visit(expressio2)
    # Se ha sustituido root por init
    def visitAsignar(self, ctx):
        [variable, operador, expressio] = list(ctx.getChildren())
        self.mem[str(variable)] = self.visit(expressio) 
    #passo el node variable a string per trobar-lo a, per exemple self.mem = {"x": 8} 
    def visitImprimir(self, ctx):
        [instr, variable] = list(ctx.getChildren())
        print(self.mem[str(variable)])
    def visitVariable(self,ctx):
        variable = ctx.getText()
        return self.mem[str(variable)]