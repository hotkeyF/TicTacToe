import kivy
import random
from kivy.app import App
from kivy.core import text
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
class TicTacToe(App):
    pass



class MainWidget(GridLayout):

    fp = 'X'
    mE = [[]]
    tE = [[]]
    rE = [[]]
    bE = [[]]
    lE = [[]] 
    d1E = [[]]
    d2E = [[]]
    cE = [[]]

   

    def winnerCheck(self, array):
        if array[1] == 'X' and array[2] == 'X' and array[3] == 'X':
            for el in array[0]:
                el.disabled = False
                el.color = (0,1,0,1)
            return 'X'
        elif array[1] == 'O' and array[2] == 'O' and array[3] == 'O':
            return 'O'
        else:
            return None
   
    def buttonPressed(self, btn):

        if 'M' in btn.text:
            self.mE[0].append(btn)
            self.mE.append(self.fp)
            print('M')
            print(self.mE)
        if 'T' in btn.text:
            self.tE[0].append(btn)
            self.tE.append(self.fp)
            print('T')
            print(self.tE)
        if 'R' in btn.text:
            self.rE[0].append(btn)
            self.rE.append(self.fp)
            print('R')
            print(self.rE)
        if 'B' in btn.text:
            self.bE[0].append(btn)
            self.bE.append(self.fp)
            print('B')
            print(self.bE)
        if 'L' in btn.text:
            self.lE[0].append(btn)
            self.lE.append(self.fp)
            print('L')
            print(self.lE)
        if 'C' in btn.text:
            self.cE[0].append(btn)
            self.cE.append(self.fp)
            print('C')
            print(self.cE)
        if btn.text == 'TL' or btn.text == 'MC' or btn.text == 'BR':
            self.d1E[0].append(btn)
            self.d1E.append(self.fp)
            print('TL|MC|BR')
            print(self.d1E)  
        if btn.text == 'TR' or btn.text == 'MC' or btn.text == 'BL':
            self.d2E[0].append(btn)
            self.d2E.append(self.fp)
            print('TR|MC|BL')
            print(self.d2E)
        btn.text = self.fp
       
        if self.fp == 'X':
            self.fp = 'O'
        else:
            self.fp = 'X'
        btn.disabled = True
        
        
        

        winner = None
        if len(self.mE) == 4:
            winner = self.winnerCheck(self.mE)
        elif len(self.tE) == 4:
            winner = self.winnerCheck(self.tE)
        elif len(self.lE) == 4:
            winner = self.winnerCheck(self.lE)
        elif len(self.bE) == 4:
            winner = self.winnerCheck(self.bE)
        elif len(self.rE) == 4:
            winner = self.winnerCheck(self.rE)
        elif len(self.cE) == 4:
            winner = self.winnerCheck(self.cE)
        elif len(self.d1E) == 4:
            winner = self.winnerCheck(self.d1E)
        elif len(self.d2E) == 4:
            winner = self.winnerCheck(self.d2E)
        if winner != None:
            wig = Label(text="Winner is: "+ winner)
            
            self.add_widget(wig)
    
            



if __name__ == "__main__":
    TicTacToe().run()