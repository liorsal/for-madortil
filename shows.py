import tkinter as tk

# Create a Tkinter window
window = tk.Tk()
window.title("Output")
window.configure(bg='black')  # Set window background color to black

# Create a Text widget to display the output
output_text = tk.Text(window, bg='black', fg='green', wrap=tk.WORD)
output_text.pack(expand=tk.YES, fill=tk.BOTH)  # Expand Text widget to fill window

# Define a function to append text to the output Text widget with bold style
def append_output(text):
    output_text.configure(state=tk.NORMAL)  # Set Text widget to normal state to allow modification
    output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))  # Configure "bold" tag with bold font
    output_text.insert(tk.END, text, "bold")  # Append text with "bold" tag
    output_text.configure(state=tk.DISABLED)  # Set Text widget back to disabled state

# Call the append_output function to append your code's output to the Text widget
# Replace the following lines with your own code that generates output
output = "Hello, world!\n"
output += "This is an example of output in a window with black background and green letters.\n"
append_output(output)

# Start the Tkinter event loop
window.mainloop()
