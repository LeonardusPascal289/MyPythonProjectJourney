# SIMPLE TIC N TOE GMAES 


# Creating the structure of the boar using aDictionaries 

board = { "T-Left": '-', "T-Middle": '-', "T-Right": '-',
          "M-Left": '-', "M-Middle": '-', "M-Right": '-',
          "B-Left": '-', "B-Middle": '-', "B-Right": '-',

}
def printBoard():
    print(
        """
        {a}  | {b}  | {c} |

        {d}  | {e}  | {f} |

        {g}  | {h}  | {i} |
        """ .format( a = board ["T-Left"], b = board ["T-Middle"], c=board ["T-Right"],
                    d = board ["M-Left"], e = board ["M-Middle"], f=board ["M-Right"],
                g= board ["B-Left"],  h = board ["B-Middle"], i=board ["B-Right"],
        )
    )


def playGame():
    userTurn= 'X'
    for i in range(9):
        printBoard()
        print("This is " + userTurn + " turn. Make Your move.")
        turnInput = input()
        # placing the input on given position
        board[turnInput] = userTurn
        # checking the winner
        checkGameWinner = checkWinner(userTurn)
        if checkGameWinner:
            print('Congratulation '+ userTurn + " You are the Winner")
            break
        if userTurn == 'X':
            userTurn = 'O'
        else:
            userTurn = 'X'

def checkWinner(turn):
    if board ["T-Left"] == board ["T-Middle"] ==board ["T-Right"] == turn :
        return True
    elif board ["M-Left"] == board ["M-Middle"] ==board ["M-Right"] == turn:
        return True
    elif board ["B-Left"] == board ["B-Middle"] ==board ["B-Right"] == turn:
        return True
    elif board ["T-Left"] == board ["M-Left"] ==board ["B-Left"] == turn:
        return True
    elif board ["M-Middle"] == board ["M-Middle"] ==board ["B-Middle"]== turn:
        return True
    elif board ["T-Right"] == board ["M-Right"] ==board ["B-Right"]== turn:
        return True
    elif board ["T-Left"] == board ["M-Middle"] ==board ["B-Right"]== turn:
        return True
    elif board ["T-Right"] == board ["T-Middle"] ==board ["B-Left"]== turn:
        return True
    else:
        return False

playGame()