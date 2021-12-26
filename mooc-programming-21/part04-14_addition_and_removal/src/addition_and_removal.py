# Write your solution here
list_of_nums = []
next_num_to_add = None
while True:
    print(f'The list is now {list_of_nums}')
    action = input('a(d)d, (r)emove or e(x)it: ')
    if action == 'd':
        if len(list_of_nums) == 0:
            next_num_to_add = 1
        else:    
            next_num_to_add = list_of_nums[len(list_of_nums)-1] + 1
        list_of_nums.append(next_num_to_add)
    elif action == 'r':
        list_of_nums.pop()
    elif action == 'x':
        print('Bye!')
        break