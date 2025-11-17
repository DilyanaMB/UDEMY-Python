import random
import my_module

random_int = random.randint(1, 10)
print(random_int)

print(my_module.my_favourite_number)


random_num_0_to_1 = random.random()
print(random_num_0_to_1)

# to expand to one number before the decimal, multiply by 10, 2 signs before the decimal -multiply by 100 etc

random_num_0_to_1 = random.random() * 10
print(random_num_0_to_1)

random_float = random.uniform(1, 10)
print(random_float)