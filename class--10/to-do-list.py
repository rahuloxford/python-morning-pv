
to_do = []

while True:
     choice = input('do you wish to add/remove a task? (add/remove): ')
     if choice in ['add', 'Add', 'a', 'ad', 'ADD']:
          task = input('please enter the task name? ').strip()
          to_do.append(task)
          print("-----------------")
          i = 0
          while i < len(to_do):
               print(to_do[i])
               i = i + 1
          print("-----------------")
     elif choice in ['remove', 'Remove', 'r', 'REMOVE']:
          task = input('please enter the task name? ')
          to_do.remove(task)
          print("-----------------")
          i = 0
          while i < len(to_do):
               print(to_do[i])
               i = i + 1
          print("-----------------")
     else:
          print("exit!!")
          break
