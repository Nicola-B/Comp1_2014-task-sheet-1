# Skeleton Program code for the AQA COMP1 Summer 2014 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA Programmer Team
# developed in the Python 3.2 programming environment
# version 2 edited 06/03/2014
# Nicola Batty

# 1/03/2015

from datetime import*
import pdb
import random

NO_OF_RECENT_SCORES = 3

class TCard():
  def __init__(self):
    self.Suit = 0
    self.Rank = 0

class TRecentScore():
  def __init__(self):
    self.Name = ''
    self.Score = ""
    self.Date = datetime.now()

Deck = [None]
RecentScores = [None]
Choice = ''

def GetRank(RankNo):
  Rank = ''
  if RankNo == 1:
    Rank = 'Ace'
  elif RankNo == 2:
    Rank = 'Two'
  elif RankNo == 3:
    Rank = 'Three'
  elif RankNo == 4:
    Rank = 'Four'
  elif RankNo == 5:
    Rank = 'Five'
  elif RankNo == 6:
    Rank = 'Six'
  elif RankNo == 7:
    Rank = 'Seven'
  elif RankNo == 8:
    Rank = 'Eight'
  elif RankNo == 9:
    Rank = 'Nine'
  elif RankNo == 10:
    Rank = 'Ten'
  elif RankNo == 11:
    Rank = 'Jack'
  elif RankNo == 12:
    Rank = 'Queen'
  elif RankNo == 13:
    Rank = 'King'
  return Rank

def GetSuit(SuitNo):
  Suit = ''
  if SuitNo == 1:
    Suit = 'Clubs'
  elif SuitNo == 2:
    Suit = 'Diamonds'
  elif SuitNo == 3:
    Suit = 'Hearts'
  elif SuitNo == 4:
    Suit = 'Spades'
  return Suit

def DisplayMenu():
  print()
  print('MAIN MENU')
  print()
  print('1. Play game (with shuffle)')
  print('2. Play game (without shuffle)')
  print('3. Display recent scores')
  print('4. Reset recent scores')
  print("5. Options")
  print("6. save scores")
  print()
  print('Select an option from the menu (or enter q to quit): ', end='')

def GetMenuChoice():
  Choice = input()
  print()
  return Choice

def LoadDeck(Deck):
  CurrentFile = open('deck.txt', 'r')
  Count = 1
  while True:
    LineFromFile = CurrentFile.readline()
    if not LineFromFile:
      CurrentFile.close()
      break
    Deck[Count].Suit = int(LineFromFile)
    LineFromFile = CurrentFile.readline()
    Deck[Count].Rank = int(LineFromFile)
    Count = Count + 1
 
def ShuffleDeck(Deck):
  SwapSpace = TCard()
  NoOfSwaps = 1000
  for NoOfSwapsMadeSoFar in range(1, NoOfSwaps + 1):
    Position1 = random.randint(1, 52)
    Position2 = random.randint(1, 52)
    SwapSpace.Rank = Deck[Position1].Rank
    SwapSpace.Suit = Deck[Position1].Suit
    Deck[Position1].Rank = Deck[Position2].Rank
    Deck[Position1].Suit = Deck[Position2].Suit
    Deck[Position2].Rank = SwapSpace.Rank
    Deck[Position2].Suit = SwapSpace.Suit

def DisplayCard(ThisCard):
  print()
  print('Card is the', GetRank(ThisCard.Rank), 'of', GetSuit(ThisCard.Suit))
  print()

def GetCard(ThisCard, Deck, NoOfCardsTurnedOver):
  ThisCard.Rank = Deck[1].Rank
  ThisCard.Suit = Deck[1].Suit
  for Count in range(1, 52 - NoOfCardsTurnedOver):
    Deck[Count].Rank = Deck[Count + 1].Rank
    Deck[Count].Suit = Deck[Count + 1].Suit
  Deck[52 - NoOfCardsTurnedOver].Suit = 0
  Deck[52 - NoOfCardsTurnedOver].Rank = 0

def IsNextCardHigher(LastCard, NextCard, AceH_Or_L):
  if AceH_Or_L == "l":
    Higher = False
    if NextCard.Rank > LastCard.Rank:
      Higher = True
  else:
    Higher = False
    if NextCard.Rank == 1:
      Higher = True
    elif LastCard.Rank == 1:
      Higher = False
    else:
      if NextCard.Rank > LastCard.Rank:
        Higher = True
  return Higher

