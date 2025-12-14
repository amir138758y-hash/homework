import random
boys = ["boy 1","boy 2","boy 3","boy 4","boy 5","boy 6","boy 7","boy 8","boy 9","boy 10"]
girls = ["girl 1","girl 2","girl 3","girl 4","girl 5","girl 6","girl 7","girl 8","girl 9","girl 10"]

random.shuffle(girls)
pairs = list(zip(boys,girls))

for boys,girls in pairs :
    print(f"{boys} {girls}")