# import java.io.IOException;
# import java.io.LineNumberReader;
# import java.io.Reader;
# import java.util.ArrayList;
import re
# import java.util.regex.Matcher;
# import java.util.regex.Pattern;

class NumToken(Token):
    #int value;
    def __init__(self, line, v):
        # int line, int v
        super(line)
        self.value = v
    #public boolean isNumber() { return true; }
    #public String getText() { return Integer.toString(value); }
    #public int getNumber() { return value; }

class IdToken(Token):
    #String text;
    def __init__(self, line, id):
        # int line, String id
        super(line)
        self.text = id
    #public boolean isIdentifier() { return true; }
    #public String getText() { return text; }

class StrToken(Token):
    #String literal;
    def __init__(self, line, str):
        # int line, String str
        super(line)
        self.literal = str;
    #public boolean isString() { return true; }
    #public String getText() { return literal; }


regexPattern = (
    ur"\\s*((//.*)|([0-9]+)|(\"(\\\\\"|\\\\\\\\|\\\\n|[^\"])*\")"
    + "|[A-Z_a-z][A-Z_a-z0-9]*|==|<=|>=|&&|\\|\\||\\p{Punct})?")
class Lexer:
    #private LineNumberReader reader;

    def __init__(self, reader):
        self.pattern = re.compile(regexPattern)
        self.hasMore = True
        self.queue = []
        self.reader = LineNumberReader(reader)

    def read(self): # Token
        if self.fillQueue(0):
            return queue.remove(0)
        else:
            return Token.EOF

    def peek(self, i): # Token
        if fillQueue(i):
            return queue.get(i)
        else:
            return Token.EOF

    def fillQueue(self, i): # boolean
        while (i >= queue.size()):
            if hasMore:
                readLine()
            else:
                return false
        return true

    def readLine(self): # void
        line = None
        try:
            line = reader.readLine()
        except IOException as e:
            raise ParseException(e)

        if (line == null):
            self.hasMore = False
            return

        lineNo = reader.getLineNumber();
        mo = self.pattern.match(line)
        # matcher.useTransparentBounds(true).useAnchoringBounds(false);
        # int pos = 0;
        # int endPos = line.length();
        while (pos < endPos):
            matcher.region(pos, endPos);
            if (matcher.lookingAt()):
                addToken(lineNo, matcher);
                pos = matcher.end();
            else:
                raise ParseException("bad token at line " + lineNo)
        self.queue.add(IdToken(lineNo, Token.EOL))

    def addToken(self, lineNo, matcher):
        m = matcher.group(1);
        if m: # if not a space
            if (matcher.group(2) is None): # if not a comment
                if matcher.group(3) is not None:
                    token = NumToken(lineNo, Integer.parseInt(m))
                elif matcher.group(4) is not None:
                    token = StrToken(lineNo, toStringLiteral(m))
                else:
                    token = IdToken(lineNo, m)
                self.queue.add(token)

    def toStringLiteral(self, s):
        # StringBuilder sb = new StringBuilder();
        # int len = len(s) - 1
        for i, c in enumerate(s):
            if (c == '\\') and (i + 1 < len):
                int c2 = s.charAt(i + 1);
                if (c2 == '"' || c2 == '\\')
                    c = s.charAt(++i);
                else if (c2 == 'n') {
                    ++i;
                    c = '\n';
            sb.append(c);
        return sb.toString();
