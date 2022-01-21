import random

########################################################################

def logRand(power, decimals,ran):
    sum = 0
    for x in range(power+1):
        sum += random.uniform(ran[0]-ran[1], ran[1])
    return round(abs(sum/(power+1)),decimals)

########################################################################

def tryMethod(power,tries):
    nums = {"0-1":0, "1-2":0, "2-3":0, "3-4":0, "4-5":0, "5-6":0, "6-7":0, "7-8":0, "8-9":0, "9-10":0}
    numbers = [0,0,0,0,0,0,0,0,0,0]
    for x in range(tries):
        rnum = logRand(power,10,[0,10])
        for y in range(0,10):
            if rnum < (y+1):
                numbers[y] += 1
                break
    for i,x in enumerate(numbers):
        nums[str(i)+"-"+str(i+1)] = str(100*x/tries) + "%"
    return nums

#print(tryMethod(3,100000000))

########################################################################

'''

If you generate a number from 0 to 10, there will be a X chance of it being between 9 and 10:
Power 0 -> X ≈ 10%
Power 1 -> X ≈ 1%
Power 2 -> X ≈ 0.112734%
Power 3 -> X ≈ 0.013167%
Power 4 ...
...

Decimals -> Decimals of the generated number

ran -> Range of the random number ( e.g. [0,10] )

'''