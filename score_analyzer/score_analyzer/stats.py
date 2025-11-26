def calculate_average(scores):
    if not scores:
        return 0
    return sum(scores) / len(scores)


def calculate_min(scores):
    if not scores:
        return 0
    return min(scores)


def calculate_max(scores):
    if not scores:
        return 0
    return max(scores)
