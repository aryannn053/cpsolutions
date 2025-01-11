import os
import requests

def fetch_accepted_solutions(username):
    # Codeforces API endpoint
    api_url = f"https://codeforces.com/api/user.status?handle={username}"
    try:
        # Fetch user's submissions
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()

        if data["status"] != "OK":
            print(f"Error: {data.get('comment', 'Unknown error')}")
            return

        # Process submissions
        for submission in data["result"]:
            if submission["verdict"] == "OK":
                contest_id = submission["problem"]["contestId"]
                index = submission["problem"]["index"]
                problem_id = f"{contest_id}{index}"

                # Determine file extension based on programming language
                language = submission["programmingLanguage"]
                if "C++" in language:
                    extension = ".cpp"
                elif "Python" in language or "PyPy" in language:
                    extension = ".py"
                elif "Java" in language:
                    extension = ".java"
                else:
                    extension = ".txt"

                # Generate file name
                filename = f"{problem_id}{extension}"

                # Create the empty file
                if not os.path.exists(filename):
                    with open(filename, "w") as file:
                        pass  # Empty file creation
                    print(f"Created file: {filename}")
                else:
                    print(f"File already exists: {filename}")

    except requests.exceptions.RequestException as e:
        print(f"HTTP Request failed: {e}")
    except KeyError as e:
        print(f"Unexpected API response structure: {e}")

if __name__ == "__main__":
    username = input("Enter Codeforces username: ").strip()
    fetch_accepted_solutions(username)
