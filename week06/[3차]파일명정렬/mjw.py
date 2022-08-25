# https://school.programmers.co.kr/learn/courses/30/lessons/17686

def split_filename(file_):
    head, number = '', ''
    i = 0
    while (i < len(file_)) and (file_[i] not in '0123456789'):
        head += file_[i].lower()
        i += 1
    while (i < len(file_)) and (len(number) < 5) and (file_[i] in '0123456789'):
        number += file_[i]
        i += 1
    return head, int(number)

def solution(files):
    files_splited = [split_filename(file_) for file_ in files]
    sorted_idx = sorted(range(len(files)), key=lambda i: (files_splited[i][0], files_splited[i][1]))
    return [files[i] for i in sorted_idx]
