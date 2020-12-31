import turtle

wn = turtle.Screen()
wn.bgcolor('black')
wn.title('Pong by @ala.bzz')
wn.setup(width=800, height=600)
wn.tracer(0)


# pod class
class Pod:
    def __init__(self):
        self.podd = turtle.Turtle()

    def speed(self, ss):
        self.podd.speed(ss)

    def shape(self, shape):
        self.podd.shape(shape)

    def color(self, color):
        self.podd.color(color)

    def shapesize(self, x, y):
        self.podd.shapesize(x, y)

    def position(self, xx, yy):
        self.podd.penup()
        self.podd.goto(xx, yy)

    def move_up_1(self):
        y = self.podd.ycor()
        y += 20
        self.podd.sety(y)
        pod1.position(-350, y)

    def move_down_1(self):
        y = self.podd.ycor()
        y -= 20
        self.podd.sety(y)   #------
        pod1.position(-350, y)

    def move_up_2(self):
        y = self.podd.ycor()
        y += 20
        self.podd.sety(y)
        pod2.position(350, y)


    def move_down_2(self):
        y = self.podd.ycor()
        y -= 20
        self.podd.sety(y)
        pod2.position(350, y)

# pod1

pod1 = Pod()
pod1.speed(0)
pod1.shape('square')
pod1.color('white')
pod1.shapesize(5, 1)
pod1.position(-350, 0)

# pod2

pod2 = Pod()
pod2.speed(0)
pod2.shape('square')
pod2.color('white')
pod2.shapesize(5, 1)
pod2.position(350, 0)

# ball
ball = Pod()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.shapesize(1, 1)
ball.position(100, 100)


wn.listen()
wn.onkeypress(pod1.move_up_1, 'w')
wn.onkeypress(pod1.move_down_1, 's')
wn.onkeypress(pod2.move_up_2, 'u')
wn.onkeypress(pod2.move_down_2, 'j')



while True:
    wn.update()
