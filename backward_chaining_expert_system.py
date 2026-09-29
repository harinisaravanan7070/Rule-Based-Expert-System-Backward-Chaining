facts = [
    "attendance_good",
    "assignments_completed",
    "exam_passed",
    "project_completed"
]

rules = [
    ("eligible_for_placement", ["attendance_good", "exam_passed"]),
    ("eligible_for_placement", ["assignments_completed", "project_completed"]),
    ("good_academic_performance", ["attendance_good", "exam_passed"]),
    ("good_academic_performance", ["assignments_completed", "exam_passed"]),
    ("ready_for_interview", ["eligible_for_placement", "project_completed"])
]

steps = []


def backward_chaining(goal):
    if goal in facts:
        steps.append("Fact: " + goal)
        return True

    for conclusion, conditions in rules:
        if conclusion == goal:
            steps.append("Trying rule: " + goal)

            result = True

            for condition in conditions:
                if not backward_chaining(condition):
                    result = False
                    break

            if result:
                steps.append("Proved: " + goal)
                return True

    steps.append("Cannot prove: " + goal)
    return False


goal = "eligible_for_placement"

result = backward_chaining(goal)

print("=== REASONING STEPS ===")
for step in steps:
    print(step)

print("\n=== FINAL CONCLUSION ===")

if result:
    print(goal, "is TRUE")
else:
    print(goal, "is FALSE")