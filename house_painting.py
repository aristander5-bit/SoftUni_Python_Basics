height_x_house = float(input())
length_y_side_wall = float(input())
height_h_triangular_wall_roof = float(input())

front_wall = 2 * (height_x_house * height_x_house)
side_wall = 2 * (height_x_house * length_y_side_wall)
windows = 2 * (1.5 * 1.5)
door = 1.2 * 2

total_green_paint = (front_wall - door) + (side_wall - windows)
green_liters = total_green_paint / 3.4

roof_wall = 2 * (height_x_house * length_y_side_wall)
roof_triangular = 2 * ((height_x_house * height_h_triangular_wall_roof) / 2)

total_red_paint = roof_wall + roof_triangular
red_liters = total_red_paint / 4.3

print(f"{green_liters:.2f}")
print(f"{red_liters:.2f}")
