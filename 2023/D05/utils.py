def get_location(seed, mapper):
    is_transformed = 0
    # print(f"Working on seed: {seed}")
    for line in mapper:
        if '-to-' in line:
            is_transformed = 0
            # print(f"{line}")
            continue

        if is_transformed == 1:
            continue

        if line == "":
            # if is_transformed == 0:
            #     print(f"Seed {orig_seed}: Going from {seed} ==> {seed} (No change)")
            continue

        destination, source, num = list(map(int, line.split()))

        # print(f"Seed {orig_seed}: Going from {seed} ==> {destination + (seed - source)}")
        # print(f"Seed: {seed} == Destination: {destination} == Source: {source} == Num: {num} == is_transformed: {is_transformed} == New Seed {destination + (seed - source)}")

        if source <= seed and source + num > seed and is_transformed == 0:
            # print(f"Seed {orig_seed}: Going from {seed} ==> {destination + (seed - source)}")
            seed = destination + (seed - source)
            is_transformed = 1
    
    return seed
