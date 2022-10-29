
import itertools


def find_two_sum(list,target):
    for numbers in itertools.combinations(list,2):
        if sum(numbers) == target:
            print([list.index(number) for number in numbers])

list = [1,2,3,4,5]
target = 8
find_two_sum(list,target)



