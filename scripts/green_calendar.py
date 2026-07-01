import os
import subprocess
import datetime
import random
import sys

def run_cmd(args, env=None):
    subprocess.run(args, env=env, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def make_green(days_back, min_commits=25, max_commits=40):
    repo_path = "/home/zainm/dotfiles"
    log_file = os.path.join(repo_path, "contribution_log.txt")
    
    # Change to repo directory
    os.chdir(repo_path)
    
    # Starting date
    today = datetime.date.today()
    start_date = today - datetime.timedelta(days=days_back)
    
    current_env = os.environ.copy()
    
    total_commits = 0
    print(f"Generating contributions for the last {days_back} days...")
    
    for i in range(days_back + 1):
        target_date = start_date + datetime.timedelta(days=i)
        # Determine number of commits for this day
        num_commits = random.randint(min_commits, max_commits)
        
        # Don't commit for future dates
        if target_date > today:
            break
            
        print(f"Processing {target_date.strftime('%Y-%m-%d')} - generating {num_commits} commits...")
        
        for commit_idx in range(num_commits):
            # Generate random hour/minute/second
            hour = random.randint(9, 21)
            minute = random.randint(0, 59)
            second = random.randint(0, 59)
            
            commit_time = datetime.datetime.combine(
                target_date, 
                datetime.time(hour, minute, second)
            )
            date_str = commit_time.isoformat()
            
            # Update log file
            with open(log_file, "a") as f:
                f.write(f"Contribution entry: {date_str} - #{commit_idx}\n")
                
            # Stage
            run_cmd(["git", "add", "contribution_log.txt"])
            
            # Set commit dates
            env = current_env.copy()
            env["GIT_AUTHOR_DATE"] = date_str
            env["GIT_COMMITTER_DATE"] = date_str
            
            # Commit
            run_cmd([
                "git", 
                "commit", 
                "-m", f"chore: update contribution log {target_date.strftime('%Y-%m-%d')} #{commit_idx}"
            ], env=env)
            
            total_commits += 1

    print(f"Successfully generated {total_commits} commits locally!")
    print("Pushing to GitHub...")
    
    # Push to origin
    res = subprocess.run(["git", "push"], capture_output=True, text=True)
    if res.returncode == 0:
        print("Push successful! Check your GitHub contribution graph!")
    else:
        print("Push failed:")
        print(res.stderr)

if __name__ == "__main__":
    days = 60
    if len(sys.argv) > 1:
        try:
            days = int(sys.argv[1])
        except ValueError:
            pass
    make_green(days)
