"""
    Scenario
    Imagine that you receive a task description of an application that monitors the process of apple packaging before the apples are sent to a shop.

    A shop owner has asked for 1000 apples, but the total weight limitation cannot exceed 300 units.

    Write a code that creates objects representing apples as long as both limitations are met. When any limitation is exceeded, than the packaging process is stopped, and your application should print the number of apple class objects created, and the total weight.

    Your application should keep track of two parameters:

    the number of apples processed, stored as a class variable;
    the total weight of the apples processed; stored as a class variable. Assume that each apple's weight is random, and can vary between 0.2 and 0.5 of an imaginary weight unit;
    Hint: Use a random.uniform(lower, upper) function to create a random number between the lower and upper float values.

"""
import random

class ApplePackaging:
    total_apples = 0
    total_weight = 0
    
    def __init__(self):
        pass
        
    def add_apple(self):
        if(ApplePackaging.total_apples >= 1000 or ApplePackaging.total_weight >= 300):
            print(f"Total Apple packaged are {ApplePackaging.total_apples}, and the total weight is: {ApplePackaging.total_weight}")
            return False
            
        weight = random.uniform(0.2, 0.5)
        ApplePackaging.total_weight += weight
        ApplePackaging.total_apples += 1
        return True
    # Decorator used when we want to specify that the method belong to the class
    @classmethod
    def print_result(cls):
        print(f"Total apples packaged: {cls.total_apples}")
        print(f"Total weight of apples: {cls.total_weight:.2f}")
        
def run_packaging():
    packaging = ApplePackaging()
    
    while packaging.add_apple():
        pass
    ApplePackaging.print_result()
run_packaging()