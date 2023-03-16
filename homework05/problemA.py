from cs1graphics import *
w=int
w=500
can=Canvas(w,(w*(.6)),'lightgray','Problem A')
rect=Rectangle((w*(4/10)),(w*(2/10)))
rect.setFillColor('white')
rect.move((w*(1/2)),(w*(4/10)))
rect.setBorderWidth(w*(1/100))
can.add(rect)

circ=Circle(w*(1/10))
circ.setFillColor('brown')
circ.move((w*(7/10)),(w*(3/10)))
can.add(circ)
