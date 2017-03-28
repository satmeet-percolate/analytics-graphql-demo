from elasticsearch import Elasticsearch


ES_URL = "http://devolate.com:9200/"


def get_campaign(id):
    from .schema import Campaign

    index = "analytics_gql_campaign"
    type_ = "campaign"
    esc = Elasticsearch(hosts=[ES_URL])
    resp = esc.get(index=index, doc_type=type_, id=id)['_source']
    # return Campaign(id=resp['uid'], name=resp['name'], tasks=resp['task'])
    return Campaign(**resp)


def get_task(id):
    from .schema import Task

    index="analytics_gql_task"
    type_="task"
    esc=Elasticsearch(hosts=[ES_URL])
    resp=esc.get(index=index, doc_type=type_, id=id)['_source']
    # return Task(id=resp['uid'], name=resp['name'])
    return Task(**resp)


def get_user(id):
    from .schema import User

    index="analytics_gql_user"
    type_="user"
    esc=Elasticsearch(hosts=[ES_URL])
    resp=esc.get(index=index, doc_type=type_, id=id)['_source']
    return User(**resp)
