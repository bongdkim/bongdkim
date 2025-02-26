T = 10

for tc in range(1, T + 1):
    # 덤프 횟수(상자를 옮길 수 있는 횟수)
    N = int(input())

    # 각 상자들의 높이가 주어진다
    boxes = list(map(int, input().split()))

    # 평탄화 작업을 N번 하면 된다.
    # 상자 높이 최대 위치 -1
    # 상자 높이 최소 위치 +1
    # N번 반복
    for i in range(N):
        # 상자 높이가 제일 높은곳 위치(인덱스)
        max_idx = 0
        max_height = 0
        # 상자 높이가 제일 낮은곳 위치(인덱스)
        min_idx = 0
        min_height = 100

        for j in range(100):
            # j번째 상자의 높이가 최대값?
            if boxes[j] > max_height:
                # j번째 상자의 높이가
                # 내가 이전에 알고 있던 최대값보다 크면 갱신
                max_height = boxes[j]
                max_idx = j

            # j번째 상자의 높이가 최소값?
            if boxes[j] < min_height:
                # j번째 상자의 높이가
                # 내가 이전에 알고 있던 최소값보다 작으면 갱신
                min_height = boxes[j]
                min_idx = j

        # 100개의 상자를 다 확인하고 나면
        # 상자 제일 높은곳(max_idx)과
        # 제일 낮은곳(min_idx) 위치를 알고 있다.
        # 덤프 1회 시작
        boxes[max_idx] -= 1
        boxes[min_idx] += 1

    # 제일 높은곳에서 제일 낮은곳으로 상자 하나 버렸으니
    # 이전에 내가 알던 최대값이 더이상 최대값이 아닐수도 있다!
    # 다시 구해야된다.
    max_height = 0
    min_height = 100

    for i in range(100):
        if boxes[i] > max_height:
            max_height = boxes[i]
        if boxes[i] < min_height:
            min_height = boxes[i]

    print(f"#{tc} {max_height - min_height}")
