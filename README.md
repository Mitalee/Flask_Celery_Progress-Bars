I wasn't able to find a single resource for hosting a small Async task queue MVP, so I pulled Miguel Grinberg's Tutorial on Flask with Celery and deployed the same with redis on a single free tier dyno on Heroku.

Note: heroku requires credit card verification for allowing the Heroku Redis add-on to be configured on the free dyno.

Modify the Procfile accordingly and make sure the celery worker is switched on in the 'Resources' Tab on the Heroku dashboard.

For the Heroku environment, the redis URL can be found from this documentation: https://devcenter.heroku.com/articles/heroku-redis#provisioning-the-add-on

Add the redis URL to the staging or the Production Environment in config.py.
