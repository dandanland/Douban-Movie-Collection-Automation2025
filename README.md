# Douban Movie Collection Automation Tool

This project provides an automation script to help Mac users quickly add a list of movies to a Douban movie collection. It eliminates the need for manual searching and clicking, greatly improving the efficiency of creating collections.

## Features

- Batch import movie names from a text file.
- Automatically search for movies and add them to a specified collection.
- Error recovery and failure logging.

## Prerequisites

Before using this script, ensure you have the following software and libraries installed:

1. **Python 3.6+**: [Download Here](https://www.python.org/downloads/)
2. **Selenium**: Python library for browser automation.
3. **Google Chrome**: The script uses Chrome as the browser.
4. **ChromeDriver**: A driver that matches your Chrome version.

## Installation Steps

### 1. Download the Project

```bash
git clone https://github.com/dandanland/Douban-Movie-Collection-Automation2025.git
cd Douban-Movie-Collection-Automation2025
```

### 2. Install Python Dependencies

```bash
pip install selenium
```

### 3. Download and Set Up ChromeDriver

#### Check Your Chrome Version:
1. Open Chrome.
2. Click on the three dots in the top right corner.
3. Select "Help" > "About Google Chrome".
4. Note down the version number (e.g., 127.0.6533.82).

#### Download the Corresponding ChromeDriver:
1. Visit the [ChromeDriver download page](https://chromedriver.chromium.org/downloads).
2. Select the version that matches your Chrome browser.
3. Download the version for your operating system.
4. Extract the downloaded file.
5. Move `chromedriver.exe` (Windows) or `chromedriver` (Mac/Linux) to your project folder（Note: The version of `chromedriver` in this repository is `113.0.5672.63` for mac arm64.

## Configuration

Before running the script, configure the following:

1. **Prepare a Movie List**: Create a text file with one movie name per line, named `YOUR_MOVIE_LIST.txt`.
2. **Create a Douban Collection**: Manually create a movie collection on Douban.
3. **Modify Script Parameters**: Open `douban_movie_collection.py` and update:
   - `collection_name`: Your collection name (e.g., "Top 100 Movies").
   - `collection_id`: Your collection ID (found in HTML source as `label[for='YOUR_ID']`).

### How to Find Collection ID

1. Open any movie page on Douban.
2. Click the "Add to collection" button.
3. Right-click on your collection > Inspect Element.
4. Look for `<label for="XXXXXXXXX">`, where the number is your collection ID.

## Usage

1. Ensure all configurations are completed.
2. Run the script:

```bash
python douban_movie_collection.py
```

3. The script will open Chrome and wait for you to log in manually.
4. After logging in, press Enter to continue.
5. The script will automatically add the first search result to your collection. To ensure accurate results, please use a correctly formatted and precise movie name list.
6. After completion, results will be displayed, and failed movies will be saved to `failed_movies.txt`.

## Notes

- You must log in manually due to Douban’s CAPTCHA mechanism.
- Running speed depends on network conditions; ensure a stable connection.
- Check for Douban website updates, as selectors may need adjustments.
- Use this script responsibly to avoid excessive requests.
- This script is for personal use only and should not be used for commercial purposes.

## Troubleshooting

### Common Issues

1. **Element not found** - Update selectors in the script if Douban changes its structure.
2. **Login issues** - Complete CAPTCHA verification and ensure a successful login.
3. **ChromeDriver version mismatch** - Use a ChromeDriver matching your Chrome version.
4. **Slow execution** - Increase `time.sleep()` wait times or check your network.

### Debugging Tips

- Review error messages in the console output.
- Test with a smaller movie list.
- Try different selectors for elements.
- Add wait times at key steps.

## License

This project is licensed under the MIT License.

## Contributions

Issues and suggestions for improvements are welcome!

