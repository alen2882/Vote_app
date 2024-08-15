from vote_model import VoteModel
from vote_view import VoteView
import tkinter as tk

class VoteController:
    def __init__(self, root: tk.Tk) -> None:
        self.model = VoteModel()
        self.view = VoteView(root, self)

    def submit_vote(self, voter_id: str, candidate: str) -> None:
        """Handle the vote submission logic."""
        try:
            self.model.record_vote(voter_id, candidate)
            self.view.update_message("Your vote has been recorded!", "green")
            self.view.vote_counted_label.config(text="Vote Counted")
        except ValueError:
            self.view.update_message("You have already voted.", "red")

    def show_results(self) -> None:
        """Fetch and display the current vote counts."""
        john_votes, jane_votes = self.model.load_votes()
        results_message = f"John: {john_votes} votes\nJane: {jane_votes} votes"
        self.view.update_message(results_message, "black")
