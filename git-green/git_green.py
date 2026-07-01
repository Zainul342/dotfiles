#!/usr/bin/env python3
import os
import sys
import argparse
import subprocess
import datetime
import random

# Built-in database of real, helpful programming tips
TIPS = {
    "linux": [
        "Use 'setsid command' to detach a process from the controlling terminal session.",
        "Redirect stdin from /dev/null ('< /dev/null') to prevent background processes from terminating on PTY EOF.",
        "Check systemd user services logs using 'journalctl --user -u service-name.service'.",
        "Use 'pgrep -fl process-name' to find PIDs along with their full command line descriptions.",
        "Run 'pkill -9 -f process-pattern' to force kill processes matching a pattern description.",
        "Use 'rsync -avz --progress source/ destination/' for efficient file synchronization.",
        "Create an archive using 'tar -czvf archive.tar.gz directory/'.",
        "Search files efficiently using 'grep -rnI \"search_term\" directory/'.",
        "Monitor disk space usage with 'df -h' and directory sizes with 'du -sh *'.",
        "Update the Fontconfig font cache using 'fc-cache -f -v'."
    ],
    "git": [
        "Modify your last commit message using 'git commit --amend -m \"new message\"'.",
        "View a clean, single-line git history tree using 'git log --oneline --graph --all'.",
        "See staged changes before committing using 'git diff --staged'.",
        "Recover lost commits or branch states using the reference log with 'git reflog'.",
        "Force-push safely with lease validation using 'git push --force-with-lease'.",
        "Reset working tree and index to a clean state using 'git reset --hard HEAD'.",
        "Temporarily save untracked or modified files using 'git stash -u'.",
        "List all tracked configurations and their origins using 'git config --list --show-origin'.",
        "Remove untracked directories and files cleanly using 'git clean -fd'.",
        "Show who modified each line of a file using 'git blame filename'."
    ],
    "python": [
        "Use list comprehensions '[x for x in items if condition]' for concise list creation.",
        "Iterate over keys and values in a dictionary using 'for k, v in dictionary.items()'.",
        "Get index and value simultaneously in loops using 'for idx, val in enumerate(items)'.",
        "Combine multiple lists element-wise using 'zip(list1, list2)'.",
        "Read command-line arguments safely via the standard library 'sys.argv'.",
        "Safely open files using context managers: 'with open(file) as f:'.",
        "Use dictionary comprehensions '{k: v for k, v in pairs}' for clean mappings.",
        "Convert objects to JSON strings using the built-in 'json.dumps(obj)'.",
        "Measure execution times using the built-in 'timeit' profiling module.",
        "Use generator expressions '(x for x in large_range)' to save system memory."
    ]
}

COMMIT_MESSAGES = {
    "linux": [
        "docs(linux): add tip on setsid daemon execution",
        "docs(linux): add note about stdin redirection in background jobs",
        "docs(linux): document journalctl systemd logs inspection",
        "docs(linux): add cheat-sheet for pgrep and pkill utilities",
        "docs(linux): document rsync backup configurations",
        "docs(linux): add note about tar archiving compress flags"
    ],
    "git": [
        "docs(git): explain git commit --amend usage",
        "docs(git): document clean git log graph tree options",
        "docs(git): explain git diff --staged verification benefits",
        "docs(git): add instructions for git reflog data recovery",
        "docs(git): document git push --force-with-lease safety"
    ],
    "python": [
        "docs(python): add cheat-sheet for list comprehensions syntax",
        "docs(python): document dictionary items iteration patterns",
        "docs(python): explain enumerate loop indexing optimization",
        "docs(python): document zip utility for parallel iterations",
        "docs(python): add instructions for sys.argv CLI parsing"
    ]
}

