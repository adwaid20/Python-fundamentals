# # from abc import ABC, abstractmethod

# # class Shape(ABC):
# #     @abstractmethod
# #     def area(self):
# #         pass

# #     @abstractmethod
# #     def perimeter(self):
# #         pass

# # class Circle(Shape):
# #     def __init__(self, radius):
# #         self.radius = radius
    
# #     def area(self):
# #         return 3.14 * self.radius ** 2
    
# #     def perimeter(self):
# #         return 2 * 3.14 * self.radius

# # class Rectangle(Shape):
# #     def __init__(self, width, height):
# #         self.width = width
# #         self.height = height
    
# #     def area(self):
# #         return self.width * self.height
    
# #     def perimeter(self):
# #         return 2 * (self.width + self.height)

# # shapes = [Circle(5), Rectangle(4, 6)]
# # for s in shapes:
# #     print(f"Area: {s.area()}, Perimeter: {s.perimeter()}")

# # def demo_args(**husna):
# #     print(husna)

# # demo_args(nam="husna",age= 21)
# # # Output: (1, 2, 3, 'hi')
# class Team:
#     def __init__(self, members):
#         self.members = list(members)

#     def __len__(self):
# #         return len(self.members)

# # team = Team(["Alice", "Bob", "Carol"])
# # print(len(team))  # 3
# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         n=len(nums)
#         for i in range(n):
#             for j in range(1,n+1):
#                 if nums[i]+nums[j]==9:
#                     return print(i,j)
# a=Solution()
# a.twoSum([2,7,11,15],9)
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        l1=l1[::-1]
        l2=l2[::-1]
        a=int("".join(map(str,l1)))
        b=int("".join(map(str,l2)))
        c=a+b
        c=str(c)
        l3=list(c)
        return l3
x=Solution()
print(x.addTwoNumbers([2,1,3],[6,5,4]))