import requests
import csv
import pandas as pd



def getRequest(start_time, end_time, month, numRows):
    # Set the API endpoint URL
    url = 'https://data.cityofchicago.org/resource/sxs8-h27x.json'

    # Set the query parameters to filter the data by time range
    # "time between '2023-01-01T00:00:00' and '2023-02-01T00:00:00'"
    params = {
        '$where': f"time between '{start_time}' and '{end_time}' and speed != '-1'",
        "$limit" : numRows

    }

    # Make the API call and get the response
    response = requests.get(url, params=params)

    filename = f'data_{month}.csv'
    # Check if the response was successful
    if response.status_code == 200:
        # Write the response content to a file
        # with open(f'data_{month}.json', 'w') as f:
        #     f.write(response.content.decode('utf-8'))

        data = response.json()
        with open(filename, 'w', newline='') as file:
            fieldnames = list(data[0].keys())
            fieldnames.append('comments')
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            # Write header row
            writer.writeheader()

            # Write data rows
            writer.writerows(data)
    else:
        # Print an error message if the API call failed
        print('API call failed with status code:', response.status_code)
    return filename

def analyseData(filename):
    df = pd.read_csv(filename)
    df.info()

filename = getRequest("2023-01-01T00:00:00", "2023-01-01T10:00:00", "jan_10_days", 1000000)
analyseData(filename)



