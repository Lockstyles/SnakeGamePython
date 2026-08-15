from helpers import load_json

SCORES_FILE = "data/scores.json"

def get_leaderboard(limit=5):
    scores = load_json(SCORES_FILE, {})
    ranked = sorted(scores.items(), key=lambda x: x[1]["high_score"], reverse=True)
    return ranked[:limit]

def display_leaderboard():
    board = get_leaderboard()
    print("--- Leaderboard ---")
    for rank, (name, data) in enumerate(board, start=1):
        print(f"{rank}. {name} - {data['high_score']}")