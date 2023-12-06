from threading import Thread
import concurrent.futures
from multiprocessing import Pool
import time
from functools import partial

from utils import get_location

from numpy import arange


def process_data(results, seeds):
    seed_locations = []
    gf = partial(get_location, mapper=results[2:])
    with Pool(processes=10) as pool:
        seed_locations = list(pool.imap_unordered(gf, seeds))

    return seed_locations


if __name__ == '__main__':
    # Part 1
    with open("input.txt", "r") as f:
        data = f.read()

    results = data.split('\n')
    seeds = list(map(int, results[0].split()[1:]))
    gf = partial(get_location, mapper=results[2:])

    # # start 4 worker processes
    with Pool(processes=10) as pool:
        part_1 = pool.map(gf, seeds)

    # Part 2
    _tmp = []
    for idx, (seed, num) in enumerate(zip(seeds[::2], seeds[1::2])):
            # # start 4 worker processes
        # print("Working on pt 2")
        start = time.time()
        with Pool(processes=18) as pool:
            result = pool.map(gf, arange(seed, seed+num))
                
            _tmp.append(min(result))

        end = time.time()
        print(f'{idx} => Time taken (s): {end - start:.4f}')
    
    print(min(part_1))
    print(_tmp)
    print(min(_tmp))




#     final_seed = seed + num
    
#     seed_pt = seed
#     print(f"Processing number: {idx}")
#     while seed_pt < final_seed:
#         final_seed = seed_pt+inc if final_seed < seed + num else final_seed
#         print("Pre")
#         seed_list = arange(seed_pt, final_seed)
#         print("During")
#         part_2.append(min(process_data(results, seed_list)))
#         print("Post")
#         seed_pt += inc

# print(min(part_2))



# test_seed_ranges = [79, 14, 55, 13]
# test_seeds = [i for j in zip(test_seed_ranges[::2], test_seed_ranges[1::2]) for i in range(j[0], sum(j))]
# test_outcome = process_data(test_results, test_seeds)
# assert min(test_outcome) == 46

# seeds = list(map(int, results[0].split()[1:]))
# # seed_list = [i for j in zip(seeds[::2], seeds[1::2]) for i in range(j[0], sum(j))]

# part_2 = []
# inc = 1000