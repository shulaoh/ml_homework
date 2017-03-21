def load_data(file_name):
	with open(file_name, 'r') as f:
		lines = f.readlines()

	number_of_lines = len(lines)
	data = []

	for line in lines:
		line = line.strip()
		rows = line.split('\t')
		row_x = rows[0].split(' ')
		row_x.append(1) # add 1 as x0
		row_y = rows[1]
		row_x.append(row_y)
		data.append(row_x)
	#print(data)
	return data


def sign(number):
	if number <= 0:
		return -1
	else:
		return 1	


def measure(w, data):
	for row in data :
		x = row[:5]
		y = int(row[5])
		sum_x = 0.0
		for i in range(5):
			sum_x += w[i] * float(x[i]) 
		fx = sign(sum_x)
		if fx != y:
			print('fx = ', fx, ' y = ', y)
			return row
	return []

def pla(file_name):
	data = load_data(file_name)
	w = [0.0, 0.0, 0.0, 0.0, 0.0]
	row = [1]
	num = len(data)
	count = 0
	change = 0;
	while len(row) > 0 and count < 400:
		row = measure(w, data)
		count += 1
		print('count: ', count)
		if len(row) > 0:
			w1 = w;
			change += 1;
			w = [w1[i] + float(row[5]) * float(row[i]) for i in range(5)]
			print('row = ', row)
			print('w = ', w)
		else:
			break
	print('change: ', change)

if __name__ == "__main__":
	data = pla('D:\ml\data\hw1_15_train.dat')
