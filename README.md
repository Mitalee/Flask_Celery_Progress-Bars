
I wasn't able to find a single, all-in-one resource for hosting a small Async task queue implementation (backend worker with frontend progress bar) on Heroku, so I pulled Miguel Grinberg's Tutorial for a Celery based Progress Bar on Flask, and deployed the same with redis on a single free tier dyno on Heroku.

Note: Heroku requires credit card verification for allowing the Heroku Redis add-on to be configured on the free dyno.

Modify the Procfile accordingly and make sure the celery worker is switched on in the 'Resources' Tab on the Heroku dashboard.

For the Heroku environment, the redis URL can be found from [this](https://devcenter.heroku.com/articles/heroku-redis#provisioning-the-add-on) documentation: 

Specifically, the following command will display the redis URL:
```bash
heroku config | grep REDIS
```
Add the redis URL to the staging or the Production Environment in config.py.
