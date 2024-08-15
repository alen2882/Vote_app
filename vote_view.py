import tkinter as tk

class VoteView:
    def __init__(self, master: tk.Tk, controller: 'VoteController') -> None:
        self.master = master
        self.controller = controller

        master.title('Voting Application')
        master.geometry('400x300')  # Set window size

        # Create UI components
        self.voter_id_label = tk.Label(master, text="Voter ID (4 digits):")
        self.voter_id_label.pack(pady=5)
        self.voter_id_entry = tk.Entry(master)
        self.voter_id_entry.pack(pady=5)

        self.candidate_label = tk.Label(master, text="Select Candidate:")
        self.candidate_label.pack(pady=5)
        self.candidate_var = tk.StringVar()
        self.candidate_var.set("John")  # Default value

        self.radio_john = tk.Radiobutton(master, text="John", variable=self.candidate_var, value="John")
        self.radio_john.pack(pady=5)
        self.radio_jane = tk.Radiobutton(master, text="Jane", variable=self.candidate_var, value="Jane")
        self.radio_jane.pack(pady=5)

        self.submit_button = tk.Button(master, text="Submit Vote", command=self.submit_vote)
        self.submit_button.pack(pady=10)

        self.view_results_button = tk.Button(master, text="View Results", command=self.view_results)
        self.view_results_button.pack(pady=10)

        self.message_label = tk.Label(master, text="")
        self.message_label.pack(pady=10)

        self.vote_counted_label = tk.Label(master, text="")
        self.vote_counted_label.pack(pady=10)

    def submit_vote(self) -> None:
        """Validate and submit the vote."""
        voter_id = self.voter_id_entry.get()
        candidate = self.candidate_var.get()
        if len(voter_id) == 4 and voter_id.isdigit():
            self.controller.submit_vote(voter_id, candidate)
        else:
            self.update_message("Voter ID must be exactly 4 digits.", "red")

    def view_results(self) -> None:
        """Request to show current vote counts."""
        self.controller.show_results()

    def update_message(self, message: str, color: str) -> None:
        """Update the message label with the given text and color."""
        self.message_label.config(text=message, fg=color)
