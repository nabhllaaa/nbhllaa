board = {
    "player1": [7, 7, 7, 7, 7, 7, 7],  # Lubang kecil pemain 1
    "player2": [7, 7, 7, 7, 7, 7, 7],  # Lubang kecil pemain 2
    "store1": 0,  # Lumbung pemain 1
    "store2": 0   # Lumbung pemain 2
}

def spread_seeds(board, player, start_pos):
    """Sebar biji dari lubang yang dipilih."""
    seeds = board[player][start_pos]
    board[player][start_pos] = 0  # Kosongkan lubang yang dipilih
    pos = start_pos
    current_player = player

    while seeds > 0:
        pos += 1

        # Sebar di lubang kecil pemain saat ini
        if pos < 7:
            board[current_player][pos] += 1

        # Sebar di lumbung pemain
        elif pos == 7:
            if current_player == "player1" and player == "player1":
                board["store1"] += 1
            elif current_player == "player2" and player == "player2":
                board["store2"] += 1
            else:
                pos = -1  # Pindah ke lubang lawan
                current_player = "player2" if current_player == "player1" else "player1"
                continue

        # Sebar ke lubang lawan
        else:
            pos = -1
            current_player = "player2" if current_player == "player1" else "player1"
            continue

        seeds -= 1

def switch_turn(current_player):
    """Beralih giliran ke pemain lain."""
    return "player2" if current_player == "player1" else "player1"

def check_game_over(board):
    """Periksa apakah permainan sudah selesai."""
    if all(seeds == 0 for seeds in board["player1"]) or all(seeds == 0 for seeds in board["player2"]):
        board["store1"] += sum(board["player1"])
        board["store2"] += sum(board["player2"])
        board["player1"] = [0] * 7
        board["player2"] = [0] * 7
        return True
    return False

def display_board(board):
    """Tampilkan papan permainan."""
    print("\nPapan Permainan:")
    print(f"Lumbung Pemain 2: {board['store2']}")
    print(f"Player 2: {board['player2']}")
    print(f"Player 1: {board['player1']}")
    print(f"Lumbung Pemain 1: {board['store1']}\n")

def play_game():
    """Fungsi utama permainan."""
    current_player = "player1"
    print("Selamat datang di permainan Congklak!")
    while not check_game_over(board):
        display_board(board)
        print(f"Giliran {current_player}.")
        try:
            choice = int(input("Pilih lubang (1-7): ")) - 1
            if 0 <= choice < 7 and board[current_player][choice] > 0:
                spread_seeds(board, current_player, choice)
                current_player = switch_turn(current_player)
            else:
                print("Lubang tidak valid atau kosong. Pilih lagi.")
        except ValueError:
            print("Masukkan angka antara 1 dan 7.")

    display_board(board)
    if board["store1"] > board["store2"]:
        print("Pemain 1 menang!")
    elif board["store2"] > board["store1"]:
        print("Pemain 2 menang!")
    else:
        print("Permainan berakhir seri!")

if __name__ == "__main__":
    play_game()
