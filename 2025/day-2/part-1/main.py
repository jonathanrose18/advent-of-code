
arr = []

with open("./input.txt", "r") as f:
    content = f.read().replace(",", "\n")
    for line in content.splitlines():
        values = line.split('-')
        start = values[0]
        end = values[1]
        for i in range(int(start), int(end) + 1):
            s = str(i)
            half = len(s) // 2
            left = s[:half]
            right = s[half:]
            
            if left == right:
                arr.append(i)
print(f"Result: {sum(arr)}")