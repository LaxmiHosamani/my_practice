# matrix_size=int(input("Enter the Size of Array"))
# matrix1=[]
# print("enter the values in ann Array:")
# for i in range(matrix_size):
#     matrix1.append(int(input()))
# print ("matrix1", matrix1)

# odd=[]
# even=[]
# for i in range(matrix1):
#     if (i%2==0):
#         even.append(i)
#         print(even)
#     else:
#         odd.append(i)
#         print(odd)
matrix_size = int(input("Enter the Size of Array: "))
matrix1 = []
print("Enter the values in the Array:")
for i in range(matrix_size):
    matrix1.append(int(input()))
print("Matrix1:", matrix1)

odd = []
even = []

for index, num in enumerate(matrix1):
    if index % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Even-indexed numbers:", even)
print("Odd-indexed numbers:", odd)
