nums = [n for n in range(1,1000001)]
print(min(nums))
print(max(nums))
print(sum(nums))

numbers = list(range(1, 21, 2))
print(numbers)

numthird = list(range(3, 30, 3))
print(numthird)

cubes = []
for n in range(1,11):
    cube = n ** 3
    cubes.append(cube)
print(cubes)

cubers = [i ** 3 for i in range(1,11)]
print(cubers)