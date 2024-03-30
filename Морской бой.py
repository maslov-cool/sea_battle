class SeaMap:
    def __init__(self):
        self.field = [['.' for _ in range(10)] for _ in range(10)]

    def shoot(self, row, col, result):
        if result == 'miss':
            self.field[row][col] = '*'
        elif result == 'hit':
            self.field[row][col] = 'x'
        else:
            self.field[row][col] = 'x'

            # задели в верхней левой клетке
            if not row and not col:
                if self.field[row][col + 1] != 'x':
                    self.field[row][col + 1] = '*'
                else:
                    if self.field[row][col + 2] != 'x':
                        self.field[row][col + 2] = '*'
                    if self.field[row + 1][col + 2] != 'x':
                        self.field[row + 1][col + 2] = '*'
                if self.field[row + 1][col] != 'x':
                    self.field[row + 1][col] = '*'
                if self.field[row + 1][col + 1] != 'x':
                    self.field[row + 1][col + 1] = '*'

            # задели в верхней правой клетке
            elif not row and col == 9:
                if self.field[row][col - 1] != 'x':
                    self.field[row][col - 1] = '*'
                else:
                    if self.field[row][col - 2] != 'x':
                        self.field[row][col - 2] = '*'
                    if self.field[row + 1][col - 2] != 'x':
                        self.field[row + 1][col - 2] = '*'
                if self.field[row + 1][col] != 'x':
                    self.field[row + 1][col] = '*'
                if self.field[row + 1][col - 1] != 'x':
                    self.field[row + 1][col - 1] = '*'

            # задели в нижней правой клетке
            elif row == 9 and col == 9:
                if self.field[row][col - 1] != 'x':
                    self.field[row][col - 1] = '*'
                else:
                    if self.field[row][col - 2] != 'x':
                        self.field[row][col - 2] = '*'
                    if self.field[row - 1][col - 2] != 'x':
                        self.field[row - 1][col - 2] = '*'
                if self.field[row - 1][col] != 'x':
                    self.field[row - 1][col] = '*'
                if self.field[row - 1][col - 1] != 'x':
                    self.field[row - 1][col - 1] = '*'

            # задели в нижней левой клетке
            elif row == 9 and not col:
                if self.field[row][col + 1] != 'x':
                    self.field[row][col + 1] = '*'
                else:
                    if self.field[row][col + 2] != 'x':
                        self.field[row][col + 2] = '*'
                    if self.field[row - 1][col + 2] != 'x':
                        self.field[row - 1][col + 2] = '*'
                if self.field[row - 1][col] != 'x':
                    self.field[row - 1][col] = '*'
                if self.field[row - 1][col + 1] != 'x':
                    self.field[row - 1][col + 1] = '*'

            # задели вверху
            elif not row and 0 < col < 9:
                i = col
                while self.field[row][i] == 'x' and i > -1:
                    if self.field[row + 1][i] != 'x':
                        self.field[row + 1][i] = '*'
                    i -= 1
                if i != -1:
                    if self.field[row + 1][i] != 'x':
                        self.field[row + 1][i] = '*'
                    if self.field[row][i] != 'x':
                        self.field[row][i] = '*'

                i = col
                while self.field[row][i] == 'x' and i < 10:
                    if self.field[row + 1][i] != 'x':
                        self.field[row + 1][i] = '*'
                    i += 1
                if i < 10:
                    if self.field[row + 1][i] != 'x':
                        self.field[row + 1][i] = '*'
                    if self.field[row][i] != 'x':
                        self.field[row][i] = '*'

            # задели внизу
            elif row == 9 and 0 < col < 9:
                i = col
                while self.field[row][i] == 'x' and i > -1:
                    if self.field[row - 1][i] != 'x':
                        self.field[row - 1][i] = '*'
                    i -= 1
                if i != -1:
                    if self.field[row][i] != 'x':
                        self.field[row][i] = '*'
                    if self.field[row - 1][i] != 'x':
                        self.field[row - 1][i] = '*'

                i = col
                while self.field[row][i] == 'x' and i < 10:
                    if self.field[row - 1][i] != 'x':
                        self.field[row - 1][i] = '*'
                    i += 1
                if i < 10:
                    if self.field[row][i] != 'x':
                        self.field[row][i] = '*'
                    if self.field[row - 1][i] != 'x':
                        self.field[row - 1][i] = '*'

            # задели справа
            elif 0 < row < 9 and col == 9:
                i = row
                while self.field[i][col] == 'x' and i > -1:
                    if self.field[i][col - 1] != 'x':
                        self.field[i][col - 1] = '*'
                    i -= 1
                if i != -1:
                    if self.field[i][col - 1] != 'x':
                        self.field[i][col - 1] = '*'
                    if self.field[i][col] != 'x':
                        self.field[i][col] = '*'

                i = row
                while self.field[i][col] == 'x' and i < 10:
                    if self.field[i][col - 1] != 'x':
                        self.field[i][col - 1] = '*'
                    i += 1
                if i < 10:
                    if self.field[i][col - 1] != 'x':
                        self.field[i][col - 1] = '*'
                    if self.field[i][col] != 'x':
                        self.field[i][col] = '*'

            # задели слева
            elif 0 < row < 9 and not col:
                i = row
                while self.field[i][col] == 'x' and i > -1:
                    if self.field[i][col + 1] != 'x':
                        self.field[i][col + 1] = '*'
                    i -= 1
                if i != -1:
                    if self.field[i][col + 1] != 'x':
                        self.field[i][col + 1] = '*'
                    if self.field[i][col] != 'x':
                        self.field[i][col] = '*'

                i = row
                while self.field[i][col] == 'x' and i < 10:
                    if self.field[i][col + 1] != 'x':
                        self.field[i][col + 1] = '*'
                    i += 1
                if i < 10:
                    if self.field[i][col + 1] != 'x':
                        self.field[i][col + 1] = '*'
                    if self.field[i][col] != 'x':
                        self.field[i][col] = '*'

            # задели внутри
            elif 0 < row < 9 and 0 < col < 9:
                i = col
                while self.field[row][i] == 'x':
                    if self.field[row + 1][i] != 'x':
                        self.field[row + 1][i] = '*'
                    if self.field[row - 1][i] != 'x':
                        self.field[row - 1][i] = '*'
                    i -= 1
                if self.field[row + 1][i] != 'x':
                    self.field[row + 1][i] = '*'
                if self.field[row][i] != 'x':
                    self.field[row][i] = '*'
                if self.field[row - 1][i] != 'x':
                    self.field[row - 1][i] = '*'

                i = col
                while self.field[row][i] == 'x':
                    if self.field[row + 1][i] != 'x':
                        self.field[row + 1][i] = '*'
                    if self.field[row - 1][i] != 'x':
                        self.field[row - 1][i] = '*'
                    i += 1
                if self.field[row + 1][i] != 'x':
                    self.field[row + 1][i] = '*'
                if self.field[row][i] != 'x':
                    self.field[row][i] = '*'
                if self.field[row - 1][i] != 'x':
                    self.field[row - 1][i] = '*'

                i = row
                while self.field[i][col] == 'x' and i:
                    if self.field[i][col + 1] != 'x':
                        self.field[i][col + 1] = '*'
                    if self.field[i][col - 1] != 'x':
                        self.field[i][col - 1] = '*'
                    i -= 1
                if self.field[i][col - 1] != 'x':
                    self.field[i][col - 1] = '*'
                if self.field[i][col] != 'x':
                    self.field[i][col] = '*'
                if self.field[i][col + 1] != 'x':
                    self.field[i][col + 1] = '*'

                i = row
                while self.field[i][col] == 'x' and i < 9:
                    if self.field[i][col + 1] != 'x':
                        self.field[i][col + 1] = '*'
                    if self.field[i][col - 1] != 'x':
                        self.field[i][col - 1] = '*'
                    i += 1
                if self.field[i][col - 1] != 'x':
                    self.field[i][col - 1] = '*'
                if self.field[i][col] != 'x':
                    self.field[i][col] = '*'
                if self.field[i][col + 1] != 'x':
                    self.field[i][col + 1] = '*'

    def cell(self, row, col):
        return 'x' if self.field[row][col] == 'sink' else self.field[row][col]
