def best_move(n):
    r = n % 4
    if r != 0:
        return r
    return 1

def winner(n):
    if n % 4 != 0:
        return "First player"
    return "Second player"

def play(n):
    turn = 1
    while n > 0:
        take = best_move(n)
        n -= take

        print("Player", turn, "takes", take, ",", n, "left")

        if n == 0:
            print("Player", turn, "wins!")

        turn = 3 - turn

n = int(input("Number of stones: "))

print(winner(n), "wins with perfect play")
play(n)