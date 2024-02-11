from poc import get_severity, get_level

import pandas as pd

# Your data
# data = {
#     'Ticket ID': ['IM-20240206-00000001', 'IM-20240206-00000002', 'IM-20240206-00000003'],
#     'regional': ['EAST JAVA', 'SUMBAGTENG', 'EAST JAVA'],
#     'Start Time(Create TT_alarm_start_time)': ['2024-02-05 23:44:39', '2024-02-05 23:45:05', '2024-02-05 23:45:40'],
#     'Severity(Create TT_severity)': ['Low', 'Low', 'Low'],
#     'revenue_hourly': [0.178025, 0.043261, 0.042216],
#     'site_id': [3, 1, 1],
#     'subscriber_4g_hourly': [1081.5, 171.5, 193.0],
#     # 'rev_score': [0.068086, 0.005026, 0.013105],
#     # 'subs_score': [0.280944, 0.010824, 0.030209],
#     # 'site_score': [0.050000, 0.003231, 0.008875],
#     # 'final_score': [0.399031, 0.019081, 0.052189],
#     'Severity': ['Minor', 'Low', 'Low']
# }

data = {
    'Ticket ID': [12015, 12016, 12017, 12018, 12019],
    'regional': ['SUMBAGUT', 'BALI NUSRA', 'KALIMANTAN', 'SULAWESI', 'SUMBAGUT'],
    'Start Time(Create TT_alarm_start_time)': ['2024-02-09 13:17:03', '2024-02-09 13:17:02', '2024-02-09 13:02:57', '2024-02-09 13:18:27', '2024-02-09 13:18:01'],
    'Severity(Create TT_severity)': ['Low', 'Minor', 'Minor', 'Low', 'Low'],
    'revenue_hourly': [0.394633, 0.411260, 0.188475, 0.025357, 0.145759],
    'site_id': [2, 1, 1, 1, 1],
    'subscriber_4g_hourly': [715.5, 850.0, 339.0, 99.0, 578.5],
    # 'rev_score': [0.051955, 0.217324, 0.025313, 0.003434, 0.016713],
    # 'subs_score': [0.047853, 0.196040, 0.028538, 0.006875, 0.037552],
    # 'site_score': [0.006192, 0.008875, 0.003846, 0.003231, 0.002786],
    # 'final_score': [0.106001, 0.422239, 0.057697, 0.013541, 0.057050],
    'Severity': ['Low', 'Minor', 'Low', 'Low', 'Low'],
    # 'final_score_crit': [0.0, 0.0, 0.0, 0.0, 0.0],
    # 'Level': ['SPV', 'Manager', 'SPV', 'SPV', 'SPV']
}

# Create DataFrame
df = pd.DataFrame(data)

hasil = get_level(df)
print(hasil)