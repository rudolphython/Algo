'''
출저 : 프로그래머스
문제 : 단어 변환
풀이 방법 : BFS / 한 글자 차이 나는 것들은 stack에 넣는 것을 반복 -> 반복 후 target과 같다면 반환
'''

def solution(begin, target, words):
    answer = 0
    # stack에 처음 단어와 횟수 추가
    stack = [(begin, 0)]
    my_len = len(words)
    
    # 똑같은 단어를 재방문하지 않게 위해 visited 초기화
    visited = [0]*my_len
    
    # target이 words에 없다면 0 return
    if target not in words:
        return 0
    
    # stack이 비어있지 않다면 실행
    while stack:
        # 지금 단어와 횟수 pop
        now = stack.pop(-1)
        now_word = now[0]
        turn = now[1]
        
        # 지금 단어와 target이 같다면 횟수 리턴
        if now_word == target:
            return turn
        
        # words를 순회
        for i in range(my_len):
            if visited[i] == 1:
                continue
            
            # 알파벳이 하나만 다른지 확인
            flag = 0
            for now_alpha, next_alpha in zip(now_word, words[i]):
                if now_alpha != next_alpha:
                    flag += 1

            # 하나만 다르다면 방문 및 stack에 추가  
            if flag == 1:
                visited[i] = 1
                stack.append((words[i], turn + 1))
        
    return answer