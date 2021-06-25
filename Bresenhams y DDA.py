importar  matplotlib . pylab  como  pl
desde  numpy  import  ComplexWarning


def  Algoritmo_Bresenham ( xUno , yUno , xDos , yDos ):
    x  =  xUno
    y  =  yUno
    dx  =  abs ( xDos  -  xUno )
    dy  =  abs ( yDos  -  ydos )
    p  = ( 2  *  dy  -  dx )

    mientras que  x  <=  x2 :
        pl . trama ( x , y , 'm.' )
        x  =  x  +  1
        si ( p  <  0 ):
            p  =  p  +  2  *  dy
        otra cosa :
            p  =  p  + ( 2  *  dy ) - ( 2  *  dx )
            y  =  y  +  1

        imprimir ( '(' , x , ',' , y , ')' )

    pl . título ( 'Codigo' )
    pl . xlabel ( 'X' )
    pl . ylabel ( 'Y' )
    pl . cuadrícula ( color = 'k' , estilo de línea = 'punteado' , ancho de línea = 1 )
    pl . mostrar ()

    print ( "Valor dx:" , dx )
    print ( "Valor dy:" , dy )


def  principal ():
    x1  =  int ( input ( "Ingrese el valor de xUno:" ))
    y1  =  int ( input ( "Ingrese el valor de yDos:" ))
    x2  =  int ( input ( "Ingrese el valor de xDos:" ))
    y2  =  int ( input ( "Ingrese el valor de yDos:" ))

    Algoritmo_Bresenham ( xUno , yUno , xDos , yDos )


if  __name__  ==  "__main__" :
    principal ()