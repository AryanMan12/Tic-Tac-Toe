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

    def main(self):
        run = True
        pos = (0, 0)
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    self.detect_square(pos)

            self.draw()

        pygame.quit()

    def check_win(self):
        # horizontal comparison
        for i in range(1, len(self.marked_list)+1, 3):
            if self.marked_list[i] == self.marked_list[i+1] and self.marked_list[i+1] == self.marked_list[i+2] and self.marked_list[i] != '':
                if self.x_turn:
                    self.winner = "X is the winner!!"
                else:
                    self.winner = "O is the winner!!"

        # vertical comparison
        for i in range(1, 4):
            if self.marked_list[i] == self.marked_list[i+3] and self.marked_list[i+3] == self.marked_list[i+6] and self.marked_list[i] != '':
                if self.x_turn:
                    self.winner = "X is the winner!!"
                else:
                    self.winner = "O is the winner!!"

        # diagonal comparison
        if self.marked_list[1] == self.marked_list[5] and self.marked_list[5] == self.marked_list[9] and self.marked_list[1] != '':
            if self.x_turn:
                self.winner = "X is the winner!!"
            else:
                self.winner = "O is the winner!!"

        if self.marked_list[3] == self.marked_list[5] and self.marked_list[5] == self.marked_list[7] and self.marked_list[3] != '':
            if self.x_turn:
                self.winner = "X is the winner!!"
            else:
                self.winner = "O is the winner!!"

        # check for tie
        if self.winner == '':
            for i in range(1, len(self.marked_list)+1):
                if self.marked_list[i] == '':
                    break
            else:
                self.winner = "It's a draw!!"

    def mark_square(self, box):
        if self.marked_list[box] != '':
            return None

        if self.x_turn:
            self.marked_list[box] = self.X_TEXT
        else:
            self.marked_list[box] = self.O_TEXT
        self.check_win()
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
