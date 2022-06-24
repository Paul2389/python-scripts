#! Cross platform path
# home_path = os.path.expandser('~')
# windows ('\\Downloads')

# folder = os.path.abspath('.') # find the absolute path
# print(folder)
# print(os.path.basename(folder)) # find the base folder

#! Zip backp
# zipfilename = os.path.basename(folder) +'.zip'
# backupzip = zipfile.ZipFile(zipfilename,'w')

# for foldername, subfolders, filenames in os.walk(folder):
#     backupzip.write(foldername)
#     for filename in filenames:
#         backupzip.write(os.path.join(foldername, filename))

#! Print f strings
# print(f'{} text {}') #{} means variable

#! defining function
# def thisName(name, age):
#     name = name
#     age = age
#     print(name, age)
# thisName('paul', 'twelve')

# def printer(number):
#     print('text', number, 'text')
  
# def message(message, number):
#     print(f'{message} {number} $')
# message('this is the message', round(number_int, 2))

#!ACCESS 2D LIST
# def check():
#     with open ('tracker.csv', 'r' , newline='') as file:
#         reader = csv.reader(file, delimiter = ',')
#         lines = list(reader)
#         for x in enumerate(lines):
            
#             if lines[x[0]][2] == current_date.strftime("%B"):
#                 print('same month')
            
#             year = int(lines[x[0]][3])
#             if year == current_date.year:
#                 print('same year')
#! round by the closest to 3.8
# round(3.75, 1)

#! prints index location of compsci
# courses.index('CompSci')

#! extend for adding to the list new items
# courses.extend(courses2)

#! Memory location of item
# id(a)
