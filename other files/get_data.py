import pypixoto

# Create main Pixoto object with Username of user whose you want to get data
obj = pypixoto.Pixoto('davesansomga')

# full_name = obj.full_name() # full name of user

# about = obj.about() # bio of user

# location_country = obj.location('country') # country of user
# location_region = obj.location('region') # region of user
# location_locality = obj.location('locality') # locality of user
 
# n_awards = obj.n_awards() # number of awards

# n_points = obj.n_points() # number of points

# n_images = obj.n_images() # number of images posted

# n_followers = obj.n_followers() # number of followers 

# n_following = obj.n_following() # number of following users 

img_info = obj.get_images_info(2, ['title', 'description', 'category', 'subcategory', 'tags', 'date_published', 'date_taken', 'image_url', 'data_url', 'wins', 'losses', 'completed_duels', 'rating', 'cam_company', 'cam_model', 'focal_length', 'shutter_speed', 'aperture', 'iso_film', 'width', 'height']) # getting recent 3 images title and description

print img_info