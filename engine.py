import const
import chess

class Engine(chess.Board):
    def __init__(self,fen='rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1',chess960=False,side=-1):
        super().__init__(fen)
        self.side = side

    def search(self) -> str:
        good_moves = {}
        for move in list(self.legal_moves):
            self.push(move)
            good_moves[str(move)] = self.evaluate()
            self.pop()
        print(good_moves)
        if self.side == -1:
            return min(good_moves, key=good_moves.get)
        else:
            return max(good_moves, key=good_moves.get)

    def evaluate(self) -> int:
        evaluation = 0
        piece_map = self.piece_map()
        for square in piece_map:
            material_of_square = 0
            side = 0
            if str(piece_map[square]).upper() == str(piece_map[square]):
                material_of_square = 1
                side = -1
            else:
                material_of_square = -1
                side = 1
            if str(piece_map[square]).lower() == 'p':
                material_of_square *= const.PAWN * const.mg_pawn_table[::side][square//8][square%8]
            elif str(piece_map[square]).lower() == 'b':
                material_of_square *= const.BISHOP * const.mg_bishop_table[::side][square//8][square%8]
            elif str(piece_map[square]).lower() == 'n':
                material_of_square *= const.KNIGHT * const.mg_knight_table[::side][square//8][square%8]
            elif str(piece_map[square]).lower() == 'r':
                material_of_square *= const.ROOK * const.mg_rook_table[::side][square//8][square%8]
            elif str(piece_map[square]).lower() == 'q':
                material_of_square *= const.QUEEN * const.mg_queen_table[::side][square//8][square%8]
            elif str(piece_map[square]).lower() == 'k':
                material_of_square *= const.KING * const.mg_king_table[::side][square//8][square%8]
            evaluation += material_of_square
        return evaluation
