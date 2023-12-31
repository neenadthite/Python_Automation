
# coding: utf-8
import xlrd
import os

#Delete footer
original_file = "Gradesheet"
temp_file = "temp"
string_to_delete = ['---------------------- Congragulations to all!! --------------------']
with open(original_file, "r") as input:
    with open(temp_file, "w") as output:
        for line in input:
            for word in string_to_delete:
                line = line.replace(word, "")
            output.write(line)

# replace file with original name
os.replace('temp', 'Gradesheet')

# Open the Workbook
filename=os.path.join("/home/ninad","grade_calculator/Marksheet.xlsx")
workbook = xlrd.open_workbook(filename)

# Open the worksheet
worksheet = workbook.sheet_by_index(0)

for i in range(1, worksheet.nrows):
       #Extract variable name
    for j in range(0, 1):
        # Print the cell values with tab space
        student_name = worksheet.cell_value(i, j)
        print(student_name)
    #Extract class
    for j in range(1, 2):
        # Print the cell values with tab space
        print(worksheet.cell_value(i, j))
        if worksheet.cell_value(i, j) > 90:
            grade = 'A';
        elif worksheet.cell_value(i, j) > 80 and worksheet.cell_value(i, j) < 90 :
            grade = 'B';
        elif worksheet.cell_value(i, j) > 60 and worksheet.cell_value(i, j) < 80:
            grade = 'C';
        elif worksheet.cell_value(i, j) > 40 and worksheet.cell_value(i, j) < 60:
            grade = 'D';
        print(grade)

    #Writing into Marksheet file

    # Opening a file
    file1 = open('Gradesheet', 'a')
    a = student_name + "\t\t\t\t"
    b = grade + "\n" 

    c = [a,b]

    # Writing multiple strings
    # at a time
    file1.writelines(c)

    # Closing file
    file1.close()

# Opening a file
file1 = open('Gradesheet', 'a')
f = "\n---------------------- Congragulations to all!! --------------------\n"

# Write single line
file1.write(f)

# Closing file
file1.close()


# Checking if the data is
# written to file or not
file1 = open('Gradesheet', 'r')
print(file1.read())
file1.close()
