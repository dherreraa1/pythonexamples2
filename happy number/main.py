def happy_number(number: int) -> bool:
    seen = set()
    cur = str(number)
    
    while cur not in seen:
        seen.add(cur)
        summ = 0
        for digit in cur:
            digit = int(digit)
            summ += digit**2
            
        if summ == 1: 
            return True
        cur = str(summ)
        
    return False
    
print(happy_number(19))