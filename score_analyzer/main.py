from score_analyzer.stats import calculate_average, calculate_min, calculate_max
from score_analyzer.grade import grade_from_average


def main():
    scores = [95, 82, 76, 88, 90]

    avg = calculate_average(scores)
    min_score = calculate_min(scores)
    max_score = calculate_max(scores)
    grade = grade_from_average(avg)

    print("Scores:", scores)
    print("Average:", round(avg, 2))
    print("Min:", min_score)
    print("Max:", max_score)
    print("Grade:", grade)


if __name__ == "__main__":
    main()