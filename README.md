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
