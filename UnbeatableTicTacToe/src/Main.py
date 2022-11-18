import random


class TicTacToe:
    row1 = ["1", "2", "3"]
    row2 = ["4", "5", "6"]
    row3 = ["7", "8", "9"]
    possible_moves = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    finished = False
    oTurn = True
    ai_turn = False

    def __init__(self):
        self.ai_turn = bool(random.getrandbits(1))
        while not self.finished:
            self.refresh_board()

    def print_board(self):
        print("", self.row1[0], self.row1[1], self.row1[2])
        print("", self.row2[0], self.row2[1], self.row2[2])
        print("", self.row3[0], self.row3[1], self.row3[2])
        print()

    def check_if_win(self,curr_char=None):
        if curr_char is None:
            for i in range(3):
                if self.row1[i] == self.row2[i] and self.row2[i] == self.row3[i]:
                    return True

            rows = [self.row1, self.row2, self.row3]
            for i in rows:
                if i[0] == i[1] and i[1] == i[2]:
                    return True

            if self.row1[0] == self.row2[1] and self.row2[1] == self.row3[2]:
                return True

            if self.row1[2] == self.row2[1] and self.row2[1] == self.row3[0]:
                return True
        else:
            rows = [self.row1, self.row2, self.row3]
            for i in rows:
                if i[0] == i[1]:
                    if self.possible_moves.__contains__(i[2]):
                        return i[2]
                if i[0] == i[2]:
                    if self.possible_moves.__contains__(i[1]):
                        return i[1]
                if i[1] == i[2]:
                    if self.possible_moves.__contains__(i[0]):
                        return i[0]

            new_rows = [[self.row1[0],self.row2[0],self.row3[0]],[self.row1[1],self.row2[1],self.row3[1]],[self.row1[2],self.row2[2],self.row3[2]]]
            for i in new_rows:
                if i[0] == i[1]:
                    if self.possible_moves.__contains__(i[2]):
                        return i[2]
                if i[0] == i[2]:
                    if self.possible_moves.__contains__(i[1]):
                        return i[1]
                if i[1] == i[2]:
                    if self.possible_moves.__contains__(i[0]):
                        return i[0]

            if self.row1[0] == self.row2[1]:
                if self.possible_moves.__contains__(self.row3[2]):
                    return self.row3[2]
            if self.row1[0] == self.row3[2]:
                if self.possible_moves.__contains__(self.row2[1]):
                    return self.row2[1]
            if self.row2[1] == self.row3[2]:
                if self.possible_moves.__contains__(self.row1[0]):
                    return self.row1[0]

        return False

    def refresh_board(self, ai=False):
        if len(self.possible_moves) == 9:
            if not self.ai_turn:
                print()
                self.print_board()
        else:
            print()
            self.print_board()

        curr_char = ''
        if self.oTurn:
            curr_char = 'o'
            other_char = 'x'
        else:
            curr_char = 'x'
            other_char = 'o'

        if not self.ai_turn: print("Turn (Player):", curr_char)
        else: print ("Turn (AI):", curr_char)


        done = False
        if not self.ai_turn:
            replace = input("Move: ")
            self.ai_turn = True
        else:
            if not self.check_if_win(other_char): replace = self.possible_moves[random.randint(0, len(self.possible_moves) - 1)]
            else: replace = self.check_if_win(other_char)

            print("AI Move:", replace)
            self.ai_turn = False

        for i in range(len(self.row1)):
            if replace == self.row1[i]:
                self.row1[i] = curr_char
                done = True
                break

        if not done:
            for i in range(len(self.row2)):
                if replace == self.row2[i]:
                    self.row2[i] = curr_char
                    done = True
                    break

        if not done:
            for i in range(len(self.row3)):
                if replace == self.row3[i]:
                    self.row3[i] = curr_char
                    done = True
                    break

        self.possible_moves.remove(replace)

        if self.oTurn: self.oTurn = False
        else: self.oTurn = True
        print()

        if self.check_if_win():
            self.print_board()
            self.finished = True
            print("Player", curr_char, "has won.")

        if len(self.possible_moves) == 0:
            self.print_board()
            self.finished = True
            print("Draw")


TicTacToe()
