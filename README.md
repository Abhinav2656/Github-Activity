# GitHub User Events Tracker  

A lightweight Python script that fetches and displays the latest GitHub events for a specified user in a visually appealing format using the [GitHub REST API](https://docs.github.com/en/rest) and the [`rich`](https://github.com/Textualize/rich) library.    

## Features  
- Fetches recent events using GitHub's API  
- Displays events in a readable format with emojis  
- Uses the `rich` library for better terminal output  

## Prerequisites  
- Python 3.x  
- `requests` and `rich` modules (install using `pip install requests rich`)  

## Usage  
```sh
python github_events.py <github_username>
```

## Event Types Supported
- Issue comments 💬
- Push events 🚀
- Issue creation 📝
- Repository stars ⭐
- Pull request actions 🔀
- Review comments 💭
- New branches, tags, or repositories 🆕
### Notes
- The script requires an internet connection to fetch data.
- It may hit GitHub's rate limit if used frequently.
- The GitHub API returns at most 30 events per request.


### Project URL:- 
- https://roadmap.sh/projects/github-user-activity
