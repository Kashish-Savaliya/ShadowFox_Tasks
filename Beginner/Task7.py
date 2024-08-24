# Program 1
file_path = 'C:\\Users\\abc\\OneDrive\\Desktop\\ShadowFox\\task7.csv'

with open(file_path, mode='r') as file:
    content = file.read()

lines = content.splitlines()

header = lines[0].split(',')   #First Line

list_of_dicts = []
for line in lines[1:]:
    dict = {}
    row = line.split(',')
    for i in range(len(header)):
        dict[header[i]] = row[i]
    list_of_dicts.append(dict)

for ele in list_of_dicts:
    total_marks = int(ele['Science_marks']) + int(ele['Maths_marks']) + int(ele['English_marks'])
    average_marks = total_marks/3
    ele['total_marks'] = total_marks
    ele['average_marks'] = int(average_marks)

for ele in list_of_dicts:
    print(ele)

# Program 2
file2_path = file_path = 'C:\\Users\\abc\\OneDrive\\Desktop\\ShadowFox\\task7_modified.csv'
header.append('total_marks')
header.append('average_marks')

with open(file2_path, mode='w') as file:
    file.write(','.join(header)+'\n')

    for ele in list_of_dicts:
        row = [str(ele[col]) for col in header]
        file.write(','.join(row)+'\n')
