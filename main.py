from datetime import date
import time
import sys
import argparse

from StravaActivityTracker import StravaToken

def main(filename, page_number, recursive_strava_data):
    strava_tokens = None

    try:
        with open("credentials.txt", 'r+') as file:  # Open the credentials.txt with read/write and closes once complete
            credentials_content = file.readlines()
            credentials = {}

            for line in credentials_content:
                if "=" in line:
                    key, value = line.strip().split("=", 1)
                    credentials[key.strip()] = value.strip()

            if not credentials:
                raise FileNotFoundError("")
            strava_tokens = StravaToken(credentials=credentials, output_file=filename)
            print("\nFile opened successfully and credentials loaded into StravaTokens object!\n")
            
            file.seek(0)
            cred_list = dir(strava_tokens)
            for key, value in cred_list:
                file.write(f'{key}={value}\n')
            print("Credentials have been saved.")

        if recursive_strava_data:
            strava_tokens.club_data_repeat(page_number)
        else:
            strava_tokens.club_data(page_number)
        print(f"All club data from Strava has been saved")

    except FileNotFoundError as e:
        with open(f"ErrorLogs/{date.today()}.txt", "a") as f:
            f.write(f"{time.ctime()}: ")
            f.write(f"Error: Could not open the file {e}. Please ensure the file exists in the current directory and contains the necessary credentials.\n")
    except Exception as e:
        with open(f"ErrorLogs/{date.today()}.txt", "a") as f:
            f.write(f"{time.ctime()}: ")
            f.write(f"{str(e)} \n")

if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("filename", help="Outputs values to the given filename or name of csv", type=str)
        parser.add_argument("page_number", nargs="?", const=1, default=1,
                            help="The maximum number of pages (inclusive) this will fetch from Strava activity (Default: 1) (Max 50 per minute set by Strava API)", type=int)
        parser.add_argument('-r', action='store_true', help="flag argument to recursively gather Strava club (Will overwrite the file)")
        args = parser.parse_args()

        filename = args.filename if ".csv" in args.filename else args.filename + ".csv"
        if args.page_number > 50:
            raise ValueError("The number of pages can not exceed 50 as per Strava API requests")
        elif args.page_number < 1:
            raise ValueError("The number of pages can not be negative or zero")
        else:
            page_number = args.page_number
        recursive_strava_data = args.r

        main(filename, page_number, recursive_strava_data)

    except:
        e = sys.exc_info()[0], sys.exc_info()[1]
        print (e)
