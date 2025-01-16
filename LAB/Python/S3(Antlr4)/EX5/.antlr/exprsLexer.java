// Generated from /home/nil/Documents/Q5/LP/Compiladors/EX5/exprs.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class exprsLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, DIV=7, MUL=8, SUM=9, RES=10, 
		MENOR=11, MENORIGUAL=12, MAJOR=13, MAJORIGUAL=14, IGUAL=15, DIFERENT=16, 
		NUM=17, VAR=18, WS=19;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "DIV", "MUL", "SUM", 
			"RES", "MENOR", "MENORIGUAL", "MAJOR", "MAJORIGUAL", "IGUAL", "DIFERENT", 
			"NUM", "VAR", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "':='", "'write'", "'if'", "'then'", "'end'", "'^'", "'/'", "'*'", 
			"'+'", "'-'", "'<'", "'<='", "'>'", "'>='", "'='", "'<>'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, "DIV", "MUL", "SUM", "RES", 
			"MENOR", "MENORIGUAL", "MAJOR", "MAJORIGUAL", "IGUAL", "DIFERENT", "NUM", 
			"VAR", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public exprsLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "exprs.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000\u0013f\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002"+
		"\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002"+
		"\u0012\u0007\u0012\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0005\u0001"+
		"\u0005\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\b\u0001\b"+
		"\u0001\t\u0001\t\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001\u000b\u0001"+
		"\f\u0001\f\u0001\r\u0001\r\u0001\r\u0001\u000e\u0001\u000e\u0001\u000f"+
		"\u0001\u000f\u0001\u000f\u0001\u0010\u0004\u0010W\b\u0010\u000b\u0010"+
		"\f\u0010X\u0001\u0011\u0004\u0011\\\b\u0011\u000b\u0011\f\u0011]\u0001"+
		"\u0012\u0004\u0012a\b\u0012\u000b\u0012\f\u0012b\u0001\u0012\u0001\u0012"+
		"\u0000\u0000\u0013\u0001\u0001\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005"+
		"\u000b\u0006\r\u0007\u000f\b\u0011\t\u0013\n\u0015\u000b\u0017\f\u0019"+
		"\r\u001b\u000e\u001d\u000f\u001f\u0010!\u0011#\u0012%\u0013\u0001\u0000"+
		"\u0003\u0001\u000009\u0002\u0000AZaz\u0003\u0000\t\n\r\r  h\u0000\u0001"+
		"\u0001\u0000\u0000\u0000\u0000\u0003\u0001\u0000\u0000\u0000\u0000\u0005"+
		"\u0001\u0000\u0000\u0000\u0000\u0007\u0001\u0000\u0000\u0000\u0000\t\u0001"+
		"\u0000\u0000\u0000\u0000\u000b\u0001\u0000\u0000\u0000\u0000\r\u0001\u0000"+
		"\u0000\u0000\u0000\u000f\u0001\u0000\u0000\u0000\u0000\u0011\u0001\u0000"+
		"\u0000\u0000\u0000\u0013\u0001\u0000\u0000\u0000\u0000\u0015\u0001\u0000"+
		"\u0000\u0000\u0000\u0017\u0001\u0000\u0000\u0000\u0000\u0019\u0001\u0000"+
		"\u0000\u0000\u0000\u001b\u0001\u0000\u0000\u0000\u0000\u001d\u0001\u0000"+
		"\u0000\u0000\u0000\u001f\u0001\u0000\u0000\u0000\u0000!\u0001\u0000\u0000"+
		"\u0000\u0000#\u0001\u0000\u0000\u0000\u0000%\u0001\u0000\u0000\u0000\u0001"+
		"\'\u0001\u0000\u0000\u0000\u0003*\u0001\u0000\u0000\u0000\u00050\u0001"+
		"\u0000\u0000\u0000\u00073\u0001\u0000\u0000\u0000\t8\u0001\u0000\u0000"+
		"\u0000\u000b<\u0001\u0000\u0000\u0000\r>\u0001\u0000\u0000\u0000\u000f"+
		"@\u0001\u0000\u0000\u0000\u0011B\u0001\u0000\u0000\u0000\u0013D\u0001"+
		"\u0000\u0000\u0000\u0015F\u0001\u0000\u0000\u0000\u0017H\u0001\u0000\u0000"+
		"\u0000\u0019K\u0001\u0000\u0000\u0000\u001bM\u0001\u0000\u0000\u0000\u001d"+
		"P\u0001\u0000\u0000\u0000\u001fR\u0001\u0000\u0000\u0000!V\u0001\u0000"+
		"\u0000\u0000#[\u0001\u0000\u0000\u0000%`\u0001\u0000\u0000\u0000\'(\u0005"+
		":\u0000\u0000()\u0005=\u0000\u0000)\u0002\u0001\u0000\u0000\u0000*+\u0005"+
		"w\u0000\u0000+,\u0005r\u0000\u0000,-\u0005i\u0000\u0000-.\u0005t\u0000"+
		"\u0000./\u0005e\u0000\u0000/\u0004\u0001\u0000\u0000\u000001\u0005i\u0000"+
		"\u000012\u0005f\u0000\u00002\u0006\u0001\u0000\u0000\u000034\u0005t\u0000"+
		"\u000045\u0005h\u0000\u000056\u0005e\u0000\u000067\u0005n\u0000\u0000"+
		"7\b\u0001\u0000\u0000\u000089\u0005e\u0000\u00009:\u0005n\u0000\u0000"+
		":;\u0005d\u0000\u0000;\n\u0001\u0000\u0000\u0000<=\u0005^\u0000\u0000"+
		"=\f\u0001\u0000\u0000\u0000>?\u0005/\u0000\u0000?\u000e\u0001\u0000\u0000"+
		"\u0000@A\u0005*\u0000\u0000A\u0010\u0001\u0000\u0000\u0000BC\u0005+\u0000"+
		"\u0000C\u0012\u0001\u0000\u0000\u0000DE\u0005-\u0000\u0000E\u0014\u0001"+
		"\u0000\u0000\u0000FG\u0005<\u0000\u0000G\u0016\u0001\u0000\u0000\u0000"+
		"HI\u0005<\u0000\u0000IJ\u0005=\u0000\u0000J\u0018\u0001\u0000\u0000\u0000"+
		"KL\u0005>\u0000\u0000L\u001a\u0001\u0000\u0000\u0000MN\u0005>\u0000\u0000"+
		"NO\u0005=\u0000\u0000O\u001c\u0001\u0000\u0000\u0000PQ\u0005=\u0000\u0000"+
		"Q\u001e\u0001\u0000\u0000\u0000RS\u0005<\u0000\u0000ST\u0005>\u0000\u0000"+
		"T \u0001\u0000\u0000\u0000UW\u0007\u0000\u0000\u0000VU\u0001\u0000\u0000"+
		"\u0000WX\u0001\u0000\u0000\u0000XV\u0001\u0000\u0000\u0000XY\u0001\u0000"+
		"\u0000\u0000Y\"\u0001\u0000\u0000\u0000Z\\\u0007\u0001\u0000\u0000[Z\u0001"+
		"\u0000\u0000\u0000\\]\u0001\u0000\u0000\u0000][\u0001\u0000\u0000\u0000"+
		"]^\u0001\u0000\u0000\u0000^$\u0001\u0000\u0000\u0000_a\u0007\u0002\u0000"+
		"\u0000`_\u0001\u0000\u0000\u0000ab\u0001\u0000\u0000\u0000b`\u0001\u0000"+
		"\u0000\u0000bc\u0001\u0000\u0000\u0000cd\u0001\u0000\u0000\u0000de\u0006"+
		"\u0012\u0000\u0000e&\u0001\u0000\u0000\u0000\u0004\u0000X]b\u0001\u0006"+
		"\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}