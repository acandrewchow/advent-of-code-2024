# day 1 part 1
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
    total_distance = 0

    list1.sort()
    list2.sort()

    for i in range(len(list1)):
        result = abs(list1[i] - list2[i])

        total_distance += result

    return total_distance


list1, list2 = read_file()

total_distance = solution(list1, list2)

print("Total Distance:", total_distance)