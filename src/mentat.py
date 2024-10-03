import threading
from engine.scheduler import ApplicationQueue, create_worker_threads, stop_all_workers, wait_until_workers_complete
from dotenv import load_dotenv
from prompts import KnowledgeExtractionPrompt, AddKnowledgePrompt
from langchain.chains import LLMChain
from langchain_openai import AzureChatOpenAI
from data_factory import import_data, Application, ret_name_desc

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

    # create a list of knowledge prompts
    apps_akp_list = []
    for app in applications:
        apps_akp_list.append(AddKnowledgePrompt(app.name, app.description))

    # Application request queue
    app_q = ApplicationQueue()

    # add application tasks to the queue
    for akp in apps_akp_list:
        app_q.add_application_task(akp.prompt)

    # create worker threads
    workers = create_worker_threads(3, app_q)

    # wait until all tasks are done
    app_q.wait_until_done()

    # stop workers
    stop_all_workers(workers)

    # wait until all workers are done
    wait_until_workers_complete(workers)





        





    



    









    


#     kep = KnowledgeExtractionPrompt()

#      # configure llm using azure openai service
#     llm = AzureChatOpenAI(
#         azure_endpoint=os.getenv("OPENAI_API_EP"),
#         deployment_name=os.getenv("DEPLOYMENT_NAME"),
#         temperature=0.5,
#         openai_api_key=os.getenv("OPENAI_API_KEY"),
#         openai_api_version=os.getenv("OPENAI_API_VER"),
#     )

#     chain = LLMChain(llm=llm, prompt=kep.prompt)
   
#     text = """
#     Marie Curie, born in 1867, was a Polish and naturalised-French physicist and chemist who conducted pioneering research on radioactivity.
#     She was the first woman to win a Nobel Prize, the first person to win a Nobel Prize twice, and the only person to win a Nobel Prize in two scientific fields.
#     Her husband, Pierre Curie, was a co-winner of her first Nobel Prize, making them the first-ever married couple to win the Nobel Prize and launching the Curie family legacy of five Nobel Prizes.
#     She was, in 1906, the first woman to become a professor at the University of Paris.
#     """


#     triples = chain.invoke(
#         {'text' : text}
#     ).get('text')

#     print(parse_triples(triples))


# def parse_triples(response, delimiter=KG_TRIPLE_DELIMITER):
#     if not response:
#         return []
#     return response.split(delimiter)



if __name__ == "__main__":
    main()