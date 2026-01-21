# Problem-1607A---Linear-Keyboard
for _ in range(int(input())):
    target = input().strip()
    s = input().strip()
    lst = []
    for i in range(len(s)):
        lst.append(target.index(s[i])+1)
    count = 0
    for j in range(len(lst)-1):
        count += abs(lst[j+1] - lst[j])
    print(count)
