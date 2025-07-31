import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


def published_most_rides(club_data):
    club_data_grouped = club_data.groupby(['firstname', 'lastname'])
    club_data_count = club_data_grouped.count()

    rider = club_data_count['distance'][club_data_count['distance'].max() == club_data_count['distance']].rename("number_of_rides")
    
    print("Rider with the most published rides:")
    print(rider)
    print(f"\n")

def calculate_avg_speed(club_data):
    club_data_copy = club_data.copy(deep=True)
    
    club_data_copy['speed_ms'] = club_data_copy['distance'] / club_data_copy['moving_time']
    club_data_copy['speed_kmh'] = club_data_copy['speed_ms'] * 3.6

    # Converting to km/h instead of m/s (distance(m) to distance(km), moving_time(s) to moving_time(h))
    club_data_copy['distance'] = club_data_copy['distance'] / 1000
    club_data_copy['moving_time'] = club_data_copy['moving_time'] / 3600

    avg_speed_grouped = club_data_copy.groupby(['firstname', 'lastname'])
    avg_speed_club = avg_speed_grouped[['speed_ms', 'speed_kmh']].mean(numeric_only=True)


    print("Average speed per ride:")
    print(avg_speed_club)
    print(f"\n")

    return club_data_copy


def k_mean_something(club_data):
    scaler = StandardScaler()

    model = KMeans(n_clusters=3)
    club_data['cluster'] = model.fit_predict(scaler.fit_transform(club_data[['distance', 'speed_kmh', 'total_elevation_gain']]))

    plt.figure(1)
    plt.scatter(club_data['distance'], club_data['total_elevation_gain'], c=club_data['cluster'], edgecolors='k')

    plt.xlabel("Distance (km)")
    plt.ylabel("Elevation Gain (m)")
    plt.title("KMeans Clustering of Rides (k=3)")
    plt.show()

    print(club_data.groupby("cluster")[["distance", "speed_kmh", "total_elevation_gain"]].mean().round(2))


def main():
    """
        distance (m)
        moving_time (s)
        total_elevation_gain (m)

        The CSV format:
            ["date", "firstname", "lastname", "title", "distance", "moving_time", "elapsed_time", "total_elevation_gain", "type", "sport_type", "workout_type"]
        Questions:
            Clean data
                distance, moving_time, elapsed_time, total_elevation_gain from any 0 or NAN values
            1. Who has the most rides published
            2. Calculate avg speed per ride or over all the rides distance/moving_time (maybe standard deviation)
            3. Use KMeans to cluster rides into categories (based on distance, speed_kmh, and total_elevation_gain)
                - Idea: Rides can be clustered into 3 groups short rides, elevation gain rides, long rides (ideally with no elevation gain)
    """
    club_data = pd.read_csv('CyclingData.csv')

    club_data_cleaned = club_data[(club_data['distance'] > 0) | (club_data['moving_time'] > 0) | (club_data['elapsed_time'] > 0) | (club_data['total_elevation_gain'] > 0)]
    club_data_filtered = club_data_cleaned[['firstname', 'lastname',  'distance',  'moving_time', 'elapsed_time', 'total_elevation_gain', 'type']]

    published_most_rides(club_data_filtered)

    club_data = calculate_avg_speed(club_data_filtered)

    k_mean_something(club_data)
    

if __name__ == '__main__':
    main()