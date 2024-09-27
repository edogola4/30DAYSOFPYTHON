##### Building API #####

# In this section, we will cove a RESTful API that uses HTTP request methods to GET, PUT, POST and DELETE data.
# RESTful API is an application program interface (API) that uses HTTP requests to GET, PUT, POST and DELETE data. In the previous sections, we have learned about python, flask and mongoDB. We will use the knowledge we acquire to develop a RESTful API using python flask and mongoDB. Every application which has CRUD(Create, Read, Update, Delete) operation has an API to create data, to get data, to update data or to delete data from database.
#The browser can handle only get request. Therefore, we have to have a tool which can help us to handle all request methods(GET, POST, PUT, DELETE).
#The browser can handle only get request. Therefore, we have to have a tool which can help us to handle all request methods(GET, POST, PUT, DELETE).


''' Examples of API:
               'Countries API: https://restcountries.eu/rest/v2/all'
               'Cats breed API: https://api.thecatapi.com/v1/breeds'''


# Structure of an API
'''An API end point is a URL which can help to retrieve, create, update or delete a resource. The structure looks like this: Example: https://api.twitter.com/1.1/lists/members.json Returns the members of the specified list. Private list members will only be shown if the authenticated user owns the specified list. The name of the company name followed by version followed by the purpose of the API. The methods: HTTP methods & URLs'''

#The API uses the following HTTP methods for object manipulation:
'''
GET        Used for object retrieval
POST       Used for object creation and object actions
PUT        Used for object update
DELETE     Used for object deletion
'''


