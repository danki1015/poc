import pandas as pd
from .get_severity import get_severity

def calculate_score_crit(datalevel, column_name, numerator_column, denominator_column, weight):

    datalevel[f'{column_name}_score_crit'] = (5 ** (datalevel[numerator_column] / datalevel[denominator_column])).apply(lambda x: 1 if x > 5 else (x - 1) / 4)
    datalevel[f'{column_name}_score_crit'] *= weight

def get_level_category(value, severity):
    if severity == 'Critical':
        if 0 <= value <= 40:
            return "GM"
        elif 40 < value <= 98:
            return "VP"
        else:
            return "BOD"
    elif severity == 'Major':
        return "GM"
    elif severity == 'Minor':
        return "Manager"
    elif severity == 'Low':
        return "SPV"
    else:
        return "Undefined" 

def get_level(datalevel):
    # Add 'Severity' column if not already present
    if 'Severity' or 'final_score' not in datalevel.columns:
        datalevel['Severity'] = get_severity(datalevel)['Severity']
        datalevel['final_score'] = get_severity(datalevel)['final_score']

    thresh = {
        'Revenue': [25.3657502341003],
        'Subscriber': [76107.3135000001],
        'Site': [190.775000000002]
    }

    # Tambahkan nilai dari threshold ke DataFrame Anda
    for col, values in thresh.items():
        datalevel[col] = values[0]

    # Example calls to calculate_score_crit function with respective parameters
    calculate_score_crit(datalevel, 'rev', 'revenue_hourly', 'Revenue', 40)
    calculate_score_crit(datalevel, 'subs', 'subscriber_4g_hourly', 'Subscriber', 55)
    calculate_score_crit(datalevel, 'site', 'site_id', 'Site', 5)

    # Example final_score_crit calculation
    datalevel['final_score_crit'] = datalevel['rev_score_crit'] + datalevel['subs_score_crit'] + datalevel['site_score_crit']

    # Example function to get level category
    datalevel['Level'] = datalevel.apply(lambda row: get_level_category(row['final_score_crit'], row['Severity']), axis=1)

    selected_columns = ['Ticket ID', 'regional', 'Start Time(Create TT_alarm_start_time)',
                    'Severity(Create TT_severity)', 'revenue_hourly', 'site_id',
                    'subscriber_4g_hourly', 'final_score', 'Severity', 'final_score_crit', 'Level']

    result = datalevel[selected_columns]
    result.loc[result['Severity'] != 'Critical', 'final_score_crit'] = 0

    return result