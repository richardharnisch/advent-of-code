def is_safe(report):
    if report[0] < report[1]:
        for level in range(len(report) - 1):
            delta = report[level + 1] - report[level]
            if not (delta > 0 and delta < 4):
                return 0

    if report[0] > report[1]:
        for level in range(len(report) - 1):
            delta = report[level] - report[level + 1]
            if not (delta > 0 and delta < 4):
                return 0

    if report[0] == report[1]:
        return 0

    return 1


safe_reports = 0

report = input()

while report != "":
    report = [int(x) for x in report.split()]

    report_safe = is_safe(report)

    for level in range(len(report)):
        if report_safe:
            safe_reports += 1
            break
        dampened = report[:level] + report[level + 1 :]
        if is_safe(dampened):
            safe_reports += 1
            break

    try:
        report = input()
    except EOFError:
        break

print(safe_reports)
