menu_input = input("""
    Please enter one of the following options:
    r - register user
    a - add task
    va- view all tasks
    vm - view my tasks
    gr - generate reports
    ds - display statistics
    e - exit
    """)
if menu_input == "r":
 register()
elif menu_input == "a":
 add_task()
elif menu_input == "va":
 generate_task_overview()
elif menu_input == "vm":
 view_more()
elif menu_input == "gr":
 reports()
elif menu_input == "ds":
 display_admin_stats() 
elif menu_input == "e":
 exit()
 #return menu_input


#A menu should be displayed once the user has successfully logged in.
    
def displayMenu():
 global menu_input
    
menu_input = input("""
    Please enter one of the following options:
    a - add task
    va- view all tasks
    vm - view my tasks
    e - exit
    """)
    
if menu_input == "a":
    add_task()
elif menu_input == "va":
    view_all()
elif menu_input == "vm":
    view_more()
elif menu_input == "e":
    exit()
#return menu_input

    
def login():
 username = input("Please enter your username?:\n")
 password = input("Please enter your password?:\n")
    
for line in open("user.txt","r").readlines():
    field = line.strip().split(", ")
if username == field[0] and password == field[1]:
    print("Hello " + username + ", welcome back!\n")
#return True, field[0]== "admin"
    
#return False, False
login_success, is_admin = login()
if login_success and is_admin:
       displayMenu_Admin()
elif login_success:
       displayMenu()
else:
 print("Username or Password Incorrect\n")



# Displaying only admin specific statistics to the screen.
def display_admin_stats():
 generate_task_overview() # Calls the function that generates 'task_overview.txt'.
 generate_user_overview() # Calls the function that generates 'user_overview.txt'.

print("Displaying statistics for admin:\n")
user_dictionary = user_dict()
task_dictionary = task_dict()
    
print(f"Total number of tasks: {len(task_dictionary)}")
print(f"Total number of users: {len(user_dictionary)}")
            
with open('task_overview.txt', 'r') as task:
 print('\nTASK OVERVIEW STATS:\n')
for line in task:
 print(line.strip())
        
with open('user_overview.txt', 'r') as task:
 print('\nUSER OVERVIEW STATS:\n')
for line in task:
    print(line.strip())
exit_menu()

# Generate the task overview text file.
def generate_task_overview():
    task_dictionary = task_dict()
    completed_tasks = 0
    uncompleted_tasks = 0
    overdue_tasks = 0
    
# Open the file, or creates it if it doesn't exist.
# Reads each task from the task_dict function.
# And applies the logic to write to the file.
with open('task_overview.txt', 'w') as task_overview:
 for count in task_dictionary:
  task = task_dictionary[count]
if 'Yes' == task['task_complete']:
 completed_tasks += 1
elif 'No' == task['task_complete']:
 uncompleted_tasks += 1
            
# Comparing the dates to check if the task is overdue.
datetime_object = datetime.datetime.strptime(task['date_due'], '%d %b %Y') # 'strptime()' parses a string representing a time according to a format.
if datetime_object < datetime.datetime.today() and 'No' == task['task_complete']: # 'today()' method of date class under datetime module returns a date object which contains the value of Today's date.
 overdue_tasks += 1
#calculate percentage                
percentage_incomplete = (uncompleted_tasks * 100)/(len(task_dictionary))
percentage_overdue = (overdue_tasks * 100)/(len(task_dictionary))

# Print / write everything to the file.
task_overview.write(f"Total number of tasks generated using Task Manager: {len(task_dictionary)}\n")
task_overview.write(f"Number of completed tasks: {completed_tasks}\n")
task_overview.write(f"Number of uncompleted tasks: {uncompleted_tasks}\n")
task_overview.write(f"Number of uncompleted tasks that are overdue: {overdue_tasks:.0f}\n")
task_overview.write(f"Percentage of uncompleted tasks: {percentage_incomplete:.0f}%\n")
task_overview.write(f"Percentage of uncompleted overdue tasks: {percentage_overdue:.0f}%\n")
    
print("Task_overview.txt written.")  
