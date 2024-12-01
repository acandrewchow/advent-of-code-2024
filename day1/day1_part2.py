# day 1 part 2
def read_file():

    with open("data.txt", "r") as file:
        list1 = []
        list2 = []
        
        for line in file:
            num1, num2 = map(int, line.split())

            list1.append(num1)
            list2.append(num2)

    return list1, list2

def solution(list1, list2):
    total_similarity = 0  

    list2_freq = {}
    for num in list2:
        if num in list2_freq:
            list2_freq[num] += 1
        else:
            list2_freq[num] = 1

    for i, num in enumerate(list1):
        if num in list2_freq: 
            similarity = list2_freq[num] * num
            total_similarity += similarity


    return total_similarity


list1, list2 = read_file()

total_similarity = solution(list1, list2)

print("Total Similarity:", total_similarity)