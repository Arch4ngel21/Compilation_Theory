
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'nonassocIFXnonassocELSEleft=ADDASSIGNSUBASSIGNMULASSIGNDIVASSIGNnonassocLESSEQMOREEQNOTEQUALEQUAL<>left+-DOTADDDOTSUBleft*/DOTMULDOTDIVleft\'rightUMINUSADDASSIGN BREAK CONTINUE DIVASSIGN DOTADD DOTDIV DOTMUL DOTSUB ELSE EQUAL EYE FLOATNUM FOR ID IF INTNUM LESSEQ MOREEQ MULASSIGN NOTEQUAL ONES PRINT RETURN STRING SUBASSIGN WHILE ZEROSprogram : instructions_optinstructions_opt : instructions instructions_opt : instructions : instructions instruction\n                    | instructioninstruction : \'{\' instructions \'}\' instruction : if\n                   | if \';\'\n                   | return\n                   | return \';\'\n                   | break\n                   | break \';\'\n                   | continue\n                   | continue \';\'\n                   | for_loop\n                   | for_loop \';\'\n                   | while_loop\n                   | while_loop \';\'\n                   | assignment\n                   | assignment \';\'\n                   | print\n                   | print \';\'\n                   if : IF \'(\' expression \')\' instruction %prec IFX\n          | IF \'(\' expression \')\' instruction ELSE instructionbreak : BREAKcontinue : CONTINUEwhile_loop : WHILE \'(\' expression \')\' instruction for_loop : FOR id \'=\' expression \':\' expression instructionreturn : RETURN expression\n              | RETURNprint : PRINT \'(\' list_for_print \')\'\n             | PRINT list_for_printlist_for_print : expression \',\' list_for_print\n                      | expressionexpression : var\n                  | \'(\' expression \')\'\n                  | int\n                  | float\n                  | stringint : INTNUM float : FLOATNUM string : STRING var : idid : IDvar : id \'[\' mat_func_args \']\' assignment : var \'=\' expression\n                  | var ADDASSIGN expression\n                  | var SUBASSIGN expression\n                  | var MULASSIGN expression\n                  | var DIVASSIGN expressionexpression : expression "\'" expression : \'-\' expression %prec UMINUSexpression : expression \'+\' expression\n                  | expression \'-\' expression\n                  | expression \'*\' expression\n                  | expression \'/\' expression\n\n                  | expression DOTADD expression\n                  | expression DOTSUB expression\n                  | expression DOTMUL expression\n                  | expression DOTDIV expression\n\n                  | expression \'<\' expression\n                  | expression \'>\' expression\n                  | expression LESSEQ expression\n                  | expression MOREEQ expression\n                  | expression EQUAL expression\n                  | expression NOTEQUAL expression\n                  expression : matrix matrix : \'[\' matrix \']\'\n              | \'[\' sub_string_1 \']\'\n              | \'[\' sub_string_1 \',\' matrix \']\' sub_string_1 : sub_string_1 \',\' expression\n                    | expressionexpression : matrix_creation \'(\' mat_func_args \')\' mat_func_args : mat_func_args \',\' expression\n                     | expressionmatrix_creation : ZEROS\n                       | ONES\n                       | EYE'
    
