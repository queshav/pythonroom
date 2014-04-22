gameover = False
td = 5, tx = 3

while not gameover:
	# Clear the output screen
	print ":clear"
	# Print the board
	print "   |   |   "
	print "---+---+---"
	print "   |   |   "
	print "---+---+---"
	print "   |   |   "
	
	row = input("Enter a row")
	col = input("Enter a column")
	
	if row == "5":
		gameover = True
