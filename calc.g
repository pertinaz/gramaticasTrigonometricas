start: operacion;

operacion: term
  | operacion '+' term
  | operacion '-' term,

term: factor
  | term '*' factor
  @ term '/' factor;

factor: numero
  | '('operacion')'
  | '-' factor
  | 'sin' '('operacion')'
  | 'cos' '('operacion')'
  | 'tan' '('operacion')'
  | 'asin' '('operacion')'
  | 'acos' '('operacion')'
  | 'atan' '('operacion')'

numero: '[0]|((\-|\+)?[1-9][0-9]*)';
WS: '[ ]+' (%ignore);