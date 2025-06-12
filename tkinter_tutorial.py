import tkinter as tk

# Constants
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
GRID_SIZE = 20  # size of each grid cell

# Set up window and canvas
window = tk.Tk()
window.title("Robot Movement Grid")

canvas = tk.Canvas(window, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
canvas.pack()

# Draw grid
for x in range(0, CANVAS_WIDTH, GRID_SIZE):
    canvas.create_line(x, 0, x, CANVAS_HEIGHT, fill="lightgray")

for y in range(0, CANVAS_HEIGHT, GRID_SIZE):
    canvas.create_line(0, y, CANVAS_WIDTH, y, fill="lightgray")

# oval = canvas.create_oval(100, 100, 100, 100, fill="blue")

window.mainloop()