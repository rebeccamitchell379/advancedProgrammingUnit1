import requests

def get_random_joke():
    url = "https://icanhazdadjoke.com/"
    headers = {'Accept': 'application/json'}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  
        data = response.json()
        joke = data['joke']

        # Modify the joke if it has a question mark
        if '?' in joke:
            parts = joke.split('?')  # Split the joke where the question mark is
            return f"{parts[0]}?\n{parts[1]}"  # Print with a newline
        else:
            return joke

    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    joke = get_random_joke()
    print(joke)