def GetPlayerName():
  print()
  BlankSpace = True
  while BlankSpace:
    PlayerName = input('Please enter your name: ')
    if PlayerName == "":
      BlankSpace = True
    else:
      BlankSpace = False
  print()
  return PlayerName

def GetChoiceFromUser():
  Choice = input('Do you think the next card will be higher than the last card (enter y or n)? ')
  return Choice

def DisplayEndOfGameMessage(Score):
  print()
  print('GAME OVER!')
  print('Your score was', Score)
  if Score == 51:
    print('WOW! You completed a perfect game.')
  print()

def DisplayCorrectGuessMessage(Score):
  print()
  print('Well done! You guessed correctly.')
  print('Your score is now ', Score, '.', sep='')
  print()

def ResetRecentScores(RecentScores):
  for Count in range(1, NO_OF_RECENT_SCORES + 1):
    RecentScores[Count].Name = ''
    RecentScores[Count].Score = 0
    RecentScores[Count].Date = datetime.now()

def BubbleSortScores(RecentScores):
  #pdb.set_trace()
  Changes = False
  while not Changes:
    Changes = True
    Count = 0
    for itam in RecentScores:
      if Count < NO_OF_RECENT_SCORES - 1:
        if itam.Score < RecentScores[Count+1].Score:
          Changes = False
          Temp = itam
          RecentScores[Count] = RecentScores[Count+1]
          RecentScores[Count+1] = Temp
        Count = Count+1
  return RecentScores

def DisplayRecentScores(RecentScores):
  RecentScores = BubbleSortScores(RecentScores)
  for line in RecentScores:
    line.Date = datetime.now()
  print()
  print('Recent Scores: ')
  print()
  print("_"*42)
  print("|{0:<25}|{1:<5}|{2:<8}|".format("Name", "Score", "Date"))
  print("_"*42)
  for score in RecentScores:
    current_date = RecentScores[Count].Date
    current_date_string = datetime.strftime(current_date,"%d/%m/%y")
    print("|{0:<25}|{1:<5}|{2:<8}|".format(score.Name, score.Score, current_date_string))
    print("_"*42)
  print()
  print('Press the Enter key to return to the main menu')
  input()
  print()

def UpdateRecentScores(RecentScores, Score):
  Score = str(Score)
  #pdb.set_trace()
  Uplode = input("Do you want to add your score to the high socres table? (y or n): ")
  if ((Uplode == "y") or (Uplode == "Y") or (Uplode == "yes") or (Uplode == "Yes")):
    current_date = datetime.now()
    PlayerName = GetPlayerName()
    FoundSpace = False
    Count = 1
    while (not FoundSpace) and (Count <= NO_OF_RECENT_SCORES - 1):
      if RecentScores[Count].Name == '':
        FoundSpace = True
      else:
        Count = Count + 1
    if not FoundSpace:
      for Count in range(NO_OF_RECENT_SCORES - 1):
        RecentScores[Count].Name = RecentScores[Count + 1].Name
        RecentScores[Count].Score = RecentScores[Count + 1].Score
        RecentScores[Count].Date = RecentScores[Count + 1].Date
      Count = NO_OF_RECENT_SCORES
    RecentScores[Count].Name = PlayerName
    RecentScores[Count].Score = Score
    RecentScores[Count].Date = current_date
  elif ((Uplode != "y") and (Uplode != "Y") and (Uplode != "yes") and (Uplode != "Yes") and (Uplode != "n") and (Uplode != "N") and (Uplode != "no") and (Uplode != "No")):
    UpdateRecentScores(RecentScores, Score)

def SavedScores(RecentScores):
  #pdb.set_trace()
  with open("save_scores.txt", mode="w", encoding="utf-8") as SaveScores:
    for line in RecentScores:
      line_date = line.Date
      line_date_string = datetime.strftime(line_date, "%d/%m/%Y")
      SaveScores.write(line.Name)
      SaveScores.write("/n")
      SaveScores.write(line.Score)
      SaveScores.write("/n")
      SaveScores.write(line_date_string)
      SaveScores.write("/n")

