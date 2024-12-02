from enum import Enum


class Direction(Enum):
    INCREASING = "INCREASING"
    DECREASING = "DECREASING"


def run():
    part_one()
    part_two()


def part_one():
    with open('input.txt', 'r') as f:
        reports = {}
        for line in f:
            array = [int(num) for num in line.split()]
            if len(array) > 1:
                if array[0] < array[1]:
                    reports[tuple(array)] = Direction.INCREASING
                elif array[0] > array[1]:
                    reports[tuple(array)] = Direction.DECREASING

    valid_reports = 0
    for report, direction in reports.items():
        for index in range(0, len(report) - 1):
            largest = max(report[index], report[index + 1])
            smallest = min(report[index], report[index + 1])
            difference = abs(largest - smallest)
            if direction == Direction.INCREASING:
                if report[index] > report[index + 1] or report[index] == report[index + 1] or difference > 3:
                    break  # Not a valid report
            elif direction == Direction.DECREASING:
                if report[index] < report[index + 1] or report[index] == report[index + 1] or difference > 3:
                    break  # Not a valid report

            if index == len(report) - 2:  # If we came this far, the report is valid.
                valid_reports = valid_reports + 1

    print(valid_reports)


def part_two():
    with open('input.txt', 'r') as f:
        reports = {}
        for line in f:
            array = [int(num) for num in line.split()]
            if len(array) > 1:
                if array[0] < array[1]:
                    reports[tuple(array)] = Direction.INCREASING
                else: # Do not filter out equal numbers as we did in part one, since they might become valid later here
                    reports[tuple(array)] = Direction.DECREASING

    valid_reports = 0
    for report, direction in reports.items():
        for index in range(0, len(report) - 1):
            largest = max(report[index], report[index + 1])
            smallest = min(report[index], report[index + 1])
            difference = abs(largest - smallest)
            if direction == Direction.INCREASING:
                if report[index] > report[index + 1] or report[index] == report[index + 1] or difference > 3:
                    valid_reports = valid_reports + check_bad_report(report)
                    break  # Not a valid report
            elif direction == Direction.DECREASING:
                if report[index] < report[index + 1] or report[index] == report[index + 1] or difference > 3:
                    valid_reports = valid_reports + check_bad_report(report)
                    break  # Not a valid report

            if index == len(report) - 2:  # If we came this far, the report is valid.
                valid_reports = valid_reports + 1

    print(valid_reports)

def check_bad_report(report) -> int:
    for i in range(len(report)):
        one_level_removed = report[:i] + report[i + 1:]
        direction = None
        for index in range(0, len(one_level_removed) - 1):
            if one_level_removed[0] < one_level_removed[1]:
                direction = Direction.INCREASING
            elif one_level_removed[0] > one_level_removed[1]:
                direction = Direction.DECREASING
            elif one_level_removed[0] == one_level_removed[1]: # No need to check, equal numbers are not valid anyway
                break
            largest = max(one_level_removed[index], one_level_removed[index + 1])
            smallest = min(one_level_removed[index], one_level_removed[index + 1])
            difference = abs(largest - smallest)
            if direction == Direction.INCREASING:
                if one_level_removed[index] > one_level_removed[index + 1] or one_level_removed[index] == one_level_removed[index + 1] or difference > 3:
                    break  # Not a valid report
            elif direction == Direction.DECREASING:
                if one_level_removed[index] < one_level_removed[index + 1] or one_level_removed[index] == one_level_removed[index + 1] or difference > 3:
                    break  # Not a valid report

            if index == len(one_level_removed) - 2:  # If we came this far, the report is valid.
                return 1
    return 0



if __name__ == "__main__":
    run()
