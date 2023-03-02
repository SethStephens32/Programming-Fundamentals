/* symexpr.y */
%{
#include <stdio.h>
#include <string.h>
int zzz_yylineno;
int yydebug = 0;
char* temp;
char* errmsg;
int lexerror = 0;
int yyerror(char* errmsg);
int yylex(void);
int res, num;
extern char* yytext;

%}

%%
input: input sym_expr '\n' { printf ("\"%s\" is an expression. Result: %d\n", temp, res );
                             *temp = '\0'; }
     | sym_expr '\n'       { printf ("\"%s\" is an expression. Result: %d\n", temp, res ); 
                             *temp = '\0'; }
     | error '\n'          { if (lexerror) {
                                printf ("\"%s\" contains invalid ", temp);
                                printf ("lexemes and, thus, ");
                                printf ("is not a sentence.\n");
                                lexerror = 0;
                             } else {
                                   printf ("\"%s\" is not an ", temp);
                                   printf ("expression.\n");
                               }
                             *temp = '\0';
                             yyclearin; /* discard lookahead */
                             yyerrok; }
    ;
sym_expr: expr				{ res=$1; }
	;
expr: term				    { $$ = $1;
							  res=$$;
							}
        | term '+' expr 	{ $$ = $1 + $3;
							  res=$$;
							}
    ;
term: 	  fact            	{ $$ = $1; }
		| fact '*' term		{ $$ = $1 * $3; }
    ;
fact:	  integer			{ $$ = $1; }
	;
integer:  '1'				{ sscanf( yytext, "%d", &num );	$$ = num; }
		| '2'				{ sscanf( yytext, "%d", &num ); $$ = num; }
		| '3'				{ sscanf( yytext, "%d", &num ); $$ = num; }
		| '4'				{ sscanf( yytext, "%d", &num ); $$ = num; }
		| '5'				{ sscanf( yytext, "%d", &num ); $$ = num; }
		| '6'				{ sscanf( yytext, "%d", &num ); $$ = num; }
		| '7'				{ sscanf( yytext, "%d", &num ); $$ = num; }
		| '8'				{ sscanf( yytext, "%d", &num ); $$ = num; }
		| '9'				{ sscanf( yytext, "%d", &num ); $$ = num; }
	;
%%
int yyerror(char *errmsg) {
   fprintf(stderr, "%s\n", errmsg);
   return 0;
}
int main(void) {
   temp = malloc (sizeof(*temp)*255);
   *temp = '\0';
   errmsg = malloc (sizeof(*errmsg)*255);
   yyparse();
   free(temp);
   return 0;
}
