'''def outerdecorator(*kwargs):
    print("Inside decorator")
    def innerfunc(func):#-->second it will come here,here the func is timer
            for arg in kwargs:
                print(arg)
                if arg=='Admin':
                    func()
                else:
                    print("He can't access the site")
    return innerfunc
@outerdecorator('Admin','sandhya') 
def my_func():
    print("He can access the site")'''
class Roles:
    def outerdecorator(*kwargs):
        print("Inside decorator")
        def innerfunc(func):#-->second it will come here,here the func is timer
            def inner(self):
                print(kwargs)
                for arg in kwargs:
                    print(arg)
                    if arg=='admin':
                        func(self)

                    else:
                        print("Can't access the site")
            return inner
        return innerfunc
    list=['admin','sandhya']
    @outerdecorator('admin','sandhya')
    def update(self):
        print("Only Admin will be able to provide updates")
    
    
object= Roles()
object.update()  

