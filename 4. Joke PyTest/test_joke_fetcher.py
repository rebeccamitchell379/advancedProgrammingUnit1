import pytest
from joke_fetcher import get_random_joke
from unittest.mock import patch

@patch('joke_fetcher.requests.get')
def test_get_random_joke_success(mock_get):
    # Mock response from the API
    mock_response = {'joke': 'Why did the scarecrow win an award? Because he was outstanding in his field.'}

    # Mock the response from requests.get()
    mock_get.return_value.json.return_value = mock_response

    # Call the function to get a random joke
    joke = get_random_joke()

    # Assert that the function returned the expected joke
    assert joke == "Why did the scarecrow win an award?\n Because he was outstanding in his field."

@patch('joke_fetcher.requests.get')
def test_get_random_joke_error(mock_get):
    # Mock an error response from the API
    mock_get.side_effect = Exception("Connection error")

    # Call the function to get a random joke
    joke = get_random_joke()

    # Assert that the function returned an error message
    assert joke == "An error occurred: Connection error"

if __name__ == "__main__":
    pytest.main()
