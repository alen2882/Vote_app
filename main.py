import tkinter as tk
from vote_controller import VoteController

def main() -> None:
    """Main function to initialize the application."""
    root = tk.Tk()
    app = VoteController(root)
    root.mainloop()

if __name__ == "__main__":
    main()
