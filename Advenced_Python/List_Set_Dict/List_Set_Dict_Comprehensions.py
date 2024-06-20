numbers = [1,2,3,4,5,6,7,1,3,9]
even = []

# for i in numbers:
#     if i%2 ==0:
#         even.append(i)

even = [i for i in numbers if i%2 == 0]
sq = [i*i for i in numbers]
print(even)
print(sq)

s = set([1,2,3,4,5,2,3])
print(s)
even = {i for i in numbers if i not in even}
print(even)