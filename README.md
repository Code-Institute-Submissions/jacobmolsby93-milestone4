# Fe_ED

The web-application I have created is a reddit style news site, witch lets the users register to the site and post articles on a wall. The users have the ability to interact with each other through liking the posts and commenting of eachothers posts through the article. The aim for the website is simple, it is for the users to engage in whatever content they wish with some guidelines ofcourse.

Users have the ability to create and update there own profiles through the my-profile tab in the navigation bar. where a short description of each user is displayed under the profile image.


![Landing Page](https://github.com/jacobmolsby93/milestone4/blob/main/media/images/readme-images/Sk%C3%A4rmbild%20(35).png?raw=true)

## Features 
The different areas of the site includes: 
<hr>
- The Home Page 
    - A list view of all the articles posted by users. where you have the ability to see an overview of the post. who has posted it and the featured image that is chosen. 

- Add Post
    - In the navigation bar you have link to the page where if you are logged in you can create a post.

- The Detail View
    - When you have navigated through one of the posts from the home page you get the full page of the article, where you can read everything about it. As well as comment and like if you wish to interact with the author or the other users of the page.
'
- Profile page
    - If you like the author and want to know more about them you can do so by checking out there profile page from the detail page by clicking on the image of the author.

- Your Profile page
    - Here as the above, you can see what information you have typed into your own profile page. And edit if you wish to.
 <hr>
### Existing Features

- __Navigation Bar__

  - The Navigation bar is placed in the base.html which is extended through all of the other html pages on the website. When you are logged in the website, you have the options to add a post, view your profile or log out. As well as a standard home button. 
  If you're not a member of the sight or simply just not logged in you have the option to either sign up or to login. 
  - This section of the page is good for the user, becuase you can see if you're logged in or not. As well as to easily navigate through the page with the search bar.


- __The landing page__

  - The landing page on my website, is where you can navigate through the different users posts and to create your own. this is the page where you see a list view of the posts that are created.
  - Grabs you with interesting stories that the other members have created.


- __My Profile Section__

  - The profile section is for the user to update his personal information, where the posts of the user is vissible in a list, as well as the drafts created and not posted. 
  - The User will gather an overview of their activity on the page.

![Profile](https://github.com/jacobmolsby93/milestone4/blob/main/media/images/readme-images/Sk%C3%A4rmbild%20(36).png?raw=true)

- __Article Detail Section__

  - Through the home page the user can navigate through the detailed view of the article of their liking, giving them the full story of what that article has to say. And to interact with the other users of the page through the comment section. If the post was interesting enough a like button has been added to give the user a way of expressing how they felt about the article. 


- __The Footer__ 

  - The footer is added just for a "copyright" purpose and to signal that the user has come to the end of the page.

<hr>
### Features Left to Implement
- On the home page i want to implement a way so that you can see the top trending posts aswell as the top trending authors.

- I also want to implement a better search system so you can search for everything not just titles.

-  
<hr>
## Testing 

Testing has been done by me, althou most of the developing of this project has been to trying to figure out how django works. I had created multiple users to check that they all connect to the database and that the right information is shown on the right places. The urls has been tested back and fort to ensure that everything works, the good thing about django is that when something is really wrong it lets you know that it is. 
Again on this project ive had my brother as an outsider come and look at the application and tell me whwat he thinks, about the parts that work. the parts that dont work is something i will have study more. 

### Validator Testing 

- HTML
  - Errors return only for django input [W3C validator](https://github.com/jacobmolsby93/milestone4/blob/main/media/images/readme-images/Sk%C3%A4rmbild%20(42).png?raw=true)
- CSS
  - No errors were found when passing through the official [(Jigsaw) validator](https://github.com/jacobmolsby93/milestone4/blob/main/media/images/readme-images/css-validator.png?raw=true)

### Unfixed Bugs
There will be a few unfixed bugs, becase I couldnt complete the project in time for the deadline. This has been really hard to grasp and to understand fully. Im not expecting a pass on this subject and would happyily redo it as soon as possible.
Nevertheless I'l list all the bugs here.

- Profile page is not complete. i could not get the posts from the user and showed on a list view. under the bio description.
- The website is not made to a responsive design to this point. I was focusing on getting the django logic to work.


## Deployment
The web application is deployed using heroku.

- The site was deployed to GitHub pages. The steps to deploy are as follows: 
  - In the GitHub repository, navigate to the Settings tab 
  - From the source section drop-down menu, select the Master Branch
  - Once the master branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment. 

The live link can be found here - https://milestone-news-4.herokuapp.com/

## Credits 
- Code institute for the list view and detail view. And parts of the model in Articles.
- Aneeq on fiverr for beeing an instructor for me for a few hours.
- Markus winker Photo from unsplash.com
- used stackflow for the slugify instance

### Content 
- Instructions for getting the slugify_instance_title was taken from [https://www.codingforentrepreneurs.com/blog/a-unique-slug-generator-for-django/]
- The image on the homepage is taken from [https://unsplash.com/photos/k_Am9hKISLM]
- The post_detail view, comment and like function was taken from [https://learn.codeinstitute.net/]
- Instructor for django who helped me solve some problems with Member model and User model auth [https://github.com/aneeqakbar]
  - Aswell as the LoginView and SignupView, which he guided me through to help me understand what i was doing.
- Bootstrap was used for layout of the pages.

### Media

- The image on the homepage is taken from [https://unsplash.com/photos/k_Am9hKISLM]



