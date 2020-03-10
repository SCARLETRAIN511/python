import turtle


def listsum(numlist):
    if len(numlist) == 1:
        return numlist[0]
    else:
        return numlist[0] + listsum(numlist[1:])

def toStr(n, base):
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        return toStr(n//base, base) + convertString[n%base]

def main1():
    t = turtle.Turtle()
    def drawSpecial(t, lineLen):

        if lineLen > 0:
            t.forward(lineLen)
            t.right(90)
            drawSpecial(t,lineLen - 5)    
    drawSpecial(t,100)
    turtle.done()

def main2():
    def SieTri(degree, points):
        colormap = ['blue','red','green','white','yellow','orange']
        drawTriangle(points, colormap[degree])
        if degree > 0:
            SieTri(degree - 1, {'left':points['left'],
                                'top':getMid(points['left'],points['top']),
                                'right':getMid(points['left'],points['right'])})

            SieTri(degree - 1, {'left':getMid(points['left'],points['top']),
                                'top':points['top'],
                                'right':getMid(points['top'],points['right'])})

            SieTri(degree - 1, {'left':getMid(points['left'],points['right']),
                                'top':getMid(points['top'],points['right']),
                                'right':points['right']})

    t=turtle.Turtle()
    def drawTriangle(points,color):
        t.fillcolor(color)
        t.penup()
        t.goto(points['top'])
        t.pendown()
        t.begin_fill()
        t.goto(points['left'])
        t.goto(points['right'])
        t.goto(points['top'])
        t.end_fill()

    def getMid(p1,p2):
        return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

    points = {'left':(-200,-100),'top':(0,200),'right':(200,-100)}

    SieTri(5,points)
    turtle.done()

def main3():
    def moveDisk(disk, fromPole, toPole):
        print(f"Moving disk[{disk}] from {fromPole} to {toPole}")

    def moveTower(height, fromPole, withPole, toPole):
        if height >= 1:
            moveTower(height - 1, fromPole, toPole , withPole)
            moveDisk(height, fromPole, toPole)
            moveTower(height - 1, withPole, fromPole, toPole)

    moveTower(10,'#1','#2','#3')


if __name__ == "__main__":
    main3()

