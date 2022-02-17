import random
cardpl = {1:'A',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'10',11:'J',12:'Q',13:'K'}
rvrspl = {'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':11,'Q':12,'K':13}

hold1 = []
hold2 = []
hold3 = []
class game:
    def __init__(self,a):
        self.name = a
    def pick(self):  #pick card
        num = ''
        take = random.randrange(1,14)
        card = cardpl[take]
        if self.name == p1:
            hold1.append(card)
        elif self.name == p2:
            hold2.append(card)
        elif self.name == p3:
            hold3.append(card)
        print('Picked ',card)
    def show(self): #show all of cards
        print('You are holding: ')
        num = names[self.name]
        if num == 1:
            print(hold1)
        elif num == 2:
            print(hold2)
        elif num == 3:
            print(hold3)


p1_result = 0
p2_result = 0
p3_result = 0
def calculate(name):
    print("Total point is: ")
    if name == p1:
        num = 0
        for i in range(len(hold1)):
            num += rvrspl[hold1[i]]
        p1_result = num
        print(num)
        return num
    elif name == p2:
        num = 0
        for i in range(len(hold2)):
            num += rvrspl[hold2[i]]
        p2_result = num
        print(num)
        return num
    elif name == p3:
        num = 0
        for i in range(len(hold3)):
            num += rvrspl[hold3[i]]
        p3_result = num
        print(num)
        return num
        
print('---------------------------enter name---------------------------')

p1 = input('player1: ')
p2 = input('player2: ')
p3 = input('player3: ')
names = {p1:1,p2:2,p3:3}

def start(times):
    print('---------------------------round{0}---------------------------'.format(times))
    print('**Please enter "Quit" here if you want to quit**')
    quit_exit = input('Continue or Quit?   ')
    if quit_exit == "Quit":
        pass
    print("---------------------------<<<PLAYER 1'S TURN>>>---------------------------")
    x1 = game(p1)
    while True:
        answer = input("Pick card? Y/N ")
        if answer == 'Y':
            x1.pick()
            pass
        elif answer == 'N':
            break
        else:
            print("You may made a typo, please type again")
            pass
    x1.show()
    p1_result = calculate(p1)
    print("---------------------------<<<PLAYER 2'S TURN>>>---------------------------")
    x2 = game(p2)
    while True:
        x2.pick()
        answer = input("Continue? Y/N ")
        if answer == 'Y':
            pass
        elif answer == 'N':
            break
        else:
            print("You may made a typo, please type again")
            pass
    x2.show()
    p2_result = calculate(p2)
    print("---------------------------<<<PLAYER 3'S TURN>>>---------------------------")
    x3 = game(p3)
    while True:
        x3.pick()
        answer = input("Continue? Y/N ")
        if answer == 'Y':
            pass
        elif answer == 'N':
            break
        else:
            print("You may made a typo, please type again")
            pass
    x3.show()
    p3_result = calculate(p3)   
    boomtime = 0
    report = []     #爆掉的
    if p1_result>21:
        print(p1," You boom boom")
        boomtime += 1
        report.append(1)
    if p2_result>21:
        print(p2," You boom boom")
        boomtime += 1
        report.append(2)
    if p3_result>21:
        print(p3," You boom boom")
        boomtime += 1
        report.append(3)
    if boomtime == 3:
        print('You all bombed :)')
    else:
        thename = ''
        print(boomtime,"players boomed.")
        if boomtime == 2:
            for i in range(1,4):
                if i not in report:
                    if i == 1:
                        thename = p1
                    if i == 2:
                        thename = p2
                    if i == 3:
                        thename = p3
        if boomtime ==1:
            cmpr = []   #用来比较
            name = ''
            for i in range(1,4):
                if i not in report:
                    cmpr.append(i)    
            if 1 not in cmpr:
                if p2_result<p3_result:
                    name = p3
                if p2_result>p3_result:
                    name = p2
                if p2_result == p3_result:
                    name = p2+'and'+p3
            if 2 not in cmpr:
                if p1_result<p3_result:
                    name = p3
                if p1_result>p3_result:
                    name = p1
                if p1_result == p3_result:
                    name = p1+'and'+p3    
            if 3 not in cmpr:
                if p2_result<p1_result:
                    name = p1
                if p2_result>p1_result:
                    name = p2
                if p2_result == p1_result:
                    name = p2+'and'+p1
            thename = name
        if boomtime == 0:
            if p1_result>p2_result:
                if p1_result>p3_result:
                    thename = p1
                if p1_result<p3_result:
                    thename = p3
                if p1_result == p3_result:
                    thename = p1+' and '+p3
            if p1_result<p2_result:
                if p2_result>p3_result:
                    thename = p2
                if p2_result<p3_result:
                    thename = p3
                if p2_result == p3_result:
                    thename = p2+' and '+p3    
            if p1_result == p2_result:
                if p2_result>p3_result:
                    thename = p1+' and '+p2
                if p2_result<p3_result:
                    thename = p3
                if p2_result == p3_result:
                    thename = p1+' and '+p2+' and '+p3                
        print("The WINNER is: ",thename)
    
times = input("How many rounds would you like to play?  Enter: ")
for i in range(int(times)):
    start(i+1)
