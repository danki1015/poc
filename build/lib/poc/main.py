# my_package/score_calculator.py

def calculate_score(merged_df, column_name, numerator_column, denominator_column, weight):
    merged_df[f'{column_name}_score'] = (5 ** (merged_df[numerator_column] / merged_df[denominator_column])).apply(lambda x: 1 if x > 5 else (x - 1) / 4)
    merged_df[f'{column_name}_score'] *= weight

def get_severity_category(value, regional_code):
    if regional_code in ['R03', 'R12']:
        if 0 <= value <= 0.375:
            return "Low"
        elif 0.375 < value <= 0.625:
            return "Minor"
        elif 0.625 < value <= 0.975:
            return "Major"
        elif 0.975 < value <= 1:
            return "Critical"
        else:
            return "Undefined"
    else:
        if 0 <= value <= 0.25:
            return "Low"
        elif 0.25 < value <= 0.5:
            return "Minor"
        elif 0.5 < value <= 0.975:
            return "Major"
        elif 0.975 < value <= 1:
            return "Critical"
        else:
            return "Undefined"

def get_severity(merged_df):
    # Use your functions here
    calculate_score(merged_df, 'rev', 'revenue_hourly', 'Revenue Hourly', 0.4)
    calculate_score(merged_df, 'subs', 'subscriber_4g_hourly', 'Subscriber 4G Hourly', 0.55)
    calculate_score(merged_df, 'site', 'site_id', 'Site ID Uniq Down', 0.05)

    # Calculate the final score
    merged_df['final_score'] = merged_df['rev_score'] + merged_df['subs_score'] + merged_df['site_score']

    # Apply severity category to final_score and add 'Severity' column to the dataframe
    merged_df['Severity'] = merged_df.apply(lambda row: get_severity_category(row['final_score'], row['No. Regional']), axis=1)

    # Drop unnecessary columns from the merged dataframe
    hasil = merged_df.drop(columns=['No. Regional', 'Regional Name', 'Revenue Hourly', 'Subscriber 4G Hourly', 'Ticket Number','Site ID Uniq Down'])
    
    return hasil