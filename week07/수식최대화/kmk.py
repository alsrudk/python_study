def solution(expression):
  answer = []
  oper = [('+','-','*'),('+','*','-'),('-','+','*'),('-','*','+'),('*','+','-'),('*','-','+')]

  for op in oper:
    a = op[0]
    b = op[1]
    temp = []
    print('a',a,'b',b)
    for e in expression.split(a):
      print('e',e)
      temp_split = [f"({i})" for i in e.split(b)]
      print('temp_split',temp_split)
      temp.append(f'({b.join(temp_split)})')
      print('temp', f'({b.join(temp_split)})')
  
    print('answer', a.join(temp))
    answer.append(abs(eval(a.join(temp))))
    
    
  
  return max(answer)
