class Greeter(object):

    def __init__(self, name):
        self.name = name

    def hello(self):
        print("Hello " + self.name)
        
    def goodbye(self):
        print("Goodbye " + self.name)
        

g1 = Greeter("Alae")
g1.hello()
g1.goodbye()

g2 = Greeter("Alyae")
g2.hello()
g2.goodbye()

