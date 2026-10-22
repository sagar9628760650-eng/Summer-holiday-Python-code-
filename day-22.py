for row in range (7):
    for col in range (5):
        if(( col==0) or (col==4) or (col==2 and row==2) or (row==1 and col!=2)): 
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()         