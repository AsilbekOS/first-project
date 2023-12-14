import math
'''->->-> 1 - masala <-<-<-'''
# file = open("products.txt", 'w')
# strs = '''Product Name,Price,Discount,Created At,Category
# Laptop,1200,100,2023-01-15,Electronics
# Headphones,150,20,2023-02-20,Electronics
# T-shirt,25,5,2023-03-10,Clothing
# Smartphone,800,50,2023-04-05,Electronics
# Book,30,2,2023-05-12,Books'''
# file.write(strs)
# file.close()

'''->->-> 2 - masala <-<-<-'''
# satr = input("Matn kiriting: ")
# 'Hp,700,100,2021-11-21,Electronic'
# file = open('products.txt', 'a')
# file.write('\n')
# file.write(satr)
# file = open("products.txt", 'r')
# data = file.read().split("\n")
# for i in data:
#     print(i)
# file.close()


'''ikkilikdan o'nlikka o'tish'''
# son = int(input("Ikkilik sonni kiriting: "))
# son = str(son)
# son_ = [int(i) for i in son]
# son_ = son_[::-1]
# sum = 0
# for i in range(len(son_)):
#     sum += son_[i] * pow(2, i)
# print(sum)

'''o'nlikdan ikkilikka o'tish'''
# son = int(input('Son kiriting: '))
# sonlar = []
# while son != 0:
#     sonlar.append(son%2)
#     son = son//2
# sonlar = sonlar[::-1]
# print(sonlar)

# ikkita binary sonlarni decimialga aylantirib bir biriga qo'shib binaryga qaytarish
# son1 = '11'
# son2 = '1'
# son1 = [int(i) for i in son1]
# son2 = [int(i) for i in son2]
# son1 = son1[::-1]
# son2 = son2[::-1]
# sum1 = 0
# sum2 = 0
# for i in range(len(son1)):
#     sum1 += son1[i] * pow(2, i)
# for i in range(len(son2)):
#     sum2 += son2[i] * pow(2, i)
# sum = sum1 + sum2
# sonlar = []
# while sum != 0:
#     sonlar.append(sum%2)
#     sum = sum//2
# sonlar = sonlar[::-1]
# son = "".join(map(str, sonlar))
# print(son)


'''16 likdan 10 likka o'tkazish'''
shaxs = input("HEXA kiriting: ").upper()
son = {'A': 10, 'B':11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
l = len(shaxs)-1
decimal = 0
for i in range(len(shaxs)):
    if 'A' <= shaxs[i] <= 'F':
        decimal += (son[shaxs[i]] * pow(16,l-i))
    elif '0' <= shaxs[i] <= '9':
        decimal += int(shaxs[i]) * pow(16, l-i)
print(decimal)



