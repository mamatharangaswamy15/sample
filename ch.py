def attach_greet(cls):
    def greet(self):
        return "hello world"
    cls.greet = greet
    return cls
@attach_greet # Demo = greet(Demo)
class Demo:
    def spam(self):
        return "demo spam"
