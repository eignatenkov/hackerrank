t = int(input())
questions = [int(input()) for i in range(t)]


lengths = dict()
lengths[1] = 1

for i in range(2, max(questions)+1):
    if i not in lengths:
        to_fill = []
        cur = i
        while True:
            to_fill.append(cur)
            cur = cur // 2 if not cur % 2 else cur*3 + 1
            if cur in   lengths:
                f_l = len(to_fill)
                for index, j in enumerate(to_fill):
                    lengths[j] = lengths[cur] + f_l - index
                break

for q in questions:
    subset = {key: lengths[key] for key in lengths if key <= q}
    max_chain = max(subset.values())
    print(max([x for x in subset if subset[x] == max_chain]), max_chain)

