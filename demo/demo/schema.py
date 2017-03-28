import graphene
from graphene import relay, resolve_only_args

from .fetcher import get_campaign, get_task, get_user


class User(graphene.ObjectType):
    '''User '''

    class Meta:
        interfaces = (relay.Node, )

    uid = graphene.String(description='The uid of the user.')
    name = graphene.String(description='The name of the user.')

    @classmethod
    def get_node(cls, id, context, info):
        return get_user(id)


class Task(graphene.ObjectType):
    '''A task '''

    class Meta:
        interfaces = (relay.Node, )

    uid = graphene.String(description='The uid of the task.')
    name = graphene.String(description='The name of the task.')
    assignee = relay.ConnectionField(User, description='The tasks in a campaign.')

    @resolve_only_args
    def resolve_assignee(self, **args):
        # Transform the instance ship_ids into real instances
        return [get_user(self.assignee)]

    @classmethod
    def get_node(cls, id, context, info):
        return get_task(id)


class Campaign(graphene.ObjectType):
    class Meta:
        interfaces = (relay.Node, )

    uid = graphene.String(description='The uid of the campaign.')
    name = graphene.String(description='The name of the campaign.')
    duration_seconds = graphene.Int()
    license_uid = graphene.String()
    tasks = relay.ConnectionField(Task, description='The tasks in a campaign.')

    @resolve_only_args
    def resolve_tasks(self, **args):
        # Transform the instance ship_ids into real instances
        return [get_task(task_id) for task_id in self.tasks]

    @classmethod
    def get_node(cls, id, context, info):
        return get_campaign(id)



class Query(graphene.ObjectType):
    campaign = graphene.Field(Campaign, id=graphene.ID())
    user = graphene.Field(User, id=graphene.ID())
    task = graphene.Field(Task, id=graphene.ID())

    campaigns = graphene.List(Campaign)
    users = graphene.List(User)
    tasks = graphene.List(Task)

    @resolve_only_args
    def resolve_campaign(self, id):
        return get_campaign(id)

    @resolve_only_args
    def resolve_campaigns(self):
        return [get_campaign("campaign:%s" % id) for id in [1, 2]]

    @resolve_only_args
    def resolve_user(self, id):
        return get_user(id)

    @resolve_only_args
    def resolve_users(self):
        return [get_user("user:%s" % id) for id in [1, 2]]

    @resolve_only_args
    def resolve_task(self, id):
        return get_task(id)

    @resolve_only_args
    def resolve_tasks(self):
        return [get_task("task:%s" % id) for id in [1, 2]]

schema = graphene.Schema(query=Query)
