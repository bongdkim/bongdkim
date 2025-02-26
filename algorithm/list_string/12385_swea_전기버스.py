T = int(input())

for tc in range(1, T + 1):
    K, N, M = map(int, input().split())
    charge = list(map(int, input().split()))
    charge.append(N)
    
    current = 0
    last_charge = 0
    count = 0
    possible = True
    
    while current < N:
        if current + K >= N:
            break
        
        for i in range(last_charge, M):
            if charge[i] <= current + K:
                last_charge = i
            else:
                break
        
        if charge[last_charge] <= current + K:
            count += 1
            current = charge[last_charge]
            last_charge += 1
        else:
            possible = False
            break

    if possible:
        print(f'#{tc} {count}')
    else:
        print(f'#{tc} 0')
