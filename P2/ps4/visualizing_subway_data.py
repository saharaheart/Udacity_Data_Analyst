from pandas import *
from ggplot import *
from datetime import *
from numpy import mean


# ps4.1
def plot_weather_data_1(turnstile_weather):
    '''
    This function plots the distribution of riders per day.
    '''
    plot = ggplot(turnstile_weather, aes('DATEn','ENTRIESn_hourly' )) + \
    geom_bar(stat='bar',fill='red',alpha= 0.5) + \
    ggtitle('Distribution of riders per day') + labs('Day','Entries')

    return plot

# ps4.2
def plot_weather_data_2(turnstile_weather):
    '''
    This function plots the trend of ridership by day of the week.
    '''
    df = turnstile_weather
    df['Day'] = df['DATEn'].map(lambda x:datetime.strptime(x, '%Y-%m-%d').strftime('%w'))
    agg = df.groupby(['Day'], as_index=False).aggregate(mean)

    plot = ggplot(agg, aes(x='Day', y='ENTRIESn_hourly')) +\
           geom_line() +\
           ggtitle('NYC Subway ridership by day of week') + xlab('Week day (0=Sunday)') + ylab('Entries')
    return plot

if __name__ == '__main__':
    df = pandas.DataFrame.from_csv('turnstile_data_master_with_weather.csv')

    print plot_weather_data_1(df)
    plot.show()
    raw_input("Press enter to continue...")

    print plot_weather_data_2(df)
    plot.show()