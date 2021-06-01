import random
from PIL import Image
end = 100
#start = 1
ladder_dict = {1:38,4:14,9:31,21:42,28:84,51:67,72:91,80:99}
snake_dict = {17:7,54:34,62:19,64:60,87:36,93:73,95:75,98:79}
def reached_end(points):
    if points == end:
        return True
    else:
        return False
def check_ladder(points):
    #Dict() of (ladder bottom,top) (key,value) pairs
    #check and update that
    if points in ladder_dict:
        print("!!LADDER!!")
        return ladder_dict[points]
    else:
        return points

def check_snake(points):
    #Dict() of (ladder bottom,top) (key,value) pairs
    #check and update that
    if points in snake_dict:
        print("!!Oops!Snake bite!!")
        return snake_dict[points]
    else:
        return points
def show_board():
    img = Image.open("snakes_ladders_board.jpg")
    img.show()
def play():
    #player_one name
    #raw_input is especially for strings with spaces
    p1_name = input("player_1, Enter your name : ")
    #player_two name
    p2_name = input("player_2, Enter your name : ")
    pp1 = 0;pp2 =0#points of players
    turn = 0
    #Now game starts
    while (True):
        if turn%2 == 0:
            #player_one chance
            print(p1_name,"Your Turn")
            #choice to continnue or not
            c = input("Press '0' to exit,'1' to continue : ")
            if (c == '0'):
                print(p1_name,"your score is:",pp1)
                print(p2_name,"your score is:",pp2)
                print("Thanks for playing!")
                break
            #esle c==1
            dice = random.randint(1,6) # 1,2,3,4,5,6
            print("Dice shown",dice)
            pp1 += dice
            pp1 = check_ladder(pp1)
            #if on ladder,then incraese/update points
            pp1 = check_snake(pp1)
            #if on snake,then decrease/update points or position
            if pp1>=end:
                pp1 = end
            #Need to print score after every turn
            print(p1_name,"your score :",pp1)
            if reached_end(pp1):
                print(p1_name,",Hurray!You won.")
                break
        else:
            #player_two chance
            print(p2_name,"Your Turn")
            #choice to continnue or not
            c = input("Press '0' to exit,'1' to continue : ")
            if (c =='0'):
                print(p1_name,"your score is:",pp1)
                print(p2_name,"your score is:",pp2)
                print("Thanks for playing!")
                break
            #esle c==1
            dice = random.randint(1,6) # 1,2,3,4,5,6
            print("Dice shown",dice)
            pp2 += dice
            pp2 = check_ladder(pp2)
            #if on ladder,then incraese/update points
            pp2 = check_snake(pp2)
            #if on snake,then decrease/update points or position
            if pp2>=end:
                pp2 = end
            #Need to print score after every turn
            print(p2_name,"your score :",pp2)
            if(reached_end(pp2)):
                print(p2_name,",Hurray!You won.")
                break
        turn+=1
            
show_board()
play()
