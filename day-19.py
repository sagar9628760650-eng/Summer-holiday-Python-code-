for row in range (7):
    for col in range (4):
        if( col==3) and (row!=6)  or ( row==6) and (col>0 and col<3) or (col==0 and (row>3 and row<6)): 
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()         