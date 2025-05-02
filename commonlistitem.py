#Given two lists of integers, list1 and list2, write a Python function called common_elements that returns a new list containing only the elements that are present in both input lists.

ls1 = [2,4,6,8,9]
ls2 = [8,1,2,5,7,6]
print(f"List 1 : {ls1} \nList 2 : {ls2}")

def common_list_item(ls1, ls2):
    ls=[]
    for i in ls1:
        if i in ls2:
            ls.append(i)
    return ls

lst = common_list_item(ls1, ls2)
print(f"Here is the list of the common elements : {lst}")