import re

def solve_password_part_two(filename):
    current_pos = 50  # Starting position
    total_clicks = 0
    
    with open(filename, 'r') as file:
        content = file.read()
        
    instructions = re.findall(r'([LR])(\d+)', content)
    
    for direction, amount_str in instructions:
        amount = int(amount_str)
        start = current_pos
        
        if direction == 'R':
            end = current_pos + amount
            clicks = (end // 100) - (start // 100)
            
        else:
            end = current_pos - amount
            clicks = ((start - 1) // 100) - ((end - 1) // 100)

        total_clicks += clicks
        current_pos = end

    return total_clicks
