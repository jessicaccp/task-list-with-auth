from os import path, system
from pathlib import Path
from sys import exit

BASE_DIR = Path(__file__).resolve().parent
PATH = path.join(BASE_DIR, "src", "manage.py")


def execute_command(command: str) -> int:
    print(f"Executing command: '{command}'.")
    return system(command)


def load_fixtures() -> None:
    fixtures = []

    if fixtures:
        loaddata_command = f"python {PATH} loaddata"
        command = loaddata_command

        for fixture in fixtures:
            command += f" {fixture}"

        if execute_command(command) != 0:
            print("Error: Failed to load fixtures.")
            exit(1)


def run_tests() -> None:
    tests = []

    if tests:
        test_command = f"python {PATH} test"
        command = test_command

        for test in tests:
            command += f" {test}"
        command += " --parallel --noinput"

        if execute_command(command) != 0:
            print("Error: Failed to run tests.")
            exit(1)


def start_server() -> None:
    makemigrations_command = f"python {PATH} makemigrations"
    migrate_command = f"python {PATH} migrate"
    runserver_command = f"python {PATH} runserver"

    if execute_command(makemigrations_command) != 0:
        print("Error: Failed to make migrations.")
        exit(1)

    if execute_command(migrate_command) != 0:
        print("Error: Failed to migrate.")
        exit(1)

    run_tests()
    load_fixtures()

    if execute_command(runserver_command) != 0:
        print("Error: Failed to run server.")
        exit(1)


if __name__ == "__main__":
    start_server()
