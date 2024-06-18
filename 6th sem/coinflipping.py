import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Button

# Initial setup
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.2)  # Adjust subplot to make room for the stop button
N_values = range(1, 1001)  # Change N from 1 to 10000 for demonstration
bars = ax.bar(['H', 'T'], [0, 0])  # Initial bar heights are 0

# Define the update function for the animation
def update(N):
    # Generate coin flips for the current N
    coins = np.random.choice(["H", "T"], N)
    unique_values, counts = np.unique(coins, return_counts=True)
    # Update bar heights
    for bar, value in zip(bars, counts):
        bar.set_height(value)
    ax.set_title(f"Total Flips: {N}")
    # Adjust y-axis limits dynamically
    ax.set_ylim(0, max(counts) + 30)  # Add some padding above the tallest bar

# Create animation
ani = FuncAnimation(fig, update, frames=N_values, repeat=False, interval=100)

# Adjust subplot to make room for buttons
plt.subplots_adjust(bottom=0.2)

# Create animation
ani = FuncAnimation(fig, update, frames=N_values, repeat=False, interval=100)

# Define a flag to track the animation state
is_anim_running = True

# Define a function to toggle the animation state
def toggle_animation(event):
    global is_anim_running
    if is_anim_running:
        ani.event_source.stop()
        toggle_button.label.set_text('Start')
    else:
        ani.event_source.start()
        toggle_button.label.set_text('Stop')
    is_anim_running = not is_anim_running

# Create a toggle button axis and button
toggle_button_ax = fig.add_axes([0.7, 0.05, 0.1, 0.075])  # Adjust the position and size as needed
toggle_button = Button(toggle_button_ax, 'Stop', color='lightblue', hovercolor='0.975')
toggle_button.on_clicked(toggle_animation)

plt.show()