def run_cmd(args, env=None):
    return subprocess.run(args, env=env, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def generate_contributions(days_back):
    repo_path = "/home/zainm/dotfiles"
    wiki_dir = os.path.join(repo_path, "wiki")
    
    # Ensure wiki directory exists
    os.makedirs(wiki_dir, exist_ok=True)
    os.chdir(repo_path)
    
    today = datetime.date.today()
    start_date = today - datetime.timedelta(days=days_back)
    
    current_env = os.environ.copy()
    total_commits = 0
    
    print(f"git-green: Generating organic contributions for the last {days_back} days...")
    
    for i in range(days_back + 1):
        target_date = start_date + datetime.timedelta(days=i)
        
        # Don't commit for future dates
        if target_date > today:
            break
            
        # Determine organic count (Workdays vs Weekends)
        is_weekend = target_date.weekday() in (5, 6)
        if is_weekend:
            # Lighter weekend commits (85% chance of 0, 15% chance of 1-2 commits)
            num_commits = random.choices([0, 1, 2], weights=[85, 10, 5])[0]
        else:
            # Normal workday commits (varying shades of green)
            num_commits = random.randint(15, 30)
            
        if num_commits == 0:
            continue
            
        print(f"Processing {target_date.strftime('%Y-%m-%d')} - generating {num_commits} commits...")
        
        for commit_idx in range(num_commits):
            # Select random topic
            topic = random.choice(["linux", "git", "python"])
            tip = random.choice(TIPS[topic])
            commit_msg = random.choice(COMMIT_MESSAGES[topic])
            
            # File path inside wiki/
            file_path = os.path.join(wiki_dir, f"{topic}.md")
            
            # Generate random timestamp
            hour = random.randint(9, 21)
            minute = random.randint(0, 59)
            second = random.randint(0, 59)
            commit_time = datetime.datetime.combine(
                target_date, 
                datetime.time(hour, minute, second)
            )
            date_str = commit_time.isoformat()
            
            # Append content to target wiki file
            with open(file_path, "a") as f:
                f.write(f"\n### Today I Learned: {topic.capitalize()}\n")
                f.write(f"> {tip}\n")
                f.write(f"*Logged at: {date_str}*\n")
                
            # Stage file
            run_cmd(["git", "add", f"wiki/{topic}.md"])
            
            # Set git backdate env variables
            env = current_env.copy()
            env["GIT_AUTHOR_DATE"] = date_str
            env["GIT_COMMITTER_DATE"] = date_str
            
            # Commit with semantic message
            run_cmd(["git", "commit", "-m", commit_msg], env=env)
            total_commits += 1
            
    print(f"git-green: Successfully created {total_commits} organic commits locally!")
    print("Pushing updates to GitHub...")
    
    res = subprocess.run(["git", "push"], capture_output=True, text=True)
    if res.returncode == 0:
        print("git-green: Push successful! Contribution graph updated.")
    else:
        print("git-green: Push failed:")
        print(res.stderr)

def install_systemd():
    service_path = "/home/zainm/.config/systemd/user/github-green.service"
    timer_path = "/home/zainm/.config/systemd/user/github-green.timer"
    
    # Ensure systemd directory exists
    os.makedirs(os.path.dirname(service_path), exist_ok=True)
    
    # Write systemd service file
    service_content = """[Unit]
Description=Run GitHub Daily Contribution Generator (git-green)
After=network-online.target

[Service]
Type=oneshot
ExecStart=/usr/bin/python3 /home/zainm/dotfiles/git-green/git_green.py generate --days 0
WorkingDirectory=/home/zainm/dotfiles
StandardOutput=journal
StandardError=journal
"""
    
    # Write systemd timer file
    timer_content = """[Unit]
Description=Run GitHub Daily Contribution Generator Timer (git-green)

[Timer]
OnCalendar=*-*-* 22:30:00
Persistent=true

[Install]
WantedBy=timers.target
"""
    
    with open(service_path, "w") as f:
        f.write(service_content)
        
    with open(timer_path, "w") as f:
        f.write(timer_content)
        
    # Reload and enable
    print("git-green: Enabling systemd user timer...")
    subprocess.run(["systemctl", "--user", "daemon-reload"])
    subprocess.run(["systemctl", "--user", "enable", "--now", "github-green.timer"])
    print("git-green: Daily timer activated successfully! Running every day at 10:30 PM.")

def main():
    parser = argparse.ArgumentParser(
        description="git-green: Maintain an organic, semantic Git contribution graph."
    )
    subparsers = parser.add_subparsers(dest="command", help="Subcommand to run")

    # generate subcommand
    generate_parser = subparsers.add_parser(
        "generate", help="Generate organic contributions for a past date range"
    )
    generate_parser.add_argument(
        "--days", type=int, default=60, help="Number of past days to generate commits for"
    )

    # install subcommand
    subparsers.add_parser(
        "install", help="Install daily systemd timer autostart configuration"
    )

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    if args.command == "generate":
        generate_contributions(args.days)
    elif args.command == "install":
        install_systemd()

if __name__ == "__main__":
    main()
