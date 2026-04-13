# class Person:
#     def __init__(self, name):
#         self.name = name  

# class Employee(Person):
#     def __init__(self, name,salary):
#         super().__init__(name)
#         self.salary = salary
   
#     def show(self):
#         print(self.name ,self.salary)       

# a1 = Employee("Shreyas", 150_000)
# a1.show()


# class BankAccount:
#     def __init__(self, name, balance):
#         self.name = name #public
#         self.__balance = balance #private - data mangling

#     def get_balance(self):
#         return self.__balance
    
#     def set_balance(self, newbal):
#         self.__balance = newbal

# acc1 = BankAccount("Rahul Kumar", 100_000)

# acc1.set_balance(2_00_000)
# print(acc1.name, acc1._BankAccount__balance)



# import numpy as np
# import time

# size = 2

# py = list(range(size))
# start = time.time()
    

# for x in py:
#     x**2
# end = time.time()
# print(f" The timings of list is {end-start} sec..")


# npy = np.array(py)
# start = time.time()
# hh = npy ** 2
# end = time.time()
# print(f" The timings of numpy is {end-start} sec..")
