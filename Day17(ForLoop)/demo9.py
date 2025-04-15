food = ['Masala Dose','Rava dose','idly','Khali dose','Pongal']

dose_list = []
for m in food:
	if 'dose' in m.lower():
		dose_list.append(m)


print(dose_list)
# ['Masala Dose', 'Rava dose', 'Khali dose']


