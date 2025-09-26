#an empty list
my_list=[]
my_list +=[10,40,30,90]


#append 15 at position two
my_list.insert(1,15)
extending_list=[50,60,70]

#extend the list further
my_list.extend(extending_list)
#removing the last element
my_list.pop()
my_list.sort()
my_list.index(30)

try:
    index=my_list.index(30)
    print(f"The element '{30}' is found at index {index}" )

except ValueError:
    print(f"The element'{30}' is not found in the list")