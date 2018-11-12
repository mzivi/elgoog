import numpy.random as rnd


def generate_problem(size=4):
    numbers = list(range(1, size * size))
    shuffled = list(rnd.choice(numbers, (size * size - 1), False))
    shuffled.append(None)
    return [list(shuffled[size * i:size * i + size]) for i in range(size)]


if __name__ == "__main__":

    print(generate_problem(4))
