# File: pyprog.py
data = [ #A list of tuples
    (10, 5, 5, 5, "menu"),
    (0, 0, 200, 20, "titlebar"),
    (50, 30, 15, 5, "end button")
]

def main():
    tx = 60  # test-x
    ty = 32  # test-y
    for x, y, w, h, descr in data:
        #die Reihenfolge der Variablen in der Schleife bildet die Reihenfolge des  Tubel ab.
        dx = tx - x
        dy = ty - y
        if dx < 0 or dx >= w:
            continue
        elif dy < 0 or dy >= h:
            continue
        print(f"test point ({tx},{ty}) inside rect '{descr}'")

if __name__ == "__main__":
    main()