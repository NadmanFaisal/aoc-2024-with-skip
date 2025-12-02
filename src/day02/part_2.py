first_ids = []
last_ids = []

with open('puzzle_pieces/sequence.txt','r') as file:
    content = file.read().strip()

ranges = content.split(',')

for range_string in ranges:
    start, end = range_string.split('-')
    
    first_ids.append(int(start))
    last_ids.append(int(end))


def is_invalid(ID: int) -> bool:
    s = str(ID)
    length = len(s)
    for pattern_len in range(1, (length // 2) + 1):
        if length % pattern_len == 0:
            pattern = s[:pattern_len]
            multiplier = length // pattern_len
            
            if pattern * multiplier == s:
                return True

    return False


total_id = 0
for i in range(0, len(first_ids)):
    from_num = first_ids[i]
    to_num = last_ids[i]

    for num in range(from_num, to_num + 1):
        if is_invalid(num):
            total_id += num

print("Total id: ", total_id)
