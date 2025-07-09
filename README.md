# Strava Club Activity Tracker

## Introduction

The Strava Club Activity Tracker allows members to fetch activity data from an specified Strava club and store the data in a CSV file. This application uses the Strava API to fetch the most recent public activities from a club, and can be configured to repeat requests made to gather data from multiple pages. (This can be automated with the use of CRON jobs or any other automation system)

This application provides an easy to use API authentication, token refreshing, and exporting activity data for sports like cycling (ride), running (run), or etc depending on the club's activity type.

If you have any questions or issues, please contact sfucycling@gmail.com.

# Demo
[ActivityTrackerDemo](https://github.com/user-attachments/assets/8f964b76-f518-4b10-874d-c0519a2ecc24)

### Prerequisites:
- Python 3.7 or higher
- `requests` version 2.32.3
- `pandas` version 2.2.3
- `numpy` version 2.2.5

To install the dependencies:

```bash
pip install -r requirements.txt
```

## Usage

To run this application, you will need to obtain your Strava credentials. You can obtain them from the [Strava API](https://www.strava.com/settings/api). 
Once you finished the steps to create a developer account, copy the following credentials and store them into the `credentials.txt` file, as follows:
   ```
   client_id=<YOUR_CLIENT_ID>
   client_secret=<YOUR_CLIENT_SECRET>
   access_token=<YOUR_ACCESS_TOKEN>
   refresh_token=<YOUR_REFRESH_TOKEN>
   club_id=<YOUR_CLUB_ID>
   ```

Once you have set up the `credentials.txt` file. Run the following command
```bash
python main.py StravaClubActivity 1
python main.py <output_filename> <page_number>
```

### Parameters:
**Required**
- `<output_filename>`: The name of a CSV file to save the activity data. The file will be created or overwritten with pd.to_csv and pd.to_json methods

**Optional**
- `<page_number>`: The maximum number of pages (inclusive) the function will fetch from Strava activity (Default: 1) (Max 50 per minute set by Strava API)

## Contributions

Contributions are welcome! If you'd like to contribute to this project, please contact an Executive on the SFUCycling Discord or by email sfucycling@gmail.com 