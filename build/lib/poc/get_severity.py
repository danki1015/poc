def calculate_score(dataseverity, column_name, numerator_column, denominator_column, weight):
    dataseverity[f'{column_name}_score'] = (5 ** (dataseverity[numerator_column] / dataseverity[denominator_column])).apply(lambda x: 1 if x > 5 else (x - 1) / 4)
    dataseverity[f'{column_name}_score'] *= weight

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

def get_severity(dataseverity):
    # Use your functions here
    calculate_score(dataseverity, 'rev', 'revenue_hourly', 'Revenue Hourly', 0.4)
    calculate_score(dataseverity, 'subs', 'subscriber_4g_hourly', 'Subscriber 4G Hourly', 0.55)
    calculate_score(dataseverity, 'site', 'site_id', 'Site ID Uniq Down', 0.05)

    # Calculate the final score
    dataseverity['final_score'] = dataseverity['rev_score'] + dataseverity['subs_score'] + dataseverity['site_score']

    # Apply severity category to final_score and add 'Severity' column to the dataframe
    dataseverity['Severity'] = dataseverity.apply(lambda row: get_severity_category(row['final_score'], row['No. Regional']), axis=1)

    # Drop unnecessary columns from the merged dataframe
    hasil = dataseverity.drop(columns=['No. Regional', 'Regional Name', 'Revenue Hourly', 'Subscriber 4G Hourly', 'Ticket Number','Site ID Uniq Down'])
    
    return hasil