import os
import chess
import chess.engine
import chess.pgn

engine = chess.engine.SimpleEngine.popen_uci("/usr/games/stockfish")
cwd_addr = os.getcwd()

game_file = open(cwd_addr+"/Database/MagnusCarlsen/2017/3/6.pgn", 'r')
game = chess.pgn.read_game(game_file)
board = game.board()
moves = list(game.mainline_moves())

for move in moves[0:5]:
    board.push(move)
    print(board.turn)

print("\n")


def top_ten_moves(analysis_board, analysis_engine):
    best_moves = []
    for legal_move in analysis_board.legal_moves:
        analysis_board.push(legal_move)
        print(analysis_board.turn)
        info = analysis_engine.analyse(analysis_board, chess.engine.Limit(depth=10))
        best_moves.append([legal_move, info["score"].relative])
        analysis_board.pop()
    best_moves.sort(key=lambda x: x[1])
    return best_moves[0:10]


this_list = top_ten_moves(board, engine)
print(board.turn)
print(this_list)
