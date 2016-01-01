import pypixoto # importing module

obj = pypixoto.Pixoto('borisfrkovic') # initializing Pixoto with username

awards = obj.n_awards() # getting number of awards user got
points = obj.n_points() # getting number of awards user got
images = obj.n_images() # getting number of images user published

followers = obj.n_followers() # getting number of followers user has
following = obj.n_following() # getting number of following users
