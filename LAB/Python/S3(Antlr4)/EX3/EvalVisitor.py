from exprsVisitor import exprsVisitor

class EvalVisitor(exprsVisitor):
    def visitRoot(self, ctx):
        [expressio] = list(ctx.getChildren())
        print(self.visit(expressio))
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