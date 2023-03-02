/* symexpr.y */
%{
#include <stdio.h>
#include <string.h>
int zzz_yylineno;
int yydebug=0;
char* temp;
char* errmsg;
int lexerror = 0;
int yyerror(char* errmsg);
int yylex(void);
int res, num;
extern char* yytext;
%}
%% 
input: input expr '\n' { printf ("\"%s\" is an expression. Result: %d\n", temp, res);
                             *temp = '\0'; 
                             res = 0;}
     | expr '\n'       { printf ("\"%s\" is an expression. Result: %d\n", temp, res); 
                             *temp = '\0'; 
                             res = 0;}
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
expr: numberOne expr       { $$ = $1 + $2;
                              res = $$ }
        | numberOne        { res = 1 }
      ;
numberOne: '1'             { sscanf( yytext, "%d", &num ); $$ = num; }
      ;
%%
int yyerror(char *errmsg) {
   fprintf(stderr, "%s\n", errmsg);
   return 0;
}
int main(void) {
   temp = malloc (sizeof(*temp)*255);
   errmsg = malloc (sizeof(*errmsg)*255);
   yyparse();
   free(temp);
   return 0;
}
