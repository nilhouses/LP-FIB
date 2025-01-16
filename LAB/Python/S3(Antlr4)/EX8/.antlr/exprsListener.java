// Generated from /dades/nil.casas.duatis/Documents/Q5/LP/Compiladors/EX8/exprs.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link exprsParser}.
 */
public interface exprsListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link exprsParser#root}.
	 * @param ctx the parse tree
	 */
	void enterRoot(exprsParser.RootContext ctx);
	/**
	 * Exit a parse tree produced by {@link exprsParser#root}.
	 * @param ctx the parse tree
	 */
	void exitRoot(exprsParser.RootContext ctx);
	/**
	 * Enter a parse tree produced by {@link exprsParser#functionDeclaration}.
	 * @param ctx the parse tree
	 */
	void enterFunctionDeclaration(exprsParser.FunctionDeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link exprsParser#functionDeclaration}.
	 * @param ctx the parse tree
	 */
	void exitFunctionDeclaration(exprsParser.FunctionDeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link exprsParser#paramList}.
	 * @param ctx the parse tree
	 */
	void enterParamList(exprsParser.ParamListContext ctx);
	/**
	 * Exit a parse tree produced by {@link exprsParser#paramList}.
	 * @param ctx the parse tree
	 */
	void exitParamList(exprsParser.ParamListContext ctx);
	/**
	 * Enter a parse tree produced by {@link exprsParser#main}.
	 * @param ctx the parse tree
	 */
	void enterMain(exprsParser.MainContext ctx);
	/**
	 * Exit a parse tree produced by {@link exprsParser#main}.
	 * @param ctx the parse tree
	 */
	void exitMain(exprsParser.MainContext ctx);
	/**
	 * Enter a parse tree produced by {@link exprsParser#statements}.
	 * @param ctx the parse tree
	 */
	void enterStatements(exprsParser.StatementsContext ctx);
	/**
	 * Exit a parse tree produced by {@link exprsParser#statements}.
	 * @param ctx the parse tree
	 */
	void exitStatements(exprsParser.StatementsContext ctx);
	/**
	 * Enter a parse tree produced by the {@code asignar}
	 * labeled alternative in {@link exprsParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterAsignar(exprsParser.AsignarContext ctx);
	/**
	 * Exit a parse tree produced by the {@code asignar}
	 * labeled alternative in {@link exprsParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitAsignar(exprsParser.AsignarContext ctx);
	/**
	 * Enter a parse tree produced by the {@code write}
	 * labeled alternative in {@link exprsParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterWrite(exprsParser.WriteContext ctx);
	/**
	 * Exit a parse tree produced by the {@code write}
	 * labeled alternative in {@link exprsParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitWrite(exprsParser.WriteContext ctx);
	/**
	 * Enter a parse tree produced by the {@code condicional}
	 * labeled alternative in {@link exprsParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterCondicional(exprsParser.CondicionalContext ctx);
	/**
	 * Exit a parse tree produced by the {@code condicional}
	 * labeled alternative in {@link exprsParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitCondicional(exprsParser.CondicionalContext ctx);
	/**
	 * Enter a parse tree produced by the {@code condwhile}
	 * labeled alternative in {@link exprsParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterCondwhile(exprsParser.CondwhileContext ctx);
	/**
	 * Exit a parse tree produced by the {@code condwhile}
	 * labeled alternative in {@link exprsParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitCondwhile(exprsParser.CondwhileContext ctx);
	/**
	 * Enter a parse tree produced by the {@code return}
	 * labeled alternative in {@link exprsParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterReturn(exprsParser.ReturnContext ctx);
	/**
	 * Exit a parse tree produced by the {@code return}
	 * labeled alternative in {@link exprsParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitReturn(exprsParser.ReturnContext ctx);
	/**
	 * Enter a parse tree produced by {@link exprsParser#cosIf}.
	 * @param ctx the parse tree
	 */
	void enterCosIf(exprsParser.CosIfContext ctx);
	/**
	 * Exit a parse tree produced by {@link exprsParser#cosIf}.
	 * @param ctx the parse tree
	 */
	void exitCosIf(exprsParser.CosIfContext ctx);
	/**
	 * Enter a parse tree produced by {@link exprsParser#cosWhile}.
	 * @param ctx the parse tree
	 */
	void enterCosWhile(exprsParser.CosWhileContext ctx);
	/**
	 * Exit a parse tree produced by {@link exprsParser#cosWhile}.
	 * @param ctx the parse tree
	 */
	void exitCosWhile(exprsParser.CosWhileContext ctx);
	/**
	 * Enter a parse tree produced by the {@code numero}
	 * labeled alternative in {@link exprsParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterNumero(exprsParser.NumeroContext ctx);
	/**
	 * Exit a parse tree produced by the {@code numero}
	 * labeled alternative in {@link exprsParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitNumero(exprsParser.NumeroContext ctx);
	/**
	 * Enter a parse tree produced by the {@code variable}
	 * labeled alternative in {@link exprsParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterVariable(exprsParser.VariableContext ctx);
	/**
	 * Exit a parse tree produced by the {@code variable}
	 * labeled alternative in {@link exprsParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitVariable(exprsParser.VariableContext ctx);
	/**
	 * Enter a parse tree produced by the {@code opLogic}
	 * labeled alternative in {@link exprsParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterOpLogic(exprsParser.OpLogicContext ctx);
	/**
	 * Exit a parse tree produced by the {@code opLogic}
	 * labeled alternative in {@link exprsParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitOpLogic(exprsParser.OpLogicContext ctx);
	/**
	 * Enter a parse tree produced by the {@code funcCall}
	 * labeled alternative in {@link exprsParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterFuncCall(exprsParser.FuncCallContext ctx);
	/**
	 * Exit a parse tree produced by the {@code funcCall}
	 * labeled alternative in {@link exprsParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitFuncCall(exprsParser.FuncCallContext ctx);
	/**
	 * Enter a parse tree produced by the {@code opArit}
	 * labeled alternative in {@link exprsParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterOpArit(exprsParser.OpAritContext ctx);
	/**
	 * Exit a parse tree produced by the {@code opArit}
	 * labeled alternative in {@link exprsParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitOpArit(exprsParser.OpAritContext ctx);
}