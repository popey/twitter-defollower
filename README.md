# twitter-defollower

A Python script to automatically remove followers from your Twitter/X account. This script helps remove people who *follow you*, not people you follow.

The script will:
* Log into your X account
* Navigate to your followers page
* Remove your followers in batches of 10
* Automatically refresh the page between batches
* Continue until stopped or no more followers found

## Notes

* Tested on macOS and Ubuntu 24.04
* The script uses human-like delays and interactions to avoid triggering anti-automation measures
* X may still detect automation and request additional verification
* Use responsibly and in accordance with X's terms of service, if you care

## Requirements

* Python 3.10 or higher
* Chrome or Chromium browser
* [uv](https://github.com/astral-sh/uv) (for virtual environment and dependency management)
* [Selenium](https://pypi.org/project/selenium/)

## Installation

1. Clone this repository
```bash
git clone https://github.com/popey/twitter-defollower
cd twitter-defollower
```

2. Create a virtual environment and install dependencies
```bash
uv venv
source .venv/bin/activate
uv pip install selenium
```

## Usage

1. Edit the script to add your credentials:
```python
username = "your_username"
password = "your_password"
email_or_phone = "your_email_or_phone"  # Used if X requires additional verification
```

2. Run the script:
```bash
python twitter-defollower.py
```

## License

* MIT

## Author

* Alan Pope (@popey)
