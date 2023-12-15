def calculate_hash_step(symbol, code_val):
    hash_val = ord(symbol)
    code_val += hash_val
    code_val *= 17
    code_val = code_val % 256
    return code_val


def convert_word_to_hash(word):
    val = 0
    for i in word:
        val = calculate_hash_step(i, val)    
    return val


def test_calculate_hash_step():
    val = convert_word_to_hash('HASH')
    assert val == 52


def parse_input(data):
    data = data.replace('\n', '')
    data = data.split(',')
    return data


def process_lens_into_boxes(lens_list):
    boxes = {i: [] for i in range(256)}
    for i in lens_list:
        # print(i)
        item = i.replace('-', '=').split('=')
        box = convert_word_to_hash(item[0])
        if item[1] != '':
            item[1] = int(item[1])
            if item[0] in [i[0] for i in boxes[box]]:
                idx = [idx for idx, i in enumerate(boxes[box]) if i[0]==item[0]].pop()
                boxes[box][idx][1] = item[1]
            else:
                boxes[box].append(item)
        elif item[1] == '' and item[0] in [i[0] for i in boxes[box]]:
            # Remove it from the box
            idx = [idx for idx, i in enumerate(boxes[box]) if i[0]==item[0]].pop()
            boxes[box].pop(idx)
    # print('\n'.join([f"{k} => {' '.join([f'[{i[0]} {i[1]}]' for i in v])}" for k, v in boxes.items() if len(v) > 0]))
    return boxes


def calculate_output(box_list):
    focusing_power = 0
    for k, v in box_list.items():
        if v:
            focusing_power += sum([(k+1) * (idx+1) * (item[1]) for idx, item in enumerate(v)])
    return focusing_power


if __name__ == "__main__":

    test_initalisation = 'rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'

    td = parse_input(test_initalisation)

    with open("input.txt", "r") as f:
        data = f.read()

    data = parse_input(data)

    test_pt1 = sum(convert_word_to_hash(i) for i in td)
    assert test_pt1 == 1320

    pt1 = sum(convert_word_to_hash(i) for i in data)
    assert pt1 == 511416

    test = process_lens_into_boxes(td)
    assert calculate_output(test) == 145

    pt2 = process_lens_into_boxes(data)
    assert calculate_output(pt2) == 290779
    print(calculate_output(pt2))
