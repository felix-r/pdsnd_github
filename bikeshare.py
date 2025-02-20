import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}
CITY_ABBR = ['c', 'ch', 'chicago',
             'n', 'ny', 'nyc', 'new york', 'new york city',
             'w', 'washington']
MONTH_LIST = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
DAY_LIST = ['monday', 'm',
            'tuesday', 'tu',
            'wednesday', 'w',
            'thursday', 'th',
            'friday', 'f',
            'saturday', 'sa',
            'sunday', 'su',
            'all']


def get_month():
    """
    Return month from user input.

    Returns:
        (str) month - name of month
    """

    print("Which month - January, February, March, April, May, or June?")
    err_msg = "Sorry, I didn't understand that. Please choose an input from {}".format(str(MONTH_LIST))
    while True:
        month = input("Month: ").lower()
        if month not in MONTH_LIST:
            print(err_msg)
            continue
        else:
            break
    return month


def get_day():
    """
    Return weekday from user input.

    Returns:
        (str) weekday - name of weekday
    """

    print("Which day - Monday (M), Tuesday (Tu), Wednesday (W), Thursday (Th), Friday (F), Saturday (Sa), "
          "or Sunday (Su)?")
    err_msg = "Sorry, I didn't understand that. Please choose an input from {}".format(str(DAY_LIST))
    while True:
        day = input("Day of week: ").lower()
        if day not in DAY_LIST:
            print(err_msg)
            continue
        else:
            if day == 'm':
                day = 'monday'
            elif day == 'tu':
                day = 'tuesday'
            elif day == 'w':
                day = 'wednesday'
            elif day == 'th':
                day = 'thursday'
            elif day == 'f':
                day = 'friday'
            elif day == 'sa':
                day = 'saturday'
            elif day == 'su':
                day = 'sunday'
            break
    return day


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    # Get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print("Which city would you like to explore? Chicago (C), New York City (NY, NYC), or Washington (W)?")
    err_msg = "Sorry, I didn't understand that. Please choose an input from {} \n".format(str(CITY_ABBR))
    while True:
        city = input("City name: ").lower()
        if city not in CITY_ABBR:
            print(err_msg)
            continue
        else:
            if city in ['c', 'ch', 'chicago']:
                city = 'chicago'
            elif city in ['n', 'ny', 'nyc', 'new york', 'new york city']:
                city = 'new york city'
            elif city in ['w', 'washington']:
                city = 'washington'
            break

    print("Would you like to filter the data by month, day, both, or not at all?")
    err_msg = "Sorry, I didn't understand that. Please choose an input from ['month', 'day', 'both', 'all']"
    while True:
        month_day_filter = input("'month', 'day', 'both', or 'all'?: ").lower()
        if month_day_filter not in ['month', 'day', 'both', 'all']:
            print(err_msg)
            continue
        else:
            break

    if month_day_filter == 'all':
        month = 'all'
        day = 'all'
    elif month_day_filter == 'month':
        day = 'all'
        # Get user input for month (all, january, february, ... , june)
        month = get_month()
    elif month_day_filter == 'day':
        month = 'all'
        # Get user input for day of week (all, monday, tuesday, ... sunday)
        day = get_day()
    elif month_day_filter == 'both':
        # Get user input for month (all, january, february, ... , june)
        month = get_month()
        # Get user input for day of week (all, monday, tuesday, ... sunday)
        day = get_day()

    print('-' * 40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name().str.lower()
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1  # dt.month creates values from 1 to 12

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    most_common_month = months[df['month'].mode()[0] - 1]
    print("Most common month: ", most_common_month.capitalize())

    # Display the most common day of week
    print("Most common day: ", df['day_of_week'].mode()[0].capitalize())

    # Display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print(f"Most popular start hour: {popular_hour}:00 - {popular_hour}:59")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("Most commonly used start station: ", df['Start Station'].mode()[0])
    # TO DO: display most commonly used end station
    print("Most commonly used end station: ", df['End Station'].mode()[0])
    # TO DO: display most frequent combination of start station and end station trip
    df['Trip'] = df['Start Station'] + ' - ' + df['End Station']
    print("Most frequent combination of start station and end station trip:\n", df['Trip'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("Total travel time: {} seconds".format(df['Trip Duration'].sum()))
    # TO DO: display mean travel time
    print("Average travel time: {} seconds".format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("Counts of user types:")
    print(df['User Type'].value_counts(), "\n")
    # TO DO: Display counts of gender
    if 'Gender' in df:
        print("Counts of gender:")
        print(df['Gender'].value_counts(), "\n")
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        print("Earliest year of birth: ", int(df['Birth Year'].min()))
        print("Most recent year of birth: ", int(df['Birth Year'].max()))
        print("Most common year of birth: ", int(df['Birth Year'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def print_dataset(df):
    """"Print 5 rows of a given dataset at a time by clicking enter until user input to stop."""

    print("Press enter to see 5 additional rows of the dataset.\n")
    n = 0
    while True:
        print(df[n : n+5])
        user_in = input("Would you like to see next five rows of raw data? [Yes], No: ").lower()
        if user_in in ['n', 'no', 'stop', 'quit']:
            break
        elif n+5 >= len(df.index):
            print("End of dataset\n")
            break
        else:
            n += 5
            continue

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        print("Would you like to look at the raw data?")
        raw_data_input = input("See raw data? Enter yes or no: ").lower()
        if raw_data_input in ['yes', 'y']:
            print_dataset(df)

        restart = input('\nWould you like to restart? Enter Yes or [No].\n')
        if restart.lower() not in ['yes', 'y']:
            break


if __name__ == "__main__":
    main()
