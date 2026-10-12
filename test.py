import random
answer = random.randint(1, 100)
for attempt in range(1, 11):                       # ① 限定最多 10 次
    guess = int(input(f"第 {attempt} 次，猜一个数（共 10 次）："))  # ② 显示当前次数
    if guess == answer:
        print(f"对了！用了 {attempt} 次猜中。")
        break                                      # ③ 猜对 → 跳出，不执行 else
    elif guess > answer:
        print("大了")
    else:
        print("小了")
else:                                               # ④ 10 次都没猜中才执行
    print(f"很遗憾，10 次机会用完，答案是 {answer}。")