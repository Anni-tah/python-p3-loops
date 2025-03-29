#!/usr/bin/env python3
def happy_new_year():
    i=10
    while (i>0):
        print(i)
        i-=1
    print("Happy New Year!")
happy_new_year()

def square_integers(int_list):
    int_list=[int * int for int in int_list ]
    print(int_list)
square_integers([1, 2, 3, 4, 5])

def fizzbuzz():
    i=1
    while(i<100):
        if(i%3==0) and (i%5==0):
            print("FizzBuzz")
        elif(i%5==0):
            print("Buzz")
        elif(i%3==0):
            print("Fizz")
        else:
            print(i)
        i+=1
fizzbuzz()
#while loop
# i=0
# while (i<5):
#     print(f"Looping {i}")
#     i+=1

# for j in range(10):
#     print("looping")
#     print(f"j is {j}")

# player_heights = [0.008, 0.008, 0.008, 0.009, 0.008, 0.01, 0.009, 0.009, 0.01, 0.008, 0.009, 0.009, 0.008, 0.008, 0.008, 0.009, 0.008, 0.009, 0.01, 0.01]
# # inch_heights=list()
# # for heights in player_heights:
# #     inch_height=heights * 7920
# #     inch_heights.append(inch_height)
# #     print(inch_heights)
    
# player_heights=[height * 7920 for height in player_heights]
# print(player_heights)