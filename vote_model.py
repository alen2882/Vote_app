import os
import pandas as pd

DATA_FILE = 'votes.txt'
VOTER_FILE = 'voters.txt'
VOTING_RECORD_FILE = 'voting_records.xlsx'

class VoteModel:
    def load_votes(self) -> tuple[int, int]:
        """Load votes from file, returns a tuple (john_votes, jane_votes)."""
        if not os.path.exists(DATA_FILE):
            return 0, 0
        with open(DATA_FILE, 'r') as file:
            data = file.read().split(',')
            return int(data[0]), int(data[1])

    def save_votes(self, john_votes: int, jane_votes: int) -> None:
        """Save votes to file."""
        with open(DATA_FILE, 'w') as file:
            file.write(f"{john_votes},{jane_votes}")

    def has_voted(self, voter_id: str) -> bool:
        """Check if the voter has already voted."""
        if not os.path.exists(VOTER_FILE):
            return False
        with open(VOTER_FILE, 'r') as file:
            voters = file.read().splitlines()
        return voter_id in voters

    def record_vote(self, voter_id: str, candidate: str) -> None:
        """Record the vote and save the voter ID."""
        john_votes, jane_votes = self.load_votes()
        if not self.has_voted(voter_id):
            with open(VOTER_FILE, 'a') as file:
                file.write(voter_id + '\n')
            if candidate == 'John':
                john_votes += 1
            elif candidate == 'Jane':
                jane_votes += 1
            self.save_votes(john_votes, jane_votes)
            self.save_voting_record(voter_id, candidate)
        else:
            raise ValueError("ID already used")

    def save_voting_record(self, voter_id: str, candidate: str) -> None:
        """Save the voting record to an Excel file."""
        record = {'ID': [voter_id], 'Candidate': [candidate]}
        df = pd.DataFrame(record)

        if os.path.exists(VOTING_RECORD_FILE):
            existing_df = pd.read_excel(VOTING_RECORD_FILE)
            df = pd.concat([existing_df, df], ignore_index=True)

        df.to_excel(VOTING_RECORD_FILE, index=False)
