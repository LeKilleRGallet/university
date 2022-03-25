import random
import os
import numpy as np

def clear():
    if os.name == "posix":
        os.system("clear")
    elif os.name == ("ce", "nt", "dos"):
        os.system("cls")

def print_cube(top, mid1, mid2, mid3, mid4, bottom):

    print()

    mid_face=[mid1,mid2,mid3,mid4]

    for i in range(3):
        
        for j in range(3):
            print(top[i][j],end=" ")
        print()

    print('-'*30)

    j = 0
    while j < 3:
        i=0
        while i < 4:
            
            for k in range(3):
                print(mid_face[i][j][k],end=" ")
            print('|', end = '')
            i += 1
        print()
        j += 1
    print('-'*30)

    for i in range(3):
        
        for j in range(3):
            print(bottom[i][j],end=" ")
        print()

def mov_face_right(face):
    for _ in range(2):
        temp2=face[0][0]

        temp1=temp2
        temp2=face[1][0]
        face[1][0]=temp1

        temp1=temp2
        temp2=face[2][0]
        face[2][0]=temp1

        temp1=temp2
        temp2=face[2][1]
        face[2][1]=temp1

        temp1=temp2
        temp2=face[2][2]
        face[2][2]=temp1

        temp1=temp2
        temp2=face[1][2]
        face[1][2]=temp1

        temp1=temp2
        temp2=face[0][2]
        face[0][2]=temp1

        temp1=temp2
        temp2=face[0][1]
        face[0][1]=temp1

        temp1=temp2
        temp2=face[0][0]
        face[0][0]=temp1

def mov_face_left(face):
    for _ in range(2):
        temp2=face[0][0]

        temp1=temp2
        temp2=face[0][1]
        face[0][1]=temp1

        temp1=temp2
        temp2=face[0][2]
        face[0][2]=temp1

        temp1=temp2
        temp2=face[1][2]
        face[1][2]=temp1

        temp1=temp2
        temp2=face[2][2]
        face[2][2]=temp1

        temp1=temp2
        temp2=face[2][1]
        face[2][1]=temp1

        temp1=temp2
        temp2=face[2][0]
        face[2][0]=temp1

        temp1=temp2
        temp2=face[1][0]
        face[1][0]=temp1

        temp1=temp2
        temp2=face[0][0]
        face[0][0]=temp1

def move_row(v1,v2,v3,v4, side):
    if side == 'r':
        return v4, v1, v2,v3
    elif side == 'l':
        return v2, v3, v4,v1

def transpose(matrix, vector, row):
    for i in range(3):
        matrix[i][row]=vector[i]

