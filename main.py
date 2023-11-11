import copy

class Game:

    def __init__(self, obj = None):
        if obj == None:
            self.array = ["0","0","0","0",'0','0','0',"0",'0','0','0']
            self.turn = 0
        else:
            self.array = copy.copy(obj.array)
            self.turn = copy.copy(obj.turn)


    
    def input_p1(self, s):
        if s >= 0 and s <= (len(self.array)-1):
            if self.array[s] != "0":
                return -1
            else:
                self.array[s]="B"
                i = s + 1
                if (i>=0 and i < len(self.array)):
                    x = self.array[i]
                    while(i>=0 and i < len(self.array)):
                        if(self.array[i] == x and x == "B"):
                            self.array[i]="W"
                            i+=1
                        elif(self.array[i] == x and x == "W"):
                            self.array[i]="B"
                            i+=1
                        else:
                            break
                i = s - 1
                if (i>=0 and i < len(self.array)):
                    x = self.array[i]
                    while(i>=0 and i < len(self.array)):
                        if(self.array[i] == x and x == "B"):
                            self.array[i]="W"
                            i-=1
                        elif(self.array[i] == x and x == "W"):
                            self.array[i]="B"
                            i-=1
                        else:
                            break
                self.turn += 1
                return self
        else:
            return -1
    
    def input_p2(self, s):
        if s >= 0 and s <= (len(self.array)-1):
            if self.array[s] != "0":
                return -1
            else:
                self.array[s]="W"
                i = s + 1
                if (i>=0 and i < len(self.array)):
                    x = self.array[i]
                    while(i>=0 and i < len(self.array)):
                        if(self.array[i] == x and x == "W"):
                            self.array[i]="B"
                            i+=1
                        elif(self.array[i] == x and x == "B"):
                            self.array[i]="W"
                            i+=1
                        else:
                            break
                i = s - 1
                if (i>=0 and i < len(self.array)):
                    x = self.array[i]
                    while(i>=0 and i < len(self.array)):
                        if(self.array[i] == x and x == "W"):
                            self.array[i]="B"
                            i-=1
                        elif(self.array[i] == x and x == "B"):
                            self.array[i]="W"
                            i-=1
                        else:
                            break
                self.turn += 1
                return self
        else:
            return -1
    
    def output(self):
        s = ""
        for i in self.array:
            s += str(i)+" "
        print(s) 
    
    def fin(self):

        if "0" in self.array:  
            return False
        else:
            return True
    
    def value(self):
        val = 0
        for i in self.array:
            if i == "B":
                val += 1
        return val

    def player(self):
        if (self.turn % 2 == 0):
            return 1
        else:
            return 2

    def actions(self):
        actions = []
        for i in range(len(self.array)):
            if self.array[i] == "0":
                actions.append(i)
        return actions
    
    def minimax(self):

        if (self.fin()):
            return self.value()

        if self.player() == 1:
            val = -99999
            for a in self.actions():
                self.input_p1(a)
                val = max(val, self.minimax())
            return val
        if self.player() == 2:
            val = 99999
            for a in self.actions():
                self.input_p2(a)
                val = min(val, self.minimax())
            return val


    


'''

game = Game()
game.input_p1(10)
game.input_p1(8)
game.input_p1(6)
game.input_p1(9)
game.input_p2(7)
print(game.fin())
print(minimax(game))
game.output()
'''


while(True):
    game = Game()
    
    turn = 0
    while(True):
        if (turn % 2 == 0):
            print("Player 1:-")
            x = int(input("Enter value: "))
            while (game.input_p1(x) == -1):
                x = int(input("Enter value: "))
        else:
            print("Player 2:-")
            x = int(input("Enter value: "))
            while (game.input_p2(x) == -1):
                x = int(input("Enter value: "))
        turn+=1
        temp = Game(game)
        #temp.copy(game)
        print(f"\nUtiity: {temp.minimax()}")
        game.output()
        print()
        if (game.fin()):
            print("Game over.")
            break
    
    x = input("Do you want to play again? (y/n): ").lower().strip()
    print("\n\n\n")
    if(x == "n"):
        break
