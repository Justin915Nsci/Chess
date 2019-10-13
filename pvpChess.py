from chesslib import *
from chessPlayer import *

def main():
   board = GenBoard()
   white = 10
   black = 20
   Game = True
   while Game:
      PrintBoard(board)
      print()
      whiteMove = True
      blackMove =  True
      while whiteMove:
         print("White Turn!")
         move1 = input("What piece do you want to move?: ")
         inPos = int(move1)
         if inPos>63 or inPos<0:
            print("That position is outside of he board.")
         else:
            if board[int(inPos)]>20 or board[int(inPos)]==0:
               print("You do not own a piece in that spot.")
            else:
               move2 = input("Where do you want to move that piece?: ")
               endPos = int(move2)
               if validMove(board,inPos,endPos) == False:
                  print("You cannot move there.")
               else:
                  board[endPos] = board[inPos]
                  board[inPos] = 0
                  break                                                  
      PrintBoard(board)
      print()
      while blackMove:
         print("Black Turn!")
#         inPos = int(input("What piece do you want to move?: "))   
 #        if inPos>63 or inPos<0:
  #          print("That position is outside of he board.")
 #        else:
  #          if board[int(inPos)]>20 or board[int(inPos)]==0:
   #            print("You do not own a piece in that spot.")
    #        else:
     #          move2 = input("Where do you want to move that piece?: ")
      #         endPos = int(move2)
       #        if validMove(board,inPos,endPos) == False:
        #          print("You cannot move there.")
      #         else:
         tree = evalTree(board,20,0,None,None)
         move = maxMin(tree,20)
         print("black moved "  + str(move[1]))
         board[move[1][1]] = board[move[1][0]]
         board[move[1][0]] = 0
         break                                                  

  # printi(move)

def validMove(board,inPos,endPos):
   if endPos>63 or endPos<0:
      return False
   tempBoard = list(board)
   if board[inPos]>19:
      player = 20
   else:
      player = 10
   legalMoves = GetPieceLegalMoves(board,inPos)
   if board[inPos] == 10:
      print("This pawn can move " + str(legalMoves))
   if board[inPos] == 15 or board[inPos] == 25:
      tempBoard[endPos] = tempBoard[inPos]
      tempBoard[inPos] = 0
      death = IsPositionUnderThreat(tempBoard,endPos,player)
      if death == True:
         return False
      else:
         return True
    
   for i in legalMoves:
      if i == endPos:
         return True
   
   return False
   
   

main()

