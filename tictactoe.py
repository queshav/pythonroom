gameover = False
tl = " "
t = " "
tr = " "
l = " "
c = " "
r = " "
bl = " "
b = " "
br = " "

current = "X"

while not gameover:
	# Clear the output screen
	print ":clear"
	# Print the board
	print " " + tl + " | " + t + " | " + tr
	print "---+---+---"
	print " " + l + " | " + c + " | " + r
	print "---+---+---"
	print " " + bl + " | " + b + " | " + br
	
	row = 0
	col = 0
	while row < 1 or col < 1 or row > 3 or col > 3:	
		row = int(input("Enter a row"))
		col = int(input("Enter a column"))
		if row == 5:
			gameover = True
	
	if row == 1 and col == 1:
		tl = current
	if row == 1 and col == 2:
		t = current
	if row == 1 and col == 3:
		tr = current
	if row == 2 and col == 1:
		l = current
	if row == 2 and col == 2:
		c = current
	if row == 2 and col == 3:
		r = current
	if row == 3 and col == 1:
		bl = current
	if row == 3 and col == 2:
		b = current
	if row == 3 and col == 3:
		br = current
	
	if current == "X":
		current = "O"
	else:
		current = "X"