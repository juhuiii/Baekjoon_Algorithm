while True:
    pages = [False for i in range(int(input()))]
    if len(pages) == 0:
        break
    toPrint = input().split(",")
    for i in toPrint:
        to_print = list(map(int, i.split("-")))
        if to_print[0] > len(pages):
            continue
        if len(to_print) == 1:
            pages[to_print[0]-1] = True
            continue
        if to_print[0] > to_print[1]:
            continue
        if to_print[1] > len(pages):
            to_print[1] = len(pages)
        for j in range(to_print[0], to_print[1]+1):
            pages[j-1] = True
    print(pages.count(True))