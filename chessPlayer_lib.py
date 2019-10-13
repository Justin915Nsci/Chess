
def GenBoard():
   board = []
   for i in range(0,65,1):
      board = board + [0]
   board[0] = 13
   board[1] = 11
   board[2] = 12
   board[3] = 14
   board[4] = 15
   board[5] = 12
   board[6] = 11
   board[7] = 13
   for j in range(8,16,1):
       board[j] = 10
   for k in range(48,56,1):
       board[k] = 20
   board[56] = 23
   board[57] = 21
   board[58] = 22
   board[59] = 24
   board[60] = 25
   board[61] = 22
   board[62] = 21
   board[63] = 23
   return board

def PrintBoard(board):
   accum = []
   row = ""
   for i in range(0,len(board),1):
      if i<10:
         end = ")  "
      else:
         end = ") "
#      print(str(board[i]))
      if i%2 == 0:
         squareCol = 20
         #black square (_)
      else:
         squareCol = 10

      if board[i] == 0:
         player = 0
      elif board[i] >=20:
         player = 20
      else:
         player = 10

      if player == 0:
         if squareCol == 20:
            row = row + "__(" + str(i) + end
         else:
            row = row + "##(" + str(i) + end
#      print(str(board[i]-player))
      if player == 10:
         if board[i]-player == 0:
            row = row + "wP(" + str(i) + end
         elif board[i]-player == 1:
            row = row + "wN(" + str(i) + end 
         elif board[i]-player == 2:
            row = row + "wB(" + str(i) + end
         elif board[i]-player == 3:
            row = row + "wR(" + str(i) + end
         elif board[i]-player == 4:
            row = row + "wQ(" + str(i) + end
         elif board[i]-player == 5:
            row = row + "wK(" + str(i) + end

      elif player == 20:
         if board[i]-player == 0:
            row = row + "bP("+ str(i) + end
         elif board[i]-player == 1:
            row = row + "bN(" + str(i) + end
         elif board[i]-player == 2:
            row = row + "bB(" + str(i) + end
         elif board[i]-player == 3:
            row = row + "bR(" + str(i) + end
         elif board[i]-player == 4:
            row = row + "bQ(" + str(i) + end
         elif board[i]-player == 5:
            row = row + "bK(" + str(i) + end

      if (i+1)%8==0:
         accum = [row] + accum
         row = ""

   for j in range(0,len(accum),1):
          print(accum[j])

   return True

def GetPlayerPositions(board,player):
   playerPos = []
   for i in range(0,len(board),1):
       pos = board[i] - player
       if pos<player and pos>=0:
          playerPos = playerPos + [i]
   return playerPos
                  
   
def GetPawnMoves(board,position,player):
   legalMoves = []
#   print(str(board[position+8]))
   if player == 10:
      if (position + 8) <64 and board[position + 8] ==0:
         legalMoves = legalMoves + [position + 8]
#         print("pawn 4ward added")
      if (position + 7)<64 and (position+8)%8 != 0:
         #check if space occupied by enemy
         if board[position + 7]>=20:
            legalMoves = legalMoves + [position+7]
      if (position+9)<64 and (position+9)%8 != 0:
         if board[position + 7] >=20:
            legalMoves = legalMoves + [position+9]
   if player == 20:
      if (position - 8) >= 0 and board[position - 8] ==0:
         legalMoves = legalMoves + [position - 8]
      if (position - 7)>=0 and (position-7)%8 != 0:
         if board[position-7]<20 and board[position-7]>9:
            legalMoves = legalMoves + [position-7]
      if (position-9)>=0 and (position-8)%8 != 0:
         if board[position - 9]<20 and board[position-9]>9:
           legalMoves = legalMoves + [position-9]
   return legalMoves

