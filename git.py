import subprocess
import os


def run_command(command):
    print(f"\n▶ {' '.join(command) if isinstance(command, list) else command}")

    result = subprocess.run(
        command,
        text=True,
        capture_output=True
    )

    if result.stdout:
        print(result.stdout)

    if result.stderr:
        print(result.stderr)

    return result.returncode


def load_config():
    config = {}

    if not os.path.exists(".gitconfig_project"):
        print("❌ .gitconfig_project missing")
        exit()

    with open(".gitconfig_project", "r") as file:
        for line in file:
            if line.strip():
                key, value = line.strip().split("=", 1)
                config[key] = value

    return config


print("🚀 GitHub Auto Push Tool")


# Load config
config = load_config()

repo_url = config["GITHUB_REPO"]
branch = config["BRANCH"]


# Check git repository
if not os.path.exists(".git"):
    print("❌ Not a git repository")
    exit()


# Show status
run_command(["git", "status"])


# Add files
run_command(["git", "add", "."])


# Commit message
commit_message = input(
    "\n📝 Enter commit message: "
)


# Commit safely
commit_result = run_command(
    ["git", "commit", "-m", commit_message]
)


if commit_result != 0:
    print("\n❌ Commit failed. Push cancelled.")
    exit()


# Check remote
remote = subprocess.run(
    ["git", "remote"],
    text=True,
    capture_output=True
)


if "origin" not in remote.stdout:

    print("\n🔗 Adding GitHub remote...")

    run_command(
        ["git", "remote", "add", "origin", repo_url]
    )

else:
    print("\n✅ Remote already configured")


# Set branch
run_command(
    ["git", "branch", "-M", branch]
)


# Push
print("\n🚀 Pushing code to GitHub...")

push_result = run_command(
    ["git", "push", "-u", "origin", branch]
)


if push_result == 0:
    print("\n✅ Successfully pushed to GitHub!")
else:
    print("\n❌ Push failed")