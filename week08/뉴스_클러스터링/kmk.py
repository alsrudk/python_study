def solution(str1, str2):
    answer = 0
    str1 = str1.upper()
    str2 = str2.upper()
    str1_list,str2_list = [], []
    
    for i in range(len(str1)-1):
        element = str1[i:i+2]
        if element.isalpha():
            str1_list.append(element)
            
    for i in range(len(str2)-1):
        element = str2[i:i+2]
        if element.isalpha():
            str2_list.append(element)
            
    str1_list1 = str1_list.copy()
    union = str1_list.copy()
    for e in str2_list:
        if e not in str1_list1:
            union.append(e)
        else:
            str1_list1.remove(e)
    
    inter = []
    str1_list1 = str1_list.copy()
    for e in str2_list:
        if e in str1_list1:
            str1_list1.remove(e)
            inter.append(e)
            
    if not union and not inter:
        return 65536
    else:
        return int((len(inter)/len(union))*65536)
