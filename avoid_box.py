# Helpful documentation: https://www.geeksforgeeks.org/python-tkinter-tutorial/
import tkinter as tk

# Set up window and canvas
window = tk.Tk()
window.title("Move the Particle")

canvas_size = 400
canvas = tk.Canvas(window, width=canvas_size, height=canvas_size, bg="white")
canvas.pack()

# Create a circle (particle) in the center
radius = 10
x = canvas_size // 2
y = canvas_size // 2
particle = canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill="red")

# Create a box somewhere
box_radius = 20
a = canvas_size // 4
b = canvas_size // 4
box = canvas.create_rectangle(a-box_radius, b-box_radius, a + box_radius, b + radius, fill="blue")

# Movement step size
step = 10

# Move the particle
def move_particle(event):
    global x, y

    # Predict next position
    new_x, new_y = x, y
    if event.keysym == "Up":
        if y - radius - step >= 0:
            new_y -= step
    elif event.keysym == "Down":
        if y + radius + step <= canvas_size:
            new_y += step
    elif event.keysym == "Left":
        if x - radius - step >= 0:
            new_x -= step
    elif event.keysym == "Right":
        if x + radius + step <= canvas_size:
            new_x += step

    # Get box coordinates
    box_coords = canvas.coords(box)
    box_left = box_coords[0]
    box_top = box_coords[1]
    box_right = box_coords[2]
    box_bottom = box_coords[3]

    # Check for collision with the box
    future_left = new_x - radius
    future_top = new_y - radius
    future_right = new_x + radius
    future_bottom = new_y + radius

    overlaps_box = not (
        future_right < box_left or
        future_left > box_right or
        future_bottom < box_top or
        future_top > box_bottom
    )

    if not overlaps_box:
        x, y = new_x, new_y
        canvas.coords(particle, x - radius, y - radius, x + radius, y + radius)


# Bind arrow keys
window.bind("<Up>", move_particle)
window.bind("<Down>", move_particle)
window.bind("<Left>", move_particle)
window.bind("<Right>", move_particle)

# Start the GUI loop
window.mainloop()