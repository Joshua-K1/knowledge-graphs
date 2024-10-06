from engine.scheduler import ApplicationQueue, create_worker_threads, stop_all_workers, Task
from dotenv import load_dotenv
from prompts import KnowledgeExtractionPrompt, AddKnowledgePrompt
from data_factory import import_data, Application, ret_name_desc

import random

# load environment variables
load_dotenv()

KG_TRIPLE_DELIMITER = "<|>"

from langchain_community.graphs import Neo4jGraph
from langchain_experimental.graph_transformers import LLMGraphTransformer
from langchain_core.documents import Document
from langchain_openai import AzureChatOpenAI


def main():
    # import raw data
    df_x = import_data()

    # extract name and description columns
    df_y = ret_name_desc(df_x)

    # create a list of applications
    applications = []
    for index, row in df_y.iterrows():
        applications.append(Application(row['Name'], row['Application Description']))

    # create a list of tasks
    tasks = []

    # create type of prompt to send || AddKnowledgePrompt() or KnowledgeExtractionPrompt()
    akp = AddKnowledgePrompt()

    for i, app in enumerate(applications):
        tasks.append(Task(i, app))

    # Application request queue
    app_q = ApplicationQueue()

    # add application tasks to the queue
    for task in tasks:
        app_q.add_application_task(task)

    # create worker threads
    workers = create_worker_threads(3, app_q)

    # wait until all tasks are done
    app_q.wait_until_done()

    # stop workers
    stop_all_workers(workers)


if __name__ == "__main__":
    main()