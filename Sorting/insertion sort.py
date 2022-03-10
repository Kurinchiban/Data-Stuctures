#Creating the function for the insertion sort 
def insertionsort(list):
    #Itrating the value for front order(1,2,3,4,5)
    for i in range(1,len(list)):
        temp=list[i]
        # Assigning the befor index of i to the j
        j=i-1
        # Comparing the last value with the currentvalue and adding the special condition 
        while temp < list[j] and j>-1:
            list[j+1]=list[j]
            list[j]=temp
            j-=1
    return list 

#Calling the function 
print(insertionsort([3,5,6,4,2,1]))



class Coordinate:
    """ A coordinate made up of an x and y value """
    def __init__(self, x, y):
        """ Sets the x and y values """
        self.x = x
        self.y = y
    def __str__(self):
        """ Returns a string representation of self """
        return "<" + str(self.x) + "," + str(self.y) + ">"
    def distance(self, other):
        """ Returns the euclidean distance between two points """
        x_diff_sq = (self.x-other.x)**2
        y_diff_sq = (self.y-other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5

c = Coordinate(3,4)
origin = Coordinate(0,0)
print(c.x, origin.x)
print(c.distance(origin))
print(Coordinate.distance(c, origin))
print(origin.distance(c))
print(c)


class Fraction:
    def __init__(self,num,deno):
        self.num=num
        self.deno=deno 
    def __str__(self):
        return "The fraction is : " + str(self.num) + "/" + str(self.deno) 
    def add(self,other):
        addvalue=(self.num*other.deno)+(self.deno*other.num)
        final_value=(self.deno*other.deno)
        return Fraction (addvalue,final_value)

new_fraction=Fraction(3,5)
clone_fraction=Fraction (2,4)
print(new_fraction.add(clone_fraction)) 