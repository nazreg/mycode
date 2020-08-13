line= ["*","* *","* * *","* * * *","* * * * *"];

for x in line:
    print(x)
    if x == line[-1]:
        line.pop(-1)
        newline = reversed(line)
        for x in newline:
            print(x)