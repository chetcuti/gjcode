import random as random_ext

def random(options, rolls):
    """Run the main program"""
    sorted_results = sort_results(get_results(options, rolls))
    print_headers(options, rolls)
    print_results(rolls, sorted_results)

def get_results(options, rolls):
    """Get the results"""
    count = 0
    results = {}
    while count < rolls:
        selection = random_ext.randint(1, options)
        if selection in results:
            results[selection] += 1
        else:
            results[selection] = 1
        count += 1
    return results

def sort_results(unsorted_results):
    """Sort the results"""
    return sorted(unsorted_results.items(), key=lambda x: x[1], reverse=True)

def print_headers(options, rolls):
    """Print the headers"""
    print()
    print("Options:", f"{options:,}")
    print("Rolls:", f"{rolls:,}")

    print()

def print_results(rolls, results):
    """Print the results"""
    row_count = 0
    for each in results:
        percent = f"{each[1] * 100 / rolls:.2f}"
        row = "#" + str(each[0]) + " - " + f"{each[1]:,}" + " (" + percent + "%)"
        print(row + " -- WINNER!") if row_count == 0 else print(row)
        row_count += 1
