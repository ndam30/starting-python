t = [0,1,2,3,4,5,6,7,8]


playerx = "x"
playerO = "o"

def display_board():
    b =f'''              *************
              * {t[0]} |{t[1]} |{t[2]} | *
              * __|__|__| *
              * {t[3]} |{t[4]} |{t[5]} | *
              * __|__|__| *
              * {t[6]} |{t[7]} |{t[8]} | *
              ************* ''' 
    print(b)


def player_input(player):
        n = int(input(player+" entert the number you will like to occupy"));
        t[n]=player

def check_win() :
    
    if t[0]==t[1]==t[2]=='x' or  t[3]==t[4]==t[5]=='x' or t[6]==t[7]==t[8] =='x' :
        print("congratulations playerx  you have won")
        print("end game")
        return True
    elif   t[0]==t[3]==t[6]=='x' or t[1]==t[4]==t[7]=='x' or t[2]==t[5]==t[8]=='x' :
        print("you made it over playero")
        print("end game")
        return True
    elif   t[0]==t[4]==t[8]=='x' or t[2]==t[4]==t[6]=='x' :
        print("you made it over playero")
        print("end game")
        return True
    if t[0]==t[1]==t[2]=='o' or  t[3]==t[4]==t[5]=='o' or t[6]==t[7]==t[8] =='o' :
        print("congratulations playero  you have won")
        print("end game")
        return True
    elif   t[0]==t[3]==t[6]=='o' or t[1]==t[4]==t[7]=='o' or t[2]==t[5]==t[8]=='o' :
        print("you made it over playero")
        print("end game")
        return True
    elif   t[0]==t[4]==t[8]=='o' or t[2]==t[4]==t[6]=='o' :
        print("you made it over playero")
        print("end game")
    # else:
        # print("you both are loosers")

def play():
    print("welcome tictac toe")
    display_board()
    
    for x in range(0,9) :
        if x >= 5:
                if check_win(): 
                   break
        if x%2==0:
            player_input(playerx)
            display_board()
            
        else:
            player_input(playerO)
            display_board()
            
        

    if x > 10:
        print("end game") 

play()