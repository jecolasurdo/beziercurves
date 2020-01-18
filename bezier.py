points = [
    [4, 10],
    [0, 180],
    [90, 0],
    [180, 120],
    [270, 60]
]

n = 10

def main(points, n):
    for a in return_alpha_values(n):
        print(a)


def return_alpha_values(n):
    delta = 1 / n
    alpha = 0 
    for _ in range(n):
        alpha = alpha + delta
        yield alpha

if __name__ == "__main__":
    main(points, n)