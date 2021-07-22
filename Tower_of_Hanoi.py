def tower_of_Hanoi(num_disc, from_pos, to_pos, aux_pos):
    if num_disc == 1:
        move_disc(from_pos, to_pos)
    else:
        tower_of_Hanoi(num_disc-1, from_pos, aux_pos, to_pos)
        move_disc(from_pos, to_pos)
        tower_of_Hanoi(num_disc-1, aux_pos, to_pos, from_pos)

def move_disc(from_pos, to_pos):
    print('Moved 1 disc from {} to {}'.format(from_pos, to_pos))

tower_of_Hanoi(4, 'A', 'C', 'B')

'''
tower_of_Hanoi(4, 'A', 'C', 'B')
    tower_of_Hanoi(3, 'A', 'B', 'C')
        tower_of_Hanoi(2, 'A', 'C', 'B')
            tower_of_Hanoi(1, 'A', 'B', 'C')
                move_disc('A', 'B')
            move_disc('A', 'C')
            tower_of_Hanoi(1, 'B', 'C', 'A')
                move_disc('B', 'C')
        move_disc('A', 'B')
        tower_of_Hanoi(2, 'C', 'B', 'A')
            tower_of_Hanoi(1, 'C' , 'A', 'B')
                move_disc('C', 'A')
            move_disc('C', 'B')
            tower_of_Hanoi(1, 'A', 'B', 'C')
                move_disc('A', 'B')
    move_disc('A', 'C')
    tower_of_Hanoi(3, 'B', 'C', 'A')
'''
