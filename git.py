import subprocess
import os


def run_command(command):
    print(f"\n▶ {command}")

    result = subprocess.run(
        command,
        shell=True,
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
            key, value = line.strip().split("=")
            config[key] = value

    return config


print("🚀 GitHub Auto Push Tool")


# Load GitHub configuration
config = load_config()

repo_url = config["GITHUB_REPO"]
branch = config["BRANCH"]


# Check git repository
if not os.path.exists(".git"):
    print("❌ Not a git repository")
    print("Run: git init")
    exit()


# Show changes
run_command("git status")


# Add files
run_command("git add .")


# Commit message
commit_message = input(
    "\n📝 Enter commit message: "
)


# Commit
commit_result = run_command(
    f'git commit -m "{commit_message}"'
)


# Add remote if not exists
remote = subprocess.run(
    "git remote",
    shell=True,
    text=True,
    capture_output=True
)


if "origin" not in remote.stdout:

    print("\n🔗 Adding GitHub remote...")
    run_command(
        f"git remote add origin {repo_url}"
    )

else:
    print("\n✅ Remote already configured")


# Set branch
run_command(
    f"git branch -M {branch}"
)


# Push
print("\n🚀 Pushing code to GitHub...")

run_command(
    f"git push -u origin {branch}"
)


print(
    "\n✅ Successfully pushed to GitHub!"
)