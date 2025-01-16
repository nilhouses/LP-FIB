GRAMMAR=scheme.g4

all: generate  

generate: $(GRAMMAR)
	@echo "Generant fitxers amb ANTLR..."
	antlr4 -Dlanguage=Python3 -no-listener -visitor $(GRAMMAR)

clean:
	@echo "Eliminant fitxers generats per ANTLR..."
	rm -f *.interp *.tokens *.pyc *.class *.jar schemeParser.py schemeLexer.py schemeVisitor.py __pycache__/* .antlr/*

# Generar fitxers -> $ make
# Eliminar fitxers generats -> $ make clean