import pandas as pd


def import_data() -> pd.DataFrame:
    data = pd.read_csv('data/data.csv')
    return data

def ret_name_desc(frame: pd.DataFrame) -> pd.DataFrame:
    data = frame[['Name', 'Application Description']]
    return data


# Individual applications
class Application():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.enhanced_description = None

    def set_enhanced_description(self, enhanced_description):
        self.enhanced_description = enhanced_description


# Application Stakeholders
class ApplicationStakeholder():
    def __init__(self, name, contact_type, business_unit, department, number, email, position):
        self.name = name
        self.contact_type = contact_type
        self.business_unit = business_unit
        self.department = department
        self.number = number
        self.email = email
        self.position = position


# Overview of application with dictionary for details
class ApplicationOverview():
    '''
    Application Overview : app_details dict structure

    {
        'ApplicationName': 'app_name',
        'ApplicationDescription': 'app_desc',
        'ApplicationType: 'app_type',
        'ApplicationVersion': 'app_version',
        'ApplicationRunTimeLang': 'app_runtime_lang',
        'OtherRuntimeLang': 'other_runtime_lang',
        'Documentation': 'documentation'
        'BusinessOwner': 'business_owner'
        'BusinessPurpose': 'business_purpose',
        'NumberOfUsers': 'number_of_users',
        'ReleaseFrequency': 'release_frequency',
        'WorkHoursStandard': 'work_hours_standard',
        'PlannedRegulgarDowntime': 'planned_regular_downtime',
        'Description': 'description',
        'Age': 'age',
        'BusinessCriticality': 'business_criticality',
        'BusinessImpact': 'business_impact',
        'Complexity': 'complexity',
        'ApplicationSupport': 'application_support',
        'Envionment': 'environment',
        'Exists': 'exists',
        'HighlyAvailable': 'highly_available',
        'DisasterRecovery': 'disaster_recovery',
        'RTO': 'rto',
        'RPO': 'rpo',
        'BusinessCapabilityModel': 'business_capability_model',
        'FrontOffice': 'front_office',
        'MiddleOffice': 'middle_office',
        'BackOffice': 'back_office',
        'ITForIT': 'it_for_it',
        'Enterprise': 'enterprise',
        'NotMapped': 'not_mapped',
        'Application Stakeholders': [
            {
                'Name': 'stakeholder_name',
                'Contact Type': 'contact_type',
                'Business Unit': 'business_unit',
                'Department': 'department',
                'Number': 'number',
                'Email': 'email',
                'Position': 'position'
            }
        ]
    }
    '''
    def __init__(self, app_name: str, app_details: dict):
        self.app_name = app_name
        self.app_details = app_details