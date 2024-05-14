data_inputs = {
    'data sources': ['Penn World Table'],
    'Penn World Table': {
        'path': './data/raw_data/pwt1001.xlsx',
        'file_type': 'excel',
        'sheet_name': 'Data',
        'variables': {
            'countrycode': 'ISO code',
            'country': 'Country Name',
            'year': 'year',
            'statcap': 'Statistical Capacity Indicator',
            'pop': 'Population (millions)',
            'hc': 'Human Capital Index',
            'emp': 'Number of People Engaged (millions)',
            'avh': 'Average Annual Hours Worked by Person Engaged',
            'cgdpo': 'Output-Side Real GDP at Current PPPs (Mill. 2017US$)',
            'csh_c': 'Household Consumption',
            'csh_i': 'Capital Formation',
            'csh_g': 'Government Consumption',
            'csh_x': 'Merchandise Exports',
            'csh_m': 'Merchandise Imports',
            'csh_r': 'Residual Trade and GDP Statistical Discrepancy',
            'cn': 'Capital Stock at Current PPPs (Mill. 2017US$)',
            'ck': 'Capital Services at Current PPPs (USA=1)',
            'ctfp': 'TFP level at Current PPPs (USA=1)',
            'cwtfp': 'Welfare-Relevant TFP levels at Current PPPs (USA=1)'
        }
    }
}