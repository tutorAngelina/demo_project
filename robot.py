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

# Movement step size
step = 10

# Move the particle
def move_particle(event):
    global x, y

    if event.keysym == "Up":
        if y - radius - step >= 0:
            y -= step
    elif event.keysym == "Down":
        if y + radius + step <= canvas_size:
            y += step
    elif event.keysym == "Left":
        if x - radius - step >= 0:
            x -= step
    elif event.keysym == "Right":
        if x + radius + step <= canvas_size:
            x += step

    # Redraw the particle
    canvas.coords(particle, x - radius, y - radius, x + radius, y + radius)

# Bind arrow keys
window.bind("<Up>", move_particle)
window.bind("<Down>", move_particle)
window.bind("<Left>", move_particle)
window.bind("<Right>", move_particle)

# Start the GUI loop
window.mainloop()
