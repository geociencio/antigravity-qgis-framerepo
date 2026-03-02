#!/usr/bin/env python3
"""
Bootstrap script for Antigravity-powered projects.
Automates project initialization and agentic setup.
"""

import os
import sys
import subprocess
from pathlib import Path


def run_command(command, shell=True):
    """Run a shell command and return success."""
    try:
        subprocess.run(command, shell=shell, check=True, capture_output=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def setup_project():
    print("🚀 Antigravity Project Bootstrapper")
    print("-----------------------------------")

    # Get project name
    project_name = input("\nEnter the new PyQGIS plugin name (e.g., my_awesome_plugin): ").strip()
    if not project_name:
        print("❌ Error: Plugin name cannot be empty.")
        sys.exit(1)

    # Replace Project Name in template files
    files_to_process = [
        Path("pyproject.toml"),
        Path("README.md"),
        Path("metadata.txt")
    ]

    placeholder_name = "{{PROJECT_NAME}}"

    print(f"\n📝 Replacing placeholders in base files...")

    for file_path in files_to_process:
        if file_path.exists():
            try:
                content = file_path.read_text(encoding="utf-8")
                if placeholder_name in content:
                    content = content.replace(placeholder_name, project_name)
                    file_path.write_text(content, encoding="utf-8")
                    print(f"  ✅ Updated {file_path}")
            except Exception as e:
                print(f"  ❌ Error processing {file_path}: {e}")

    # Initialize Agentic Framework
    agent_init_script = Path(".agent/init_agent_system.sh")
    if agent_init_script.exists():
        print("\n🤖 Initializing Agentic Framework...")
        os.chmod(agent_init_script, 0o755)
        subprocess.run([str(agent_init_script)], shell=False)

    # Git Initialization
    print("\n🐙 Git Initialization...")
    if not Path(".git").exists():
        if run_command("git init"):
            print("  ✅ Git repository initialized.")
            if run_command("git add .") and run_command(
                'git commit -m "initial: project setup with Antigravity Framework"'
            ):
                print("  ✅ Initial commit created.")
    else:
        print("  ℹ️ Git repository already exists.")

    print("\n✨ Bootstrap complete! Your project is ready.")
    print("Next steps:")
    print("1. Review '.agent/AGENTS.md' and customize your system.")
    print("2. Run '/inicia-sesion' to start collaborating with your agent.")

    delete_self = input("\nDo you want to delete this bootstrap script? (y/N): ").lower()
    if delete_self == "y":
        try:
            os.remove(__file__)
            print("  ✅ bootstrap.py removed.")
        except Exception as e:
            print(f"  ⚠️  Could not remove bootstrap.py: {e}")


if __name__ == "__main__":
    setup_project()
