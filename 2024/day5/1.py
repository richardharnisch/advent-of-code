import sys

input = sys.stdin.read()

sections = input.strip().split("\n\n")
rules = [_.split("|") for _ in sections[0].split("\n")]
updates = [_.split(",") for _ in sections[1].split("\n")]


def is_ordered_correctly(rules, update):
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            if update.index(rule[0]) >= update.index(rule[1]):
                return False
    return True


page_sum = 0
for update in updates:
    if is_ordered_correctly(rules, update):
        middle_page = update[len(update) // 2]
        page_sum += int(middle_page)

print(page_sum)
