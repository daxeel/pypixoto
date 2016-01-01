# pypixoto
Python SDK for accessing data of Pixoto.com

# What is Pixoto.com?
Pixoto.com is an online world famous photo sharing social network for photographers similar to 500px.com, flickr etc. Check out its site for more information.

# Why this project (pypixoto)?
I have searched for official API or SDK for pixoto.com but not found anything from where i can access the user's information from pixot.com. That is why i decided to make one. And here it is - Python SDK for accessing user's data from pixoto.com.

# Installation
## Installation of dependency
pypixoto is using beautifulsoup4. So, before installing pypixoto you need to install beautifulsoup.<br>
<code>pip install beautifulsoup4</code>
## Installation of pypixoto
##### Install using pip
<code>pip install pypixoto</code>
##### Install using setup.py
STEP 1 : Clone this repository<br>
<code>git clone https://github.com/daxeel/pypixoto.git</code><br><br>
STEP 2 : Change working directory<br>
<code>cd pypixoto</code><br><br>
STEP 3 : Install pypixoto using setip.py<br>
<code>python setup.py install</code>

# Documentation
Now you are ready to work with pypixoto.
### Getting the user's information
##### Initialize pypixoto with targeted username
<code>obj = pypixoto.Pixoto('USERNAME')</code>
##### Now, let's get the full name of this user
<code>obj.full_name()</code>
##### Biography of user
<code>obj.about()</code>
##### Location of user
<p>User's country</p>
<code>obj.location('country')</code>
<p>User's region</p>
<code>obj.location('region')</code>
<p>User's locality</p>
<code>obj.location('locality')</code>
##### Number of awards awarded to user
<code>obj.n_awards()</code>
##### Number of points collected by user
<code>obj.n_points()</code>
##### Number of images posted by user
<code>obj.n_images()</code>
##### Number of followers
<code>obj.n_followers()</code>
##### Number of following
<code>obj.n_following()</code>

### Getting the information of user's published photos
##### Syntax
<code>obj.get_images_info(N, LIST)</code><br><br>
Here, N = Information of how much images you want to get <br>
LIST = List of required information <br><br>
You can pass the following items to LIST 
<table>
	<tr>
		<td>title</td>
		<td>get the title of image</td>
	</tr>
	<tr>
		<td>description</td>
		<td>get the description of image</td>
	</tr>
	<tr>
		<td>category</td>
		<td>get the category in which the image is published</td>
	</tr>
	<tr>
		<td>subcategory</td>
		<td>get the subcategory of image</td>
	</tr>
	<tr>
		<td>tags</td>
		<td>get the tags</td>
	</tr>
	<tr>
		<td>date_published</td>
		<td>get the date of image published</td>
	</tr>
	<tr>
		<td>date_taken</td>
		<td>get the date of image taken</td>
	</tr>
	<tr>
		<td>image_url</td>
		<td>get direct image link</td>
	</tr>
	<tr>
		<td>data_url</td>
		<td>get the link to pixoto page of that image</td>
	</tr>
	<tr>
		<td>wins</td>
		<td>get total wins of image</td>
	</tr>
	<tr>
		<td>losses</td>
		<td>get total losses of image</td>
	</tr>
	<tr>
		<td>completed_duels</td>
		<td>get the number of duels completed</td>
	</tr>
	<tr>
		<td>rating</td>
		<td>get the ratings of image</td>
	</tr>
	<tr>
		<td>cam_company</td>
		<td>get the campany of camera by which the image is taken</td>
	</tr>
	<tr>
		<td>cam_model</td>
		<td>get the camera model by which the image is taken</td>
	</tr>
	<tr>
		<td>focal_length</td>
		<td>get the focal length</td>
	</tr>
	<tr>
		<td>shutter_speed</td>
		<td>get the shutter speed</td>
	</tr>
	<tr>
		<td>aperture</td>
		<td>get the aperture setting</td>
	</tr>
	<tr>
		<td>iso_film</td>
		<td>get the iso</td>
	</tr>
	<tr>
		<td>width</td>
		<td>get width of actual image</td>
	</tr>
	<tr>
		<td>height</td>
		<td>get height of actual image</td>
	</tr>
</table>
