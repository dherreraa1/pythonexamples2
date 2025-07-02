my_input = "aaaabbbcca"
output = []
start = 0
end = 0
while end < len(my_input):
    if my_input[start] == my_input[end]:
        end += 1
    else:
        output.append((my_input[start],end-start))
        start = end
    if end == len(my_input):
        output.append((my_input[start],end-start))
        
print(output)