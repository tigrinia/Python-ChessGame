import pygame
import math

# initializing the game
pygame.init()
screen = pygame.display.set_mode((400,400))

def drawBoard():
    for i in range(0,8):
        for j in range(0,8):
            if (i + j) % 2 == 0:
                pygame.draw.rect(screen, (230, 250, 255), (j*50,i*50,50,50))
            else:
                pygame.draw.rect(screen, (185, 247, 176), (j*50,i*50,50,50))

# Creating the chessboard in Backend
chessBoard = [
    [9,10,11,12,13,14,15,16],
    [1,2,3,4,5,6,7,8],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [17,18,19,20,21,22,23,24],
    [25,26,27,28,29,30,31,32]
]

numberOfMoves = 0

class Gameplay:
    def __init__(self, name, color, idNum ,image):
        self.name = name
        self.color = color
        self.idNum = idNum
        self.image = image
        self.selected = False
        self.listOfMoves = []
        
        for array in chessBoard:
            for piece in array:
                if piece == self.idNum:
                    self.coordinates = (array.index(piece), chessBoard.index(array))

        if self.name == 'Pawn':
            self.firstMove = True
        
        if self.name == 'King':
            self.checked = False

    def possibleMoves(self):
        listOfQueenMoves = []
        X, Y = self.coordinates
        listOfPossibleMoves = []
        if self.name == 'Pawn':
            if self.color == 'W':
                try:
                    if 0 < chessBoard[Y - 1][X - 1] <= 16:
                        listOfPossibleMoves.append((X*50 - 25, Y*50 - 25))
                except:
                    pass
                try:
                    if chessBoard[Y - 1][X] == 0:
                        if self.firstMove == True and chessBoard[Y -2][X] == 0:
                            listOfPossibleMoves.append((X*50 + 25, Y*50 - 25))
                            listOfPossibleMoves.append((X*50 + 25, Y*50 - 75))
                        else:
                            listOfPossibleMoves.append((X*50 + 25, Y*50 - 25))
                except:
                    pass
                try:
                    if 0 < chessBoard[Y - 1][X + 1] <= 16:
                        listOfPossibleMoves.append((X*50 + 75, Y*50 - 25))
                except:
                    pass

                return listOfPossibleMoves
            
            if self.color == 'B':
                try:
                    if chessBoard[Y + 1][X - 1] >= 17:
                        listOfPossibleMoves.append((X*50 - 25, Y*50 + 75))
                except:
                    pass
                try:
                    if chessBoard[Y + 1][X] == 0:
                        if self.firstMove == True and chessBoard[Y + 2][X] == 0:
                            listOfPossibleMoves.append((X*50 + 25, Y*50 + 75))
                            listOfPossibleMoves.append((X*50 + 25, Y*50 + 125))
                        else:
                            listOfPossibleMoves.append((X*50 + 25, Y*50 + 75))
                except:
                    pass
                try:
                    if chessBoard[Y + 1][X + 1] >= 17:
                        listOfPossibleMoves.append((X*50 + 75, Y*50 + 75))
                except:
                    pass
                return listOfPossibleMoves

        if self.name == 'Knight':
            for i in range(-2,3):
                for j in range(-2,3):
                    if i != 0 and j != 0:
                        if i != j and -i != j:
                            if self.color == 'W':
                                try:
                                    if chessBoard[Y + i][X + j] <= 16 or chessBoard[Y + i][X + j] == 0:
                                        if X*50 + j*50 + 25 >=0 and Y*50 + i*50 + 25 >= 0:
                                            listOfPossibleMoves.append((X*50 + j*50 + 25, Y*50 + i*50 + 25))
                                except:
                                    pass
                            
                            if self.color == 'B':
                                try:
                                    if chessBoard[Y + i][X + j] >= 17 or chessBoard[Y + i][X + j] == 0:
                                        if X*50 + j*50 + 25 >=0 and Y*50 + i*50 + 25 >= 0:
                                            listOfPossibleMoves.append((X*50 + j*50 + 25, Y*50 + i*50 + 25))
                                except:
                                    pass
            
            return listOfPossibleMoves

        if self.name == 'Rook' or self.name == 'Queen':
            for i in range(1,8):
                try:
                    if chessBoard[Y][X + i] == 0:
                        if X*50 + i*50 + 25 >=0 and Y*50 + 25 >= 0:
                            listOfPossibleMoves.append((X*50 + i*50 + 25, Y*50 + 25))
                            listOfQueenMoves.append((X*50 + i*50 + 25, Y*50 + 25))
                    elif self.color == 'B':
                        if chessBoard[Y][X + i] >= 17:
                            if X*50 + i*50 + 25 >=0 and Y*50 + 25 >= 0:
                                listOfPossibleMoves.append((X*50 + i*50 + 25, Y*50 + 25))
                                listOfQueenMoves.append((X*50 + i*50 + 25, Y*50 + 25))
                                break
                        elif 0 < chessBoard[Y][X + i] <= 16:
                            break
                    elif self.color == 'W':
                        if 0 < chessBoard[Y][X + i] <= 16:
                            if X*50 + i*50 + 25 >=0 and Y*50 + 25 >= 0:
                                listOfPossibleMoves.append((X*50 + i*50 + 25, Y*50 + 25))
                                listOfQueenMoves.append((X*50 + i*50 + 25, Y*50 + 25))
                                break
                        elif chessBoard[Y][X + i] >= 17:
                            break
                except:
                    pass

            for i in range(1,8):
                try:
                    if chessBoard[Y][X - i] == 0:
                        if X*50 - i*50 + 25 >=0 and Y*50 + 25 >= 0:
                            listOfPossibleMoves.append((X*50 - i*50 + 25, Y*50 + 25))
                            listOfQueenMoves.append((X*50 - i*50 + 25, Y*50 + 25))
                    elif self.color == 'B':
                        if chessBoard[Y][X - i] >= 17:
                            if X*50 - i*50 + 25 >=0 and Y*50 + 25 >= 0:
                                listOfPossibleMoves.append((X*50 - i*50 + 25, Y*50 + 25))
                                listOfQueenMoves.append((X*50 - i*50 + 25, Y*50 + 25))
                                break
                        elif 0 < chessBoard[Y][X - i] <= 16:
                            break
                    elif self.color == 'W':
                        if 0 < chessBoard[Y][X - i] <= 16:
                            if X*50 - i*50 + 25 >=0 and Y*50 + 25 >= 0:
                                listOfPossibleMoves.append((X*50 - i*50 + 25, Y*50 + 25))
                                listOfQueenMoves.append((X*50 - i*50 + 25, Y*50 + 25))
                                break
                        elif chessBoard[Y][X - i] >= 17:
                            break
                except:
                    pass

            for i in range(1,8):
                try:
                    if chessBoard[Y + i][X] == 0:
                        if X*50 + 25 >=0 and Y*50 + i*50 + 25 >= 0:
                            listOfPossibleMoves.append((X*50 + 25, Y*50 + i*50 + 25))
                            listOfQueenMoves.append((X*50 + 25, Y*50 + i*50 + 25))
                    elif self.color == 'B':
                        if chessBoard[Y + i][X] >= 17:
                            if X*50 + 25 >=0 and Y*50 + i*50 + 25 >= 0:
                                listOfPossibleMoves.append((X*50 + 25, Y*50 + i*50 + 25))
                                listOfQueenMoves.append((X*50 + 25, Y*50 + i*50 + 25))
                                break
                        elif 0 < chessBoard[Y + i][X] <= 16:
                            break
                    elif self.color == 'W':
                        if 0 < chessBoard[Y + i][X] <= 16:
                            if X*50 + 25 >=0 and Y*50 + i*50 + 25 >= 0:
                                listOfPossibleMoves.append((X*50 + 25, Y*50 + i*50 + 25))
                                listOfQueenMoves.append((X*50 + 25, Y*50 + i*50 + 25))
                                break
                        elif chessBoard[Y + i][X] >= 17:
                            break
                except:
                    pass

            for i in range(1,8):
                try:
                    if chessBoard[Y - i][X] == 0:
                        if X*50 + 25 >=0 and Y*50 - i*50 + 25 >= 0:
                            listOfPossibleMoves.append((X*50 + 25, Y*50 - i*50 + 25))
                            listOfQueenMoves.append((X*50 + 25, Y*50 - i*50 + 25))
                    elif self.color == 'B':
                        if chessBoard[Y - i][X] >= 17:
                            if X*50 + 25 >=0 and Y*50 - i*50 + 25 >= 0:
                                listOfPossibleMoves.append((X*50 + 25, Y*50 - i*50 + 25))
                                listOfQueenMoves.append((X*50 + 25, Y*50 - i*50 + 25))
                                break
                        elif 0 < chessBoard[Y - i][X] <= 16:
                            break
                    elif self.color == 'W':
                        if 0 < chessBoard[Y - i][X] <= 16:
                            if X*50 + 25 >=0 and Y*50 -i*50 + 25 >= 0:
                                listOfPossibleMoves.append((X*50 + 25, Y*50 - i*50 + 25))
                                listOfQueenMoves.append((X*50 + 25, Y*50 - i*50 + 25))
                                break
                        elif chessBoard[Y - i][X] >= 17:
                            break
                except:
                    pass
            if self.name == 'Rook':
                return listOfPossibleMoves

        if self.name == 'Bishop' or self.name == 'Queen':
            for i in range(1,8):    
                    try:
                        if chessBoard[Y + i][X + i] == 0:
                            if X*50 + i*50 + 25 >= 0 and Y*50 + i*50 + 25 > 0:
                                listOfPossibleMoves.append((X*50 + i*50 + 25, Y*50 + i*50 + 25))
                                listOfQueenMoves.append((X*50 + i*50 + 25, Y*50 + i*50 + 25))
                        elif self.color == 'B':
                            if chessBoard[Y + i][X + i] >= 17:
                                if X*50 + i*50 + 25 >= 0 and Y*50 + i*50 + 25 >= 0:
                                    listOfPossibleMoves.append((X*50 + i*50 + 25, Y*50 + i*50 + 25))
                                    listOfQueenMoves.append((X*50 + i*50 + 25, Y*50 + i*50 + 25))
                                    break
                            elif 0 < chessBoard[Y + i][X + i] <= 16:
                                break
                        elif self.color == 'W':
                            if 0 < chessBoard[Y + i][X + i] <= 16:
                                if X*50 + i*50 + 25 >= 0 and Y*50 + i*50 + 25 >= 0:
                                    listOfPossibleMoves.append((X*50 + i*50 + 25, Y*50 + i*50 + 25))
                                    listOfQueenMoves.append((X*50 + i*50 + 25, Y*50 + i*50 + 25))
                                    break
                            elif chessBoard[Y + i][X + i] >= 17:
                                break
                    except:
                        pass
                
            for i in range(1,8):    
                    try:
                        if chessBoard[Y + i][X - i] == 0:
                            if X*50 - i*50 + 25 >= 0 and Y*50 + i*50 + 25 >= 0:
                                listOfPossibleMoves.append((X*50 - i*50 + 25, Y*50 + i*50 + 25))
                                listOfQueenMoves.append((X*50 - i*50 + 25, Y*50 + i*50 + 25))
                        elif self.color == 'B':
                            if chessBoard[Y + i][X - i] >= 17:
                                if X*50 -i*50 + 25 >= 0 and Y*50 + i*50 + 25 >= 0:
                                    listOfPossibleMoves.append((X*50 -i*50 + 25, Y*50 + i*50 + 25))
                                    listOfQueenMoves.append((X*50 -i*50 + 25, Y*50 + i*50 + 25))
                                    break
                            elif chessBoard[Y + i][X - i] <= 16:
                                break
                        elif self.color == 'W':
                            if 0 < chessBoard[Y + i][X - i] <= 16:
                                if X*50 -i*50 + 25 >= 0 and Y*50 + i*50 + 25 >= 0:
                                    listOfPossibleMoves.append((X*50 -i*50 + 25, Y*50 + i*50 + 25))
                                    listOfQueenMoves.append((X*50 -i*50 + 25, Y*50 + i*50 + 25))
                                    break
                            elif chessBoard[Y + i][X - i] >= 17:
                                break
                    except:
                        pass
                
            for i in range(1,8):    
                    try:
                        if chessBoard[Y - i][X - i] == 0:
                            if X*50 - i*50 + 25 >= 0 and Y*50 - i*50 + 25 >= 0:
                                listOfPossibleMoves.append((X*50 - i*50 + 25, Y*50 - i*50 + 25))
                                listOfQueenMoves.append((X*50 - i*50 + 25, Y*50 - i*50 + 25))
                        elif self.color == 'B':
                            if chessBoard[Y - i][X - i] >= 17:
                                if X*50 - i*50 + 25 >= 0 and Y*50 - i*50 + 25 >= 0:
                                    listOfPossibleMoves.append((X*50 - i*50 + 25, Y*50 - i*50 + 25))
                                    listOfQueenMoves.append((X*50 - i*50 + 25, Y*50 - i*50 + 25))
                                    break
                            elif 0 < chessBoard[Y - i][X - i] <= 16:
                                break
                        elif self.color == 'W':
                            if 0 < chessBoard[Y - i][X - i] <= 16:
                                if X*50 - i*50 + 25 >= 0 and Y*50 - i*50 + 25 >= 0:
                                    listOfPossibleMoves.append((X*50 - i*50 + 25, Y*50 - i*50 + 25))
                                    listOfQueenMoves.append((X*50 - i*50 + 25, Y*50 - i*50 + 25))
                                    break
                            elif chessBoard[Y - i][X - i] >= 17:
                                break
                    except:
                        pass
                
            for i in range(1,8):    
                    try:
                        if chessBoard[Y - i][X + i] == 0:
                            if X*50 + i*50 + 25 >= 0 and Y*50 - i*50 + 25 >= 0:
                                listOfPossibleMoves.append((X*50 + i*50 + 25, Y*50 - i*50 + 25))
                                listOfQueenMoves.append((X*50 + i*50 + 25, Y*50 - i*50 + 25))
                        elif self.color == 'B':
                            if chessBoard[Y - i][X + i] >= 17:
                                if X*50 + i*50 + 25 >= 0 and Y*50 - i*50 + 25 >= 0:
                                    listOfPossibleMoves.append((X*50 + i*50 + 25, Y*50 - i*50 + 25))
                                    listOfQueenMoves.append((X*50 + i*50 + 25, Y*50 - i*50 + 25))
                                    break
                            elif 0 < chessBoard[Y - i][X + i] <= 16:
                                break
                        elif self.color == 'W':
                            if 0 < chessBoard[Y - i][X + i] <= 16:
                                if X*50 + i*50 + 25 >= 0 and Y*50 - i*50 + 25 >= 0:
                                    listOfPossibleMoves.append((X*50 + i*50 + 25, Y*50 - i*50 + 25))
                                    listOfQueenMoves.append((X*50 + i*50 + 25, Y*50 - i*50 + 25))
                                    break
                            elif chessBoard[Y - i][X + i] >= 17:
                                break
                    except:
                        pass
            if self.name == 'Bishop': 
                return listOfPossibleMoves

            else:
                return listOfQueenMoves

        if self.name == 'King':
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i != 0 or j != 0:
                        try:
                            if chessBoard[Y + i][X + j] == 0:
                                if X*50 + j*50 + 25 >= 0 and Y*50 + i*50 + 25 >= 0:
                                    listOfPossibleMoves.append((X*50 + j*50 + 25, Y*50 + i*50 + 25))
                            elif self.color == 'B':
                                if chessBoard[Y + i][X + j] >= 17:
                                    if X*50 + j*50 + 25 >= 0 and Y*50 + i*50 + 25 >= 0:
                                        listOfPossibleMoves.append((X*50 + j*50 + 25, Y*50 + i*50 + 25))
                            elif self.color == 'W':
                                if 0 < chessBoard[Y + i][X + j] <= 16:
                                    if X*50 + j*50 + 25 >= 0 and Y*50 + i*50 + 25 >= 0: 
                                        listOfPossibleMoves.append((X*50 + j*50 + 25, Y*50 + i*50 + 25))
                        except:
                            pass
            
            return listOfPossibleMoves

     

    def display(self):
        def selection():
            if pygame.mouse.get_pressed() == (1,0,0) and abs(X - math.floor(A/50)) == 0 and abs(Y - math.floor(B/50)) == 0:
                self.selected = True
            elif pygame.mouse.get_pressed() == (0,0,1) and abs(X - math.floor(A/50)) == 0 and abs(Y - math.floor(B/50)) == 0:
                self.selected = False


        def move():
            global numberOfMoves
            if self.selected == True:
                listOfPieces = listOfWhitePieces + listOfBlackPieces
                for p in listOfPieces:
                    if p.idNum != self.idNum:
                        p.selected = False

                if len(self.listOfMoves) > 0:
                    for possibleMove in self.listOfMoves:
                        Px, Py = possibleMove
                        pygame.draw.circle(screen, (255,100,100), possibleMove, 5)
                        if pygame.mouse.get_pressed() == (1,0,0) and abs(math.floor(A/50) - math.floor(Px/50)) == 0 and abs(math.floor(B/50) - math.floor(Py/50)) == 0:
                            self.selected = False
                            self.firstMove = False
                            chessBoard[Y][X] = 0
                            chessBoard[math.floor(Py/50)][math.floor(Px/50)] = self.idNum
                            self.coordinates = (math.floor(Py/50),math.floor(Px/50))
                            numberOfMoves += 1

        if self.name == 'Pawn':
            if self.idNum in chessBoard[7] or self.idNum in chessBoard[0]:
                self.name = 'Queen'
                if self.color == 'W':
                    self.image = pygame.image.load('chess/QueenW.png')
                else:
                    self.image = pygame.image.load('chess/QueenB.png')

        def seeCheck(king):
            D, C = king.coordinates
            if king.color == 'W':
                listOfPieces = listOfBlackPieces
            else:
                listOfPieces = listOfWhitePieces
            
            for arr in chessBoard:
                for pie in arr:
                    for pi in listOfPieces:
                        if pie == pi.idNum:
                            pi.listOfMoves = pi.possibleMoves()
                            if len(pi.listOfMoves) > 0:
                                for myMove in pi.listOfMoves:
                                    B, A = myMove
                                    if D - math.floor(B/50) == 0 and C - math.floor(A/50) == 0:
                                        return True

        for array in chessBoard:
            for piece in array:
                if piece == self.idNum:
                    self.coordinates = (array.index(piece), chessBoard.index(array))
                    X, Y = self.coordinates
                    screen.blit(self.image, (X*50 +15, Y*50 + 10))
                    A, B = pygame.mouse.get_pos()
                    if self.color == 'W':
                        kingW.checked = seeCheck(kingW)
                        if kingW.checked != True:
                            self.listOfMoves = self.possibleMoves()
                            listOfIllegalmove = []
                            if len(self.listOfMoves) > 0:
                                for mo in self.listOfMoves:
                                    Q, W = mo
                                    element = chessBoard[math.floor(W/50)][math.floor(Q/50)]
                                    chessBoard[Y][X] = 0
                                    chessBoard[math.floor(W/50)][math.floor(Q/50)] = self.idNum
                                    self.coordinates = (math.floor(Q/50), math.floor(W/50))
                                    if seeCheck(kingW) == True:
                                        listOfIllegalmove.append(mo)
                                    
                                    chessBoard[Y][X] = self.idNum
                                    chessBoard[math.floor(W/50)][math.floor(Q/50)] = element
                                    self.coordinates = (X,Y)

                                for i in listOfIllegalmove:
                                    if i in self.listOfMoves:
                                        self.listOfMoves.pop(self.listOfMoves.index(i))
                        
                        else:
                            print('White is checked')
                            if len(self.listOfMoves) > 0:
                                listOfLegalmove = []
                                for mo in self.listOfMoves:
                                    Q, W = mo
                                    element = chessBoard[math.floor(W/50)][math.floor(Q/50)]
                                    chessBoard[Y][X] = 0
                                    chessBoard[math.floor(W/50)][math.floor(Q/50)] = self.idNum
                                    self.coordinates = (math.floor(Q/50), math.floor(W/50))
                                    if seeCheck(kingW) != True:
                                        listOfLegalmove.append(mo)

                                    chessBoard[Y][X] = self.idNum
                                    chessBoard[math.floor(W/50)][math.floor(Q/50)] = element
                                    self.coordinates = (X,Y)
                                self.listOfMoves = listOfLegalmove
                            else:
                                self.listOfMoves = []
                        
                        if numberOfMoves % 2 == 0:
                            selection()
                            move()

                    else:
                        kingB.checked = seeCheck(kingB)
                        if kingB.checked != True:
                            self.listOfMoves = self.possibleMoves()
                            listOfIllegalmoves = []
                            if len(self.listOfMoves) > 0:
                                for m in self.listOfMoves:
                                    Q, W = m
                                    element = chessBoard[math.floor(W/50)][math.floor(Q/50)]
                                    chessBoard[Y][X] = 0
                                    chessBoard[math.floor(W/50)][math.floor(Q/50)] = self.idNum
                                    self.coordinates = (math.floor(Q/50), math.floor(W/50))
                                    if seeCheck(kingB) == True:
                                        listOfIllegalmoves.append(m)
                                    
                                    chessBoard[Y][X] = self.idNum
                                    chessBoard[math.floor(W/50)][math.floor(Q/50)] = element
                                    self.coordinates = (X,Y)

                                for i in listOfIllegalmoves:
                                    if i in self.listOfMoves:
                                        self.listOfMoves.pop(self.listOfMoves.index(i))
                        
                        else:
                            print('Black is checked')
                            if len(self.listOfMoves) > 0:
                                listOfLegalmoves = []
                                for m in self.listOfMoves:
                                    Q, W = m
                                    element = chessBoard[math.floor(W/50)][math.floor(Q/50)]
                                    chessBoard[Y][X] = 0
                                    chessBoard[math.floor(W/50)][math.floor(Q/50)] = self.idNum
                                    self.coordinates = (math.floor(Q/50), math.floor(W/50))
                                    if seeCheck(kingB) != True:
                                        listOfLegalmoves.append(m)

                                    chessBoard[Y][X] = self.idNum
                                    chessBoard[math.floor(W/50)][math.floor(Q/50)] = element
                                    self.coordinates = (X,Y)
                                self.listOfMoves = listOfLegalmoves
                            else:
                                self.listOfMoves = []
                        if numberOfMoves % 2 == 1:
                            selection()
                            move()
        
        Chess = []
        for array in chessBoard:
            for piece in array:
                Chess.append(piece)
        
        if self.idNum not in Chess:
            self.coordinates = None
            self.listOfMoves = []
        
