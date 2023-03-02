/* symexpr.l */
%{
#include<string.h>
extern char* temp;
extern int lexerror;
int yyerror(char* errmsg);
extern char* errmsg;
%}
%%
[1]   { strcat(temp,yytext); return *yytext; }
\n         { return *yytext; }
[ \t]      { strcat(temp,yytext); } /* ignore whitespace */
.          { strcat(temp,yytext);
             sprintf(errmsg, "Invalid lexeme: '%c'.", *yytext);
             yyerror(errmsg);
             lexerror = 1; return *yytext; }
%%
int yywrap (void) {
   return 1;
}
