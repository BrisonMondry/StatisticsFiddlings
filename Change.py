"""This file does a simulaiton of what kind of change I might have in my jar at the moment"""
import random

nums = []


def run_sim(trials):
    piggyBank = [0, 0, 0, 0]
    for i in range(0,trials):
        cents = random.randint(0,99)
        newCoins = coin_count(cents)
        for i in range(0, len(piggyBank)):
            piggyBank[i] += newCoins[i]

    return piggyBank


def stats(arr):
    total = 0
    for i in arr:
        total += i
    percents = []
    for i in range(0, len(arr)):
        percents.append(percent(arr[i], total))
    return percents


def percent(val, total):
    return "{:5.2f}".format((float(val)/float(total)*100)) + "%"


def coin_count(num):
    nums.append(num)
    quarters = int(num/25)
    num = num - quarters*25
    dimes = int(num/10)
    num = num - dimes*10
    nickles = int(num/5)
    num = num - nickles*5
    return [quarters, dimes, nickles, num]


def get_avg():
    total = 0
    for i in nums:
        total += i
    return total/len(nums)


bank = run_sim(10000)
print("avg of", get_avg())
print(['quarters', 'dimes', 'nickles', 'pennies'])
print(stats(bank))
print(bank)


"""end"""