pawnB1 = Gameplay('Pawn', 'B', 1 ,pygame.image.load('chess/PawnB.png'))
pawnB2 = Gameplay('Pawn', 'B', 2 ,pygame.image.load('chess/PawnB.png'))
pawnB3 = Gameplay('Pawn', 'B', 3 ,pygame.image.load('chess/PawnB.png'))
pawnB4 = Gameplay('Pawn', 'B', 4, pygame.image.load('chess/PawnB.png'))
pawnB5 = Gameplay('Pawn', 'B', 5, pygame.image.load('chess/PawnB.png'))
pawnB6 = Gameplay('Pawn', 'B', 6, pygame.image.load('chess/PawnB.png'))
pawnB7 = Gameplay('Pawn', 'B', 7, pygame.image.load('chess/PawnB.png'))
pawnB8 = Gameplay('Pawn', 'B', 8, pygame.image.load('chess/PawnB.png'))
rookB1 = Gameplay('Rook', 'B', 9, pygame.image.load('chess/RookB.png'))
rookB2 = Gameplay('Rook', 'B', 16, pygame.image.load('chess/RookB.png'))
knightB1 = Gameplay('Knight', 'B', 10, pygame.image.load('chess/KnightB.png'))
knightB2 = Gameplay('Knight', 'B', 15, pygame.image.load('chess/KnightB.png'))
bishopB1 = Gameplay('Bishop', 'B', 11, pygame.image.load('chess/BishopB.png'))
bishopB2 = Gameplay('Bishop', 'B', 14, pygame.image.load('chess/BishopB.png'))
queenB = Gameplay('Queen', 'B', 12, pygame.image.load('chess/QueenB.png'))
kingB = Gameplay('King', 'B', 13, pygame.image.load('chess/KingB.png'))
pawnW1 = Gameplay('Pawn', 'W', 17, pygame.image.load('chess/PawnW.png'))
pawnW2 = Gameplay('Pawn', 'W', 18, pygame.image.load('chess/PawnW.png'))
pawnW3 = Gameplay('Pawn', 'W', 19, pygame.image.load('chess/PawnW.png'))
pawnW4 = Gameplay('Pawn', 'W', 20, pygame.image.load('chess/PawnW.png'))
pawnW5 = Gameplay('Pawn', 'W', 21, pygame.image.load('chess/PawnW.png'))
pawnW6 = Gameplay('Pawn', 'W', 22, pygame.image.load('chess/PawnW.png'))
pawnW7 = Gameplay('Pawn', 'W', 23, pygame.image.load('chess/PawnW.png'))
pawnW8 = Gameplay('Pawn', 'W', 24, pygame.image.load('chess/PawnW.png'))
rookW1 = Gameplay('Rook', 'W', 25, pygame.image.load('chess/RookW.png'))
rookW2 = Gameplay('Rook', 'W', 32, pygame.image.load('chess/RookW.png'))
knightW1 = Gameplay('Knight', 'W', 26, pygame.image.load('chess/KnightW.png'))
knightW2 = Gameplay('Knight', 'W', 31, pygame.image.load('chess/KnightW.png'))
bishopW1 = Gameplay('Bishop', 'W', 27, pygame.image.load('chess/BishopW.png'))
bishopW2 = Gameplay('Bishop', 'W', 30, pygame.image.load('chess/BishopW.png'))
queenW = Gameplay('Queen', 'W', 28, pygame.image.load('chess/QueenW.png'))
kingW = Gameplay('King', 'W', 29, pygame.image.load('chess/KingW.png'))

