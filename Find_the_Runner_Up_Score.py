if __name__ == '__main__':
    n = int(input())
    scores = list(map(int, input().split()))

    sorted_scores = sorted(scores, reverse=True)

    unique_scores = list(set(sorted_scores))

    if len(unique_scores) > 1:
        runner_up_score = unique_scores[1]
    else:
        runner_up_score = sorted_scores[-1]

    print(runner_up_score)

