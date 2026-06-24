import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import csv

def get_user_input():
    while True:
        try:
            print("\n--- Damped Oscillation Settings ---")
            amp = float(input("Enter initial amplitude (e.g., 5.0): "))
            decay = float(input("Enter decay coefficient (e.g., 0.5): "))
            
            if amp <= 0 or decay < 0:
                print("Error: Amplitude must be > 0 and decay must be >= 0. Try again.")
                continue
            return amp, decay
        except ValueError:
            print("Exception error: Invalid input. Please enter numbers using a dot for decimals.")

def generate_data(amplitude, decay):
    try:
        t = np.linspace(0, 10, 200)
        y = amplitude * np.exp(-decay * t) * np.cos(2 * np.pi * t)
        return t, y
    except Exception as e:
        print(f"Error during data computation: {e}")
        return None, None

def save_data_to_csv(filename, t, y):
    try:
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Time (s)", "Amplitude"])
            for i in range(len(t)):
                writer.writerow([round(t[i], 3), round(y[i], 3)])
        print(f"[*] Data successfully saved to file: {filename}")
    except IOError:
        print(f"Exception error: Cannot access {filename}. The file might be open in another program.")
    except Exception as e:
        print(f"Unexpected error while saving data: {e}")

def create_animation(t, y):
    try:
        print("[*] Creating animation... Please wait.")
        fig, ax = plt.subplots()
        
        ax.set_xlim(0, 10)
        ax.set_ylim(-max(abs(y))-1, max(abs(y))+1)
        ax.set_title("Damped Oscillation Animation")
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Amplitude")
        ax.grid(True)

        line, = ax.plot([], [], lw=2, color='red')

        def init():
            line.set_data([], [])
            return line,

        def animate(i):
            line.set_data(t[:i], y[:i])
            return line,

        ani = animation.FuncAnimation(
            fig, animate, init_func=init, frames=len(t), interval=20, blit=True
        )

        writer = animation.PillowWriter(fps=30)
        gif_filename = "damped_oscillation.gif"
        ani.save(gif_filename, writer=writer)
        print(f"[*] Animation successfully saved to file: '{gif_filename}'")
        
        print("[*] Launching interactive window. Close the plot window to exit.")
        plt.show() 

    except Exception as e:
        print(f"Error during animation creation or saving: {e}")

def main():
    print("="*50)
    print("Mathematical Function Visualization Program")
    print("="*50)
    
    amp, decay = get_user_input()
    t, y = generate_data(amp, decay)
    
    if t is not None and y is not None:
        save_data_to_csv("oscillation_data.csv", t, y)
        create_animation(t, y)
    else:
        print("Program execution stopped due to calculation errors.")

if __name__ == "__main__":
    main()