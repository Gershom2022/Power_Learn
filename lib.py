import os
import requests
from urllib.parse import urlparse
import sys

def get_filename_from_url(url):
    """
    Extract filename from URL path.
    If no valid filename, generate a default one.
    """
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)
    if not filename or '.' not in filename:
        # Generate a default filename if none found or no extension
        filename = "downloaded_image"
    return filename

def download_image(url, save_dir="Fetched_Images"):
    # Create directory if it doesn't exist
    os.makedirs(save_dir, exist_ok=True)

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise HTTPError for bad responses

        # Check content-type to ensure it's an image
        content_type = response.headers.get('Content-Type', '')
        if not content_type.startswith('image/'):
            print("Error: URL does not point to an image.")
            return False

        filename = get_filename_from_url(url)

        # If filename exists, avoid overwriting by appending a number
        filepath = os.path.join(save_dir, filename)
        base, ext = os.path.splitext(filename)
        counter = 1
        while os.path.exists(filepath):
            filepath = os.path.join(save_dir, f"{base}_{counter}{ext}")
            counter += 1

        # Save image in binary mode
        with open(filepath, 'wb') as f:
            f.write(response.content)

        print(f"Image successfully downloaded and saved as: {filepath}")
        return True

    except requests.exceptions.MissingSchema:
        print("Error: Invalid URL format.")
    except requests.exceptions.ConnectionError:
        print("Error: Failed to connect to the URL.")
    except requests.exceptions.Timeout:
        print("Error: The request timed out.")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return False

def main():
    print("Ubuntu-Inspired Image Fetcher")
    url = input("Please enter the URL of the image to download: ").strip()
    if not url:
        print("No URL entered. Exiting.")
        sys.exit(1)

    download_image(url)

if __name__ == "__main__":
    main()