import numpy as np
import random
import matplotlib.pyplot as plt
from timeit import default_timer as timer


def random_list_timer(number_numbers):
    '''
    Measures time of creating random lists orr arrays.
    For a more accurate calculation, the measurement is repeated 10 rows.
    '''
    end_random_generate, end_random_prelist, end_np = 0, 0, 0
    iters = 10

    for _ in range(iters):
        start_random = timer()
        [random.random() for _ in range(number_numbers)]
        end_random_generate += timer() - start_random

        start_random = timer()
        pre_list = [0] * number_numbers
        for i in range(number_numbers):
            pre_list[i] = random.random()
        end_random_prelist += timer() - start_random

        start_np = timer()
        np.random.uniform(0, 1, number_numbers)
        end_np += timer() - start_np

    return end_random_generate / iters, end_random_prelist / iters, end_np / iters


def random_timer_range(number_numbers):
    '''
    Measures time of creating random numbers in "range" loop.
    For a more accurate calculation, the measurement is repeated 10 rows.
    '''
    end_random_generate, end_np = 0, 0
    iters = 10

    for _ in range(iters):
        start_random = timer()
        for _ in range(number_numbers):
            random.random()
        end_random_generate += timer() - start_random

        start_np = timer()
        for _ in range(number_numbers):
            np.random.uniform(0, 1)
        end_np += timer() - start_np

    return end_random_generate / iters, end_np / iters


def generate_plot_list():
    '''
    Measures time of generete random list via Random (uses pre-created list and without it) and
    random array via Numpy.
    Also measures time of generete random numbers via Random and via Numpy in 'range' loop.
    Generates plot.
    '''
    timer_random_generate, timer_random_prelist, timer_np = [], [], []
    timer_random_loop, timer_np_loop = [], []
    number_n = [int(i) for i in np.logspace(0, 8, num=8-0, endpoint=False)]

    for n in number_n:
        end_random_generate, end_random_prelist, end_np = random_list_timer(n)
        end_range_random, end_range_np = random_timer_range(n)
        timer_random_generate.append(end_random_generate)
        timer_random_prelist.append(end_random_prelist)
        timer_np.append(end_np)
        timer_random_loop.append(end_range_random)
        timer_np_loop.append(end_range_np)

    fig = plt.figure()
    ax = fig.add_subplot()
    ax.plot(number_n, timer_random_generate, label='Generate via Random', color='blue')
    ax.plot(number_n, timer_random_prelist, label='Generate via Random to exist list', color='red')
    ax.plot(number_n, timer_np, label='Generate via Numpy in array', color='green')
    ax.plot(number_n, timer_random_loop, label='Generate via Random in Range loop', color='orange')
    ax.plot(number_n, timer_np_loop, label='Generate via Numpy in Range loop', color='black')
    plt.title('Measuring time of creating random numbers')
    plt.xlabel('Number of numbers, log')
    plt.ylabel('Measured time [s], log')
    plt.tight_layout()
    ax.legend()
    ax.set_yscale('log')
    ax.set_xscale('log')
    plt.gcf().set_size_inches(8, 6)
    plt.savefig('python_homework/random_practice/Plots/random_numbers.png', dpi=100, bbox_inches='tight')
    plt.close()


def is_sorted(list_sort):
    '''
    Check if List is sorted - return True, if not - return False.
    '''
    for i in range(len(list_sort) - 1):
        if list_sort[i] <= list_sort[i+1]:
            continue
        else:
            return False
    return True


def monkey_sort(list_sort):
    '''
    Sort list by shaffling (Monkey sort).
    '''
    while is_sorted(list_sort) is False:
        random.shuffle(list_sort)

    return list_sort


def measure_sort(list_sort):
    '''
    Measured the time needed for Monkey sorting of input list.
    For a more accurate calculation, the measurement is repeated 5 rows.
    '''
    end_sort = 0
    iters = 5

    for _ in range(iters):
        start_sort = timer()
        monkey_sort(list_sort)
        end_sort += timer() - start_sort

    return end_sort / iters


