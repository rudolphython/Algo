import heapq


def solution(jobs):
    heap = []
    answer = 0
    
    # 현재 시간 체크
    time_now = 0
    
    # 시작 시간은 -1로 설정
    start = -1
    
    # task 체크용 변수 선언
    i = 0
    while i <= len(jobs) - 1:
        for job in jobs:
            # task의 시작 가능 시간이 start와 현재 시간 사이라면,
            if start < job[0] <= time_now:
                # 최소힙으로 push
                heapq.heappush(heap, [job[1], job[0]])
        
        # task가 있다면
        if len(heap) >= 1:
            i += 1
            # task를 끄내고
            task_now = heapq.heappop(heap)
            # 시작 시간은 지금 시간으로 바뀜
            start = time_now
            # 지금 시간은 task가 끝나는 시점으로 바뀜
            time_now += task_now[0]
            # answer 업데이트
            answer += time_now - task_now[1]        
        # task가 없다면 단순히 시간 업데이트
        else:
            time_now += 1
            
            
    return answer // len(jobs)