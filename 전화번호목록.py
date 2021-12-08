'''
프로그래머스 : 전화번호 목록
문제 유형 : 해쉬
'''

def solution(phone_book):
    answer = True
    check = sorted(phone_book)
    # 문자열의 길이에 따라 일단 소팅
    for i in range(len(check)-1):
        if check[i] == check[i+1][:len(check[i])]:
            # 해당 길이만큼 슬라이싱 후 비교
            answer = False
            break
    return answer