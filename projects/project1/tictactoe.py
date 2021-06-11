import random

def display_board(board):
    print('\n'*50)
    print(board[7]+' | '+board[8]+' | '+board[9])
    print('---------')
    print(board[4]+' | '+board[5]+' | '+board[6])
    print('---------')
    print(board[1]+' | '+board[2]+' | '+board[3])

def player_input():
    """
    player input dan assign marker untuk player sebagai "X" atau "O", menggunakan while loops untuk secara terus
    menerus memberikan pertanyaan sampai player memberikan input jawaban yang benar
    """
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Player1: Pilih X atau O: ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board, marker, position):
    """
    marker ("X" atau "O"), dan position yang diinginkan (nomor 1-9) dan taruh di dalam board
    """
    # panggil board[index position] = marker yang harus ditaruh di dalam board
    board[position] = marker

def win_check(board, mark):
    """
    check board dan marker untuk melihat apakah marker dari player1 atau player2 yang menang
    """
    # Winner check marker
    #   cek row atau baris , apakah deretan baris tersebut mempunyai marker yang sama
    #   cek column, apakah deretan column mempunyai marker yang sama
    #   cek 2 diagonal, apakah mempunyai kolom yang sama

    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # garis3
            (board[4] == mark and board[5] == mark and board[6] == mark) or # garis2
            (board[1] == mark and board[2] == mark and board[3] == mark) or # garis1
            (board[7] == mark and board[4] == mark and board[1] == mark) or # kolom1
            (board[8] == mark and board[5] == mark and board[2] == mark) or # kolom2
            (board[9] == mark and board[6] == mark and board[3] == mark) or # kolom3
            (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal1
            (board[1] == mark and board[5] == mark and board[9] == mark)) # diagonal2

def choose_first():
    """ pilih player yang mulai duluan """
    flip = random.randint(0, 1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):
    """
     cek apakah space atau masih ada ruang kosong di dalam board
     """
    return board[position] == ' '

def full_board_check(board):
    """
     cek apakah board sudah penuh akan marker, True jika full dan False jika tidak
     """
    for i in range(1, 10):
        # jika masih ada space di dalam board maka board berarti masih kosong atau False
        if space_check(board, i):
            return False
    # board penuh, berarti True
    return True

def player_choice(board):
    """
     bertanya kepada player untuk posisi berikutnya di board sebagai number 1-9 dan kemudian gunakan function
     space_check dan full_board_check untuk mengecek space kosong, jika ada tampilkan posisinya
     """
    position = 0

    # selama posisi tidak ada di dalam list.... atau cek space masih ada dalam board
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        # maka tanya posisi player berikutnya
        position = int(input('Pilih langkah anda berikutnya (1-9) '))
    return position

def replay():
    """
     tanya player apakah mau main lagi
     """
    choice = input("Main lagi? (ketik 'Y' atau 'T'): ")
    return choice == 'Y'


print('Selamat datang di permainan Tic TAC TOE')
# loop game play
while True:
    # play the game

    ## setting up (board, undi player yang main duluan, pilih marker apakah X atau O)
    the_board = [' ']*10
    player1_marker, player2_marker = player_input()

    # undi player yang main duluan
    turn = choose_first()
    print(turn + ' akan mulai duluan')

    # konfirmasi menanyakan
    play_game = input("Siap untuk main? y atau n? ")
    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    ## actual game play
    while game_on:
        ### Player1 turn
        if turn == 'Player 1':
            # show the board
            display_board(the_board)
            # pilih position
            position =  player_choice(the_board)
            # place marker di position
            place_marker(the_board, player1_marker, position)
            # check apakah Player 1 menang
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('Player 1 MENANG!!!')
                game_on = False
            # atau cek jika imbang
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Game Imbang')
                    game_on = False
                else:
                    turn = 'Player 2'

        ### Player2 turn
        else:
            # show the board
            display_board(the_board)
            # pilih position
            position = player_choice(the_board)
            # place marker di position
            place_marker(the_board, player2_marker, position)
            # check apakah Payer 1 menang
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('Player 2 MENANG!!!')
                game_on = False
            # atau cek jika imbang
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Game Imbang')
                    game_on = False
                else:
                    turn = 'Player 1'


    # Berhenti main game
    if not replay():
        break




