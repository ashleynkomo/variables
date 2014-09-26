#Ashley Nkomo
#23-09-14
#Balancing weights

weight = int(input('Please input the number of weights: '))

hundreds = weight // 100
remainder = weight % 100

fifties = remainder // 50
remainder = remainder % 50

tens = remainder // 10
remainder = remainder % 10

fives = remainder // 5
remainder = remainder % 5

twos = remainder // 2
remainder = remainder % 2

ones = remainder // 1
remainder = remainder % 1

print('To equal your weights you need {0} 100g, {1} 50g, {2} 10g, {3} 5g, {4} 2g, {5} 1g'.format(hundreds, fifties, tens, fives, twos, ones))

