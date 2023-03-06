import pygame
from constants import Black, rows, lsquare, square_size, dsquare, cols, White
from piece import Piece


class board:
    def __init__(self):
        self.board = []
        self.black_left = self.white_left = 12
        self.black_kings = self.white_kings = 0
        self.create_board()

    # Draws Squares of Board
    def draw_squares(self, win):
        win.fill(lsquare)
        for row in range(rows):
            for col in range(row % 2, cols, 2):
                pygame.draw.rect(win, dsquare, (row * square_size, col * square_size, square_size, square_size))

    # Moves
    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

        if row == rows - 1 or row == 0:
            piece.make_king()
            if piece.color == White:
                self.white_kings += 1
            else:
                self.black_kings += 1

    # Selects Piece
    def get_piece(self, row, col):
        return self.board[row][col]

    # Draws Pieces on board
    def create_board(self):
        for row in range(rows):
            self.board.append([])
            for col in range(cols):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, White))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, Black))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    # draws board
    def draw(self, win):
        self.draw_squares(win)
        for row in range(rows):
            for col in range(cols):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)

    # Removes pieces that were jumped over
    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.color == Black:
                    self.black_left -= 1
                else:
                    self.white_left -= 1

    # Unfinished
    def winner(self):
        if self.black_left <= 0:
            return White
        elif self.white_left <= 0:
            return Black

        return None

    # Gets Valid Moves - This Until The End is Taken
    def get_valid_moves(self, piece):
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row

        if piece.color == Black or piece.king:
            moves.update(self._traverse_left(row - 1, max(row - 3, -1), -1, piece.color, left))
            moves.update(self._traverse_right(row - 1, max(row - 3, -1), -1, piece.color, right))
        if piece.color == White or piece.king:
            moves.update(self._traverse_left(row + 1, min(row + 3, rows), 1, piece.color, left))
            moves.update(self._traverse_right(row + 1, min(row + 3, rows), 1, piece.color, right))

        return moves

    # Moves left
    def _traverse_left(self, start, stop, step, color, left, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break

            current = self.board[r][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last

                if last:
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, rows)
                    moves.update(self._traverse_left(r + step, row, step, color, left - 1, skipped=last))
                    moves.update(self._traverse_right(r + step, row, step, color, left + 1, skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            left -= 1

        return moves

    # Moves Right
    def _traverse_right(self, start, stop, step, color, right, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= cols:
                break

            current = self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, right)] = last + skipped
                else:
                    moves[(r, right)] = last

                if last:
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, rows)
                    moves.update(self._traverse_left(r + step, row, step, color, right - 1, skipped=last))
                    moves.update(self._traverse_right(r + step, row, step, color, right + 1, skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            right += 1

        return moves