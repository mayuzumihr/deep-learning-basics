kinoko_takenoko = input("\'kinoko\' or \'takenoko\' >>> ")
aka_midori = input("\'aka\' or \'midori\' >>> ")

if (kinoko_takenoko != 'kinoko') and (kinoko_takenoko != 'takenoko'):
    print("入力に誤りがあります（kinoko_takenoko）")
    exit(0)

if (aka_midori != 'aka') and (aka_midori != 'midori'):
    print("入力に誤りがあります（aka_midori）")
    exit(0)

# 黛は「たけのこの里」「緑のたぬき」派です。

print()
print((kinoko_takenoko == 'kinoko') and (aka_midori == 'aka'))
print((kinoko_takenoko == 'kinoko') and (aka_midori == 'midori'))
print((kinoko_takenoko == 'takenoko') and (aka_midori == 'aka'))
print((kinoko_takenoko == 'takenoko') and (aka_midori == 'midori'))
print()
print((kinoko_takenoko == 'kinoko') or (aka_midori == 'aka'))
print((kinoko_takenoko == 'kinoko') or (aka_midori == 'midori'))
print((kinoko_takenoko == 'takenoko') or (aka_midori == 'aka'))
print((kinoko_takenoko == 'takenoko') or (aka_midori == 'midori'))
print()

# なので
#「きのこの山」部分と「赤いきつね」部分が 0
#「たけのこの里」部分と「緑のたぬき」部分が 1
# となります

print()
print(0 and 0)
print(0 and 1)
print(1 and 0)
print(1 and 1)
print()
print(0 or 0)
print(0 or 1)
print(1 or 0)
print(1 or 1)
print()
