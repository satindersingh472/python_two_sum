
import itertools


def find_two_sum(list,target):
    for numbers in itertools.combinations(list,2):
        if sum(numbers) == target:
            print([list.index(number) for number in numbers])


def find_sums(list,target):
    for num1 in list:
        for num2 in list:
            if num1 + num2 == target:
                index1 = list.index(num1)
                index2 = list.index(num2)
                return([index1,index2])
            
def find(list,target):
    num1 = list[0]
    num2 = list[0]
    for x in list:
        if x + num2 == target:
            index1 = list.index(num2)
            index2 = list.index(x)
            return [index1,index2]
        elif x + num1 == target:
            index1 = list.index(num1)
            index2 = list.index(x)
            return [index1,index2]
        elif num1 + num2 == target:
            index1 = list.index(num1)
            index2 = list.index(num2)
            return [index1,index2]
        else:
            num1 = num2
            num2 = x
        
def find_dict(list,target):
    i = 0 
    seen_nums = {}
    while(i < len(list)):
        seen_nums[list[i]] = i
        if(seen_nums.get(target - list[i]) != None):
            return [seen_nums.get(target - list[i]), i]
        i += 1

list = [2,5,4,3,1]
target = 8

find_dict(list,target)
