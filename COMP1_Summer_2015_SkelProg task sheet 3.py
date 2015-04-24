# Skeleton Program code for the AQA COMP1 Summer 2015 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA COMP1 Programmer Team
# developed in the Python 3.4 programming environment
# Nicola Batty

import pdb
BOARDDIMENSION = 8
yes_list = ["y", "Y", "yes", "Yes"]
no_list = ["n", "N", "no", "No"]

def CreateBoard():
  #pdb.set_trace()
  Board = []
  for Count in range(BOARDDIMENSION + 1):
    Board.append([])
    for Count2 in range(BOARDDIMENSION + 1):
      Board[Count].append("  ")
  return Board

def DisplayWhoseTurnItIs(WhoseTurn):
  #pdb.set_trace()
  if WhoseTurn == "W":
    print("It is White's turn")
  else:
    print("It is Black's turn")

def GetTypeOfGame():
  #pdb.set_trace()
  yes_list = ["y", "yes", "Y", "Yes"]
  no_list = ["n", "no", "N", "No"]
  TypeOfGame = input("Do you want to play the sample game (enter Y for Yes)? ")
  if TypeOfGame in no_list:
    TypeOfGame = "n"
  elif TypeOfGame in yes_list:
    TypeOfGame = "y"
  else:
    TypeOfGame = GetTypeOfGame()
  return TypeOfGame

def DisplayWinner(WhoseTurn):
  #pdb.set_trace()
  if WhoseTurn == "W":
    print("Black's Sarrum has been captured.  White wins!")
  else:
    print("White's Sarrum has been captured.  Black wins!")

def CheckIfGameWillBeWon(Board, FinishRank, FinishFile):
  #pdb.set_trace()
  if Board[FinishRank][FinishFile][1] == "S":
    return True
  else:
    return False

def display_menu():
  #pdb.set_trace()
  print("Main Menu")
  print()
  print("1. Start new game")
  print("2. Load existing game")
  print("3. Play sample game")
  print("4. View high scores")
  print("5. Settings")
  print("6. Quit program")
  print()

def display_in_game_menu():
  #pdb.set_trace()
  print("Options")
  print()
  print("1. Save Game")
  print("2. Quit to Menu")
  print("3. Return to Game")
  print("4. Surender")
  print()

def DisplayBoard(Board):
  #pdb.set_trace()
  print()
  for RankNo in range(1, BOARDDIMENSION + 1):
    print("     -------------------------")
    print("R{0}".format(RankNo), end="   ")
    for FileNo in range(1, BOARDDIMENSION + 1):
      print("|" + Board[RankNo][FileNo], end="")
    print("|")
  print("     -------------------------")
  print()
  print("      ", end="")
  for FileNo in range(1, BOARDDIMENSION + 1):
    print("F{0} ".format(FileNo), end="")
  print()
  print()

def CheckRedumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, ColourOfPiece):
  #pdb.set_trace()
  CheckRedumMoveIsLegal = False
  if ColourOfPiece == "W":
    if StartRank == BOARDDIMENSION - 1:
      if FinishRank == StartRank - 2:
        if FinishFile == StartFile and Board[FinishRank][FinishFile] == "  ":
          CheckRedumMoveIsLegal = True
        elif abs(FinishFile - StartFile) == 1 and Board[FinishRank][FinishFile][0] == "B":
          CheckRedumMoveIsLegal = True
      elif FinishRank == StartRank - 1:
        if FinishFile == StartFile and Board[FinishRank][FinishFile] == "  ":
          CheckRedumMoveIsLegal = True
        elif abs(FinishFile - StartFile) == 1 and Board[FinishRank][FinishFile][0] == "B":
          CheckRedumMoveIsLegal = True
    else:
      if FinishRank == StartRank - 1:
        if FinishFile == StartFile and Board[FinishRank][FinishFile] == "  ":
          CheckRedumMoveIsLegal = True
        elif abs(FinishFile - StartFile) == 1 and Board[FinishRank][FinishFile][0] == "B":
          CheckRedumMoveIsLegal = True
  elif ColourOfPiece == "B":
    if StartRank == 2:
      if FinishRank == StartRank + 2:
        if FinishFile == StartFile and Board[FinishRank][FinishFile] == "  ":
          CheckRedumMoveIsLegal = True
        elif abs(FinishFile - StartFile) == 1 and Board[FinishRank][FinishFile][0] == "B":
          CheckRedumMoveIsLegal = True
      elif FinishRank == StartRank + 1:
        if FinishFile == StartFile and Board[FinishRank][FinishFile] == "  ":
          CheckRedumMoveIsLegal = True
        elif abs(FinishFile - StartFile) == 1 and Board[FinishRank][FinishFile][0] == "B":
          CheckRedumMoveIsLegal = True
    else:
      if FinishRank == StartRank + 1:
        if FinishFile == StartFile and Board[FinishRank][FinishFile] == "  ":
          CheckRedumMoveIsLegal = True
        elif abs(FinishFile - StartFile) == 1 and Board[FinishRank][FinishFile][0] == "B":
          CheckRedumMoveIsLegal = True

    if FinishRank == StartRank + 1:
      if FinishFile == StartFile and Board[FinishRank][FinishFile] == "  ":
        CheckRedumMoveIsLegal = True
      elif abs(FinishFile - StartFile) == 1 and Board[FinishRank][FinishFile][0] == "W":
        CheckRedumMoveIsLegal = True
  return CheckRedumMoveIsLegal

def CheckSarrumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  #pdb.set_trace()
  CheckSarrumMoveIsLegal = False
  if abs(FinishFile - StartFile) <= 1 and abs(FinishRank - StartRank) <= 1:
    CheckSarrumMoveIsLegal = True
  return CheckSarrumMoveIsLegal

def CheckGisgigirMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  #pdb.set_trace()
  GisgigirMoveIsLegal = False
  RankDifference = FinishRank - StartRank
  FileDifference = FinishFile - StartFile
  if RankDifference == 0:
    if FileDifference >= 1:
      GisgigirMoveIsLegal = True
      for Count in range(1, FileDifference):
        if Board[StartRank][StartFile + Count] != "  ":
          GisgigirMoveIsLegal = False
    elif FileDifference <= -1:
      GisgigirMoveIsLegal = True
      for Count in range(-1, FileDifference, -1):
        if Board[StartRank][StartFile + Count] != "  ":
          GisgigirMoveIsLegal = False
  elif FileDifference == 0:
    if RankDifference >= 1:
      GisgigirMoveIsLegal = True
      for Count in range(1, RankDifference):
        if Board[StartRank + Count][StartFile] != "  ":
          GisgigirMoveIsLegal = False
    elif RankDifference <= -1:
      GisgigirMoveIsLegal = True
      for Count in range(-1, RankDifference, -1):
        if Board[StartRank + Count][StartFile] != "  ":
          GisgigirMoveIsLegal = False
  return GisgigirMoveIsLegal

def CheckNabuMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn):
  pdb.set_trace()
  CheckNabuMoveIsLegal = True
  if abs(FinishFile - StartFile) == abs(FinishRank - StartRank):
    SquareNo = 1
    while CheckNabuMoveIsLegal and SquareNo <= FinishFile - 1:
      if WhoseTurn == "W":        
        Square = Board[StartRank - SquareNo][SquareNo - SquareNo]
        if Square == "":
          CheckNabuMoveIsLegal = True
          SquareNo = SquareNo + 1
        else:
          CheckNabuMoveIsLegal = False
      elif WhoseTurn == "B":
        Square = Board[StartRank + SquareNo][SquareNo + SquareNo]
        if Square == "":
          CheckNabuMoveIsLegal = True
        else:
          CheckNabuMoveIsLegal = False
  return CheckNabuMoveIsLegal

def CheckMarzazPaniMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  #pdb.set_trace()
  CheckMarzazPaniMoveIsLegal = False
  if (abs(FinishFile - StartFile) == 1 and abs(FinishRank - StartRank) == 0) or (abs(FinishFile - StartFile) == 0 and abs(FinishRank - StartRank) ==1):
    CheckMarzazPaniMoveIsLegal = True
  elif abs(FinishFile - StartFile) == 1 and abs(FinishRank - StartRank) == 1:
    CheckMarzazPaniMoveIsLegal = True
  return CheckMarzazPaniMoveIsLegal

def CheckEtluMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  #pdb.set_trace()
  CheckEtluMoveIsLegal = False
  if (abs(FinishFile - StartFile) == 2 and abs(FinishRank - StartRank) == 1) or (abs(FinishFile - StartFile) == 1 and abs(FinishRank - StartRank) == 2):
    CheckEtluMoveIsLegal = True
  elif (abs(FinishFile - StartFile) == 1 and abs(FinishRank - StartRank) == 2) or (abs(FinishFile - StartFile) == 2 and abs(FinishRank - StartRank) == 1):
    CheckEtluMoveIsLegal = True
  return CheckEtluMoveIsLegal

def CheckMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn):
  #pdb.set_trace()
  MoveIsLegal = True
  if FinishRank == 0:
    MoveIsLegal = False
  elif FinishRank == BOARDDIMENSION + 1:
    MoveIsLegal = False
  elif FinishFile == 0:
    MoveIsLegal = False
  elif FinishFile == BOARDDIMENSION + 1:
    MoveIsLegal = False
  if MoveIsLegal == True:
    if (FinishFile == StartFile) and (FinishRank == StartRank):
      MoveIsLegal = False
    else:
      PieceType = Board[StartRank][StartFile][1]
      PieceColour = Board[StartRank][StartFile][0]
      if WhoseTurn == "W":
        if PieceColour != "W":
          MoveIsLegal = False
        if Board[FinishRank][FinishFile][0] == "W":
          MoveIsLegal = False
      else:
        if PieceColour != "B":
          MoveIsLegal = False
        if Board[FinishRank][FinishFile][0] == "B":
          MoveIsLegal = False
    if MoveIsLegal == True:
      if PieceType == "R":
        MoveIsLegal = CheckRedumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, PieceColour)
      elif PieceType == "S":
        MoveIsLegal = CheckSarrumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
      elif PieceType == "M":
        MoveIsLegal = CheckMarzazPaniMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
      elif PieceType == "G":
        MoveIsLegal = CheckGisgigirMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
      elif PieceType == "N":
        MoveIsLegal = CheckNabuMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn)
      elif PieceType == "E":
        MoveIsLegal = CheckEtluMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
      elif PieceType == "K":
        MoveIsLegal = CheckRedumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, PieceColour)
        if not MoveIsLegal:
          MoveIsLegal = CheckMarzazPaniMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
          if not MoveIsLegal:
            MoveIsLegal = CheckGisgigirMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
            if not MoveIsLegal:
              MoveIsLegal = CheckNabuMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn)
              if not MoveIsLegal:
                MoveIsLegal = CheckEtluMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
  return MoveIsLegal

#def load_game():
# pdb.set_trace()
#  try:
#    with open("saved_game.dat", mode="rb") as SavedGame:
#      Board = SavedGame
#      return Board
#  except FileNotFoundError:
#    print()
#   print("There is no saved game")
#    print()
    
#def save_game(Board):
# pdb.set_trace()
#  with open("saved_game.dat", mode="wb") as SavedGame:
#    for line in Board:
#      for count in line:
#        SavedGame.write(count)
#      SavedGame.write("/n")

def DisplaySettings():
  #pdb.set_trace()
  print()
  print("1. Use Kashshaptu Piece")
  print("9.Return to Main Menu")
  print()

def GetSttingChange():
  #pdb.set_trace()
  try:
    Solection = int(input("Please select setting to change: "))
  except ValueError:
    print("Please enter a number.")
    Solection = GetSettingChange()
  return solection

def MakeSettingChange(Selection, Setting, Quit):
  if Selection == 1:
    Correct = False
    while not Correct:
      Confomation = input("Do you wish to use the Kashshaptu piece (Y/N)?: ")
      if Confomation in yes_list:
        Settings = True
        Correct = True
      elif Confomation in no_list:
        Settings = False
        Correct = True
      else:
        print("Plese enter yes or no!")
  elif Selsction == 9:
    Quit = True
  return Settings, Quit

def Settings(Setting):
  #pdb.set_trace()
  Quit = False
  while not Quit:
    DisplaySettings()
    Selection = GetSettingChange()
    Setting, Quit = MakeSettingChange(Selection, Setting, Quit)
  return Setting

def ConfirmMove(StartRank, StartFile, FinishRank, FinishFile):
  #pdb.set_trace()
  print()
  print("Move form Rank {0}, File {1} to Rank {2}, File {3}".format(StartRank, StartFile, FinishRank, FinishFile))
  confirm_move = input("Confirm move (yes/no): ")
  print()
  return confirm_move

def InitialiseBoard(Board, SampleGame):
  #pdb.set_trace()
  if SampleGame == "Y":
    InitialiseSampleBoard(Board)
  else:
    InitialiseNewBoard(Board)

def InitialiseSampleBoard(Board):
  #pdb.set_trace()
  for RankNo in range(1, BOARDDIMENSION + 1):
    for FileNo in range(1, BOARDDIMENSION + 1):
      Board[RankNo][FileNo] = "  "
  Board[1][2] = "BG"
  Board[1][4] = "BS"
  Board[1][8] = "WG"
  Board[2][1] = "WR"
  Board[3][1] = "WS"
  Board[3][2] = "BE"
  Board[3][8] = "BE"
  Board[6][8] = "BR"

