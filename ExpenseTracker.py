from Employee import EmployeeDetails
import matplotlib.pyplot as plt
import calendar
import datetime

def main():# i am using this  to run only this specific function instead of running it whole.
    print(f'🎰Running employee expense tracker!')
    file_path = "tracker.csv"
    budget = 10000# lets say company budget permonth
    user_input = add_expense() # getting input for expense.
    save_expense(user_input,file_path)#write and save expense
    summarize_expense(file_path,budget)

def add_expense():
    print(f'📊Getting expense details')
    enter_name = input("📛Enter employee name:")
    enter_employee_id = input("👤Enter your employee ID:")
    enter_amount: float = float(input("🈷️Enter expense amount:"))
    enter_category = ["Travel", "laptop", "meal", "Headset", "Stationary", "hard disk", "Mobile",
                        "Accommodation"]
    # created list here so user can select it.
    print("Select the category: ")
    for i, category in enumerate(enter_category):
        print(f"{i + 1}. {category}") # make sure number starts from 1 adding +1 here
# adding while loop if in case user selects other than the given list.
    while True: # now need to prompt employee to select from category so using value range
        value_range = f"[1- {len(enter_category)}]"
        # -1 is as we know according to python index is 0# adding integer to avoid if in case user adds alphabets
        select_index = int(input(f"⌖Enter a category name{value_range}: "))-1
        # now creating if statement to make sure person is selecting within the range
        if select_index in range(len(enter_category)):
            # i have imported class from expense.py however category is not selected yet so creating new variable to get it as we have only expense category and select index
            updated_category = enter_category[select_index]
            updated_expense = EmployeeDetails(name=enter_name,id=enter_employee_id,category=updated_category,amount=enter_amount)
            return updated_expense
        else:
            print("Invalid category. Please try again")
def save_expense(user_input: EmployeeDetails,file_path): # to get the class details we can mention Expense class name in row 49
    print(f"Saving expense details:{user_input} to {file_path}")
    #to open the file and to append
    with open(file_path,"a") as f:
        f.write(f"{user_input.name},{user_input.employee_ID},{user_input.category},{user_input.amount}\n")

def summarize_expense(file_path,budget):
    print(F"Summarizing expense details")
    total: list[EmployeeDetails] = []
    with open(file_path,"r") as f:
        lines = f.readlines()# its creating space between each lines so need to use strip method and split to avoid extra lines in between
        for line in lines:#here i need to mention expense details .  in def add expenses so that i can get the variables else it wil through the error
           expense_name,expense_id,expense_category,expense_amount = line.strip().split(",")
           line_expense = EmployeeDetails(name=expense_name, id=expense_id,category=expense_category,amount=float(expense_amount))
           total.append(line_expense)

    amount_category_wise ={}# now i need all the expense in category wise so creating dict
    for expense in total:# here expense is not recognizing with the details so we added 'list' option in line 47 to work
        x = expense.category # here x represents key word
        if x in amount_category_wise:# we need to make sure key word is exists in category so using if functino
            amount_category_wise[x] += expense.amount ## indicating category value if it exists then amt will get added
        else:
            amount_category_wise[x] = expense.amount# if in case its not mentioned this create new entry .
        #   here key is category and value is total amount.
        # here to print the category details in nice looking way doing looping
        print("Expense information by category")
        for x,amount in amount_category_wise.items():
            print(f"{x}: €{amount:}")
 #finally need to check for the final budget how much amount is left we team after all the deductions so we are summarizing that as well
        TotalSpent = sum([expense.amount for expense in total])# its sums all the variables of expense in one line under totalspend.
        print(f"💶Total amount spent : €{TotalSpent: .2f} ")

# now to get the remaining budget after total amount spent
        surplus = budget - TotalSpent
        print(yellow(f"📉Remaining budget for the month: €{surplus: .2f}"))

# to get the no of days in a present month and current date and remaining days .imported calender and date/time file
    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day

    daily_budget = surplus / remaining_days
    print(green(f"📊👉 Budget Per Day: €{daily_budget:.2f}"))

# if  Total expense goes to -ve then we need to send a warning message
    if TotalSpent > budget:
        print(red(f"📉⚠︎Total expenses is more than a given budget."))
# preparing bar chart with this
    categories = list(amount_category_wise.keys())
    amounts = list(amount_category_wise.values())

    plt.figure(figsize=(8,5))
    plt.bar(categories, amounts,  color="yellow")
    plt.xlabel("Expense Category")
    plt.ylabel("Amount (€)")
    plt.title("Employees Expense summery")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

# just to get the main lines in different colour using below def
def green(text):
    return f"\033[92m{text}\033[0m"

def yellow(text):
    return f"\033[33m{text}\033[0m"

def red(text):
    return f"\033[31m{text}\033[0m"





if __name__ == "__main__":# this name variable is used to run directly instead of importing it. its like condition
    main()
