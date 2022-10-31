# My Food Blog PP4

The website I decided to make is a food blog which lets users visiting the site, explore numerous different recipes, while also sharing their own cooking tips and tricks. The goal of the blog site is to give people an easily accessible website to find delicious recipes, and to also give users their own platform to be able to share their love of cooking and baking with the world. This blog is aimed at anybody that has a passion for cooking and wants to discover new recipes or ideas. Also, people who just want to share their own thoughts and opinions on anything food related will feel welcome in this friendly, passionate community.

Users have the ability to register for an account and this will then allow them to like and comment on blog posts as well as giving them the ability to upload their very own posts and recipes. Any blogs uploaded by users will need to be verified and published by the site admin before it becomes live on the website. This is to ensure the content is relevant and that we do not become a platform where offensive or discriminatory views are being spread amongst our community. Comments are free to be posted by any registered users, but they too will be monitored for any remarks that breach our community standards.

(Insert AmIResponsive image here)

## Current Features

### Home Page
(Home Screen Image)

This is the initial page users visiting the site will land on. At the very top is the blog name alongside the navigation links leading to other pages of the website. These links will change depending on what area of the site you are on and whether or not you are signed in with your account. There is the standard login, logout and register for an account buttons. On top of that, there is also a browse categories dropdown list. This makes it quick and easy to find whatever it is that you are interested in reading.

Directly underneath the navigation, there is a intoductory paragraph welcoming visitors to the site along with a brief description of what you can find and do while visiting the blog site.

The rest of the content on this home page are blog posts that have been uploaded by other people. A maximum of four posts are present per page before it is paginated and will have to click next to explore more posts. Each blog is displayed in a card showing a large image, the blog title and a brief introductory text outlining the content incase you wish to open the post and read further. The purpose of the image is to give the reader an insight into what content the blog contains without having to open the post first. Since the majority of posts on the site are recipes, it makes sense to attach an image of the finished dish here. 

Each blog uploaded gets assiged to a category chosen by the author at the time of publication. Also on the card is a link that if clicked, will take you to more posts within the same category as the one you are reading. The purpose of this is to make it as simple as possible to find blogs that you are interested in. The number of likes each post has is also present here. If you want to like a post yourself, you will have to open it fully first and also be a registered user.

If you are the user that uploaded the post, you will see two extra buttons, edit and delete. These are present to make it as simle as possible to make changes or completely delete a blog that you uploaded. Clicking either of these buttons will take you a seperate page where you can make any changes you desire before being redirected back to the homepage. Authentication is present to ensure only the author of the post is the one that has access to this functionality.

Lastly at the bottom of the home page, you will find the footer. I kept this very clean and simple. It contains links to all the relevant social media and standard copyright information.

### Full Blog Post Page
(Blog Post Image)

When a user clicks on a link to open a post fully, they are greeted with a fully formatted, traditonal blog post layout. The blog title is displayed in a large header tag at the top of the page, with further information stating the author and when the post was created/last updated.

The way the blog is laid out in relation to the formatting and inclusion of images is totally up to the person who uploaded it. Most of the blog posts currently uploaded contain pictures at the top of the page as I feel anyone visiting the site will get drawn in more by images along with quality text content that follows it. 

As blogs have to be approved by the admin before publication, this helps to ensure the content being shared is relevant to the sites purpose and that the quality of the posts are up to the standard that the site admin would like. Adding to that, it is a much easier way to monitor posts rather than having to manually scroll through every published blog and pick out any for editing or deletion incase of a error or misuse of the platform.

Directly under the blog content, is a like button and a section containing the comments. Here it once again shows the number of likes the post, but this time also with the ability to like the post yourself. You can click the like button only if you are signed in. If not, there is a comment explaining this and a link that will take you to the 'Register for an account' page.

The same applies as above for the comments section. Any comments the post has received already are displayed here, along with the name of the user and the date it was made. If you are a signed in user, you can click the 'Add comment' button and be taken to the page where you can leave comments.

At the very bottom of the page is one last button, that if clicked will take you back to the homepage. 

### Upload Blog Page
(Upload blog image)

When you are all signed up with an account, the 'Upload Post' page will then become available for you to use! This is the page you will be using to uplaod all of your wonderful recipe ideas. 

The format of the page is a form primarily, composing of the fields you will need to fill in to upload a post. At the very top, is a line of text outlining the steps to fill out the form correctly. The form consists of six fields that are to be filled in. Most of them are self explanatory such as the title, extract and category. One or two of them are a little bit more complicated such as the 'slug' field. This is the url that will be displayed for the post that you create for example /your-first-post/. There is a placeholder telling you to include the - symbol between words so the slug is accepted. The ideal situation would be for this to be automatically generated from the title but unfortunataly, I did not get time to implement this before my submission date.

Underneath the slug field, is the main body of the blog post that you will create. I implemented a text editor called summernote here, so you have more capabilities to format and customise your posts. The editor includes options to change fonts, colours, add pictures and much, much more. Getting this implemented into the form was imperative, to ensure the content being put out is posted with the correct formatting and so its as simple as possible to put together a good-looking blog.

The last field on the form is the ability to attach a picture which will feature as the primary image on the home screen of the website. It is not possible to see an example of how it will look so its quite important that the image you use is the correct size so it is not altered in any way. If it does not come out as expected, theres no need to worry as this can be swapped out easily in the edit page which is described in more detail below.

### Edit Blog Page
(Edit post page)

The edit post page can be accessed either on the home page or at the bottom of the actual blog post when it is opened fully. Only you who wrote the post has access to this page so you don't have to worry about anybody else editing or deleting your blogs.

This page is very similar to the previous 'Upload a Blog' page, with just a few minor differences. The edit page lets you change everything except the slug field. All of the content that you have wrote here previously is present, and you are free to change whatever you like and then click the update button. Any changes will be saved and you will then be redirected to the home page with a freshly updated post.

### Delete Blog Page
(Delete post page)

Very similar to the edit page above, this option is only available to authors of the particular post. Clicking this button redirects you to a seperate delete page, where you then need to confirm your decision by clicking 'Delete post'. This page contains nothing more than a button and a message stating this decision cannot be changed. Once deleted, your post is removed from the database and will consequently disappear from the website.

### Sign In/Out Page

For all the authentication on this blog site, I used the Django AllAuth built in authentication system. This comes with already made html pages for signing in and out. These pages can be accessed and edited which I have the documented steps outlined further on in this read-me.

### Register An Account Page


color scheme

bugs 
- slug field on form 


write how to edit allauth html pages