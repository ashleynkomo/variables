#Ashley Nkomo
#18-09-2014
#Currency Exercise

money = int(input("Please enter your amount of money "))

twenties = money // 20
remainder1 = money % 20

tens = remainder1 // 10
remainder1 = remainder1 % 10

fives = remainder1 // 5
remainder1 = remainder1 % 5

twos = remainder1 // 2
remainder1 = remainder1 % 2

ones = remainder1 // 1
remainder1 = remainder1 % 1

print("Number of £20 notes is {0}. Number of £10 notes is {1}. Number of £5 notes is {2}. Number of £2 coins is {3}. Number of £1 coins is {4}.".format(twenties, tens, fives, twos, ones))


