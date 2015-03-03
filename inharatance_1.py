__author__ = 'Agnieszka'

# class BaseClass(object):
#     def printHam(self):
#         print 'Ham'
# class InheritingClass(BaseClass):
#     pass
#
# x = InheritingClass()
# x.printHam()

class Character(object):
    def __init__(self, name):
        self.health = 100
        self.name = name
    def printName(self):
        print self.name

class Blacksmith (Character):
    def __init__(self, name, forgeName):
        #  we call here super function SUPER
        super(Blacksmith, self).__init__(name)
        self.forge = Forge(forgeName)
class Forge:
    def __init__(self, forgeName):
        self.name = forgeName

bs = Blacksmith("Bob","Rick")
print bs.health
bs.printName()
print bs.forge.name



# UML (Unified Modeling Language)
