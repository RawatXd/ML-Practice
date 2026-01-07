def find_total(expenses):
    total = 0
    for expense in expenses:
        total += expense

    return total


expenses_survey = [20,23,32,38]
expenses_done =[40,23,10,85]

total_expenses_survey = find_total(expenses_survey)
print(f"Total Expenses Survey : {total_expenses_survey}")

total_expenses_done = find_total(expenses_done)

print(f"Total Expenses Done : {total_expenses_done}")