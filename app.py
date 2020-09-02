class TicTacToe():
    def __init__(self):
        self.board = {'7' : '-', '8' : '-', '9': '-',
                      '4' : '-', '5' : '-', '6': '-',
                      '1' : '-', '2' : '-', '3': '-'  }
        self.whoseTurn = 'X'
        self.count = 0
        self.finished = False
        self.won = "Tie"
        while self.finished == False:
            self.printBoard()
            self.turn()
            if self.count >= 5:
                self.checkWin()
            if self.count == 9:
                print(f'Game finished! {self.won}')
        if self.finished == True:
            print(self.won)
                 
    def printBoard(self):        
        print("""
7 | 8 | 9
4 | 5 | 6
1 | 2 | 3
""")
        print("*" * 10)        
        print(self.board['7'] + " | " + self.board['8'] + " | " + self.board['9'] + "\n" +
        self.board['4'] + " | " + self.board['5'] + " | " + self.board['6'] + "\n" +
        self.board['1'] + " | " + self.board['2'] + " | " + self.board['3'] + "\n")

    def turn(self):
        print(f'{self.whoseTurn} turn. Choose well!')
        a = input('Choose number between 1-9 \n')
        if a == '1' or a == '2' or a == '3' or a == '4' or a == '5' or a == '6' or a == '7' or a == '8' or a =='9':
            if self.board[a] == '-':
                self.board[a] = self.whoseTurn
                self.count += 1
                if self.whoseTurn == 'X':
                    self.whoseTurn = 'O'
                else:
                    self.whoseTurn = 'X'
            else:
                print("You can't play here!!")
                self.turn()
        else:
            print('Wrong input! Try Again')
            self.turn()

    def checkWin(self):
        if (self.board['1'] == self.board['2'] == self.board['3'] or self.board['1'] == self.board['4'] == self.board['7'] or self.board['1'] == self.board['5'] == self.board['9']) and self.board['1'] != '-':
            self.won = self.board['1'] + ' Won'
            self.finished = True
        elif (self.board['5'] == self.board['2'] == self.board['8'] or self.board['5'] == self.board['4'] == self.board['6'] or self.board['5'] == self.board['7'] == self.board['3']) and self.board['5'] != '-':
            self.won = self.board['5'] + ' Won'
            self.finished = True
        elif self.board['6'] == self.board['9'] == self.board['3'] and self.board != "-":
            self.won = self.board['6'] + ' Won'
            self.finished = True



def main():
    app = TicTacToe()

if __name__ == "__main__":
    main()
