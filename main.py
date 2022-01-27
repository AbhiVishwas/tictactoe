#dictionary 

theBoard = {'7': ' ', '8': ' ','9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' ',}


# making/mapping the board 


def printBoard(theBoard):
  print (theBoard['7'] + '|' + theBoard['8'] + '|' + theBoard['9'])
  print ('-*-*-')
  print (theBoard['4'] + '|' + theBoard['5'] + '|' + theBoard['6'])
  print ('-*-*-')
  print (theBoard['1'] + '|' + theBoard['2'] + '|' + theBoard['3'])

# take input for turns
def game(): 
  turn = 'X'
  count = 0 
  for i in range (10):
    printBoard(theBoard)
    print ("It's your turn " + turn + " Move to what place?")
    move = input()
    if theBoard[move] == ' ' : 
      theBoard[move] = turn
      count+=1
    else: 
      print ('that place is taken, move to a new place?')
      continue


  # check winners 
  # horizontal
  if count >= 5:
    if theBoard['1'] == theBoard['2'] == theBoard['3'] !='' : 
      printBoard(theBoard)
      print ('******'+ turn + 'wins!' + '******')
      print ("\nGame Over. \n")
    elif theBoard['4'] == theBoard['5'] == theBoard['6'] !='' : 
      printBoard(theBoard)
      print ('******'+ turn + 'wins!' + '******')
      print ("\nGame Over. \n")
    elif theBoard['7'] == theBoard['8'] == theBoard['9'] !='' : 
      printBoard(theBoard)
      print ('******'+ turn + 'wins!' + '******')
      print ("\nGame Over. \n")

    # vertical
    elif theBoard['9'] == theBoard['6'] == theBoard['3'] !='' : 
      printBoard(theBoard)
      print ('******'+ turn + 'wins!' + '******')
      print ("\nGame Over. \n")
    elif theBoard['8'] == theBoard['5'] == theBoard['2'] !='' : 
      printBoard(theBoard)
      print ('******'+ turn + 'wins!' + '******')
      print ("\nGame Over. \n")
    elif theBoard['1'] == theBoard['4'] == theBoard['7'] !='' : 
      printBoard(theBoard)
      print ('******'+ turn + 'wins!' + '******')
      print ("\nGame Over. \n")
  
  if count == 9:
    print ("\nGame Over. \n")
    print("It's a tie!")
   
  if turn == 'X':
    turn = 'O'
  else : 
    turn = 'O'

game()
