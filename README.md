# Activity Tracker

## Introduction

The Strava Club Activity Tracker allows members to fetch activity data from a specified Strava club and store the data in a CSV file. This application uses the Strava API to fetch the most recent public activities from a club and can be configured to repeat requests made to gather data from multiple pages. (This can be automated with the use of CRON jobs or any other automation system)

This application provides an easy to use API authentication, token refreshing, and exporting activity data for sports like cycling (ride), running (run), or etc depending on the club's activity type.

### Prerequisites:
- Python 3.7 or higher
- `requests` library
- `pandas` library

To install the necessary dependencies, run the following:

```bash
pip install -r requirements.txt
```

## Usage

To run this application, you will first need to obtain your Strava credentials. You can obtain them from the [Strava API](https://www.strava.com/settings/api). Once you finished the steps to create a developer account, copy the following credentials and store them into the `credentials.txt` file, as follows:
   ```
   client_id=<YOUR_CLIENT_ID>
   client_secret=<YOUR_CLIENT_SECRET>
   access_token=<YOUR_ACCESS_TOKEN>
   refresh_token=<YOUR_REFRESH_TOKEN>
   club_id=<YOUR_CLUB_ID>
   ```
Both `expires_at` and `expires_in` in the credentials file are optional and not required.

```bash
python main.py <output_filename>.csv <page_number>
```

# Demo
[ActivityTrackerDemo](https://github.com/user-attachments/assets/8f964b76-f518-4b10-874d-c0519a2ecc24)


### Parameters:
**Required**
- `<output_filename>`: The name of a CSV file to save the activity data. The file will be created or appended with the activities retrieved from the club.

**Optional**
- `<page_number>`: The maximum number of pages (inclusive) the function will fetch from Strava activity (Default: 1) (Max 50 per minute set by Strava API)

### Configuration:
There is JSON support included only for the `repeat_club_data` function. You will have to manually uncomment the areas that will produce the JSON file. Specifically, these lines:
```
# json_file = self.output_file
# if ".csv" in json_file:
#     json_file = json_file.removesuffix(".csv")
#     json_file += ".json"

# with open(json_file, 'a') as file:
.
.
.
# file.write(str(response.json()))
```
They will use the given file name as the output file.

## Contributions

Contributions are welcome! If you'd like to contribute to this project, please contact an Executive on the SFUCycling Discord or by email sfucycling@gmail.com 

Here are some ways to contribute:

- Fixing bugs
- Improving documentation
- Adding features like additional filters for activities

You are welcome to fork or clone this repository to use for your own club or personal collection.