def shuff_sort_plot():
    '''
    Create a list for measuring time needed for Monkey sort, plot the results.
    '''
    number_n = [i for i in range(1, 15, 5)]
    timer_sort = []

    for n in number_n:
        list_sort = [random.randrange(1, 50, 1) for i in range(n)]
        timer_sort.append(measure_sort(list_sort))

    fig = plt.figure()
    ax = fig.add_subplot()
    ax.plot(number_n, timer_sort, color='blue')
    plt.title('Measuring time of Monkey sort of List')
    plt.xlabel('List Lenght')
    plt.ylabel('Measured time [s], log')
    ax.set_yscale('log')
    plt.gcf().set_size_inches(8, 6)
    plt.savefig('python_homework/random_practice/Plots/Monkey.png', dpi=100, bbox_inches='tight')
    plt.close()


def create_walk(steps):
    '''
    Create a x and y positions for random walk.
    '''
    x_steps = np.random.rand(steps) - 0.5
    y_steps = np.random.rand(steps) - 0.5

    x_position = np.cumsum(x_steps)
    y_position = np.cumsum(y_steps)

    x_position[0] = 0
    y_position[0] = 0

    return x_position, y_position


def random_walk_visualizaton():
    '''
    Create a plot with Random Walk visualisation.
    '''
    steps = 1000
    x_position, y_position = create_walk(steps)
    plt.scatter(x_position, y_position, cmap=plt.cm.Blues, c=y_position, edgecolors='none', s=50)
    plt.plot(x_position, y_position, alpha=0.3)
    plt.scatter(0, 0, c='red', edgecolors='none')
    plt.scatter(x_position[-1], y_position[-1], c='green', edgecolors='none')
    plt.title('Random walk Visualisation')
    plt.gcf().set_size_inches(8, 6)
    plt.savefig('python_homework/random_practice/Plots/random_walk.png', dpi=100, bbox_inches='tight')
    plt.close()


def create_sierpinski():
    '''
    Generate and plot Sierpiński triangle.
    '''
    vertices = [(0.0, 0.0), (0.5, 1.0), (1.0, 0.0)]
    points = []

    x, y = random.choice(vertices)

    for i in range(1000000):
        vx, vy = random.choice(vertices)
        x = (vx + x) / 2.0
        y = (vy + y) / 2.0
        points.append((x, y))

    x = [x for (x, y) in points]
    y = [y for (x, y) in points]

    plt.figure(figsize=(10,10))
    plt.plot(x, y, 'b.', markersize=0.05)
    plt.title('Sierpiński Triangle')
    plt.savefig('python_homework/random_practice/Plots/Sierpiński.png', dpi=100, bbox_inches='tight')
    plt.close()


def shuffle_text(input_text):
    '''
    Shuffle words in text. Shuffle from second to penultimate letter (like "word[1:-1]".
    '''
    input_text = input_text.split(' ')

    for i, word in enumerate(input_text):
        if len(word) > 2 and len(word[1:-1]) > 1:
            if word[-1] != '.' and word[-1] != ',':
                inside_letters = word[1:-1]
                inside_letters = ''.join(random.sample(inside_letters, len(inside_letters)))
                input_text[i] = word[0] + inside_letters + word[-1]
            else:
                inside_letters = word[1:-2]
                inside_letters = ''.join(random.sample(inside_letters, len(inside_letters)))
                input_text[i] = word[0] + inside_letters + word[-2:]

    return ' '.join(input_text)


def main():
    generate_plot_list()
    shuff_sort_plot()
    random_walk_visualizaton()
    create_sierpinski()
    input_text = 'This tool helps you create text for all your layout needs.'
    shuffle_text(input_text)


if __name__ == '__main__':
    main()
