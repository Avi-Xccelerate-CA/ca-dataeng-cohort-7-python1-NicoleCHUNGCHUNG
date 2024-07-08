# week 0 problem 1
# create a function that returns a list of (vitamins,injections) tuples for each attribute that they need.
# Complete problem statement in README.mds


# your input type should be a list,
# output should also be a list containing tuples
# Example:
# input: [250, 0, 250, 0, 0, 0]
# expected output: [(25,0),(0,0),(25,0),(0,0),(0,0),(0,0)]
# input: [500, 1, 2, 3, 4, 5]
#expected output: "No medicine given"
# HINT: using % operator to find remainder may be helpful
def dose(needs):
    #YOUR SOLUTION STARTS HERE

    if len(needs) < 6:
        return("No medicine given")
        return
    elif sum(needs) >= 500:
        return("No medicine given")
        return
    
    result = []
    for value in needs:
        x, y = calculate_x_y(value)
        result.append((x, y))
    
    return result


def calculate_x_y(A):
    if A == 0:
        return (0, 0)
    elif A % 10 == 0:
        x = A // 10
        y = 0
    else:
        x = (A // 10) + 1
        y = 10 - (A % 10)
    return (x, y)


A = [250, 0, 250, 0, 0, 0]

print(f"input: {A}")
output = dose(A)
if output:
    print("output:", output)




    #YOUR SOLUTION ENDS HERE

