This is a blogsite I made to showcase some of my projects. A hosted version is available at http://luis.bobet.co.uk

To deploy this, simply ensure this repo is available at your home directory and run:
```
deploy.bash
```

The site is served at localhost. If you want to create any posts you will need to create a superuser via manage.py and then login via the admin page.


Note that if you want to properly deploy this you need to change the following for security and other reasons:
- SECRET_KEY
- ALLOWED_HOSTS
- mySql credentials
- NGINX template
