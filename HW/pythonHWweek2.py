# ----------Question 1---------- #

# list_num = []

# for value in range(1,1000000):
#     list_num = value**3
#     print(list_num)
#     if list_num >= 1000:
#         break
    

# --------- Question 2 -------- #

# what makes a prime number:
    # can only be divisible by 1 and itself 
    # greater than 1, smallest prime number is 2 


def is_prime(num):
    for x in range(2,num):
        if num % x == 0:
            return False
    return True


for value in range(2,100):
    if is_prime(value):
        print(value)
    else:
        continue


# ----------- QUESTION 3 --------- #

# age = input("How old are you?")
# change_type_age = int(age)


# if int(age) >= 18: 
#     print("adults")
# elif age < 18:
#     print("kids")


