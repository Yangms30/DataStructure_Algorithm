def solution(mats, park):
    # 돗자리 크기를 내림차순 정렬
    mats.sort(reverse=True)
    n, m = len(park), len(park[0])  # 공원 크기
    
    def can_place(x, y, size):
        """(x, y)에서 size x size 돗자리를 배치할 수 있는지 확인"""
        if x + size > n or y + size > m:
            return False
        for i in range(x, x + size):
            for j in range(y, y + size):
                if park[i][j] != "-1":
                    return False
        return True
    
    for size in mats:
        for i in range(n):
            for j in range(m):
                if can_place(i, j, size):
                    return size
    return -1