height = float(input('Type your height: '))
weight = int(input('Type your weight: '))

if height > 3:
    raise ValueError('Human Heights should not be over 3 meters!')

bmi = weight / (height ** 2)
print(bmi)
