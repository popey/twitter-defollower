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
* [uv](https://github.com/astral-sh/uv) (for virtual environment and dependency management) or any other virtual-env system
  * I just really like uv, okay 
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

## Sample output

```bash
No additional verification required
Successfully logged in!
Loading followers page...
Found 147 followers to process
Successfully removed follower. Total processed: 1
Successfully removed follower. Total processed: 2
Successfully removed follower. Total processed: 3
Successfully removed follower. Total processed: 4
Successfully removed follower. Total processed: 5
Successfully removed follower. Total processed: 6
Successfully removed follower. Total processed: 7
Successfully removed follower. Total processed: 8
Successfully removed follower. Total processed: 9
Successfully removed follower. Total processed: 10
Processed 10 followers, refreshing page...
Loading followers page...
Found 145 followers to process
Successfully removed follower. Total processed: 11
Successfully removed follower. Total processed: 12
Successfully removed follower. Total processed: 13
Successfully removed follower. Total processed: 14
Successfully removed follower. Total processed: 15
Successfully removed follower. Total processed: 16
Successfully removed follower. Total processed: 17
Successfully removed follower. Total processed: 18
Successfully removed follower. Total processed: 19
Successfully removed follower. Total processed: 20
Processed 10 followers, refreshing page...
```

## FAQ

* Why do this?

  Why not?

* Why don't you just delete your Twitter/X account?

  🤷‍♂️

* Does it stop people re-following you?

  Nope. Use Twitter profile security settings to do that, if you can.

* What if they change the flow / add bot detection?

  The script might break. 😱 (patches welcome)

* What if they block or suspend the account?

  Then the account will be blocked or suspended.

* Does it require uv?

  Nope, you can use `python-venv` or whatever other favourtie way you have for making python virtual environments. I've only tested with uv.

## License

* MIT

## Author

* Alan Pope (@popey)
