if __name__ == '__main__':
    names = []
    scores = []
    for _ in range(int(raw_input())):
        name = raw_input()
        score = float(raw_input())
        names.append(name)
        scores.append(score)
    sorted_score = scores[:]
    sorted_score.sort()
    sec_max = 0
    for i in range(len(sorted_score)):
        if sorted_score[i] != sorted_score[0]:
            sec_max = sorted_score[i]
            break
    result = []
    for i in range(len(names)):
        if scores[i] == sec_max:
            result += [names[i]]
    result.sort()
    for i in result:
        print(i)
