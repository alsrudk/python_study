# https://school.programmers.co.kr/learn/courses/30/lessons/17677

from collections import Counter

def jaccard(a, b):
    if len(a)==0 and len(b)==0:
        return 65536
    a, b = Counter(a), Counter(b)
    intersection, union = a&b, a|b
    res = sum(intersection.values()) / sum(union.values())
    return int(res * 65536)

def solution(str1, str2):
    A = [str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    B = [str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]
    return jaccard(A, B)