def InitialiseNewBoard(Board):
  #pdb.set_trace()
  for RankNo in range(1, BOARDDIMENSION + 1):
    for FileNo in range(1, BOARDDIMENSION + 1):
      if RankNo == 2:
        Board[RankNo][FileNo] = "BR"
      elif RankNo == 7:
        Board[RankNo][FileNo] = "WR"
      elif RankNo == 1 or RankNo == 8:
        if RankNo == 1:
          Board[RankNo][FileNo] = "B"
        elif RankNo == 8:
          Board[RankNo][FileNo] = "W"
        if FileNo == 1 or FileNo == 8:
          Board[RankNo][FileNo] = Board[RankNo][FileNo] + "G"
        elif FileNo == 2 or FileNo == 7:
          Board[RankNo][FileNo] = Board[RankNo][FileNo] + "E"
        elif FileNo == 3 or FileNo == 6:
          Board[RankNo][FileNo] = Board[RankNo][FileNo] + "N"
        if Board[RankNo][FileNo] == "W":
          if FileNo == 4:
            Board[RankNo][FileNo] = Board[RankNo][FileNo] + "M"
          elif FileNo == 5:
            Board[RankNo][FileNo] = Board[RankNo][FileNo] + "S"
        elif Board[RankNo][FileNo] == "B":
          if FileNo == 4:
            Board[RankNo][FileNo] = Board[RankNo][FileNo] + "S"
          elif FileNo == 5:
            Board[RankNo][FileNo] = Board[RankNo][FileNo] + "M"
      else:
        Board[RankNo][FileNo] = "  "

def GetSquare(message, Board, WhoseTurn, Quit):
  #pdb.set_trace()
  Check = False
  while not Check:
    try:
      Square = int(input(message))
      if Square == -1:
        display_in_game_menu()
        solection = get_menu_solection()
        Quit = make_in_game_solection(solection, Board, WhoseTurn)
        if Quit:
          Check = True
      elif Square < 10:
        print("Please provide both FILE and RANK for this move")
        Square = GetSquare(message, Board, WhoseTurn, Quit)
        Square = GetSquare(message, Board, WhoseTurn, Quit)
      else:
        Check = True
    except ValueError:
      print("That is not coordinates - please try again")
  Rank = Square % 10
  File = Square // 10
  return File, Rank, Quit

def GetMove(Board, WhoseTurn):
  #pdb.set_trace()
  StartSquareMessage = "Enter coordinates of square containing piece to move (file first) or type '-1' for menu: "
  FinishSquareMessage = "Enter coordinates of square to move piece to (file first): "
  Quit = False
  StartFile, StartRank, Quit = GetSquare(StartSquareMessage, Board, WhoseTurn, Quit)
  if not Quit:
    FinishFile, FinishRank, Quit  = GetSquare(FinishSquareMessage, Board, WhoseTurn, Quit)
  else:
    FinishFile = ""
    FinishRank = ""
  return StartFile, StartRank, FinishFile, FinishRank, Quit

def get_menu_solection():
  #pdb.set_trace()
  try:
    solection = int(input("Please select an option: "))
  except ValueError:
    print("Please enter a number.")
    solection = get_menu_solection()
  return solection

def make_in_game_solection(solection, Borad, WhoseTurn):
  #pdb.set_trace()
  if solection == 1:
    save_game(Borad)
    Quit = make_in_game_solection(solection, Borad)
  elif solection == 2:
    Quit = True
  elif solection == 3:
    Quit = False
  elif solection == 4:
    print()
    print("Surrendering...")
    print()
    if WhoseTurn == "W":
      print("White surrendered. Black wins!")
    else:
      print("Black surrendered. White wins!")
    print()
    Quit = True
  else:
    print("please make a valid solection")
    solection = get_menu_solection()
    Quit = make_in_game_solection(solection, Borad, WhoseTurn)
  return Quit

def make_solection(solection, Quit, Setting):
  #pdb.set_trace()
  if solection == 1:
    play_game("N", Setting)
  elif solection == 2:
    load_game()
  elif solection == 3:
    play_game("Y", Setting)
  elif solection == 4:
    display_high_scores
  elif solection == 5:
    Setting = Settings(Setting)
  elif solection == 6:
    Quit = True
  else:
    print("please make a valid solection")
    solection = get_menu_solection()
    Quit = make_solection(solection, Quit)
  return Quit, Setting

