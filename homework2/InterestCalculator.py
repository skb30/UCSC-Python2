# homework 2.1 - Scott Barth
class InterestCalculator():
    # initialize the instance vars
    def __init__(self, years, rate, principle):
        self.years = years
        self.rate = rate
        self.principle = principle
        self.finalval  = 0.0

class CICalculator(InterestCalculator):
     # calculate compound interest
    def calcfinalval(self):
        cinterest = [(1+self.rate)**i for i in range(1, self.years+1)]

        self.finalval = '{:.2f}'.format(cinterest[self.years-1] * self.principle)


class SICalculator(InterestCalculator):

    # calculate simple interest
    def calcfinalval(self):
        self.finalval = '{:.2f}'.format((1 + self.rate * self.years) * self.principle)


class Sclass():
    def __init__(self):
        self.mylist = [4,6,9]

    # private method used for printing list contents
    def __printList(self, element, add=True ):
        if add:
            print("Printing contents of list after adding item {}".format(element))
        else:
            print("Printing contents of list after removing item {}.".format(element))

        for item in self.mylist:
            print(item)

    # add an element to the list
    def sadd(self, element):
        self.mylist.append(element)
        self.__printList(element)
    # pop an element off
    def sretreive(self):
        element = self.mylist.pop()
        self.__printList(element, add=False)
        return element


# homework 2.1
c = CICalculator(2,0.1,5000)
c.calcfinalval()
print(c.finalval)


s = SICalculator(2,0.1,5000)
s.calcfinalval()
print(s.finalval)

# homework 2.2
l = Sclass()
l.sadd(12)
# l.sretreive()


for i in range(len(l.mylist)):
    l.sretreive()

# if we made it here then the list will be empty
# probably should check though

if len(l.mylist) == 0:
    print("The list is empty")

exit()




