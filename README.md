# proj_site
Quick demo DRF project by Matt Needham 2022. In this project I use Python, Django, Django REST Framework, PostgreSQL, Docker, and AWS Elastic Beanstalk.

The API is available online at http://drf-proj-dev.us-east-2.elasticbeanstalk.com/

The API serves a database of NFL teams and players.
Authenticated users can create/edit subscriptions to a particular team or player. Potential use cases include:
1) A frontend app that consumes the API to display data for favorite teams/players for a user
2) A backend service that sends push notifications, emails, etc. to users when data is updated for a team/player they are subscribed to