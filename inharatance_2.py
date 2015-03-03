__author__ = 'Agnieszka'
class BaseClass(object):
    def __init__(self):
        self.x=10

class InClass(BaseClass):
    def __init__(self):
        super(InClass, self).__init__()
        # if we need we can overwrite variable from BaseClass
        self.x = 20
i = InClass()
print i.x

# we can overwrite function
# we should separate BaseClasses into separate files