def LoadScores():
  try:
    with open("save_scores.txt", mode="r", encoding="utf-8") as SaveScores:
      scores = TRecentScore()
      RecentScores = []
      Count = 0
      for line in SaveScores:
        if Count == 0:
          scores.Name = line
          Count = Count + 1
        elif Count == 1:
          scores.Score = line
          Count = Count + 1
        elif Count == 2:
          scores.Date = line
          Count = 0
          RecentScores.append(scores)
  except FileNotFoundError:
    RecentScores = []
    for Count in range(1, NO_OF_RECENT_SCORES + 1):
      RecentScores.append(TRecentScore())
  return RecentScores

def DisplayOptions():
  print()
  print("OPTION MENU")
  print()
  print("1. Set Ace to be HIGH or LOW")
  print()
  print("Select anoption frommenu(or enter q to quit): ",end = "")

def GetOptionChoice():
  OptionChoice = input()
  print()
  return OptionChoice

def SetAceHighOrLow():
  #pdb.set_trace()
  AceH_Or_L = ""
  print()
  while (AceH_Or_L != "h") and (AceH_Or_L != "l"):
    AceH_Or_L = input("Do you want the Ace to be (h)igh or (l)ow: ")
  print()
  return AceH_Or_L

def SetOptions(OptionChoice):
  while (OptionChoice!= "q") and (OptionChoice != "Q") and (OptionChoice != "quit") and (OptionChoice != "Quit"):
    if OptionChoice == "1":
      AceH_or_L = SetAceHighOrLow()
      OptionChoice = "q"
  return AceH_or_L

def PlayGame(Deck, RecentScores, AceH_Or_L):
  #pdb.set_trace()
  LastCard = TCard()
  NextCard = TCard()
  GameOver = False
  GetCard(LastCard, Deck, 0)
  DisplayCard(LastCard)
  NoOfCardsTurnedOver = 1
  while (NoOfCardsTurnedOver < 52) and (not GameOver):
    GetCard(NextCard, Deck, NoOfCardsTurnedOver)
    Choice = ""
    while (Choice!= "y") and (Choice != "Y") and (Choice != "yes") and (Choice != "Yes") and (Choice != "n") and (Choice != "N") and (Choice != "no") and (Choice != "No"):
      Choice = GetChoiceFromUser()
    DisplayCard(NextCard)
    NoOfCardsTurnedOver = NoOfCardsTurnedOver + 1
    Higher = IsNextCardHigher(LastCard, NextCard, AceH_Or_L)
    if (Higher and ((Choice == "y") or (Choice == "Y") or (Choice == "yes") or (Choice == "Yes"))) or (not Higher and ((Choice == "n") or (Choice == "N") or (Choice == "no") or (Choice == "No"))):
      DisplayCorrectGuessMessage(NoOfCardsTurnedOver - 1)
      LastCard.Rank = NextCard.Rank
      LastCard.Suit = NextCard.Suit
    else:
      GameOver = True
  if GameOver:
    DisplayEndOfGameMessage(NoOfCardsTurnedOver - 2)
    UpdateRecentScores(RecentScores, NoOfCardsTurnedOver - 2)
  else:
    DisplayEndOfGameMessage(51)
    UpdateRecentScores(RecentScores, 51)

if __name__ == "__main__":
  RecentScores = LoadScores()
  for Count in range(1, 53):
    Deck.append(TCard())
  AceH_Or_L = "l"
  Choice = ""
  while (Choice!= "q") and (Choice != "Q") and (Choice != "quit") and (Choice != "Quit"):
    DisplayMenu()
    Choice = GetMenuChoice()
    if Choice == "1":
      LoadDeck(Deck)
      ShuffleDeck(Deck)
      PlayGame(Deck, RecentScores, AceH_Or_L)
    elif Choice == "2":
      LoadDeck(Deck)
      PlayGame(Deck, RecentScores, AceH_Or_L)
    elif Choice == "3":
      DisplayRecentScores(RecentScores)
    elif Choice == "4":
      ResetRecentScores(RecentScores)
    elif Choice == "5":
      DisplayOptions()
      OptionChoice = GetOptionChoice()
      AceH_Or_L = SetOptions(OptionChoice)
    elif Choice == "6":
      SavedScores(RecentScores)
