""" Tower of Hanoi moving all disc to bar B"""
def TowerOfHanoi(Num_of_disc, move_from, move_to, assist_bar):
    if Num_of_disc == 0:
        return
    TowerOfHanoi(Num_of_disc - 1, move_from, assist_bar, move_to )
    print(f"Move disc {Num_of_disc}  from {move_from} to {move_to }")
    TowerOfHanoi(Num_of_disc - 1, assist_bar, move_to, move_from )
    
if __name__ == '__main__':
    numberOfDisc = input('Enter number of disc')
    if numberOfDisc.isdigit():
        num = int(numberOfDisc)
        TowerOfHanoi(num,'A','B','C' )
    else:
        print(f"{numberOfDisc} is not a number")
    
    
    

