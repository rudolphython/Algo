def solution(n, words):
    answer = []
    my_len = len(words)
    
    turn = 1
    loser = 0
    loser_turn = 0
    stack = []
    for i in range(my_len):
        if i == my_len - 1:
            if words[i] in stack:
                loser = (i % n) + 1
                loser_turn = turn
        elif words[i][-1] != words[i+1][0] and i != my_len - 1:
            loser = (i+1 % n) + 1
            loser_turn = turn
        elif words[i] in stack:
            loser = (i+1 % n) + 1
            loser_turn = turn
        elif words[i] not in stack and words[i][-1] == words[i+1][0] and i != my_len - 1:
            stack.append(words[i])
            turn += 1
        elif loser != 0 and loser_turn != 0:
            break
            
    
    answer = [loser, loser_turn // n]    
            
            
        
    return answer


print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))