def GetKnightMoves(board,position,player):
      legalMoves = []
      if player == 10:
         if (position + 17)<64 and (position + 17)%8!=0:
            if board[position + 17]>19 or board[position + 17] == 0:
               legalMoves = legalMoves + [position + 17]
         if (position+15)<64 and (position+15+1)%8!=0:
            if board[position + 15]>19 or board[position + 15] == 0:
               legalMoves = legalMoves + [position + 15]
         if (position+6)<64 and (position+6+1)%8!=0 and (position+6+2)%8!=0:
            if board[position+6]>19 or board[position+6] == 0:
               legalMoves = legalMoves + [position+6]
         if (position + 10)<64 and (position+10)%8!= 0 and (position+10-1)%8!=0:
            if board[position+10]>19 or board[position+10] == 0:
               legalMoves = legalMoves +[position+10]
         if (position - 17)>=0 and (position - 17+1)%8 != 0:
            if board[position-17]>19 or board[position - 17] == 0:
               legalMoves = legalMoves + [position-17]
         if (position - 15)>=0 and (position - 15)%8!=0:
            if board[position-15]>19 or board[position-16]==0:
               legalMoves =  legalMoves + [position - 15]
         if (position - 6) >= 0 and (position-6)%8 != 0 and (position-6-1)%8 !=0:
            if board[position - 6]>19 or board[position-6]==0:
               legalMoves = legalMoves + [position -6]
         if (position-10)>=0 and (position-10+1)%8!=0 and (position-10+2)%8!=0:
            if board[position -10]>19 or board[position - 10]==0:
               legalMoves = legalMoves + [position-10]                              

      if player == 20:
         if (position + 17)<64 and (position + 17)%8!=0:
            if (board[position+17]>9 and board[position+17]<16)or board[position + 17] == 0:
               legalMoves = legalMoves + [position + 17]
         if (position+15)<64 and (position+15+1)%8!=0:
            if (board[position + 15]>9 and board[position+15]<16) or board[position+15] == 0:
               legalMoves = legalMoves + [position + 15]
         if (position+6)<64 and (position+6+1)%8!=0 and (position+6+2)%8!=0:
            if (board[position+6]>9 and board[position+6]<16) or board[position+6] == 0:
               legalMoves = legalMoves + [position+6]
         if (position + 10)<64 and (position+10)%8!= 0 and (position+10-1)%8!=0:
            if (board[position+10]>9 and board[position+10<16])or board[position+10] == 0:
               legalMoves = legalMoves +[position+10]
         if (position - 17)>=0 and (position - 17-1)%8 != 0:
            if (board[position-17]>9 and board[position-17]<16) or board[position - 17] == 0:
               legalMoves = legalMoves + [position-17]
         if (position - 15)>=0 and (position - 15)%8!=0:
            if (board[position-15]>9 and board[position-15]<16) or board[position-16]==0:
               legalMoves =  legalMoves + [position - 15]
         if (position - 6) >= 0 and (position-6)%8 != 0 and (position-6-1)%8 !=0:
            if (board[position - 6]>9 and board[position-6]<16) or board[position-6]==0:
               legalMoves = legalMoves + [position -6]
         if (position-10)>=0 and (position-10+1)%8!=0 and (position-10+2)%8!=0:
            if (board[position -10]>9 and board[position<16])or board[position - 10]==0:
               legalMoves = legalMoves + [position-10]                              
      
      return legalMoves                                            

def GetBishopMoves(board,position,player):
   i = position + 7
   j = position + 9
   k = position - 9
   l = position - 7
   legalMoves = []
   if player == 10:
      while((i+1)%8!=0):
         if i>63:
            break
         if (i-7)%8 ==0:
            break
         if board[i]>19 or board[i]==0:
            legalMoves = legalMoves + [i]
            if board[i]>19:
               break;        
         else: 
            break 
         i = i + 7
      while(j%8!=0):
         if j>63:
            break
         if (j-9+1)%8==0:
            break
         if board[j]>19 or board[j]==0:
            legalMoves = legalMoves + [j]
            if board[j]>19:
               break;        
         else: 
            break 
         j = j + 9
      while(k%8!=0):
         if k<0:
            break
         if (k+9)%8 == 0:
            break
         if board[k]>19 or board[k]==0:
            legalMoves = legalMoves + [k]
            if board[k]>19:
               break;        
         else: 
            break 
         k = k - 9
      while((l+1)%8!=0):
         if l<0:
            break
         if (l+7+1)%8 == 0:
            break
         if board[l]>19 or board[l]==0:
            legalMoves = legalMoves + [l]
            if board[l]>19:
               break;        
         else: 
            break 

         l = l -7

   i = position + 7
   j = position + 9
   k = position - 9
   l = position - 7

   if player == 20:
      while((i+1)%8!=0):
         if i>63:
            break
         if (i-7)% 8== 0:
            break
#         print("in while loop")
         if (board[i]>9 and board[i]<16) or board[i]==0:
            legalMoves = legalMoves + [i]
