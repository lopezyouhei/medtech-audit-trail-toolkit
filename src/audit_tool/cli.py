import subprocess


def lint():
    subprocess.run(["ruff", "check", "."])
    subprocess.run(["ty", "check"])


def fix():
    subprocess.run(["ruff", "check", "--fix", "."])
    subprocess.run(["ruff", "format", "."])
