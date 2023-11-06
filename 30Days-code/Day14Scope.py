class Difference:
    def __init__(self, a):
        self.__elements = a

	# Add your code here
    def computeDifference(self):
        dif = 0
        for i in self.__elements:
            for j in self.__elements:
                new_dif = i -j
                if new_dif>dif:
                    dif=new_dif
        self.maximumDifference=dif


# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)