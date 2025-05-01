#Luke Aaron T. Velasquez
#Grade 12 Neird

import random

class SearchAlgorithm:
    def __init__(self):
        self.target_number = random.randint(1, 10) #Generating the target number
        self.number_list = [] #Making an empty array for the nun=mber lists
    
    def generate_number_list(self):
        for x in range(10): #loop for generating random numbers
            self.random = random.randint(1, 10) #Generating a random number
            self.number_list.append(self.random) #Putting the generated number in the array

    def bubbleSort(self):
        for passnum in range(len(self.number_list)-1,0,-1): 
            for i in range(passnum):
                if self.number_list[i] > self.number_list[i+1]:
                    self.number_list[i], self.number_list[i+1] = self.number_list[i+1], self.number_list[i] #replacing the lower number to the left and the higher number to the right
        return self.number_list #Return the number list
    
    def sequential_search(self, target):
        #Perform sequential search
        iterations = 0
        for index, number in enumerate(self.number_list):
            iterations += 1
            if number == target:
                return index, iterations
        return -1, iterations
    
    def binary_search(self, target):
        #Perform binary search
        left, right = 0, len(self.number_list) - 1
        iterations = 0
        while left <= right:
            iterations += 1
            
            #Finding the midpoint
            mid = (left + right) // 2
            
            #Finding the target number by dividing the list
            if self.number_list[mid] == target:
                return mid, iterations
            elif self.number_list[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1, iterations
    
    def ternary_search(self, target):
        left, right = 0, len(self.number_list) - 1
        iterations = 0
        while left <= right:
            iterations += 1
            
            #Finding the midpoint
            first_midpoint = left + (right - left) // 3
            second_midpoint = right - (right - left) // 3
            
            #Find the target number by finding in different midpoints
            if self.number_list[first_midpoint] == target:
                return first_midpoint, iterations
            elif self.number_list[second_midpoint] == target:
                return second_midpoint, iterations
            elif target < self.number_list[first_midpoint]:
                right = first_midpoint - 1
            elif target > self.number_list[second_midpoint]:
                left = second_midpoint + 1
            else:
                left = first_midpoint + 1
                right = second_midpoint - 1
        return -1, iterations
    
    def main(self):
        #Print the target number
        print(f"The target number is: {self.target_number}")
        
        #Print the generated list
        self.generate_number_list()
        print(f"Generated list of numbers (sorted using bubbleSort): \n{self.bubbleSort()}")
        
        #Perform sequential search
        seq_index, seq_iterations = self.sequential_search(self.target_number)
        if seq_index != -1:
            print(f"Sequential Search: Number {self.target_number} found at index {seq_index} in {seq_iterations} iterations.")
        else:
            print(f"Sequential Search: Number {self.target_number} not found after {seq_iterations} iterations.")
        
        #Perform binary search
        bin_index, bin_iterations = self.binary_search(self.target_number)
        if bin_index != -1:
            print(f"Binary Search: Number {self.target_number} found at index {bin_index} in {bin_iterations} iterations.")
        else:
            print(f"Binary Search: Number {self.target_number} not found after {bin_iterations} iterations.")
            
        #Perform ternary search
        ter_index, ter_iterations = self.ternary_search(self.target_number)
        if ter_index != -1:
            print(f"Ternary Search: Number {self.target_number} found at index {ter_index} in {ter_iterations} iterations.")
        else:
            print(f"Ternary Search: Number {self.target_number} not found after {ter_iterations} iterations.")

if __name__ == "__main__":
    search = SearchAlgorithm()
    search.main()
