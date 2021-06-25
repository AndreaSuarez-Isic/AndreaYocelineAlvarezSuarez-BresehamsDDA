def  principal ():
    print ( ' \ n ¿QUE FIGURA DESEAS DIBUJAR? \ n \ n \
1 = CUADRADO \ n 2 = TRIANGULO \ n 3 = RECTANGULO \ n 4 = TRIANGULO RECTANGULO ' )
    figura =  int ( input ( 'OPCIÓN:' ))
    #CUADRADO
    si  figura ==  1 :
        print ( ' \ n INGRESA 1 PARA DIBUJAR EL CUADRADO CON ALGORITMO BRESENHAMS \ n INGRESA 2 PARA DIBUJAR EL CUADRADO CON ALGOTITMO DDA' )
        n =  int ( input ( 'OPCIÓN:' ))
        si  n == 1 :
            CBRESEN ()
            principal ()
        elif  n == 2 :
            
            CDDA ()
            principal ()
    # TRIANGULO
    elif  figura == 2 :
        print ( ' \ n INGRESA 1 PARA DIBUJAR EL TRIANGULO CON ALGORITMO BRESENHAMS \ n INGRESA 2 PARA DIBUJAR EL TRIANGULO CON ALGOTITMO DDA )
        n =  int ( input ( 'OPCIÓN:' ))
        si  n == 1 :
            TBRESEN ()
            principal ()
        elif  n == 2 :
            
            TDDA ()
            principal ()
    #RECTANGULO
    elif  figura == 3 :
        print ( ' \ n INGRESA 1 PARA DIBUJAR EL RECTANGULO CON ALGORITMO BRESENHAMS \ n INGRESA 2 PARA DIBUJAR EL RECTANGULO CON ALGOTITMO DDA ' )
        n =  int ( input ( 'OPCIÓN:' ))
        si  n == 1 :
            RBRESEN ()
            principal ()
        elif  n == 2 :
            RDDA ()
            principal ()
if  __name__ == '__main__' :
    principal ()