listOfWhitePieces = [pawnW1, pawnW2, pawnW3,pawnW4, pawnW5, pawnW6, pawnW7, pawnW8, 
rookW1, rookW2, knightW1, knightW2, bishopW1, bishopW2, queenW, kingW]

listOfBlackPieces = [pawnB1, pawnB2, pawnB3,pawnB4, pawnB5, pawnB6, pawnB7, pawnB8, 
rookB1, rookB2, knightB1, knightB2, bishopB1, bishopB2, queenB, kingB]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255,255,255))
    drawBoard()

    listOfBlackMoves = []
    listOfWhiteMoves = []

    for i in range(0, len(listOfBlackPieces)):
        listOfWhitePieces[i].display()
        
        if len(listOfWhitePieces[i].listOfMoves) > 0:
            for h in listOfWhitePieces[i].listOfMoves:
                listOfWhiteMoves.append(h)
        
    for i in range(0, len(listOfBlackPieces)):
        listOfBlackPieces[i].display()
        if len(listOfBlackPieces[i].listOfMoves) > 0:
            for j in listOfBlackPieces[i].listOfMoves:
                listOfBlackMoves.append(j)
    
    if len(listOfBlackMoves) == 0:
        print('Black Loses')
        running = False
    
    if len(listOfWhiteMoves) == 0:
        print('White Loses')
        running = False

    pygame.display.update()

pygame.quit()