def rubik_shuffle(top, mid1, mid2, mid3, mid4, bottom):
    num_moves = random.randint(1,10)

    for _ in range(num_moves):

        move=random.randint(1,9)
        side=random.randint(0,1)

        if move == 1:
            print('move top face')
            n=0
            if side==0:
                print('right')
                mov_face_right(top)
                mid1[n],mid2[n],mid3[n],mid4[n]=move_row(mid1[n],mid2[n],mid3[n],mid4[n], 'r')
            elif side==1:
                print('left')
                mov_face_left(top)
                mid1[n],mid2[n],mid3[n],mid4[n]=move_row(mid1[n],mid2[n],mid3[n],mid4[n], 'l')
                
        elif move == 2:
            print('move mid1 face')
            if side==0:
                print('right')
                mov_face_right(mid1)
                pass

            elif side==1:
                print('left')
                mov_face_left(mid1)
                pass
                
        elif move == 3:
            print('move mid2 face')
            if side==0:
                print('right')
                mov_face_right(mid2)
                pass

            elif side==1:
                print('left')
                mov_face_left(mid2)
                pass
                
        elif move == 4:
            print('move mid3 face')
            if side==0:
                print('right')
                mov_face_right(mid3)
                pass

            elif side==1:
                print('left')
                mov_face_left(mid3)
                pass
                
        elif move == 5:
            print('move mid4 face')
            if side==0:
                print('right')
                mov_face_right(mid4)
                pass

            elif side==1:
                print('left')
                mov_face_left(mid4)
                pass
                
        elif move == 6:
            print('move bottom face')
            n=2
            if side==0:
                print('right')
                mov_face_right(bottom)
                mid1[n],mid2[n],mid3[n],mid4[n]=move_row(mid1[n],mid2[n],mid3[n],mid4[n], 'r')
            elif side==1:
                print('left')
                mov_face_left(bottom)
                mid1[n],mid2[n],mid3[n],mid4[n]=move_row(mid1[n],mid2[n],mid3[n],mid4[n], 'l')
                
        elif move == 7:
            print('move mid row')
            n=1
            if side==0:
                print('right')
                mid1[n],mid2[n],mid3[n],mid4[n]=move_row(mid1[n],mid2[n],mid3[n],mid4[n], 'r')
            elif side==1:
                print('left')
                mid1[n],mid2[n],mid3[n],mid4[n]=move_row(mid1[n],mid2[n],mid3[n],mid4[n], 'l')
        elif move == 8:
            print('move mid column - mid1 - mid 3')
            n=1
            if side==0:
                print('right')

                tempmtx1=np.array(top)
                tempmtx2=np.array(mid1)
                tempmtx3=np.array(bottom)
                tempmtx4=np.array(mid3)

                v1t,v2t,v3t,v4t=move_row(list(tempmtx1.T[n]),list(tempmtx2.T[n]),list(tempmtx3.T[n]),list(tempmtx4.T[n]), 'r')

                transpose(top,v1t,n)
                transpose(mid1,v2t,n)
                transpose(bottom,v3t,n)
                transpose(mid3,v4t,n)

            elif side==1:
                print('left')

                tempmtx1=np.array(top)
                tempmtx2=np.array(mid1)
                tempmtx3=np.array(bottom)
                tempmtx4=np.array(mid3)

                v1t,v2t,v3t,v4t=move_row(list(tempmtx1.T[n]),list(tempmtx2.T[n]),list(tempmtx3.T[n]),list(tempmtx4.T[n]), 'l')

                transpose(top,v1t,n)
                transpose(mid1,v2t,n)
                transpose(bottom,v3t,n)
                transpose(mid3,v4t,n)
                
        elif move == 9:
            print('move mid column - mid2 - mid 4')

            n=1

            if side==0:
                print('right')

                tempmtx1=np.array(mid2)
                tempmtx2=np.array(mid4)

                top[n],v1t,bottom[n],v2t=move_row(top[n],list(tempmtx1.T[n]),bottom[n],list(tempmtx2.T[n]), 'r')

                transpose(mid2,v1t,n)
                transpose(mid4,v2t,n)

            elif side==1:
                print('left')

                tempmtx1=np.array(mid2)
                tempmtx2=np.array(mid4)

                top[n],v1t,bottom[n],v2t=move_row(top[n],list(tempmtx1.T[n]),bottom[n],list(tempmtx2.T[n]), 'l')

                transpose(mid2,v1t,n)
                transpose(mid4,v2t,n)

        print_cube(top,mid1,mid2,mid3,mid4,bottom)

def run():
    top=[[0,0,0],[0,0,0],[0,0,0]]
    mid1=[[1,1,1],[1,1,1],[1,1,1]]
    mid2=[[2,2,2],[2,2,2],[2,2,2]]
    mid3=[[3,3,3],[3,3,3],[3,3,3]]
    mid4=[[4,4,4],[4,4,4],[4,4,4]]
    bottom=[[5,5,5],[5,5,5],[5,5,5]]

    print_cube(top, mid1, mid2, mid3, mid4, bottom)

    rubik_shuffle(top, mid1, mid2, mid3, mid4, bottom)
    
    print_cube(top, mid1, mid2, mid3, mid4, bottom)

if __name__ == "__main__":
    run()