#            print("in if statement left up diagonal")
            if board[i]>9:
               break;        
         else: 
            break 
         i = i + 7
         if i>63:
            break

      while(j%8!=0):
         if j>63:
            break
         if (j-9+1)%8 == 0:
            break
         if (board[j]>9 and board[j]<16) or board[j]==0:
            legalMoves = legalMoves + [j]
            if board[j]>9:
               break        
         else: 
            break 
         j = j + 9
         if j>63:
            break
      while(k%8!=0):
         if k<0:
            break
         if (k+9)%8 == 0:
            break
         if (board[k]>9 and board[k]<16) or board[k]==0:
            legalMoves = legalMoves + [k]
            if board[k]>9:
               break;       
         else: 
            break 
         k = k - 9
         if k<0:
            break
      while((l+1)%8!=0):
         if l<0:
            break
         if (l+7+1)%8 == 0:
            break
         if (board[l]>9 and board[l]<16)or board[l]==0:
            legalMoves = legalMoves + [l]
            if board[l]>9:
               break        
         else:
            break
         l = l - 7                                        
 
   return legalMoves                                          



def GetRookMoves(board,position,player):
   legalMoves = []
   i = position + 8
   j = position -1
   k = position +1
   l = position - 8
   
   if player ==10:
      while (i<63):
         if board[i]>19 or board[i] == 0:
            legalMoves = legalMoves + [i]
            if board[i]>19:
               break       
         else:
            break
         i = i +8
      while ((j+1)%8!=0):
         if board[j]>19 or board[j] == 0:
            legalMoves = legalMoves + [j]
            if board[j]>19:
               break       
         else:
            break
         j = j-1
      while ((k)%8!=0):
#         print(str(board[k]))
         if board[k]>19 or board[k]==0:
            legalMoves = legalMoves + [k]
            if board[k]>19:
               break       
         else:
            break
         k = k+1
      while (l>=0):
         if board[l]>19 or board[l] == 0:
            legalMoves = legalMoves + [l]
            if board[l]>19:
               break       
         else:
            break
         l = l -8                               

   i = position + 8
   j = position -1
   k = position +1
   l = position - 8
   
   if player ==20:
      while (i<63):
         if (board[i]>9 and board[i]<16) or board[i] == 0:
            legalMoves = legalMoves + [i]
            if board[i]>19:
               break       
         else:
            break
         i = i +8
      while ((j+1)%8!=0):
         if (board[j]>9 and board[j]<16) or board[j] == 0:
            legalMoves = legalMoves + [j]
            if board[j]>19:
               break       
         else:
            break
         j = j-1
      while ((k)%8!=0):
#         print(str(board[k]))
         if (board[k]>9 and board[k]<16) or board[k]==0:
            legalMoves = legalMoves + [k]
            if board[k]>19:
               break       
         else:
            break
         k = k+1
      while (l>=0):
         if (board[l]>9 and board[l]<16) or board[l] == 0:
            legalMoves = legalMoves + [l]
            if board[l]>19:
               break       
         else:
            break
         l = l -8                                                

   return legalMoves

def GetQueenMoves(board,position,player):
   legalMoves = []
   i = position + 7
   j = position + 9
   k = position - 9
   l = position - 7
   legalMoves = []
   if player == 10:
      while((i+1)%8!=0):
         if i>63:
            break
         if (i-7)%8 ==0:
            break
         if board[i]>19 or board[i]==0:
            legalMoves = legalMoves + [i]
            if board[i]>19:
               break;        
         else: 
            break 
         i = i + 7
      while(j%8!=0):
         if j>63:
            break
         if (j-9+1)%8==0:
            break
         if board[j]>19 or board[j]==0:
            legalMoves = legalMoves + [j]
            if board[j]>19:
               break;        
         else: 
            break 
         j = j + 9
      while(k%8!=0):
         if k<0:
            break
         if (k+9)%8 == 0:
            break
         if board[k]>19 or board[k]==0:
            legalMoves = legalMoves + [k]
            if board[k]>19:
               break;        
         else: 
            break 
         k = k - 9
      while((l+1)%8!=0):
         if l<0:
            break
         if (l+7+1)%8 == 0:
            break
         if board[l]>19 or board[l]==0:
            legalMoves = legalMoves + [l]
            if board[l]>19:
               break;        
         else: 
            break 

         l = l -7

   i = position + 7
   j = position + 9
   k = position - 9
   l = position - 7

   if player == 20:
      while((i+1)%8!=0 and i<64):
         if i>63:
            break
         if (i-7)% 8== 0:
            break
#         print("in while loop")
         if (board[i]>9 and board[i]<16) or board[i]==0:
            legalMoves = legalMoves + [i]
