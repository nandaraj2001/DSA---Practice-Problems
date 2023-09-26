"""
Design a Dynamic Array (aka a resizable array) class, such as an ArrayList in Java or a vector in C++.

Your DynamicArray class should support the following operations:

a)DynamicArray(int capacity) will initialize an empty array with a capacity of capacity, where capacity > 0.
b)int get(int i) will return the element at index i. Assume that index i is valid.
c)void insert(int i, int n) will insert the element n at index i. Assume that index i is valid.
d)void pushback(int n) will push the element n to the end of the array.
e)int popback() will pop and return the element at the end of the array. Assume that the array is non-empty.
f)void resize() will double the capacity of the array.
g)int getSize() will return the number of elements in the array.
h)int getCapacity() will return the capacity of the array.
i)If we call void pushback(int n) but the array is full, we should resize the array first.

"""

class DynamicArray:
    def __init__(self,capacity:int):
        self.capacity=capacity   
        self.length=0
        self.arr=[0]*capacity    #initialize the array

    def get(self,i:int)->int:
        return self.arr[i]
    
    def insert(self,i:int,n:int)->None:
        self.arr[i]=n

    def pushback(self,n:int)->None:
        if self.length==self.capacity:
            self.resize()
        self.arr[self.length]=n
        self.length+=1

    def popback(self)->int:
        #soft delete
        if self.length>0:
            self.length-=1
        return self.arr[self.length]
    
    def resize(self)->None:
        self.capacity*=2
        new_arr=[0]*self.capacity

        for i in range(self.length):
            new_arr[i]=self.arr[i]
        self.arr=new_arr


    def getSize(self)->int:
        return self.length
    
    def getCapacity(self)->int:
        return self.capacity

    
