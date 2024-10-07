from pydantic import BaseModel
from typing import List, Optional
import json

class ApplicationStakeholder(BaseModel):
    name: str
    contact_type: str
    business_unit: str
    department: str
    number: int
    email: str
    position: str


class ApplicationBusCapModel(BaseModel):
    capability_model: str
    front_office: bool
    middle_office: bool
    back_office: bool
    it_for_it: bool
    enterprise: bool
    not_mapped: bool


class BusinessDetails(BaseModel):
    business_owner: str
    business_purpose: str
    buisiness_criticality: str
    business_impact: str


class ApplicationMeta(BaseModel):
    number_of_users: int
    release_frequency: str
    work_hours_standard: str
    planned_regular_downtime: str
    documentation: str

class ApplicationOperation(BaseModel):
    high_availability: bool
    disaster_recovery: bool
    rto: str
    rpo: str


class ApplicationOverview(BaseModel):
    app_name: str
    app_desc_full: str
    app_desc_one_liner: str
    app_type: str
    app_age: str
    app_version: str
    app_age: str
    app_runtime_lang: str
    app_complexity: str
    app_support: str
    app_env: str
    app_exists: bool
    other_runtime_lang: str
    business_details: BusinessDetails
    application_meta: ApplicationMeta

class Interfaces(BaseModel):
    source_app: str
    target_app: str
    direction: str
    frequency: str
    mechanism: str
    trigger: str
    bandwidth: str
    protcol: str
    other_system_owner: str


class NetworkInformation(BaseModel):
    environment: str
    hostname: str
    network_name: str
    network_range: str
    subnet: str
    ip_address: str 


class ServerInformation(BaseModel):
    environment: str
    hostname: str
    role: str
    platform_type: str
    shared_or_dedicated: str
    os: str
    os_features: str
    cpu: str
    ram: str
    os_disk_gb: int
    data_disk_count: int
    shared_data_store: str


class Application(BaseModel):
    app_name: str
    app_overview: ApplicationOverview
    #app_stakeholders: List[ApplicationStakeholder]
    #app_bus_cap_model: ApplicationBusCapModel
    #app_operation: ApplicationOperation
    #network_information: List[NetworkInformation]
    #server_information: List[ServerInformation]
    #interfaces: List[Interfaces]


class ProjectCreate(BaseModel):
    project_name: str


# returns pydantic json schema for application
def get_application_schema():
    app_schema = Application.schema()
    return json.dumps(app_schema, indent=4)


# returns pydantic json schema for project_create
def get_project_create_schema():
    project_create_schema = ProjectCreate.schema()
    return json.dumps(project_create_schema, indent=4)