def GetPieceName(FinishRank, FinishFile, Board):
  #pdb.set_trace()
  PiecesType = ""
  if Board[FinishRank][FinishFile][1] == "G":
    PiecesType = "Gisgigir"
  elif Board[FinishRank][FinishFile][1] == "E":
    PiecesType = "Etlu"
  elif Board[FinishRank][FinishFile][1] == "N":
    PiecesType = "Nabu"
  elif Board[FinishRank][FinishFile][1] == "R":
    PiecesType = "Redum"
  elif Board[FinishRank][FinishFile][1] == "S":
    PiecesType = "Sarrum"
  elif Board[FinishRank][FinishFile][1] == "M":
    PiecesType = "Marzaz pani"
  return PiecesType

def MakeMove(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn, Setting):
  #pdb.set_trace()
  PiecesType1 = GetPieceName(FinishRank, FinishFile, Board)
  if Board[FinishRank][FinishFile] != "":
    if WhoseTurn == "W":
      PiecesType1 = GetPieceName(FinishRank, FinishFile, Board)
      PiecesType2 = GetPieceName(StartRank, StartFile, Board)
      print("White {0} takes Black {1}.".format(PiecesType2, PiecesType1))
    else:
      PiecesType1 = GetPieceName(StartRank, StartFile, Board)
      PiecesType2 = GetPieceName(FinishRank, FinishFile, Board)
      print("Black {0} takes White {1}.".format(PiecesType2, PiecesType1))
  if WhoseTurn == "W" and FinishRank == 1 and Board[StartRank][StartFile][1] == "R":
    if not Setting:
      print("White Redum promoted to Marzaz Pani.")
      Board[FinishRank][FinishFile] = "WM"
      Board[StartRank][StartFile] = "  "
    else:
      print("White Redum promoted to Kashshaptu.")
      Board[FinishRank][FinishFile] = "WK"
      Board[StartRank][StartFile] = "  "
  elif WhoseTurn == "B" and FinishRank == 8 and Board[StartRank][StartFile][1] == "R":
    if not Setting:
      print("Black Redum promoted to Marzaz Pani.")
      Board[FinishRank][FinishFile] = "BM"
      Board[StartRank][StartFile] = "  "
    else:
      print("Black Redum promoted to Kashshaptu.")
      Board[FinishRank][FinishFile] = "BK"
      Board[StartRank][StartFile] = "  "
  else:
    Board[FinishRank][FinishFile] = Board[StartRank][StartFile]
    Board[StartRank][StartFile] = "  "

def play_game(SampleGame, Setting):
  #pdb.set_trace()
  Board = CreateBoard() #0th index not used
  StartSquare = 0 
  FinishSquare = 0
  PlayAgain = "Y"
  while PlayAgain == "Y":
    WhoseTurn = "W"
    GameOver = False
    if ord(SampleGame) >= 97 and ord(SampleGame) <= 122:
      SampleGame = chr(ord(SampleGame) - 32)
    InitialiseBoard(Board, SampleGame)
    while not(GameOver):
      DisplayBoard(Board)
      DisplayWhoseTurnItIs(WhoseTurn)
      MoveIsLegal = False
      while not(MoveIsLegal):
        StartFile, StartRank, FinishFile, FinishRank, Quit = GetMove(Board, WhoseTurn)
        if (Quit):
          MoveIsLegal = True
        elif not (Quit):
          MoveIsLegal = CheckMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn)
          if not(MoveIsLegal):
            print("That is not a legal move - please try again")
          else:
            correct = False
            while not correct:
              correct = True
              confirm_move = ConfirmMove(StartRank, StartFile, FinishRank, FinishFile)
              if confirm_move in yes_list:
                MoveIsLegal = True
              elif confirm_move in no_list:
                MoveIsLegal = False
              else:
                correct = False
      if Quit:
        GameOver = True
        PlayAgain = "N"
      else:
        GameOver = CheckIfGameWillBeWon(Board, FinishRank, FinishFile)
        MakeMove(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn, Setting)
        if GameOver:
          DisplayWinner(WhoseTurn)
          PlayAgain = input("Do you want to play again (enter Y for Yes)? ")
        if WhoseTurn == "W":
          WhoseTurn = "B"
        else:
          WhoseTurn = "W"
      print()
      if ord(PlayAgain) >= 97 and ord(PlayAgain) <= 122:
        PlayAgain = chr(ord(PlayAgain) - 32)

if __name__ == "__main__":
  #pdb.set_trace()
  Setting = False
  Quit = False
  while not Quit:
    display_menu()
    solection = get_menu_solection()
    Quit, Setting = make_solection(solection, Quit, Setting)
