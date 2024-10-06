import pandas as pd


def import_data() -> pd.DataFrame:
    data = pd.read_csv('data/data.csv')
    return data

def ret_name_desc(frame: pd.DataFrame) -> pd.DataFrame:
    data = frame[['Name', 'Application Description']]
    return data


class Application():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.enhanced_description = None

    def set_enhanced_description(self, enhanced_description):
        self.enhanced_description = enhanced_description

        