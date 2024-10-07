curl -X POST "http://localhost:8000/project/1/add_application" \
     -H "Content-Type: application/json" \
     -d '{
           "app_name": "My Application",
           "app_overview": {
               "app_name": "My Application",
               "app_desc_full": "This is a detailed description of my application.",
               "app_desc_one_liner": "A one-liner description.",
               "app_type": "Web Application",
               "app_age": "3 years",
               "app_version": "1.2.0",
               "app_runtime_lang": "Python",
               "app_complexity": "Medium",
               "app_support": "Internal",
               "app_env": "Production",
               "app_exists": true,
               "other_runtime_lang": "None",
               "business_details": {
                   "business_owner": "John Doe",
                   "business_purpose": "Provide a platform for online shopping.",
                   "buisiness_criticality": "High",
                   "business_impact": "Significant revenue impact if down."
               },
               "application_meta": {
                   "number_of_users": 1000,
                   "release_frequency": "Monthly",
                   "work_hours_standard": "9-5",
                   "planned_regular_downtime": "Sunday evenings",
                   "documentation": "Extensive documentation available."
               }
           }
         }'