#            print("in if statement left up diagonal")
            if board[i]>9:
               break;        
         else: 
            break 
         i = i + 7
         if i>63:
            break

      while(j%8!=0 and j<64):
         if j>63:
            break
         if (j-9+1)%8 == 0:
            break
         if (board[j]>9 and board[j]<16) or board[j]==0:
            legalMoves = legalMoves + [j]
            if board[j]>9:
               break        
         else: 
            break 
         j = j + 9
         if j>63:
            break
      while(k%8!=0 and k>=0):
         if k<0:
            break
         if (k+9)%8 == 0:
            break
         if (board[k]>9 and board[k]<16) or board[k]==0:
            legalMoves = legalMoves + [k]
            if board[k]>9:
               break;       
         else: 
            break 
         k = k - 9
         if k<0:
            break
      while((l+1)%8!=0 and l>=0):
         if l<0:
            break
         if (l+7+1)%8 == 0:
            break
         if (board[l]>9 and board[l]<16)or board[l]==0:
            legalMoves = legalMoves + [l]
            if board[l]>9:
               break        
         else:
            break
         l = l - 7                                        

   i2 = position + 8
   j2 = position -1
   k2 = position +1
   l2 = position - 8
   
   if player ==10:
      while (i2<64):
         if board[i2]>19 or board[i2] == 0:
            legalMoves = legalMoves + [i2]
            if board[i2]>19:
               break       
         else:
            break
         i2 = i2 +8
      while ((j2+1)%8!=0 and (j2)<64):
         if board[j2]>19 or board[j2] == 0:
            legalMoves = legalMoves + [j2]
            if board[j2]>19:
               break       
         else:
            break
         j2 = j2-1
      while ((k2)%8!=0 and (k2)<64):
#         print(str(board[k]))
         if board[k2]>19 or board[k2]==0:
            legalMoves = legalMoves + [k2]
            if board[k2]>19:
               break       
         else:
            break
         k2 = k2+1
      while (l2>=0):
         if board[l2]>19 or board[l2] == 0:
            legalMoves = legalMoves + [l2]
            if board[l2]>19:
               break       
         else:
            break
         l2 = l2 -8                               

   i2 = position + 8
   j2 = position -1
   k2 = position +1
   l2 = position - 8
   
   if player ==20:
      while (i2<63):
         if (board[i2]>9 and board[i2]<16) or board[i2] == 0:
            legalMoves = legalMoves + [i2]
            if board[i2]>9:
               break       
         else:
            break
         i2 = i2 +8
      while ((j2+1)%8!=0):
         if (board[j2]>9 and board[j2]<16) or board[j2] == 0:
            legalMoves = legalMoves + [j2]
            if board[j2]>9:
               break       
         else:
            break
         j2 = j2-1
      while ((k2)%8!=0):
#         print(str(board[k]))
         if (board[k2]>9 and board[k2]<16) or board[k2]==0:
            legalMoves = legalMoves + [k2]
            if board[k2]>9:
               break       
         else:
            break
         k2 = k2+1
      while (l2>=0):
         if (board[l2]>9 and board[l2]<16) or board[l2] == 0:
            legalMoves = legalMoves + [l2]
            if board[l2]>9:
               break       
         else:
            break
         l2 = l2 -8                                                

   return legalMoves

def GetKingMoves(board,position,player):
   legalMoves = []
   if player == 10:
      if (position + 8)<64:
         if board[position + 8]>19 or board[position+8]==0:
            temp = list(board)
            temp[position + 8] = 15
            temp[position] = 0
            cantMove = IsPositionUnderThreat(temp,position+8,10)
   #         if cantMove == False:
            legalMoves = legalMoves + [position + 8]            
      if board[position + 1]<64:
         if (position + 1)>19 or board[position+1]==0:          
            temp = list(board)
            temp[position + 1] = 15
            temp[position] = 0
            cantMove = IsPositionUnderThreat(temp,position+1,10)
  #          if cantMove == False:
            legalMoves = legalMoves + [position + 1]         
      if (position -1)>=0:
         if board[position - 1]>19 or board[position-1]==0:          
            temp = list(board)
            temp[position - 1] = 15
            temp[position] = 0
#            PrintBoard(temp)
            cantMove = IsPositionUnderThreat(temp,position-1,10)
 #           if cantMove == False:
            legalMoves = legalMoves + [position - 1]         


            legalMoves = legalMoves + [position - 1]
      if (position - 8)>=0:
         if board[position - 8]>19 or board[position-8]==0:          
            temp = list(board)
            temp[position - 8] = 15
            temp[position] = 0
            cantMove = IsPositionUnderThreat(temp,position-8,10)
 #           if cantMove == False:
            legalMoves = legalMoves + [position - 8]         

      if position+7<64 and position%8 != 0:
         if board[position + 7]>19 or board[position+7]==0: 
            temp = list(board)
            temp[position + 7] = 15
            temp[position] = 0
            cantMove = IsPositionUnderThreat(temp,position+7,10)
