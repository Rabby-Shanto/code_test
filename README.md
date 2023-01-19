## User Subscription and Payment API

###### Project Structure

```
UserSubscription
#Config files go here
├── config/
│├── settings/
│├── __init__.py
│├── asgi.py
│├── urls.py
│└── wsgi.py
#project app,templates go here
├── UserSubscription/
│├── Company/
│├── Customer/
│├── Payment/
│├── templates/
#others file
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── README.md
├── manage.py
└── requirements.txt
```

##### Execution

> python manage.py --settings=config.settings.local

> docker compose up --build