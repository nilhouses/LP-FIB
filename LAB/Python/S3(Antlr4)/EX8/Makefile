all: run

generar: exprs.g4
	antlr4 -Dlanguage=Python3 -no-listener -visitor exprs.g4

run: generar
	python3 exprs.py