#Two versions

# first version best for expenses when all are known up front
# expenses = [10.50, 8, 5, 15, 20, 5, 3]
# total = sum(expenses)
# print("You spent $", total, " on lunch this week.", sep='')

#second version for daily entry
# total = 0
# expenses = []
# for i in range(7):
#     expenses.append(float(input("Enter an expense:")))
# total = sum(expenses)
# print("You spent $", total, sep='')

# third version allows user to add range
total = 0
expenses = []
num_expenses = int(input("Enter # of expenses:"))
for i in range(num_expenses):
    expenses.append(float(input("Enter an expense:")))
    
total = sum(expenses)
print("You spent $", total, sep='')
    
    