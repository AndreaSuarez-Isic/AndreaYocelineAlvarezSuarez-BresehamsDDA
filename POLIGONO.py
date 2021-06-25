from turtle import Turtle
import subprocess

def main():
    subprocess.call(["cmd.exe","/C","cls"])
    t=Turtle()
    t.hideturtle()
    xuno= 0
    yuno= 0
    xdos= 30
    ydos= 30
    
    dx= abs(xdos-xuno)
    dy= abs(ydos-yuno)
    p= (2 * dy) - dx

    t.color("white")
    t.setx(dx)
    t.sety(dy)
    t.color("black")

    t.pensize("5")
    n=int(input("INGRESA EL NUMERO DE LADOS: "))
    ang=180-(((n-2)/n)*180)
    
    if n <= 306:
        for i in range(n):
            t.left(ang)
            xuno=xuno+1
            if p < 0:
                p = p + (2 * dy)
            else:
                p = p + (2 * dy) - (2 * dx)
                yuno=yuno+1
            print(xuno, ',', yuno)
            t.fd(p)
    else:
        print("NO EXCEDER LOS 360")    
    

if __name__== '__main__':
    main()