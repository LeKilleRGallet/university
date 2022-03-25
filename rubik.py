import random

def clear():
    if os.name == "posix":
        os.system("clear")
    elif os.name == ("ce", "nt", "dos"):
        os.system("cls")

def print_cube(top, mid1, mid2, mid3, mid4, bottom):

    print()

    mid_face=[mid1,mid2,mid3,mid4]

    for i in range(3):
        print('\t', end = '')
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
        print('\t', end = '')
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

def move_face_left(face):
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

def move_row_right(mid1,mid2,mid3,mid4,row):
    temp2=mid1[row]

    temp1=temp2
    temp2=mid2[row]
    mid2[row]=temp1

    temp1=temp2
    temp2=mid3[row]
    mid3[row]=temp1

    temp1=temp2
    temp2=mid4[row]
    mid4[row]=temp1

    temp1=temp2
    temp2=mid1[row]
    mid1[row]=temp1

def move_row_left(mid1,mid2,mid3,mid4,row):
    temp2=mid1[row]

    temp1=temp2
    temp2=mid4[row]
    mid4[row]=temp1

    temp1=temp2
    temp2=mid3[row]
    mid3[row]=temp1

    temp1=temp2
    temp2=mid2[row]
    mid2[row]=temp1

    temp1=temp2
    temp2=mid1[row]
    mid1[row]=temp1

def run():
    top_face=[[0,0,0],[0,0,0],[0,0,0]]
    mid1_face=[[1,1,1],[1,1,1],[1,1,1]]
    mid2_face=[[2,2,2],[2,2,2],[2,2,2]]
    mid3_face=[[3,3,3],[3,3,3],[3,3,3]]
    mid4_face=[[4,4,4],[4,4,4],[4,4,4]]
    bottom_face=[[5,5,5],[5,5,5],[5,5,5]]

    print_cube(top_face, mid1_face, mid2_face, mid3_face, mid4_face, bottom_face)

if __name__ == "__main__":
    run()