a = set(map(int, input("enter set 1 with comma").split(",")))
b=set(map(int,input("enter set 2 with comma").split(",")))

union=a|b
diff=a-b
symmetricdiff=a^b

print(f"union is - {union}\ndifferance of a-b is - {diff}\nsymmetric differance of 2 sets is - {symmetricdiff}")