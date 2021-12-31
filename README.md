# cross-etl
Challenge made for the company Cross Commerce.

All code in the dev branch

Run Extract.py -> Transform.py -> Load.py (start server) ->  client_test.py (in another terminal)

Extracts 10000 pages from the API, handling errors in the way.
Orders the data using Quicksort
Load the data in an API (Flask)

Tested using pytest and pytest-mock

TODOS:
-Add a DB connection
-Change the load so that the GET will call Transform, which will call Extract
-Add more Load tests
