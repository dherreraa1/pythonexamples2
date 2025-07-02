import time

def my_timer(func):
    def wrapper(*args):
        start = time.time()
        res = func(*args)
        end = time.time()
        print("Elapsed time:",end-start)
        return res

    return wrapper

@my_timer
def max_tank(vec):
	max_area = 0
	for i in range(len(vec)-1):
		for j in range(i+1,len(vec)):
			area = (j-i)*min(vec[i], vec[j])
			if area > max_area:
				max_area = area
	return max_area

@my_timer
def max_tank_opt(vec):
    left, right = 0, len(vec)-1
    max_area = 0
    while left < right:
        area  = (right-left)*min(vec[left], vec[right])
        max_area = max(area, max_area)
        
        if vec[left] > vec[right]:
            right -= 1  
        else:
            left += 1 
    
    return max_area
	
vec = [1,8,6,2,5,4,8,3,7]
#vec = [3,2,4,1]
print(max_tank(vec))
print(max_tank_opt(vec))