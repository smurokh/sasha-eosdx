import numpy as np
from xrdanalysis.data_processing.download import get_df, RequestDB
##git checkout download_progress_bar
req = RequestDB("20ceb544d6b5aebaff4c60dc10c5a2668e99d0617a27b5258ec0163d4dd3a73f", {'measurement_date': '> 2024-03-19', 'study_id': 2}, 'data.zip', "https://api.eosdx.com/api/getmultiple", 'unzipped_path', 'data.json')
df = get_df(req)

