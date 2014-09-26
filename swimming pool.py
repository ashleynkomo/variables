#Ashley Nkomo
#23-09-14
#Swimming Pool Volume

width = float(input('Please insert width of pool: '))
length = float(input('Please insert length of pool: '))
depth = float(input('Please insert depth of pool: '))

mainSectionVolume = length * width * depth
circleRadius = width / 2

circleArea = 3.14 * circleRadius**2
halfCircleVolume = (circleArea / 2) * depth

poolVolume = mainSectionVolume + halfCircleVolume

print('The total volume of the pool is {0}'.format(poolVolume))
