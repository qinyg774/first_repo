class employee(object):
    def __init__(self, val):
        self.val=val
    
    @property
    def val(self):
        print('call getter method!')
        return self._val

    @val.setter
    def val(self,val):
        print('call setter method!')
        self._val=val

my_object = employee(3)
print('done initializing!')
print(my_object.val)
print('done printing value!')
print(dir(my_object))