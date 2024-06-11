import ctypes
class akash_ki_dyanmic_list():
    def __init__(self):
        self.size= 1 # size of array store here
        self.n= 0 # number of elements in array store here
        self.A = self.__make_array(self.size) # makes array of size self.size can be used as normal array
    
    def __len__(self):
        return self.n #helps display lengh of array
    
    def __str__(self): # funtion to print the array
        result=''
        for i in range(self.n):
            result = result + str(self.A[i]) + ","
        
        return "[" + result[:-1] + "]" # result[:-1]
    
    def __getitem__(self,__index): # helps code to get values by entering index
        if  0<= __index < self.n:
            return self.A[__index]
        else:
            return self.A[self.n+__index]
        
    def __delitem__(self,del_poistion): # del keyword funtion 
        if 0 <= del_poistion <= self.n :
            for i in range(del_poistion,self.n-1):
                self.A[i] = self.A[i+1]
            self.n-=1
        else:
            raise IndexError("index out of range")
        
    def __lt__(self): # min funtion
        try:    
            for i in self.A:
                for k in self.A:
                    if self.A[i] > self[k]:
                        i=k
            return i
        except:
            raise ValueError("Your list contains other than int values")
    
    def __lt__(self): # max funtion 
        for i in self.A:
                for k in self.A:
                    if self.A[i] < self[k]:
                        i=k
        return i
    
    def __add__(self, other): #funtion to use + as concation
        result = akash_ki_dyanmic_list()
        result.extend(self)       
        result.extend(other)      
        return result

    def __iadd__(self,given_list): # merge funtion
        for i in given_list:
            self.append(i)

    
    def __resize(self,new_size): # funtion to resize the araay once full
        B = self.__make_array(new_size)
        self.size= new_size
        
        for i in range(self.n):
            B[i]=self.A[i] 
        self.A= B
    
    def __make_array(self,g_size): # creates new c type array 
        return (g_size*ctypes.py_object)()
    
    def append(self,given_item): # funtion to append new element
        if(self.size==self.n): # cheaks if array is full
            self.__resize(self.size*2) 
        
        self.A[self.n]= given_item
        self.n+=1
        
    def pop(self): # pop funtion
        if self.n == 0:
            raise ValueError("Empty List")
        
        print("poped "+str(self.A[-1]))
        self.n -= 1

    def clear(self): # clear funtion 
        self.n=0
        self.size=1
    
    def index(self,item,start=0): # indeation method funtion + - ve indeaxtion method funtion
        for i in range(start,self.n):
            if item == self.A[i]:
                return i
        raise ValueError("item not in list")
    
    def find(self,item,start=0): # find funtion
        for i in range(start,self.n):
            if item == self.A[i]:
                return i
        return -1
    
    def insert(self,poistion,item): # insert funtion 
            if 0 <= poistion <= self.n :
        
                if(self.size==self.n): # cheaks if array is full
                    self.__resize(self.size*2)
                
                for i in range(self.n,poistion,-1): # 10 20 30 40 50 60 '60'
                    self.A[i]=self.A[i-1]
                self.n+=1
                self.A[poistion]= item
            else:
                raise IndexError("Index out of range")    
    
    
    def remove(self,item): # remove funtion
        for i,k in enumerate(self.A):
            if item == k:
                temp= i
                break
            else:
                raise ValueError("Value not found")
        for i in range(i,self.n-1):
            self.A[i] = self.A[i+1]
        self.n-=1
    
    def sort(self,reverse=False): # sort funtion
        for i in range(self.n):
            for k in range(i+1,self.n):
                if reverse==True:
                    if self.A[i] > self.A[k]:
                        temp=self.A[i]
                        self.A[i]=self.A[k]
                        self.A[k]=temp
                else:
                    if self.A[i] < self.A[k]:
                        temp=self.A[i]
                        self.A[i]=self.A[k]
                        self.A[k]=temp
            
        

    def extend(self,list_input): # extend funtion 
        for i in list_input:
            self.append(i)

# code starts here
if __name__=='__main__':
    
    obj=akash_ki_dyanmic_list()
    _string= "akash ki dyanmic list he yeh !"
    obj=[_string]
    print(obj)
    