points = [
    [0, 180],
    [90, 0],
    [180, 120],
    [270, 60]
]

n = 10

def main(points, n):
    # for a in return_alpha_values(n):
    #     print(a)
    alpha = .33
    new_points = find_new_segments(points, alpha)
    while len(new_points) > 1:
        new_points = find_new_segments(new_points, alpha)
    print(new_points)

def find_new_segments(points, alpha):
    alpha = 0.33
    i = 0 
    new_points = []
    while i < len(points) - 1:
       i += 1
       point_a = points[i - 1]
       point_b = points[i]
       new_points.append(find_intermediate_point(point_a, point_b, alpha))
    return new_points


def find_intermediate_point(point_a, point_b, alpha):
   x = ((point_b[0] - point_a[0]) * alpha) + point_a[0]
   y = ((point_b[1] - point_a[1]) * alpha) + point_a[1]
   return [x,y]

def return_alpha_values(n):
    delta = 1 / n
    alpha = 0 
    for _ in range(n):
        alpha = alpha + delta
        yield alpha

if __name__ == "__main__":
    main(points, n)