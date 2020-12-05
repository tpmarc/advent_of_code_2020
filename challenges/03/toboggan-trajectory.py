import functools

TREE_SYMBOL = '#'


def count_trees_for(map_to_count_trees, slope):
    slope_right, slope_down = slope
    height = len(map_to_count_trees)
    width = len(map_to_count_trees[0])
    right, down, trees_counter = 0, 0, 0

    while down < height - 1:
        down += slope_down
        right = right + slope_right if right + slope_right < width else right + slope_right - width
        trees_counter = 1 + trees_counter if map_to_count_trees[down][right] is TREE_SYMBOL else trees_counter

    return trees_counter


with open('inputs.txt', 'r') as file:
    toboggan_map = [list(line.strip('\n')) for line in list(file)]
    trees_count = count_trees_for(toboggan_map, [3, 1])

    print(trees_count)

    slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    slopes_trees_counts = [count_trees_for(toboggan_map, slope) for slope in slopes]
    slopes_trees_counts_multiplied = functools.reduce(lambda a, b: a * b, slopes_trees_counts)

    print(slopes_trees_counts_multiplied)
