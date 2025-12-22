student_dict = {
    "student": ["Deya", "Bill", "Tom", "Victor", "Johan", 'Charles'],
    "score": [100, 56, 40, 76, 90, 100]
}

# Looping through dictionaries:
# for key, value in student_dict.items():
#     print(key, value)

import pandas

pandas_df = pandas.DataFrame(student_dict)

# Looping through a data frame

# for key, value in student_dict.items():
#     print(value)

# Loop through each row of a data frame
for index, row in pandas_df.iterrows():
    print(row)
    if row.student == "Deya":
        print(row.score)
