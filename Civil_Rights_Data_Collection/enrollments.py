import pandas as pd

data = pd.read_csv("data/CRDC2013_14.csv", encoding="Latin-1")

race_code = ["HI", "AM", "AS", "HP", "BL", "WH", "TR"]
race_name = ["Hispanic", "American Indian", "Asian", "Hawaiin-PacIslander", "Black", "White", "Two+Races"]

totals = {}

data["total_enrollment"] = data["TOT_ENR_M"] + data["TOT_ENR_F"]
all_enrollment = data["total_enrollment"].sum()

for index, race in enumerate(race_code):
    females_race = 'SCH_ENR_{}_F'.format(race)
    males_race = 'SCH_ENR_{}_M'.format(race)
    total_this_race = 'Total_{}'.format(race_name[index])
    totals[total_this_race] = round(100 * (data[females_race].sum() + data[males_race].sum()) / all_enrollment, 2)     
    readable_female_count = '{} females: {}'.format(race_name[index], str(data[females_race].sum()))
    readable_male_count = '{} males: {}'.format(race_name[index], str(data[males_race].sum()))
    print(readable_female_count)
    print(readable_male_count)
print(totals)
