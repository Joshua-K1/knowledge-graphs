FROM neo4j:4.4.0 AS builderNeo

WORKDIR /app

COPY . /app

COPY requirements.txt requirements.txt

RUN apt update 

RUN apt-get install python3 -y

RUN apt-get install python3-pip -y

RUN pip install --trusted-host=pypi.org --trusted-host=files.pythonhosted.org --user json-repair

EXPOSE 7474
