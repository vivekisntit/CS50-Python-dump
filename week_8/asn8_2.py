# class Jar:
#     def __init__(ck, capacity=12):
#         # if capacity<0:
#         #     raise ValueError
#         ck._capacity=capacity
#         ck._size=0

#     def __str__(ck):
#         # for _ in range(ck.n):
#         #     print("🍪",end="")
#         return "🍪"*ck.size

#     def deposit(ck, n):
#         if n>ck.capacity:
#             raise ValueError
#         ck._size+=n

#     def withdraw(ck, n):
#         if n>ck.size:
#             raise ValueError
#         ck._size-=n

#     @property
#     def capacity(ck):
#         return ck._capacity
    
#     # @capacity.setter
#     # def capacity(ck,cap):
#     #     if(cap<0):
#     #         raise ValueError
#     #     ck._capacity=cap

#     @property
#     def size(ck):
#         return ck._size
    
#     # @size.setter
#     # def size(ck,bag):
#     #     ck._size=bag


# box=Jar()
# print(box)
# # box.deposit(17)
# # print(box)
# # box.withdraw(10)
# # print(box)

class Jar:
    def __init__(ck, capacity=12):
        if capacity<0:
            raise ValueError
        ck._capacity=capacity
        ck._size=0

    def __str__(ck):
        return "🍪"*ck.size

    def deposit(ck, n):
        if n>ck.capacity:
            raise ValueError
        ck._size+=n

    def withdraw(ck, n):
        if n>ck.size:
            raise ValueError
        ck._size-=n

    @property
    def capacity(ck):
        return ck._capacity

    @property
    def size(ck):
        return ck._size

box=Jar()
print(box)
