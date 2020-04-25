# put your python code here
duration = int(input())
food = int(input())
flight = int(input())
hotel = int(input())
total_cost = flight * 2 + food * duration + hotel * (duration - 1)
print(total_cost)
