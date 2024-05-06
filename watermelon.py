def can_divide_watermelon(w):
    # Check if the weight is at least 2
    if w < 2:
        return "NO"

    # Check if the weight is even and greater than 2
    if w % 2 == 0 and w > 2:
        return "YES"
    else:
        return "NO"


# Read input
w = int(input().strip())

# Check if the watermelon can be divided as required
result = can_divide_watermelon(w)
print(result)
