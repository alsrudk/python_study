def solution(numbers):
  answer = []
  for number in numbers:
    #짝수이면 ___0으로 끝남
    if number%2 == 0:
      answer.append(number+1)
    #홀수이면 ___1로 끝남
    else:
      bin_num = '0' + bin(number)[2:]
      bin_num = list(bin_num)
      
      idx = 0
      for i in range(len(bin_num)-1, -1, -1):
        if bin_num[i] == '0':
          idx = i
          break
      
      bin_num[idx] = '1'
      bin_num[idx+1] = '0'
      num = int(''.join(bin_num), 2)
      answer.append(num)
      
  return answer
    
