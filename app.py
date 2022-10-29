
import itertools
from operator import indexOf


def find_two_sum(list,target):
    for numbers in itertools.combinations(list,2):
        if sum(numbers) == target:
            print([list.index(number) for number in numbers])

list = [1,2,3,4,5]
target = 8
def find_sums(list,target):
    for num1 in list:
        for num2 in list:
            if num1 + num2 == target:
                index1 = list.index(num1)
                index2 = list.index(num2)
                return([index1,index2])
            
print(find_sums(list,target))