#            if cantMove == False:
            legalMoves = legalMoves + [position + 7]         

      if position + 9<64 and (position+1)%8 != 0:
         if board[position + 9]>19 or board[position + 9]==0:
            temp = list(board)
            temp[position + 9] = 15
            temp[position] = 0
            cantMove = IsPositionUnderThreat(temp,position+9,10)
 #           if cantMove == False:
            legalMoves = legalMoves + [position + 9]
         
      if position-7>=0 and (position + 1)%8:
         if board[position -7]>19 or board[position-7] == 0:
            temp = list(board)
            temp[position - 7] = 15
            temp[position] = 0
            cantMove = IsPositionUnderThreat(temp,position-7,10)
  #          if cantMove == False:
            legalMoves = legalMoves + [position - 7]         

      if position-9>=0 and position%8!=0:
         if board[position -9]>19 or board[position - 9] == 0:           
            temp = list(board)
            temp[position - 9] = 15
            temp[position] = 0
            cantMove = IsPositionUnderThreat(temp,position-9,10)
   #         if cantMove == False:
            legalMoves = legalMoves + [position - 9]           

   else:        
      if position + 8<64:
#         print("foward position is " + str(board[position + 8]))
         if (board[position + 8]>9 and board[position + 8]<16) or board[position+8]==0:
            legalMoves = legalMoves + [position + 8]         
      if position + 1<64:
         if (board[position + 1]>9 and board[position + 1]<16) or board[position+1]==0:
             legalMoves = legalMoves + [position + 1]
      if position -1>=0:
         if (board[position - 1]>9 and board[position - 1]<16) or board[position-1]==0:
             legalMoves = legalMoves + [position - 1]

      if position - 8>=0:
         if (board[position - 8]>9 and board[position - 8]<16) or board[position-8]==0:
             legalMoves = legalMoves + [position - 8]         

      if position+7<64 and position%8 != 0:
         if (board[position + 7]>9 and board[position + 7]<16) or board[position+7]==0: 
            legalMoves = legalMoves + [position + 7]
      if position + 9<64 and (position+1)%8 != 0:
         if (board[position + 9]>9 and board[position + 9]<16) or board[position + 9]==0:
            legalMoves = legalMoves + [position + 9]
      if position-7>=0 and (position + 1)%8:
         if (board[position -7]>9 and board[position -7]<16) or board[position-7] == 0:
            legalMoves = legalMoves + [position - 7]
      if position-9>=0 and position%8!=0:
         if (board[position -9]>9 and board[position -9]<16) or board[position - 9] == 0:
            legalMoves = legalMoves + [position - 9]           



   return legalMoves


def GetPieceLegalMoves(board,position):
   legalMoves = []
   if board[position] == 0:
      return legalMoves
   if board[position] >= 20:
      player = 20
   else:
      player = 10
   piece = board[position] - player
#   print(str(player))
   if piece == 0:
      legalMoves = GetPawnMoves(board,position,player)

   elif piece == 1:
      legalMoves = GetKnightMoves(board,position,player)
#   print(str(legalMoves))
   elif piece == 2:
      legalMoves = GetBishopMoves(board,position,player)
   elif piece == 3:
      legalMoves = GetRookMoves(board,position,player)
   elif piece == 4:
      legalMoves = GetQueenMoves(board,position,player)
   else:
      legalMoves = GetKingMoves(board,position,player)
   return legalMoves

def IsPositionUnderThreat(board,position,player):
   if player == 10:
      opponent = 20
   else:
      opponent = 10
   dangerPos = []
   enemyPos = GetKnightMoves(board,position,player)
   for i in enemyPos:
      if board[i]!=0:
         dangerPos = dangerPos + [i]
   enemyPos = GetQueenMoves(board,position,player)
   for i in enemyPos:
      if board[i]!=0:
         dangerPos = dangerPos + [i]
#   print(str(dangerPos))
   for j in dangerPos:
      killerMoves = GetPieceLegalMoves(board,j)
      #iterate through killerMoves
      for k in killerMoves:
         if k == position:
            return True


   return False


board = GenBoard()
pos = 41
board[pos] = 10
#board[41] = 10
#board[25] = 24
#board[17] = 24
#board[26] = 22
#print(str(IsPositionUnderThreat(board,pos,10)))
#print(str(GetPieceLegalMoves(board,pos)))

#:wq
#PrintBoard(board)
