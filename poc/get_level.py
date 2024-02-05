import pandas as pd

def calculate_score_crit(datalevel, column_name, numerator_column, denominator_column, weight):
    thresh = {
        'Revenue': [25.3657502341003],
        'Subscriber': [76107.3135000001],
        'Site': [190.775000000002]
    }
    thresh_df = pd.DataFrame(thresh)

    datalevel[f'{column_name}_score_crit'] = (5 ** (datalevel[numerator_column] / thresh_df[denominator_column])).apply(lambda x: 1 if x > 5 else (x - 1) / 4)
    datalevel[f'{column_name}_score_crit'] *= weight

def get_level_category(value):
    if 0 <= value <= 40:
        return "GM"
    elif 40 < value <= 98:
        return "VP"
    else:
        return "BOD"

def get_level(data):
    datalevel = pd.DataFrame(data)

    # Example calls to calculate_score_crit function with respective parameters
    calculate_score_crit(datalevel, 'rev', 'revenue_hourly', 'Revenue', 40)
    calculate_score_crit(datalevel, 'subs', 'subscriber_4g_hourly', 'Subscriber', 55)
    calculate_score_crit(datalevel, 'site', 'site_id', 'Site', 5)

    # Example final_score_crit calculation
    datalevel['final_score_crit'] = datalevel['rev_score_crit'] + datalevel['subs_score_crit'] + datalevel['site_score_crit']

    # Example function to get level category
    datalevel['Level'] = datalevel['final_score_crit'].apply(get_level_category)

    # Example dropping unnecessary columns
    result = datalevel.drop(columns=['rev_score_crit', 'subs_score_crit', 'site_score_crit', 'No. Regional', 'Regional Name', 'Revenue Hourly', 'Subscriber 4G Hourly', 'Ticket Number','Site ID Uniq Down'])

    return result