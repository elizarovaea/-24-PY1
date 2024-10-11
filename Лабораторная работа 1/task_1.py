numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

new_list = [0 if x is None else x for x in numbers]
average = sum(new_list)/len(new_list)
final = [average if x is None else x for x in numbers]

print("Измененный список:", final)
