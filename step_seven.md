How is the logged in user being kept track of?
Checking that the session key is the user_id

What is Flask’s g object?
The g object is a temporary storage for anything that needs to interact to create the application. For example, to check for a logged in user.

What is the purpose of add_user_to_g?
`Add_user_to_g` keeps track of the current user that is logged in.

What does @app.before_request mean?
A function that runs before each request. This is useful because we want to load the user from the session before each route, as well as working with the g object.