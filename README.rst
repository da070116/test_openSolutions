Enterest is a simple app based on the Django REST Framework.
It allows to create and manage the orders for entering to the building

Quick start
-----------

1. Add the applications to your INSTALLED_APPS setting like this::

      INSTALLED_APPS = (
          ...
          'enterest.orders',
          'enterest.tokenusers',
      )

2. Include the  URLS in your project urls.py like this::

      url(r'^enterest/', include('enterest.urls')),

3. Run `python manage.py migrate` to create the enterest models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/users/auth/login/ to log in.