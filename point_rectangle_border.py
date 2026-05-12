x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x = float(input())
y = float(input())

left_right_side = (x == x1 or x == x2) and (y1 <= y <= y2)
top_bottom_side = (y == y1 or y == y2) and (x1 <= x <= x2)

if left_right_side or top_bottom_side:
    print(f"Border")
else:
    print(f"Inside / Outside")