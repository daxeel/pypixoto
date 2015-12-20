import pypixoto

# Create main Pixoto object with Username of user whose you want to get data
obj = pixotopy.Pixoto('ron.maxie')


full_name = obj.full_name() # full name of user

about = obj.about() # bio of user

location_country = obj.location('country') # country of user
location_region = obj.location('region') # region of user
location_locality = obj.location('locality') # locality of user
 
n_awards = obj.n_awards() # number of awards

n_points = obj.n_points() # number of points

n_images = obj.n_images() # number of images posted

n_followers = obj.n_followers() # number of followers 

n_following = obj.n_following() # number of following users 
