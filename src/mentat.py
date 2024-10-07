from engine.scheduler import (
    ApplicationQueue,
    create_worker_threads,
    stop_all_workers,
    Task,
)
from dotenv import load_dotenv
from prompts import KnowledgeExtractionPrompt, AddKnowledgePrompt
from data_factory import app_data_classes as adc


# load environment variables
load_dotenv()

from langchain_community.graphs import Neo4jGraph
from langchain_experimental.graph_transformers import LLMGraphTransformer
from langchain_core.documents import Document
from langchain_openai import AzureChatOpenAI


def main():

    # test creating an application
    test_app = adc.Application(
        app_name="Test Application",
        app_overview=adc.ApplicationOverview(
            app_name="MyApp",
            app_desc_full="Full description of the application.",
            app_desc_one_liner="One-liner description",
            app_type="Web Application",
            app_age="5 years",
            app_version="1.0.0",
            app_runtime_lang="Python",
            app_complexity="Medium",
            app_support="In-house",
            app_env="Production",
            app_exists=True,
            other_runtime_lang="None",
            business_details=adc.BusinessDetails(
                business_owner="John Doe",
                business_purpose="E-commerce",
                buisiness_criticality="High",
                business_impact="Global",
            ),
            application_meta=adc.ApplicationMeta(
                number_of_users=1000,
                release_frequency="Monthly",
                work_hours_standard="9-5",
                planned_regular_downtime="None",
                documentation="Confluence",
            ),
        ),
    )

    print(test_app.app_overview.app_name)

    # import raw data
    # df_x = import_data()

    # # extract name and description columns
    # df_y = ret_name_desc(df_x)

    # # create a list of applications
    # applications = []
    # for index, row in df_y.iterrows():
    #     applications.append(Application(row['Name'], row['Application Description']))

    # # create a list of tasks
    # tasks = []

    # # create type of prompt to send || AddKnowledgePrompt() or KnowledgeExtractionPrompt()
    # akp = AddKnowledgePrompt()

    # for i, app in enumerate(applications):
    #     tasks.append(Task(i, app))

    # # Application request queue
    # app_q = ApplicationQueue()

    # # add application tasks to the queue
    # for task in tasks:
    #     app_q.add_application_task(task)

    # # create worker threads
    # workers = create_worker_threads(3, app_q)

    # # wait until all tasks are done
    # app_q.wait_until_done()

    # # stop workers
    # stop_all_workers(workers)


if __name__ in {"__main__", "__mp_main__"}:
    main()
