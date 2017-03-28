ES Data:

```
POST analytics_gql_campaign/campaign/campaign:1
{
        "uid": "campaign:1",
            "name": "campaign 1",
                "license_uid": "license:1",
                    "duration_seconds": 86400,
                        "tasks": ["task:1", "task:2"]
}

POST analytics_gql_campaign/campaign/campaign:2
{
        "uid": "campaign:2",
            "name": "campaign 2",
                "license_uid": "license:2",
                    "duration_seconds": 36000,
                        "tasks": []
}


POST analytics_gql_task/task/task:1
{
        "uid": "task:1",
            "name": "task 1",
                "assignee": "user:1"
}

POST analytics_gql_task/task/task:2
{
        "uid": "task:2",
            "name": "task 2",
                "assignee": "user:2"
}

POST analytics_gql_user/user/user:1
{
        "uid": "user:1",
            "name": "User 1"
}

POST analytics_gql_user/user/user:2
{
        "uid": "user:2",
            "name": "User 2"
}
```
