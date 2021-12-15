import time
import os
os.system('cls')

def gyertya (x):
    if (x==1):
        print(r"""

|/^\|
 \ /
 _|_
 | |B
 | |É
 | |K
 | |E
 """)

    elif (x==2):
        print(r"""
|/^\|
 \ /
 _|_
 | |B
 | |É
 | |K
 | |E

|/^\|
 \ /
 _|_
 | |H
 | |I
 | |T
 | |

""")

    elif (x==3):
        print(r"""
|/^\|
 \ /
 _|_
 | |B
 | |É 
 | |K
 | |E

|/^\|
 \ /
 _|_
 | |H
 | |I
 | |T
 | |


|/^\|
 \ /
 _|_
 | |SZ
 | |ER
 | |ET
 | |ET


 """)

    elif (x==4):
        print(r"""

|/^\|
 \ /
 _|_
 | |B
 | |É 
 | |K
 | |E


|/^\|
 \ /
 _|_
 | |H
 | |I
 | |T
 | |


|/^\|
 \ /
 _|_
 | |SZ
 | |ER
 | |ET
 | |ET


|/^\|
 \ /
 _|_
 | |R
 | |E
 | |MÉ
 | |NY

 """)

    else:
        print("Max 4 gyertya lehet!!!")


nap = input('December hanyadika van? ')
nap = int(nap)

kari = 24-nap
print(f"\n{kari} nap van még karácsonyig! :))")

input('A továbblépéshez ENTER-t nyomj ')

if (kari<6):
    for x in range(4):
        os.system('cls')
        gyertya(x+1)
        time.sleep(1)
elif (5<kari<13):
    for x in range(3):
        os.system('cls')
        gyertya(x+1)
        time.sleep(1)
elif (12<kari<20):
    for x in range(2):
        os.system('cls')
        gyertya(x+1)
        time.sleep(1)
else :
        os.system('cls')
        gyertya(1)
        time.sleep(1)