import copy

def get_auc(x):
    l =  copy.deepcopy(x)
    l.sort(key=lambda x: x[1])

    positive_rank = [idx + 1 for idx,(label,score) in enumerate(l) if label ]

    m = len(positive_rank)
    n = len(l) - m

    if not m:
        return 0
    if not n:
        return 1
    auc = (sum(positive_rank) - (m*(m+1))/2) / (m * n)
    return auc

print(get_auc([(1,0.2),(0,0.1),(0,0.05),(0,0.21),(0,0.28)]))