import random
win_count = 0
lose_count = 0
draw_count = 0

for i in range(1, 6):
    com = random.randint(1, 3)
    print(f'현재 스코어 컴퓨터 : {lose_count} 나 : {win_count}')
    ply = int(input(f'[{i}판]가위(1) 바위(2) 보(3)'))
    if ply == 1:
        print('당신: 가위')
    elif ply == 2:
        print('당신: 바위')
    elif ply == 3:
        print('당신: 보')
    if com == ply:
        print('비겼습니다')
        draw_count += 1
    elif com == 1:
        print('컴퓨터 : 가위')
        if ply == 3:
            print('졌습니다')
            lose_count += 1
        elif ply == 2:
            print('이겼습니다')
            win_count += 1
    elif com == 2:
        print('컴퓨터 : 바위')
        if ply == 1:
            print('졌습니다')
            lose_count += 1
        elif ply == 3:
            print('이겼습니다')
            win_count += 1
    elif com == 3:
        print('컴퓨터 : 보')
        if ply == 1:
            print('졌습니다')
            lose_count += 1
        elif ply == 2:
            print('이겼습니다')
            win_count += 1
    
    if win_count==3:
        print(f'최종 결과 : 승리{win_count} 비김{draw_count} 패배{lose_count}')
        break
    elif lose_count==3:
        print(f'최종 결과 : 승리{win_count} 비김{draw_count} 패배{lose_count}')
        break