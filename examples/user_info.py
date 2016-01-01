import pypixoto # importing module

obj = pypixoto.Pixoto('borisfrkovic') # initializing Pixoto with username

name = obj.full_name() # getting full name
bio = obj.about() # getting biography

country = obj.location('country') # getting country
region = obj.location('region') # getting region
locality = obj.location('locality') # getting locality