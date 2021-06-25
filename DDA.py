importar  matplotlib . pylab  como  pl


def  algoritmo_DDA ( x1 , y1 , x2 , y2 ):

    dx  =  abs ( x2  -  x1 )
    dy  =  abs ( y2  -  y1 )
    si ( dx ) > ( dy ):
        pasos  = ( dx )
    otra cosa :
        pasos  = ( dy )

    xinc  =  flotar ( dx  /  pasos )
    yinc  =  flotar ( dy  /  pasos )

    para  i  en el  rango ( 0 , int ( pasos  +  1 )):
        pl . plot ( round ( x1 ), round ( y1 ), "m." )

        x1  =  x1  +  xinc
        y1  =  y1  +  yinc

        imprimir ( '(' , x1 , ',' , y1 , ')' )

    pl . título ( 'DDA' )
    pl . xlabel ( 'X' )
    pl . ylabel ( 'Y' )
    pl . cuadrícula ( color = 'k' , estilo de línea = 'punteado' , ancho de línea = 1 )
    pl . mostrar ()

    print ( "Valor dx:" , dx )
    print ( "Valor dy:" , dy )
    imprimir ( "Pasos de valor:" , pasos )
    print ( "Valor xinc:" , xinc )
    print ( "Valor yinc:" , yinc )


def  principal ():
    x1  =  int ( input ( "Ingrese x1:" ))
    y1  =  int ( input ( "Ingrese y1:" ))
    x2  =  int ( input ( "Ingrese x2:" ))
    y2  =  int ( input ( "Ingrese y2:" ))

    algoritmo_DDA ( x1 , y1 , x2 , y2 )


if  __name__  ==  "__main__" :
    principal ()