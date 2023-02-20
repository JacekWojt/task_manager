#===Importing libraries===
from datetime import date
#===Login section====
with open('user.txt', 'r+') as file:
    lines = file.readlines()
login_dic = {}
user_list = []
picked_no = ''
for line in lines:
    temp = line.replace(', ', ' ')
    temp = temp.strip('\n')
    temp = temp.split(' ')
    user_list.append(temp[0])
    login_dic.update({temp[0]: temp[1]})
name = input('Enter username: ').lower()
while user_list.count(name) == 0:
    print('Invalid username.')
    name = input('Enter username again: ').lower()
word = input('Enter password: ')
con_word = input('Confirm password: ')
while word != con_word or login_dic.get(name) != word:
    word = input('Invalid password. Enter password again: ')
    con_word = input('Confirm pasword: ')
print('You are log in')
#===Display main interface====
while True:
    if name == 'admin':
        menu = input('''Select one of the following options:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
gr - generate reports
ds - display statistics
e - Exit
: ''').lower()
    elif name != 'admin':
        menu = input('''Select one of the following options:
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()
#===Register a new user===
    if menu == 'r':
        new_name = input('Enter a new username: ').lower()
        check = True
        while check == True:
            check = False
            for key in login_dic:
                if key == new_name:
                    new_name = input('The name is already in the database. Enter the new username again: ').lower()
                    check = True
                    break
        new_word = input('Enter a password: ').lower()
        con_new_word = input('Confirm password: ').lower()
        while new_word != con_new_word:
            new_word = input('Password did not match. Enter password again: ').lower()
            con_new_word = input('Confirm pasword: ').lower()
        with open('user.txt', 'a') as file:
            file.write('\n' + new_name + ", " + con_new_word)
#===Add a new task===
    elif menu == 'a':
        add_name = input('Enter the username of the person to whom the task is assigned: ').lower()
        task_title = input('Enter task title: ')
        task_info = input('Enter task description: ')
        print('Enter the deadline for the task')
        year = int(input('Enter the year (format: XXXX): '))
        month = int(input('Enter the month (format: XX): '))
        day = int(input('Enter the day (format XX): '))
        d_date = date(year, month, day)
        due_date = d_date.strftime("%d %b %Y")
        current_date = date.today().strftime("%d %b %Y")
        with open('tasks.txt', 'a') as file:
            file.write('\n' + add_name + ", " + task_title + ", " + task_info + ", " + current_date + ", " + due_date + ", No")
#===Display all tasks stored in the registry===
    elif menu == 'va':
        def print_task(temp_list):
            print(f'\nTask number:          {task_no}\n'
                    f'Task:                 {temp_list[1]}\n' 
                    f'Assigned to:          {temp_list[0]}\n'
                    f'Date assigned:        {temp_list[3]}\n'
                    f'Due date:             {temp_list[4]}\n'
                    f'Task Complete?        {temp_list[5]}\n'
                    f'Task description      {temp_list[2]}\n')
        with open('tasks.txt', 'r+') as file:
            lines = file.readlines()
        task_no = 1
        print(f'\nBelow is a list of all tasks in the database.')
        print('─' * 120)
        for line in lines:            
            temp_list = line.split(', ')
            print_task(temp_list)            
            print('─' * 120)
            task_no += 1
#===Display all tasks that are assigned to the logged-in user===
    elif menu == 'vm':
        with open('tasks.txt', 'r+') as file:
            lines = file.readlines()
        task_no = 0
        print(f'\nThe following is a list of tasks assigned to {name}.')
        print('─' * 120)
        for line in lines:
            task_no += 1            
            if line.startswith(name):
                temp_list = line.split(', ')
                print_task(temp_list)
                print('─' * 120)
        picked_no = int(input('Seleck a task by entering its number, or enter "-1" to return to the main menu\n'))
#===Display one selected task that are assigned to the logged-in user===
        if picked_no > 0:
            with open('tasks.txt', 'r+') as file:
                lines = file.readlines()
            task_no = 1
            option = True
            for line in lines:
                line = line.strip('\n')
                if task_no == picked_no and line.endswith('Yes'):
                    print('\nThe selected task cannot be edited. The task has already been completed.\n')
                    option = False
                task_no += 1
            if option:
                task_no = 1            
                for line in lines:           
                    if line.startswith(name):                    
                        if task_no == picked_no:
                            temp_list = line.split(', ')
                            print_task(temp_list)
                            print('─' * 120) 
                    task_no += 1
                task_menu = input('''Selcet one of the following options:
m - mark the task as complete
e - edit the task\n''').lower()
#===Mark the task as complete===
                if task_menu == 'm':
                    with open('tasks.txt', 'r') as file:
                        lines = file.readlines()
                    tab = []
                    line_no = 0
                    with open('tasks.txt', 'w') as file:
                        for line in lines:
                            temp = line.strip('\n')
                            tab.append(temp)
                            if line_no == picked_no - 1:
                                tab[line_no] = tab[line_no].replace('No', 'Yes')
                            file.write(tab[line_no] + "\n")
                            line_no += 1
                        print('\nThe task was marked as completed\n')
#===Edit the task===
                elif task_menu == 'e':
                    edit_menu = input('''Selcet one of the following options:
u - change the username of the user to whom a task is assigned
d - change the deadline for completing the task\n''').lower()
#===Change the name of the user to whom a task is assigned===
                    if edit_menu == 'u':
                        with open('tasks.txt', 'r') as file:
                            lines = file.readlines()
                        new_username = input('Enter a new username: ')
                        tab = []
                        line_no = 0
                        with open('tasks.txt', 'w') as file:
                            for line in lines:
                                temp = line.strip('\n')
                                tab.append(temp)
                                if line_no == picked_no - 1:
                                    tab[line_no] = tab[line_no].replace(name, new_username)
                                file.write(tab[line_no] + "\n")
                                line_no += 1
                            print(f'\nThe username for the task has been changed to {new_username}\n')
#===Change the deadline of the task===
                    elif edit_menu == 'd':
                        print('Enter a new deadline for the task')
                        year = int(input('Enter the year (format: XXXX): '))
                        month = int(input('Enter the month (format: XX): '))
                        day = int(input('Enter the day (format XX): '))
                        d_date = date(year, month, day)
                        due_date = d_date.strftime("%d %b %Y")
                        print(due_date)
                        with open('tasks.txt', 'r') as file:
                            lines = file.readlines()
                        tab = []
                        line_no = 0
                        with open('tasks.txt', 'w') as file:
                            for line in lines:
                                temp = line.strip('\n')
                                tab.append(temp)
                                if line_no == picked_no - 1:
                                    string_temp = str(tab[line_no])
                                    list = string_temp.split(', ')
                                    list[4] = due_date
                                    listToStr = ', '.join([str(elem) for elem in list])
                                    tab[line_no] = listToStr
                                file.write(tab[line_no] + "\n")
                                line_no += 1
                            print(f'\nThe deadline for the task has been changed to {due_date}\n')
        else:
            pass
#===Display of task and user overview statistics===
    elif menu == 'ds':
        try:
            with open('task_overview.txt', 'r+') as file:
                lines = file.readlines()
            print('\nTask overview statistics:\n')
            for line in lines:
                line = line.strip('\n')
                print(line)
            with open('user_overview.txt', 'r+') as file:
                lines = file.readlines()
            print('\nUser overview statistics:\n')
            for line in lines:
                line = line.strip('\n')
                print(line)
            print('─' * 120)
        except FileNotFoundError:
            print('\nThe file for statistics has not yet been created.\n'
                    'Please generate reports first, so that you can then view the statistics.\n')
#===Generate of a task overview report===
    elif menu == 'gr':
        def format_month(month):
            if month == 'Jan':
                month = 1
            elif month == 'Feb':
                month = 2
            elif month == 'Mar':
                month = 3
            elif month == 'Apr':
                month = 4
            elif month == 'May':
                month = 5
            elif month == 'Jun':
                month = 6
            elif month == 'Jul':
                month = 7
            elif month == 'Aug':
                month = 8
            elif month == 'Sep':
                month = 9
            elif month == 'Oct':
                month = 10
            elif month == 'Nov':
                month = 11
            elif month == 'Dec':
                month = 12
            return month
        with open('tasks.txt', 'r+') as file:
            lines = file.readlines()
        counter_task = 0
        counter_completed_task = 0
        counter_uncompleted_task = 0
        counter_overdue_task = 0
        for line in lines:
            counter_task += 1
            line = line.strip('\n')
            if line.endswith('Yes'):
                counter_completed_task += 1
            elif line.endswith('No'):
                counter_uncompleted_task += 1
                temp = line.strip('\n')
                temp = temp.split(', ')
                due_date_str = temp[4]
                due_date_str = due_date_str.strip(' ')
                due_date_list = due_date_str.split(' ')
                day = int(due_date_list[0])
                str_month = due_date_list[1]
                year = int(due_date_list[2])
                month = format_month(str_month)
                due_date = date(year, month, day)
                today = date.today()
                if due_date < today:
                    counter_overdue_task += 1
        with open('task_overview.txt', 'w') as file:
            file.write(f'The total number of task: {counter_task}\n')
            file.write(f'The total number of completed tasks: {counter_completed_task}\n')
            file.write(f'The total number of uncompleted tasks: {counter_uncompleted_task}\n')
            file.write(f'The total number of uncompleted and overdue tasks: {counter_overdue_task}\n')
            file.write('The percentage of tasks that are incomplete: ' + '{:.2%}'.format(counter_uncompleted_task/counter_task) + '\n')
            file.write('The percentage of tasks that are overdue: ' + '{:.2%}'.format(counter_overdue_task/counter_task) + '\n')
        print('\nThe task overview file has been created')
        print('The user overview file has been created\n')
#===Generate of a user overview report===
        with open('user.txt', 'r+') as file:
            lines = file.readlines()
        counter_users = 0
        list_user = []
        for line in lines:
            counter_users += 1
            line = line.strip('/n')
            list_login = line.split(', ')
            list_user.append(list_login[0])   
        with open ('user_overview.txt', 'w') as file:
            file.write(f'The total number of users: {counter_users}\n')
            file.write(f'The total number of tasks: {counter_task}\n')        
        def each_user(user):
            task_no = 0
            task_assigned_user = 0
            task_completed = 0
            overdue_task_no = 0            
            with open('tasks.txt', 'r+') as file:
                lines = file.readlines()
            for line in lines:
                task_no += 1
                line = line.strip('\n')
                list_user = line.split(', ')
                if list_user[0] == user:
                    task_assigned_user += 1
                if list_user[0] == user and list_user[5] == 'Yes':
                    task_completed += 1
                if list_user[0] == user and list_user[5] == 'No':                
                    due_date_str = list_user[4]
                    due_date_str = due_date_str.strip(' ')
                    due_date_list = due_date_str.split(' ')
                    day = int(due_date_list[0])
                    str_month = due_date_list[1]
                    year = int(due_date_list[2])
                    month = format_month(str_month)
                    due_date = date(year, month, day)
                    today = date.today()
                    if due_date < today:
                        overdue_task_no += 1
            with open ('user_overview.txt', 'a') as file:
                if task_assigned_user != 0:
                    file.write(f'\nUser: {user}\n')
                    file.write(f'The total number of tasks assigned: {task_assigned_user}\n')
                    file.write(f'The percentage of the total number of tasks that have been assigned: ' + '{:.2%}'.format(task_assigned_user/task_no) + '\n')
                    file.write(f'The percentage of the tasks assigned to that user that have been completed: ' + '{:.2%}'.format(task_completed/task_assigned_user) + '\n')
                    file.write(f'The percentage of the tasks assigned to that user that must still be completed: ' + '{:.2%}'.format((task_assigned_user - task_completed - overdue_task_no)/task_assigned_user) + '\n')
                    file.write(f'The percentage of the tasks assigned to that user that have not yet been completed and are overdue: ' + '{:.2%}'.format(overdue_task_no/task_assigned_user) + '\n')
                elif task_assigned_user == 0:
                    file.write(f'\nUser: {user}\n')
                    file.write(f'The total number of tasks assigned: {task_assigned_user}\n')
                    file.write(f'The percentage of the total number of tasks that have been assigned: ' + '{:.2%}'.format(0) + '\n')
                    file.write(f'The percentage of the tasks assigned to that user that have been completed: ' + '{:.2%}'.format(0) + '\n')
                    file.write(f'The percentage of the tasks assigned to that user that must still be completed: ' + '{:.2%}'.format(0) + '\n')
                    file.write(f'The percentage of the tasks assigned to that user that have not yet been completed and are overdue: ' + '{:.2%}'.format(0) + '\n')   
        for user in list_user:
            each_user(user)
#===Exit===
    elif menu == 'e':
        print('Goodbye!!!')
        exit()
#===Wrong choice===
    else:
        print('You made the wrong choice, please try again')