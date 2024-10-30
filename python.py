# Task - Maths with dictionary elements

dict1 = {   'a': 4,   'b': 16,   'c': 3 }  
dict2 = {   'a': 8,   'b': 2,   'c': 3 }
result = sum(dict1[key] * dict2[key] 
             for key in dict1)
print(result) 

# Task - Convert keys between cases


def convert_to_snake_case(natural_case):  
    snake_case = {}  
    
    for key, value in natural_case.items():   
        snake_key = key.lower().replace()   
        snake_case[snake_key] = value     
        return snake_case 
     
    
## Task - Matrix mean

import statistics 

def mean(numbers):  
    return [statistics.mean(row) for row in numbers] 
numbers = [[5, 6, 3], [8, 3, 1], [9, 10, 4], [8, 4, 2]] 
result = mean(numbers)
print(result) 

## Task - Combine lists into a dict

color_names = ['red', 'green', 'blue'] 
color_hex = ['#FF0000','#00FF00', '#0000FF'] 
colors = {name: hex_value for name, hex_value in zip(color_names, color_hex)} 
print(colors) 


## Task - Highscore

participants = ['Brian', 'Britney', 'Ben'] 
scores = {   'brian': 25,   'britney': 80,   'ben': 50 } 
def get_score(name):  
    score = scores.get(name.lower()) 
    if score is None:         
        print(f"{name} did not participate") 
    else:        
        print(f"{name} scored {score} points") 
        get_score('Paul') 
        get_score('Britney') 


## Task - Count characters

from collections import Counter  
def count_characters(string):
    return dict(Counter(string))  
string = 'Elephant'
result = count_characters(string) 
print(result) 

