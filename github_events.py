import sys
import requests
from rich import print as rich_print


def get_latest_events(username):
    url = f"https://api.github.com/users/{username}/events"
    response = requests.get(url, timeout=10)

    if response.status_code == 200:
        events = response.json()
        rich_print(f"\nLatest events for [bold green]{username}[/bold green]:")

        if not events:
            rich_print("[yellow]No recent events found.[/yellow]")
            return

        for event in events:
            event_type = event["type"]
            repo_name = event["repo"]["name"]

            if event_type == "IssueCommentEvent":
                rich_print(f"- 💬 Commented on issue #{event['payload']['issue']['number']} in {repo_name}")

            elif event_type == "PushEvent":
                rich_print(f"- 🚀 Pushed to {repo_name}")

            elif event_type == "IssuesEvent":
                rich_print(f"- 📝 Created issue #{event['payload']['issue']['number']} in {repo_name}")

            elif event_type == "WatchEvent":
                rich_print(f"- ⭐ Starred {repo_name}")

            elif event_type == "PullRequestEvent":
                rich_print(f"- 🔀 Created pull request #{event['payload']['pull_request']['number']} in {repo_name}")

            elif event_type == "PullRequestReviewEvent":
                rich_print(f"- 👀 Reviewed pull request #{event['payload']['pull_request']['number']} in {repo_name}")

            elif event_type == "PullRequestReviewCommentEvent":
                rich_print(f"- 💭 Commented on a pull request in {repo_name}")

            elif event_type == "CreateEvent":
                ref_type = event["payload"]["ref_type"]
                ref = event["payload"].get("ref", "repository")
                rich_print(f"- 🆕 Created {ref_type} {ref} in {repo_name}")

            else:
                rich_print(f"- 🔔 {event_type} in {repo_name}")

    else:
        rich_print(f"[red]Error fetching events for {username}: {response.status_code}[/red]")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        get_latest_events(sys.argv[1])
    else:
        print("Please provide a GitHub username as a command-line argument.")
