def solution(m, musicinfos):
  answer = []        #[이름, 재생시간, 인덱스]
  hour, min = 0, 0   #시간, 분
  length = 0         #악보 길이
  name = dict()      #{악보:이름} 딕셔너리 생성
  music = []         #[전체악보, 재생시간]
  
  # '#'붙은 악보 소문자로 바꿔주기
  repl = {"C#": 'c', 'D#': 'd', "F#": 'f', "G#": 'g',"A#": 'a'}
  for c in repl.keys():
    m = m.replace(c, repl[c])
  
  for info in musicinfos:
    info = info.split(',')  #시작시간 info[0], 끝난시간 info[1], 음악제목 info[2], 악보정보 info[3]
    change = info[3]
    for c in repl.keys():
      change = change.replace(c, repl[c])
      
    hour = int(info[1][:2]) - int(info[0][:2])
    if int(info[1][3:5]) < int(info[0][3:5]):
      min = (60-int(info[0][3:5])) + int(info[1][3:5])
      hour -= 1
    else:
      min = int(info[1][3:5]) < int(info[0][3:5])
      
    length = len(change)
    total = (hour*60)+min  #재생시간 
    song = change*(int(total//length)) + change[:int(total%length)]
    music.append([song, total])
    name[song] = info[2]
  
  for i in range(len(music)):
    if m in music[i][0]:
      answer.append([name[music[i][0]], music[i][1], i])
  
  if not answer:
    return '(None)'
  elif len(answer) == 1:
    return answer[0][0]
  else:
    answer.sort(key=lambda x:(-x[1], x[2]))   #재생시간 긴 순, 재생시간 같다면 먼저 입력된 제목순
    return answer[0][0]
    
  
    
    
