<a href="https://pypi.python.org/pypi/pypixoto/1.0"><img src="https://img.shields.io/pypi/v/pypixoto.svg" alt="PyPI version" height="22"></a>
<a href="https://pypi.python.org/pypi/pypixoto/1.0"><img src="https://img.shields.io/pypi/dm/pypixoto.svg" alt="PyPI downloads" height="22"></a>
<a href="https://pypi.python.org/pypi/pypixoto/1.0"><img src="https://img.shields.io/pypi/format/pypixoto.svg" alt="Format : Source" height="22"></a>

# pypixoto
Python SDK for accessing data of Pixoto.com

# What is Pixoto.com?
<img src="https://datafox-data.s3.amazonaws.com/images/cb_9262edc8f8b67bc66e2bad8bfa60dd4a.png" height="150"><br>
Pixoto.com is an online world famous photo sharing social network for photographers similar to 500px.com, flickr etc. Check out its site for more information.

# Why this project (pypixoto)?
I have searched for official API or SDK for pixoto.com but not found anything from where i can access the user's information from pixot.com. That is why i decided to make one. And here it is - Python SDK for accessing user's data from pixoto.com.

# Installation
## Installation of dependency
pypixoto is using beautifulsoup4. So, before installing pypixoto you need to install beautifulsoup.<br>
```sh
pip install beautifulsoup4
```
## Installation of pypixoto
##### Install using pip
```sh
pip install pypixoto
```
##### Install using setup.py
STEP 1 : Clone this repository<br>
```sh
git clone https://github.com/daxeel/pypixoto.git
```
STEP 2 : Change working directory<br>
```sh
cd pypixoto
```
STEP 3 : Install pypixoto using setip.py<br>
```sh
python setup.py install
```

# Documentation
Now you are ready to work with pypixoto.
### Getting the user's information
##### Initialize pypixoto with targeted username
```py
>>> obj = pypixoto.Pixoto('USERNAME')
```
##### Now, let's get the full name of this user
```py
>>> pyobj.full_name()
```
##### Biography of user
```py
>>> pyobj.about()
```
##### Location of user
<p>User's country</p>
```py
>>> pyobj.location('country')
```
<p>User's region</p>
```py
>>> pyobj.location('region')
```
<p>User's locality</p>
```py
>>> pyobj.location('locality')
```
##### Number of awards awarded to user
```py
>>> pyobj.n_awards()
```
##### Number of points collected by user
```py
>>> pyobj.n_points()
```
##### Number of images posted by user
```py
>>> pyobj.n_images()
```
##### Number of followers
```py
>>> pyobj.n_followers()
```
##### Number of following
```py
>>> pyobj.n_following()
```

### Getting the information of user's published photos
##### Syntax
```py
>>> obj.get_images_info(N, LIST)
```
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

##### Example 1
```py
>>> img_info = obj.get_images_info(3, ['title', 'description'])
>>> print img_info
[{
	'description': 'None',
	'title': 'The Path'
}, {
	'description': 'None',
	'title': 'Dawn in Simpsonville'
}, {
	'description': 'None',
	'title': 'The Point'
}]
```
##### Example 2
```py
>>> img_info = obj.get_images_info(3, ['title', 'description', 'category', 'subcategory', 'tags', 'date_published', 'date_taken', 'image_url', 'data_url', 'wins', 'losses', 'completed_duels', 'rating', 'cam_company', 'cam_model', 'focal_length', 'shutter_speed', 'aperture', 'iso_film', 'width', 'height'])
>>> print img_info
[{
	'category': 'Landscapes',
	'rating': '609.769545742',
	'data_url': 'http://www.pixoto.com/images-photography/landscapes/forests/the-path-5681033682354176',
	'losses': '49',
	'subcategory': 'Forests',
	'date_taken': 'January 8, 2014',
	'tags': "[u'dave sansom', u'maui', u'beautiful skies', u'hana', u'photographs', u'landscape', u'rainforest']",
	'completed_duels': '106',
	'wins': '57',
	'title': 'The Path',
	'cam_model': 'NIKON D810',
	'height': '7360',
	'date_published': 'January 1, 2016',
	'image_url': 'http://lh3.googleusercontent.com/ZEs-B-J5nnzuBcEmWHorYvoznP_JZv8hleL6kI5wAaKw6pQedJxtC1oTtN7tTLu0_I1fDaE2_gQSHoVUUTCkYrU',
	'focal_length': '48.0 mm',
	'cam_company': 'Nikon',
	'iso_film': '500',
	'aperture': 'F7.1',
	'shutter_speed': '1/13 sec',
	'width': '4912',
	'description': 'None'
}, {
	'category': 'Landscapes',
	'rating': '578.684773858',
	'data_url': 'http://www.pixoto.com/images-photography/landscapes/sunsets-and-sunrises/dawn-in-simpsonville-4528745496444928',
	'losses': '41',
	'subcategory': 'Sunsets & Sunrises',
	'date_taken': 'October 8, 2015',
	'tags': "[u'dave sansom', u'golf course', u'dawn', u'beautiful skies', u'sunset', u'golf club', u'louisville', u'university of louisville', u'sunrise', u'morning', u'landscape', u'kentucky']",
	'completed_duels': '100',
	'wins': '59',
	'title': 'Dawn in Simpsonville',
	'cam_model': 'NIKON D810',
	'height': '4912',
	'date_published': 'December 31, 2015',
	'image_url': 'http://lh3.googleusercontent.com/Wx2bOEL7QHj095fth8R30g11jaqezDhV6z4rv_GdfthYzGMad7jNagmdxkxD05r6S44hcetUjaYAjYPsPOvFczWr',
	'focal_length': '31.0 mm',
	'cam_company': 'Nikon',
	'iso_film': '640',
	'aperture': 'F9',
	'shutter_speed': '1/60 sec',
	'width': '7360',
	'description': 'None'
}, {
	'category': 'Landscapes',
	'rating': '509.132686773',
	'data_url': 'http://www.pixoto.com/images-photography/landscapes/sunsets-and-sunrises/the-point-5043316938244096',
	'losses': '48',
	'subcategory': 'Sunsets & Sunrises',
	'date_taken': 'November 17, 2015',
	'tags': "[u'dave sansom', u'maui', u'golf course photographs', u'kapalua', u'beautiful skies', u'landscape']",
	'completed_duels': '100',
	'wins': '52',
	'title': 'The Point',
	'cam_model': 'NIKON D810',
	'height': '7360',
	'date_published': 'December 30, 2015',
	'image_url': 'http://lh3.googleusercontent.com/EyqJ3cHtsQg36G-i2bnzL5Tx-5Md6wMa6Wa_W27K4PoZwDa6yOLOh17sJChDpOUGhAHdQqnhtomW_4S_Dv13JA',
	'focal_length': '18.0 mm',
	'cam_company': 'Nikon',
	'iso_film': '100',
	'aperture': 'F9',
	'shutter_speed': '1/4 sec',
	'width': '4912',
	'description': 'None'
}]
```
