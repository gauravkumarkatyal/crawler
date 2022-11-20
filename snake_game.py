import random
def gamewin (comp,you):
    if comp ==you:
        return None
    elif comp =='s':
        if you =='w':
            return false 
        elif you=='g':
            return True
    elif comp=='w':
        if you =='g':
            return False
        elif you=='s':
            return true
    elif comp == 'g':
        if you=='s':
            return false 
        elif you=='s':
            return true 
    elif comp =='g':
        if you =='s':
            return False
        elif you=='w':
            return True
print('comp turn:snanke(s) water(w) or gun(g)?')
randno=random.randint(1,3)
if randno==1:
    comp='s'
elif randno==2:
    comp='w'
elif randno==3 :
    comp='g'
you=input('your turn:snake(s) water(w) or gun(g)?')
a=gamewin(comp, you)   
print(f'computer chose{comp}')
print(f'you chose{you}')
if a==None:
    print('tie')
elif a:
    print('you win')
else:
    print('you lose')                                       

