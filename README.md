# telegram-group-scrapper
With this script you can get information about all users of the group in csv format.
## Setup
1. Clone this repository (`git clone https://github.com/DavisDmitry/telegram-group-scraper.git`)
2. Go to the repository directory (`cd telegram-group-scraper`)
3. Create virtualenv (`python3 -m virtualenv venv`)
4. Activate your virtualenv (`source ./venv/bin/activate`)
5. Install requirements (`pip install -r requrements.txt`)
## Usage
First you need to [create an application](https://core.telegram.org/api/obtaining_api_id) and get data to use Telegram API.
Then follow the instructions:
1. Activate your virtualenv (`source ./venv/bin/activate`)
2. Run scraper script (`python -m scraper --api-id <YOUR API ID> --api-hash <YOUR API HASH> --group-name <NAME OF THE GROUP>` (or `--group-id <ID OF THE GROUP>`))
3. Profit!

The first time you run the script, it may ask you to log in.
