import pygame
pygame.font.init()


class Tic_Tac_Toe:
    def __init__(self):
        self.BACKGROUND = (255, 244, 227)
        self.BLACK = (0, 0, 0)
        self.GREEN = (0, 255, 155)
        self.WIDTH, self.HEIGHT = 500, 500
        self.WIN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.TEXT = pygame.font.SysFont('consolas', 50)
        self.X_TEXT = self.TEXT.render('X', 1, self.BLACK)
        self.O_TEXT = self.TEXT.render('O', 1, self.BLACK)
        self.BOARD = {
            1: {'TL': {'X': 105, 'Y': 105}, 'BR': {'X': 195, 'Y': 195}},
            2: {'TL': {'X': 205, 'Y': 105}, 'BR': {'X': 295, 'Y': 195}},
            3: {'TL': {'X': 305, 'Y': 105}, 'BR': {'X': 395, 'Y': 195}},
            4: {'TL': {'X': 105, 'Y': 205}, 'BR': {'X': 195, 'Y': 295}},
            5: {'TL': {'X': 205, 'Y': 205}, 'BR': {'X': 295, 'Y': 295}},
            6: {'TL': {'X': 305, 'Y': 205}, 'BR': {'X': 395, 'Y': 295}},
            7: {'TL': {'X': 105, 'Y': 305}, 'BR': {'X': 195, 'Y': 395}},
            8: {'TL': {'X': 205, 'Y': 305}, 'BR': {'X': 295, 'Y': 395}},
            9: {'TL': {'X': 305, 'Y': 305}, 'BR': {'X': 395, 'Y': 395}},
        }
        self.marked_list = {
            1: '',
            2: '',
            3: '',
            4: '',
            5: '',
            6: '',
            7: '',
            8: '',
            9: '',
        }
        self.x_turn = True
        self.winner = ""
        self.depth = 10

    def main(self):
        run = True
        pos = (0, 0)
        while run:
            if self.x_turn:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                    if event.type == pygame.MOUSEBUTTONUP:
                        pos = pygame.mouse.get_pos()
                        self.detect_square(pos)
            else:
                self.minimax()

            self.draw()

        pygame.quit()

    def minimax(self):
        depth = self.depth
        current_board = self.marked_list.copy()
        x_turn = self.x_turn

        val = self.maximizer(current_board, depth, x_turn)

        self.mark_square(val[1])
        # print(f"minimax:{val[1]} \n")

    def minimizer(self, current_board, depth, x_turn):
        winner = self.check_win(current_board, not x_turn)

        if depth == 0 or winner != '':
            return (self.evaluate(current_board, not x_turn, depth), 0)

        min_val = float('inf')
        box = 0

        for i in range(1, len(current_board)+1):
            if current_board[i] == "":

                if x_turn:
                    current_board[i] = self.X_TEXT
                else:
                    current_board[i] = self.O_TEXT

                val = self.maximizer(current_board.copy(), depth-1, not x_turn)
                if box == 0:
                    box = i
                    min_val = val[0]
                if val[0] < min_val:
                    box = i
                    min_val = val[0]
                current_board[i] = ""
                # print(f"minimizer: {box}, {min_val} \tdepth:{depth}")
        # print()
        return (min_val, box)

    def maximizer(self, current_board, depth, x_turn):
        winner = self.check_win(current_board, not x_turn)
        if depth == 0 or winner != '':
            return (self.evaluate(current_board, not x_turn, depth), 0)

        max_val = -float('inf')
        box = 0

        for i in range(1, len(current_board)+1):
            if current_board[i] == "":
                if x_turn:
                    current_board[i] = self.X_TEXT
                else:
                    current_board[i] = self.O_TEXT

                val = self.minimizer(current_board.copy(), depth-1, not x_turn)
                if box == 0:
                    box = i
                    max_val = val[0]
                if val[0] > max_val:
                    box = i
                    max_val = val[0]
                current_board[i] = ""
                # print(f"maximizer: {box}, {max_val} \tdepth:{depth}")
        # print()
        return (max_val, box)

    def evaluate(self, board, x_turn, depth):
        winner = self.check_win(board, x_turn)
        if winner == "":
            return 0
        elif winner[0] == "X":
            return -1*(depth+1)
        else:
            return 1*(depth+1)

    def check_win(self, board, x_turn):
        winner = ''
        # horizontal comparison
        for i in range(1, len(board)+1, 3):
            if board[i] == board[i+1] and board[i+1] == board[i+2] and board[i] != '':
                if x_turn:
                    winner = "X is the winner!!"
                else:
                    winner = "O is the winner!!"

        # vertical comparison
        for i in range(1, 4):
            if board[i] == board[i+3] and board[i+3] == board[i+6] and board[i] != '':
                if x_turn:
                    winner = "X is the winner!!"
                else:
                    winner = "O is the winner!!"

        # diagonal comparison
        if board[1] == board[5] and board[5] == board[9] and board[1] != '':
            if x_turn:
                winner = "X is the winner!!"
            else:
                winner = "O is the winner!!"

        if board[3] == board[5] and board[5] == board[7] and board[3] != '':
            if x_turn:
                winner = "X is the winner!!"
            else:
                winner = "O is the winner!!"

        # check for tie
        if winner == '':
            for i in range(1, len(board)+1):
                if board[i] == '':
                    break
            else:
                winner = "It's a draw!!"

        return winner

    def mark_square(self, box):
        if self.marked_list[box] != '':
            return None

        if self.x_turn:
            self.marked_list[box] = self.X_TEXT
        else:
            self.marked_list[box] = self.O_TEXT

        self.depth -= 1
        self.winner = self.check_win(
            self.marked_list, self.x_turn)
        self.x_turn = not self.x_turn

    def detect_square(self, pos):
        for i in range(1, 10):
            if pos[0] >= self.BOARD[i]['TL']['X'] and pos[0] <= self.BOARD[i]['BR']['X'] and pos[1] >= self.BOARD[i]['TL']['Y'] and pos[1] <= self.BOARD[i]['BR']['Y']:
                self.mark_square(i)

    def draw(self):
        self.WIN.fill(self.BACKGROUND)
        self.draw_board()
        for i in range(1, len(self.marked_list)+1):
            if self.marked_list[i] == "":
                continue

            self.WIN.blit(
                self.marked_list[i], (self.BOARD[i]['TL']['X']+28, self.BOARD[i]['TL']['Y']+25))

        if self.winner != "":
            self.show_winner = self.TEXT.render(self.winner, 1, self.GREEN)
            self.WIN.blit(self.show_winner, (25, 25))
            pygame.display.update()
            pygame.time.delay(3000)
            obj = Tic_Tac_Toe()
            obj.main()
            exit(0)
        pygame.display.update()

    def draw_board(self):
        self.v1 = pygame.Rect(195, 100, 10, 300)
        pygame.draw.rect(self.WIN, self.BLACK, self.v1)
        self.v2 = pygame.Rect(295, 100, 10, 300)
        pygame.draw.rect(self.WIN, self.BLACK, self.v2)
        self.h1 = pygame.Rect(100, 195, 300, 10)
        pygame.draw.rect(self.WIN, self.BLACK, self.h1)
        self.h2 = pygame.Rect(100, 295, 300, 10)
        pygame.draw.rect(self.WIN, self.BLACK, self.h2)


if __name__ == '__main__':
    obj = Tic_Tac_Toe()
    obj.main()
