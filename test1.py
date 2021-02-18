from datetime import datetime
file = open('python_exercise_input.txt')
lines = file.readlines()
st_date = '2020-07-01'
st_date_object = datetime.strptime(st_date, '%Y-%m-%d').date()

info_dict = {}
for line in lines:
	data = line.split(';')
	date = data[1].split(' ')[0]
	date_obj = datetime.strptime(date, '%Y-%m-%d').date()
	info_dict.setdefault(data[0],0)
	if date_obj > st_date_object:
		info_dict[data[0]] +=1


print('Number of quotes after 01/07/2020:\n')
print(info_dict)
