print("====歡迎來到<<七龍珠>>遊戲世界====")

print('''請選擇你的身份:
            1.悟空
            2.特南克斯
                   ''')

playerchoose = int(input("請選擇(1-2):"))
name = ''

print("-"*35)

if playerchoose == 1:
    name = "孫悟空"
    print("你已選擇1,角色悟空!")
elif playerchoose == 2:
    name = "特南克斯"
    print("你已選擇2,角色特南克斯!")
else:
    name = "孫悟空"
    print("選擇錯誤,系統自動選擇角色悟空!")

print("-"*35)

attack = 2
life = 2

bosslife = 10
bossattack = 10

print(f'{name}的生命值{life},攻擊力{attack}')

print("-"*35)

while True:
    print('''請選擇你要進行的操作:
            1.練級
            2.打BOSS
            3.逃跑
                   ''')

    gamechoose = int(input("請選擇操作(1-3):"))

    if gamechoose == 1:
        life += 2
        attack += 2
        print("-"*35)
        print(f'升級了!!\n目前生命值:{life}\n目前攻擊力:{attack}')
        print("-"*35)

    elif gamechoose == 2:

        bosslife -= attack
        print("*"*35)

        print(f'{name}攻擊了BOSS')

        if bosslife <= 0:
            print(f'BOSS受到{attack}傷害已經死了!')
            break

        life -= bossattack
        print(f'BOSS攻擊{name}了')

        if life <= 0:
            print(f'{name}受到BOSS的{attack}傷害!GAME OVER')
            break

    elif gamechoose == 3:
        print(f'{name}逃跑囉~~GAME OVER')
        break

    else:
        print("*"*35)
        print("輸入錯誤,重新輸入")
        print("*"*35)
