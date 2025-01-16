# Aquesta classe mostra els errors personalitzats que he decidit mostrar des d'EvalVisitor.py
class ex(Exception):
    def __init__(self, missatge):
        self.missatge = missatge