from copy import deepcopy


class Monkey:
    def __init__(
        self, items: list[int], op: str, test: int, test_true: int, test_false: int
    ):
        self.items = items
        self.operation = self.parse_op(op)
        self.test_divisible_by = test
        self.test_true_throw_to = test_true
        self.test_false_throw_to = test_false
        self.inspection_count = 0

    def parse_op(self, op: str):
        def operation(old: int) -> int:
            self.inspection_count += 1
            new_val = int(eval(op))
            return new_val

        return operation

    def __repr__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


class Game:
    def __init__(self):
        self.monkeys = []

    def run_game(self):
        self.parse_monkey_notes()
        self.play()

    def parse_monkey_notes(self):

        file = open("day_11/input.txt", "r")
        line = file.readline().strip()
        monkey_index = 0

        while line != "":
            split_line = line.strip().split(" ")
            if split_line[0] == "Monkey":
                split_line = file.readline().strip().split(" ")  # get starting items
                starting_items = []
                for i in range(2, len(split_line)):
                    starting_items.append(int(split_line[i].replace(",", "")))
                line = file.readline().strip()  # get operation
                operation = line[line.index("=") + 1 : len(line)].strip()
                split_line = file.readline().strip().split(" ")  # get test
                test = int(split_line[len(split_line) - 1])
                split_line = file.readline().strip().split(" ")  # get true
                if_true = int(split_line[len(split_line) - 1])
                split_line = file.readline().strip().split(" ")  # get false
                if_false = int(split_line[len(split_line) - 1])

                self.monkeys.append(
                    Monkey(starting_items, operation, test, if_true, if_false)
                )
                monkey_index += 1
                line = file.readline()
                line = file.readline()

        file.close()

    def play(self):
        for round in range(20):
            for monkey in self.monkeys:
                items = deepcopy(monkey.items)
                for item in items:
                    monkey.items.remove(item)
                    new_val = int(monkey.operation(item) / 3)
                    if int(new_val % monkey.test_divisible_by) == 0:
                        self.monkeys[monkey.test_true_throw_to].items.append(new_val)
                    else:
                        self.monkeys[monkey.test_false_throw_to].items.append(new_val)

        self.calc_score()

    def calc_score(self) -> None:
        top_score = 0
        second_score = 0

        for monkey_index in range(len(self.monkeys)):
            if self.monkeys[monkey_index].inspection_count > top_score:
                second_score = top_score
                top_score = self.monkeys[monkey_index].inspection_count
            elif self.monkeys[monkey_index].inspection_count > second_score:
                second_score = self.monkeys[monkey_index].inspection_count
        print(top_score * second_score)


game = Game()
game.run_game()
