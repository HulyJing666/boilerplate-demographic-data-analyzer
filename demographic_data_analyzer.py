import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('/workspace/boilerplate-demographic-data-analyzer/adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()
    # What is the average age of men?
    men = df[df['sex'] == 'Male']
    average_age_men = (men['age'].mean()).round(decimals = 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = (((df['education'] == 'Bachelors').sum())/(df['education'].count())*100).round(decimals = 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    advanced = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    # What percentage of people without advanced education make more than 50K?
    notadvanced = (df['education'].count())-(advanced['education'].count())

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = ((advanced['education'].count())/(df['education'].count())*100).round(decimals = 1)
    lower_education = (notadvanced)/(df['education'].count())*100

    # percentage with salary >50K
    her = advanced[advanced['salary']=='>50K']
    higher_education_rich = ((her['education'].count())/(advanced['education'].count())*100).round(decimals = 1)
    rich = df[df['salary'] == '>50K']
    lwr = (rich['salary'].count())-(her['salary'].count())
    lower_education_rich = ((lwr)/(notadvanced)*100).round(decimals = 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    num_min_rich = num_min_workers[num_min_workers['salary'] == '>50K']

    rich_percentage = ((num_min_rich['hours-per-week'].count())/(num_min_workers['hours-per-week'].count())*100).round(decimals = 1)

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = (rich['native-country'].value_counts() / df['native-country'].value_counts() *100).sort_values(ascending=False).index[0]
    highest_earning_country_percentage = ((rich['native-country'].value_counts() / df['native-country'].value_counts() *100).max()).round(decimals = 1)

    # Identify the most popular occupation for those who earn >50K in India.
    india = df[((df['native-country'] == 'India') & (df['salary'] == '>50K'))]
    top_IN_occupation = (india['occupation'].value_counts()).index[0]
    
    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