_lr_action_items = {'$end':([0,1,2,3,4,6,7,8,9,10,11,12,13,15,16,17,19,23,24,26,27,28,29,30,31,32,33,35,36,38,39,40,42,45,46,47,60,61,62,64,80,89,90,91,92,93,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,114,115,118,121,122,123,124,129,131,133,134,],[-3,0,-1,-2,-5,-7,-9,-11,-13,-15,-17,-19,-21,-30,-25,-26,-43,-44,-4,-8,-10,-12,-14,-16,-18,-20,-22,-29,-35,-37,-38,-39,-67,-40,-41,-42,-32,-34,-6,-51,-52,-46,-47,-48,-49,-50,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-36,-68,-69,-45,-31,-33,-23,-73,-27,-70,-24,-28,]),'{':([0,3,4,5,6,7,8,9,10,11,12,13,15,16,17,19,23,24,25,26,27,28,29,30,31,32,33,35,36,38,39,40,42,45,46,47,60,61,62,64,80,89,90,91,92,93,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,114,115,118,120,121,122,123,124,129,130,131,132,133,134,],[5,5,-5,5,-7,-9,-11,-13,-15,-17,-19,-21,-30,-25,-26,-43,-44,-4,5,-8,-10,-12,-14,-16,-18,-20,-22,-29,-35,-37,-38,-39,-67,-40,-41,-42,-32,-34,-6,-51,-52,-46,-47,-48,-49,-50,5,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-36,-68,-69,-45,5,-31,-33,-23,-73,-27,5,-70,5,-24,-28,]),'IF':([0,3,4,5,6,7,8,9,10,11,12,13,15,16,17,19,23,24,25,26,27,28,29,30,31,32,33,35,36,38,39,40,42,45,46,47,60,61,62,64,80,89,90,91,92,93,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,114,115,118,120,121,122,123,124,129,130,131,132,133,134,],[14,14,-5,14,-7,-9,-11,-13,-15,-17,-19,-21,-30,-25,-26,-43,-44,-4,14,-8,-10,-12,-14,-16,-18,-20,-22,-29,-35,-37,-38,-39,-67,-40,-41,-42,-32,-34,-6,-51,-52,-46,-47,-48,-49,-50,14,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-36,-68,-69,-45,14,-31,-33,-23,-73,-27,14,-70,14,-24,-28,]),'RETURN':([0,3,4,5,6,7,8,9,10,11,12,13,15,16,17,19,23,24,25,26,27,28,29,30,31,32,33,35,36,38,39,40,42,45,46,47,60,61,62,64,80,89,90,91,92,93,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,114,115,118,120,121,122,123,124,129,130,131,132,133,134,],[15,15,-5,15,-7,-9,-11,-13,-15,-17,-19,-21,-30,-25,-26,-43,-44,-4,15,-8,-10,-12,-14,-16,-18,-20,-22,-29,-35,-37,-38,-39,-67,-40,-41,-42,-32,-34,-6,-51,-52,-46,-47,-48,-49,-50,15,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-36,-68,-69,-45,15,-31,-33,-23,-73,-27,15,-70,15,-24,-28,]),'BREAK':([0,3,4,5,6,7,8,9,10,11,12,13,15,16,17,19,23,24,25,26,27,28,29,30,31,32,33,35,36,38,39,40,42,45,46,47,60,61,62,64,80,89,90,91,92,93,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,114,115,118,120,121,122,123,124,129,130,131,132,133,134,],[16,16,-5,16,-7,-9,-11,-13,-15,-17,-19,-21,-30,-25,-26,-43,-44,-4,16,-8,-10,-12,-14,-16,-18,-20,-22,-29,-35,-37,-38,-39,-67,-40,-41,-42,-32,-34,-6,-51,-52,-46,-47,-48,-49,-50,16,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-36,-68,-69,-45,16,-31,-33,-23,-73,-27,16,-70,16,-24,-28,]),'CONTINUE':([0,3,4,5,6,7,8,9,10,11,12,13,15,16,17,19,23,24,25,26,27,28,29,30,31,32,33,35,36,38,39,40,42,45,46,47,60,61,62,64,80,89,90,91,92,93,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,114,115,118,120,121,122,123,124,129,130,131,132,133,134,],[17,17,-5,17,-7,-9,-11,-13,-15,-17,-19,-21,-30,-25,-26,-43,-44,-4,17,-8,-10,-12,-14,-16,-18,-20,-22,-29,-35,-37,-38,-39,-67,-40,-41,-42,-32,-34,-6,-51,-52,-46,-47,-48,-49,-50,17,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-36,-68,-69,-45,17,-31,-33,-23,-73,-27,17,-70,17,-24,-28,]),'FOR':([0,3,4,5,6,7,8,9,10,11,12,13,15,16,17,19,23,24,25,26,27,28,29,30,31,32,33,35,36,38,39,40,42,45,46,47,60,61,62,64,80,89,90,91,92,93,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,114,115,118,120,121,122,123,124,129,130,131,132,133,134,],[18,18,-5,18,-7,-9,-11,-13,-15,-17,-19,-21,-30,-25,-26,-43,-44,-4,18,-8,-10,-12,-14,-16,-18,-20,-22,-29,-35,-37,-38,-39,-67,-40,-41,-42,-32,-34,-6,-51,-52,-46,-47,-48,-49,-50,18,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-36,-68,-69,-45,18,-31,-33,-23,-73,-27,18,-70,18,-24,-28,]),'WHILE':([0,3,4,5,6,7,8,9,10,11,12,13,15,16,17,19,23,24,25,26,27,28,29,30,31,32,33,35,36,38,39,40,42,45,46,47,60,61,62,64,80,89,90,91,92,93,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,114,115,118,120,121,122,123,124,129,130,131,132,133,134,],[20,20,-5,20,-7,-9,-11,-13,-15,-17,-19,-21,-30,-25,-26,-43,-44,-4,20,-8,-10,-12,-14,-16,-18,-20,-22,-29,-35,-37,-38,-39,-67,-40,-41,-42,-32,-34,-6,-51,-52,-46,-47,-48,-49,-50,20,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-36,-68,-69,-45,20,-31,-33,-23,-73,-27,20,-70,20,-24,-28,]),'PRINT':([0,3,4,5,6,7,8,9,10,11,12,13,15,16,17,19,23,24,25,26,27,28,29,30,31,32,33,35,36,38,39,40,42,45,46,47,60,61,62,64,80,89,90,91,92,93,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,114,115,118,120,121,122,123,124,129,130,131,132,133,134,],[22,22,-5,22,-7,-9,-11,-13,-15,-17,-19,-21,-30,-25,-26,-43,-44,-4,22,-8,-10,-12,-14,-16,-18,-20,-22,-29,-35,-37,-38,-39,-67,-40,-41,-42,-32,-34,-6,-51,-52,-46,-47,-48,-49,-50,22,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-36,-68,-69,-45,22,-31,-33,-23,-73,-27,22,-70,22,-24,-28,]),'ID':([0,3,4,5,6,7,8,9,10,11,12,13,15,16,17,18,19,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,44,45,46,47,52,53,54,55,56,57,58,59,60,61,62,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,80,81,85,89,90,91,92,93,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,114,115,116,118,119,120,121,122,123,124,127,129,130,131,132,133,134,],[23,23,-5,23,-7,-9,-11,-13,-15,-17,-19,-21,23,-25,-26,23,-43,23,-44,-4,23,-8,-10,-12,-14,-16,-18,-20,-22,23,-29,-35,23,-37,-38,-39,23,-67,23,-40,-41,-42,23,23,23,23,23,23,23,23,-32,-34,-6,-51,23,23,23,23,23,23,23,23,23,23,23,23,23,23,-52,23,23,-46,-47,-48,-49,-50,23,23,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-36,-68,-69,23,-45,23,23,-31,-33,-23,-73,23,-27,23,-70,23,-24,-28,]),'}':([4,6,7,8,9,10,11,12,13,15,16,17,19,23,24,25,26,27,28,29,30,31,32,33,35,36,38,39,40,42,45,46,47,60,61,62,64,80,89,90,91,92,93,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,114,115,118,121,122,123,124,129,131,133,134,],[-5,-7,-9,-11,-13,-15,-17,-19,-21,-30,-25,-26,-43,-44,-4,62,-8,-10,-12,-14,-16,-18,-20,-22,-29,-35,-37,-38,-39,-67,-40,-41,-42,-32,-34,-6,-51,-52,-46,-47,-48,-49,-50,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-36,-68,-69,-45,-31,-33,-23,-73,-27,-70,-24,-28,]),'ELSE':([6,7,8,9,10,11,12,13,15,16,17,19,23,26,27,28,29,30,31,32,33,35,36,38,39,40,42,45,46,47,60,61,62,64,80,89,90,91,92,93,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,114,115,118,121,122,123,124,129,131,133,134,],[-7,-9,-11,-13,-15,-17,-19,-21,-30,-25,-26,-43,-44,-8,-10,-12,-14,-16,-18,-20,-22,-29,-35,-37,-38,-39,-67,-40,-41,-42,-32,-34,-6,-51,-52,-46,-47,-48,-49,-50,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-36,-68,-69,-45,-31,-33,130,-73,-27,-70,-24,-28,]),';':([6,7,8,9,10,11,12,13,15,16,17,19,23,26,27,28,29,30,31,32,33,35,36,38,39,40,42,45,46,47,60,61,62,64,80,89,90,91,92,93,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,114,115,118,121,122,123,124,129,131,133,134,],[26,27,28,29,30,31,32,33,-30,-25,-26,-43,-44,-8,-10,-12,-14,-16,-18,-20,-22,-29,-35,-37,-38,-39,-67,-40,-41,-42,-32,-34,-6,-51,-52,-46,-47,-48,-49,-50,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-36,-68,-69,-45,-31,-33,-23,-73,-27,-70,-24,-28,]),'(':([14,15,20,22,34,37,41,43,44,48,49,50,52,53,54,55,56,57,58,59,65,66,67,68,69,70,71,72,73,74,75,76,77,78,81,85,96,116,119,127,],[34,37,53,59,37,37,37,81,37,-76,-77,-78,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'-':([15,19,22,23,34,35,36,37,38,39,40,41,42,44,45,46,47,52,53,54,55,56,57,58,59,61,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,84,85,87,88,89,90,91,92,93,95,96,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,114,115,116,117,118,119,124,125,126,127,128,131,132,],[41,-43,41,-44,41,66,-35,41,-37,-38,-39,41,-67,41,-40,-41,-42,41,41,41,41,41,41,41,41,66,66,-51,41,41,41,41,41,41,41,41,41,41,41,41,41,41,66,-52,41,-67,66,41,66,66,66,66,66,66,66,66,41,-53,-54,-55,-56,-57,-58,-59,-60,66,66,66,66,66,66,-36,-68,-69,41,66,-45,41,-73,-67,66,41,66,-70,66,]),'INTNUM':([15,22,34,37,41,44,52,53,54,55,56,57,58,59,65,66,67,68,69,70,71,72,73,74,75,76,77,78,81,85,96,116,119,127,],[45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,]),'FLOATNUM':([15,22,34,37,41,44,52,53,54,55,56,57,58,59,65,66,67,68,69,70,71,72,73,74,75,76,77,78,81,85,96,116,119,127,],[46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,]),'STRING':([15,22,34,37,41,44,52,53,54,55,56,57,58,59,65,66,67,68,69,70,71,72,73,74,75,76,77,78,81,85,96,116,119,127,],[47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,]),'[':([15,19,22,23,34,37,41,44,52,53,54,55,56,57,58,59,65,66,67,68,69,70,71,72,73,74,75,76,77,78,81,85,96,116,119,127,],[44,52,44,-44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'ZEROS':([15,22,34,37,41,44,52,53,54,55,56,57,58,59,65,66,67,68,69,70,71,72,73,74,75,76,77,78,81,85,96,116,119,127,],[48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,]),'ONES':([15,22,34,37,41,44,52,53,54,55,56,57,58,59,65,66,67,68,69,70,71,72,73,74,75,76,77,78,81,85,96,116,119,127,],[49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,]),'EYE':([15,22,34,37,41,44,52,53,54,55,56,57,58,59,65,66,67,68,69,70,71,72,73,74,75,76,77,78,81,85,96,116,119,127,],[50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,]),'=':([19,21,23,51,118,],[-43,54,-44,85,-45,]),'ADDASSIGN':([19,21,23,118,],[-43,55,-44,-45,]),'SUBASSIGN':([19,21,23,118,],[-43,56,-44,-45,]),'MULASSIGN':([19,21,23,118,],[-43,57,-44,-45,]),'DIVASSIGN':([19,21,23,118,],[-43,58,-44,-45,]),"'":([19,23,35,36,38,39,40,42,45,46,47,61,63,64,79,80,82,84,87,88,89,90,91,92,93,95,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,114,115,117,118,124,125,126,128,131,132,],[-43,-44,64,-35,-37,-38,-39,-67,-40,-41,-42,64,64,-51,64,-52,-67,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,-36,-68,-69,64,-45,-73,-67,64,64,-70,64,]),'+':([19,23,35,36,38,39,40,42,45,46,47,61,63,64,79,80,82,84,87,88,89,90,91,92,93,95,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,114,115,117,118,124,125,126,128,131,132,],[-43,-44,65,-35,-37,-38,-39,-67,-40,-41,-42,65,65,-51,65,-52,-67,65,65,65,65,65,65,65,65,65,-53,-54,-55,-56,-57,-58,-59,-60,65,65,65,65,65,65,-36,-68,-69,65,-45,-73,-67,65,65,-70,65,]),'*':([19,23,35,36,38,39,40,42,45,46,47,61,63,64,79,80,82,84,87,88,89,90,91,92,93,95,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,114,115,117,118,124,125,126,128,131,132,],[-43,-44,67,-35,-37,-38,-39,-67,-40,-41,-42,67,67,-51,67,-52,-67,67,67,67,67,67,67,67,67,67,67,67,-55,-56,67,67,-59,-60,67,67,67,67,67,67,-36,-68,-69,67,-45,-73,-67,67,67,-70,67,]),'/':([19,23,35,36,38,39,40,42,45,46,47,61,63,64,79,80,82,84,87,88,89,90,91,92,93,95,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,114,115,117,118,124,125,126,128,131,132,],[-43,-44,68,-35,-37,-38,-39,-67,-40,-41,-42,68,68,-51,68,-52,-67,68,68,68,68,68,68,68,68,68,68,68,-55,-56,68,68,-59,-60,68,68,68,68,68,68,-36,-68,-69,68,-45,-73,-67,68,68,-70,68,]),'DOTADD':([19,23,35,36,38,39,40,42,45,46,47,61,63,64,79,80,82,84,87,88,89,90,91,92,93,95,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,114,115,117,118,124,125,126,128,131,132,],[-43,-44,69,-35,-37,-38,-39,-67,-40,-41,-42,69,69,-51,69,-52,-67,69,69,69,69,69,69,69,69,69,-53,-54,-55,-56,-57,-58,-59,-60,69,69,69,69,69,69,-36,-68,-69,69,-45,-73,-67,69,69,-70,69,]),'DOTSUB':([19,23,35,36,38,39,40,42,45,46,47,61,63,64,79,80,82,84,87,88,89,90,91,92,93,95,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,114,115,117,118,124,125,126,128,131,132,],[-43,-44,70,-35,-37,-38,-39,-67,-40,-41,-42,70,70,-51,70,-52,-67,70,70,70,70,70,70,70,70,70,-53,-54,-55,-56,-57,-58,-59,-60,70,70,70,70,70,70,-36,-68,-69,70,-45,-73,-67,70,70,-70,70,]),'DOTMUL':([19,23,35,36,38,39,40,42,45,46,47,61,63,64,79,80,82,84,87,88,89,90,91,92,93,95,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,114,115,117,118,124,125,126,128,131,132,],[-43,-44,71,-35,-37,-38,-39,-67,-40,-41,-42,71,71,-51,71,-52,-67,71,71,71,71,71,71,71,71,71,71,71,-55,-56,71,71,-59,-60,71,71,71,71,71,71,-36,-68,-69,71,-45,-73,-67,71,71,-70,71,]),'DOTDIV':([19,23,35,36,38,39,40,42,45,46,47,61,63,64,79,80,82,84,87,88,89,90,91,92,93,95,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,114,115,117,118,124,125,126,128,131,132,],[-43,-44,72,-35,-37,-38,-39,-67,-40,-41,-42,72,72,-51,72,-52,-67,72,72,72,72,72,72,72,72,72,72,72,-55,-56,72,72,-59,-60,72,72,72,72,72,72,-36,-68,-69,72,-45,-73,-67,72,72,-70,72,]),'<':([19,23,35,36,38,39,40,42,45,46,47,61,63,64,79,80,82,84,87,88,89,90,91,92,93,95,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,114,115,117,118,124,125,126,128,131,132,],[-43,-44,73,-35,-37,-38,-39,-67,-40,-41,-42,73,73,-51,73,-52,-67,73,73,73,73,73,73,73,73,73,-53,-54,-55,-56,-57,-58,-59,-60,None,None,None,None,None,None,-36,-68,-69,73,-45,-73,-67,73,73,-70,73,]),'>':([19,23,35,36,38,39,40,42,45,46,47,61,63,64,79,80,82,84,87,88,89,90,91,92,93,95,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,114,115,117,118,124,125,126,128,131,132,],[-43,-44,74,-35,-37,-38,-39,-67,-40,-41,-42,74,74,-51,74,-52,-67,74,74,74,74,74,74,74,74,74,-53,-54,-55,-56,-57,-58,-59,-60,None,None,None,None,None,None,-36,-68,-69,74,-45,-73,-67,74,74,-70,74,]),'LESSEQ':([19,23,35,36,38,39,40,42,45,46,47,61,63,64,79,80,82,84,87,88,89,90,91,92,93,95,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,114,115,117,118,124,125,126,128,131,132,],[-43,-44,75,-35,-37,-38,-39,-67,-40,-41,-42,75,75,-51,75,-52,-67,75,75,75,75,75,75,75,75,75,-53,-54,-55,-56,-57,-58,-59,-60,None,None,None,None,None,None,-36,-68,-69,75,-45,-73,-67,75,75,-70,75,]),'MOREEQ':([19,23,35,36,38,39,40,42,45,46,47,61,63,64,79,80,82,84,87,88,89,90,91,92,93,95,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,114,115,117,118,124,125,126,128,131,132,],[-43,-44,76,-35,-37,-38,-39,-67,-40,-41,-42,76,76,-51,76,-52,-67,76,76,76,76,76,76,76,76,76,-53,-54,-55,-56,-57,-58,-59,-60,None,None,None,None,None,None,-36,-68,-69,76,-45,-73,-67,76,76,-70,76,]),'EQUAL':([19,23,35,36,38,39,40,42,45,46,47,61,63,64,79,80,82,84,87,88,89,90,91,92,93,95,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,114,115,117,118,124,125,126,128,131,132,],[-43,-44,77,-35,-37,-38,-39,-67,-40,-41,-42,77,77,-51,77,-52,-67,77,77,77,77,77,77,77,77,77,-53,-54,-55,-56,-57,-58,-59,-60,None,None,None,None,None,None,-36,-68,-69,77,-45,-73,-67,77,77,-70,77,]),'NOTEQUAL':([19,23,35,36,38,39,40,42,45,46,47,61,63,64,79,80,82,84,87,88,89,90,91,92,93,95,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,114,115,117,118,124,125,126,128,131,132,],[-43,-44,78,-35,-37,-38,-39,-67,-40,-41,-42,78,78,-51,78,-52,-67,78,78,78,78,78,78,78,78,78,-53,-54,-55,-56,-57,-58,-59,-60,None,None,None,None,None,None,-36,-68,-69,78,-45,-73,-67,78,78,-70,78,]),',':([19,23,36,38,39,40,42,45,46,47,61,64,80,82,83,84,86,87,95,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,118,124,125,126,128,131,],[-43,-44,-35,-37,-38,-39,-67,-40,-41,-42,96,-51,-52,-67,116,-72,119,-75,96,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-36,119,-68,-69,-45,-73,-67,-71,-74,-70,]),')':([19,23,36,38,39,40,42,45,46,47,61,63,64,79,80,87,88,94,95,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,118,122,124,128,131,],[-43,-44,-35,-37,-38,-39,-67,-40,-41,-42,-34,97,-51,112,-52,-75,120,121,112,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-36,124,-68,-69,-45,-33,-73,-74,-70,]),']':([19,23,36,38,39,40,42,45,46,47,64,80,82,83,84,86,87,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,114,115,118,124,125,126,128,131,],[-43,-44,-35,-37,-38,-39,-67,-40,-41,-42,-51,-52,114,115,-72,118,-75,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-36,-68,-69,-45,-73,131,-71,-74,-70,]),':':([19,23,36,38,39,40,42,45,46,47,64,80,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,114,115,117,118,124,131,],[-43,-44,-35,-37,-38,-39,-67,-40,-41,-42,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-36,-68,-69,127,-45,-73,-70,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'instructions_opt':([0,],[2,]),'instructions':([0,5,],[3,25,]),'instruction':([0,3,5,25,97,120,130,132,],[4,24,4,24,123,129,133,134,]),'if':([0,3,5,25,97,120,130,132,],[6,6,6,6,6,6,6,6,]),'return':([0,3,5,25,97,120,130,132,],[7,7,7,7,7,7,7,7,]),'break':([0,3,5,25,97,120,130,132,],[8,8,8,8,8,8,8,8,]),'continue':([0,3,5,25,97,120,130,132,],[9,9,9,9,9,9,9,9,]),'for_loop':([0,3,5,25,97,120,130,132,],[10,10,10,10,10,10,10,10,]),'while_loop':([0,3,5,25,97,120,130,132,],[11,11,11,11,11,11,11,11,]),'assignment':([0,3,5,25,97,120,130,132,],[12,12,12,12,12,12,12,12,]),'print':([0,3,5,25,97,120,130,132,],[13,13,13,13,13,13,13,13,]),'id':([0,3,5,15,18,22,25,34,37,41,44,52,53,54,55,56,57,58,59,65,66,67,68,69,70,71,72,73,74,75,76,77,78,81,85,96,97,116,119,120,127,130,132,],[19,19,19,19,51,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,]),'var':([0,3,5,15,22,25,34,37,41,44,52,53,54,55,56,57,58,59,65,66,67,68,69,70,71,72,73,74,75,76,77,78,81,85,96,97,116,119,120,127,130,132,],[21,21,21,36,36,21,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,21,36,36,21,36,21,21,]),'expression':([15,22,34,37,41,44,52,53,54,55,56,57,58,59,65,66,67,68,69,70,71,72,73,74,75,76,77,78,81,85,96,116,119,127,],[35,61,63,79,80,84,87,88,89,90,91,92,93,95,98,99,100,101,102,103,104,105,106,107,108,109,110,111,87,117,61,126,128,132,]),'int':([15,22,34,37,41,44,52,53,54,55,56,57,58,59,65,66,67,68,69,70,71,72,73,74,75,76,77,78,81,85,96,116,119,127,],[38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'float':([15,22,34,37,41,44,52,53,54,55,56,57,58,59,65,66,67,68,69,70,71,72,73,74,75,76,77,78,81,85,96,116,119,127,],[39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,]),'string':([15,22,34,37,41,44,52,53,54,55,56,57,58,59,65,66,67,68,69,70,71,72,73,74,75,76,77,78,81,85,96,116,119,127,],[40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,]),'matrix':([15,22,34,37,41,44,52,53,54,55,56,57,58,59,65,66,67,68,69,70,71,72,73,74,75,76,77,78,81,85,96,116,119,127,],[42,42,42,42,42,82,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,125,42,42,]),'matrix_creation':([15,22,34,37,41,44,52,53,54,55,56,57,58,59,65,66,67,68,69,70,71,72,73,74,75,76,77,78,81,85,96,116,119,127,],[43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,]),'list_for_print':([22,59,96,],[60,94,122,]),'sub_string_1':([44,],[83,]),'mat_func_args':([52,81,],[86,113,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> instructions_opt','program',1,'p_program','Mparser.py',37),
  ('instructions_opt -> instructions','instructions_opt',1,'p_instructions_opt_1','Mparser.py',42),
  ('instructions_opt -> <empty>','instructions_opt',0,'p_instructions_opt_2','Mparser.py',47),
  ('instructions -> instructions instruction','instructions',2,'p_instructions_1','Mparser.py',51),
  ('instructions -> instruction','instructions',1,'p_instructions_1','Mparser.py',52),
  ('instruction -> { instructions }','instruction',3,'p_instructions_2','Mparser.py',68),
  ('instruction -> if','instruction',1,'p_instruction_3','Mparser.py',73),
  ('instruction -> if ;','instruction',2,'p_instruction_3','Mparser.py',74),
  ('instruction -> return','instruction',1,'p_instruction_3','Mparser.py',75),
  ('instruction -> return ;','instruction',2,'p_instruction_3','Mparser.py',76),
  ('instruction -> break','instruction',1,'p_instruction_3','Mparser.py',77),
  ('instruction -> break ;','instruction',2,'p_instruction_3','Mparser.py',78),
  ('instruction -> continue','instruction',1,'p_instruction_3','Mparser.py',79),
  ('instruction -> continue ;','instruction',2,'p_instruction_3','Mparser.py',80),
  ('instruction -> for_loop','instruction',1,'p_instruction_3','Mparser.py',81),
  ('instruction -> for_loop ;','instruction',2,'p_instruction_3','Mparser.py',82),
  ('instruction -> while_loop','instruction',1,'p_instruction_3','Mparser.py',83),
  ('instruction -> while_loop ;','instruction',2,'p_instruction_3','Mparser.py',84),
  ('instruction -> assignment','instruction',1,'p_instruction_3','Mparser.py',85),
  ('instruction -> assignment ;','instruction',2,'p_instruction_3','Mparser.py',86),
  ('instruction -> print','instruction',1,'p_instruction_3','Mparser.py',87),
  ('instruction -> print ;','instruction',2,'p_instruction_3','Mparser.py',88),
  ('if -> IF ( expression ) instruction','if',5,'p_if','Mparser.py',94),
  ('if -> IF ( expression ) instruction ELSE instruction','if',7,'p_if','Mparser.py',95),
  ('break -> BREAK','break',1,'p_break','Mparser.py',104),
  ('continue -> CONTINUE','continue',1,'p_continue','Mparser.py',109),
  ('while_loop -> WHILE ( expression ) instruction','while_loop',5,'p_while','Mparser.py',114),
  ('for_loop -> FOR id = expression : expression instruction','for_loop',7,'p_for','Mparser.py',126),
  ('return -> RETURN expression','return',2,'p_return','Mparser.py',132),
  ('return -> RETURN','return',1,'p_return','Mparser.py',133),
  ('print -> PRINT ( list_for_print )','print',4,'p_print','Mparser.py',142),
  ('print -> PRINT list_for_print','print',2,'p_print','Mparser.py',143),
  ('list_for_print -> expression , list_for_print','list_for_print',3,'p_list_for_print','Mparser.py',152),
  ('list_for_print -> expression','list_for_print',1,'p_list_for_print','Mparser.py',153),
  ('expression -> var','expression',1,'p_expression_obj','Mparser.py',161),
  ('expression -> ( expression )','expression',3,'p_expression_obj','Mparser.py',162),
  ('expression -> int','expression',1,'p_expression_obj','Mparser.py',163),
  ('expression -> float','expression',1,'p_expression_obj','Mparser.py',164),
  ('expression -> string','expression',1,'p_expression_obj','Mparser.py',165),
  ('int -> INTNUM','int',1,'p_expression_int','Mparser.py',170),
  ('float -> FLOATNUM','float',1,'p_expression_float','Mparser.py',175),
  ('string -> STRING','string',1,'p_expression_string','Mparser.py',180),
  ('var -> id','var',1,'p_expression_var','Mparser.py',185),
  ('id -> ID','id',1,'p_id','Mparser.py',190),
  ('var -> id [ mat_func_args ]','var',4,'p_expression_ref','Mparser.py',195),
  ('assignment -> var = expression','assignment',3,'p_expression_assignment','Mparser.py',200),
  ('assignment -> var ADDASSIGN expression','assignment',3,'p_expression_assignment','Mparser.py',201),
  ('assignment -> var SUBASSIGN expression','assignment',3,'p_expression_assignment','Mparser.py',202),
  ('assignment -> var MULASSIGN expression','assignment',3,'p_expression_assignment','Mparser.py',203),
  ('assignment -> var DIVASSIGN expression','assignment',3,'p_expression_assignment','Mparser.py',204),
  ("expression -> expression '",'expression',2,'p_expression_uniop_left','Mparser.py',209),
  ('expression -> - expression','expression',2,'p_expression_uniop_right','Mparser.py',214),
  ('expression -> expression + expression','expression',3,'p_expression_binop','Mparser.py',219),
  ('expression -> expression - expression','expression',3,'p_expression_binop','Mparser.py',220),
  ('expression -> expression * expression','expression',3,'p_expression_binop','Mparser.py',221),
  ('expression -> expression / expression','expression',3,'p_expression_binop','Mparser.py',222),
  ('expression -> expression DOTADD expression','expression',3,'p_expression_binop','Mparser.py',224),
  ('expression -> expression DOTSUB expression','expression',3,'p_expression_binop','Mparser.py',225),
  ('expression -> expression DOTMUL expression','expression',3,'p_expression_binop','Mparser.py',226),
  ('expression -> expression DOTDIV expression','expression',3,'p_expression_binop','Mparser.py',227),
  ('expression -> expression < expression','expression',3,'p_expression_binop','Mparser.py',229),
  ('expression -> expression > expression','expression',3,'p_expression_binop','Mparser.py',230),
  ('expression -> expression LESSEQ expression','expression',3,'p_expression_binop','Mparser.py',231),
  ('expression -> expression MOREEQ expression','expression',3,'p_expression_binop','Mparser.py',232),
  ('expression -> expression EQUAL expression','expression',3,'p_expression_binop','Mparser.py',233),
  ('expression -> expression NOTEQUAL expression','expression',3,'p_expression_binop','Mparser.py',234),
  ('expression -> matrix','expression',1,'p_expression_matrix','Mparser.py',241),
  ('matrix -> [ matrix ]','matrix',3,'p_matrix','Mparser.py',246),
  ('matrix -> [ sub_string_1 ]','matrix',3,'p_matrix','Mparser.py',247),
  ('matrix -> [ sub_string_1 , matrix ]','matrix',5,'p_matrix','Mparser.py',248),
  ('sub_string_1 -> sub_string_1 , expression','sub_string_1',3,'p_sub_matrix','Mparser.py',259),
  ('sub_string_1 -> expression','sub_string_1',1,'p_sub_matrix','Mparser.py',260),
  ('expression -> matrix_creation ( mat_func_args )','expression',4,'p_matrix_creation_1','Mparser.py',271),
  ('mat_func_args -> mat_func_args , expression','mat_func_args',3,'p_matrix_function_args','Mparser.py',276),
  ('mat_func_args -> expression','mat_func_args',1,'p_matrix_function_args','Mparser.py',277),
  ('matrix_creation -> ZEROS','matrix_creation',1,'p_matrix_creation','Mparser.py',282),
  ('matrix_creation -> ONES','matrix_creation',1,'p_matrix_creation','Mparser.py',283),
  ('matrix_creation -> EYE','matrix_creation',1,'p_matrix_creation','Mparser.py',284),
]
