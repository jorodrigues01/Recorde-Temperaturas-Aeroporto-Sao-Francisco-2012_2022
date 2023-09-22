def to_day_of_year(date):
    """
    Get the day of year excluding the leap year's Feb 29th
    :param date: timeStamp object.
    :return: returns an int value corresponding to the ordinal day of the year.
    """

    if date.is_leap_year and date.day_of_year > 60:
        return date.day_of_year-1
    return date.day_of_year


def get_historical_tmax_date(row, df):
    """
    Get the observation date of maximum temperature for a given day of year
    :param row: observation line of the grouped dataframe.
    :param df: the DataFrame object corresponding to the 10-year period before the grouping.
    :return: returns a TimeStamp object indicating the day of the maximum temperature was measured.
    """

    df_MAX10yrs = df.set_index('DAY OF YEAR').loc[row['DAY OF YEAR']]
    df_MAX10yrs = df_MAX10yrs[(df_MAX10yrs['TMAX'] == df_MAX10yrs['TMAX'].max())]

    return df_MAX10yrs['DATE'].iloc[-1]


def get_historical_tmin_date(row, df):
    """
    Get the observation date of minimum temperature for a given day of year
    :param row: observation line of the grouped dataframe.
    :param df: the DataFrame object corresponding to the 10-year period before the grouping
    :return: returns a TimeStamp object indicating the day of the minimum temperature was measured
    """

    df_MIN10yrs = df.set_index('DAY OF YEAR').loc[row['DAY OF YEAR']]
    df_MIN10yrs = df_MIN10yrs[(df_MIN10yrs['TMIN'] == df_MIN10yrs['TMIN'].min())]

    return df_MIN10yrs['DATE'].iloc[-1]
