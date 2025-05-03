import datetime
# create a file with current date and time as filename

dt = datetime.datetime.now()
print(dt)
file_name = dt.strftime('%Y-%m-%d_%H-%M-%S.txt')
print(file_name)

with open(file_name,'w')as file:
    file.write(f'Hello - This File created on {dt.strftime('%Y-%m-%d_%H-%M-%S')}')

