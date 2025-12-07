dial = 50
counter = 0

with open("./input.txt", "r", encoding="utf-8") as f:
    for line in f:
        direction = line[0]
        distance = int(line[1:])
        if direction == "R":
            for i in range(distance):
                if dial == 99:
                    dial = 0
                else:
                    dial = dial + 1
            if dial == 0:
                counter = counter + 1
        else:
            for i in range(distance):
                if dial == 0:
                    dial = 99
                else:
                    dial = dial - 1
            if dial == 0:
                counter = counter + 1
print(f"Result: {counter}")