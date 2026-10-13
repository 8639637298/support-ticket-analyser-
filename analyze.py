import json
from collections import Counter


def load_tickets(path: str) -> list[dict]:
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: file '{path}' not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: '{path}' is not valid JSON.")
        return []


def count_by_priority(tickets: list[dict]) -> Counter:
    return Counter(t["priority"] for t in tickets)


def top_error_code(tickets: list[dict]) -> str | None:
    if not tickets:
        return None
    return Counter(t["error_code"] for t in tickets).most_common(1)[0][0]


if __name__ == "__main__":
    tickets = load_tickets("tickets.json")
    print("Tickets per priority:", dict(count_by_priority(tickets)))
    print("Most common error code:", top_error_code(tickets))
