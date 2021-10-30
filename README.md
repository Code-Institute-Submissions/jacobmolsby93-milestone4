# Fe_ED

The web-application I have created is a reddit style news site, witch lets the users register to the site and post articles on a wall. The users have the ability to interact with each other through liking the posts and commenting of eachothers posts through the article. The aim for the website is simple, it is for the users to engage in whatever content they wish with some guidelines ofcourse.

Users have the ability to create and update there own profiles through the my-profile tab in the navigation bar. where a short description of each user is displayed under the profile image.


![Responsice Mockup](https://github.com/lucyrush/readme-template/blob/master/media/love_running_mockup.png)##GLÖM EJ

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

![Nav Bar](https://github.com/lucyrush/readme-template/blob/master/media/love_running_nav.png) ### GLÖM EJ #### 

- __The landing page__

  - The landing page on my website, is where you can navigate through the different users posts and to create your own. this is the page where you see a list view of the posts that are created.
  - Grabs you with interesting stories that the other members have created.

![Landing Page](https://github.com/lucyrush/readme-template/blob/master/media/love_running_landing.png) ### GLÖM EJ ####

- __My Profile Section__

  - The profile section is for the user to update his personal information, where the posts of the user is vissible in a list, as well as the drafts created and not posted. 
  - The User will gather an overview of their activity on the page.

![Club Ethos](https://github.com/lucyrush/readme-template/blob/master/media/love_running_ethos.png) ### GLÖM EJ ####

- __Article Detail Section__

  - Through the home page the user can navigate through the detailed view of the article of their liking, giving them the full story of what that article has to say. And to interact with the other users of the page through the comment section. If the post was interesting enough a like button has been added to give the user a way of expressing how they felt about the article. 

![Meetup Times](https://github.com/lucyrush/readme-template/blob/master/media/love_running_times.png) ### GLÖM EJ ####

- __The Footer__ 

  - The footer is added just for a "copyright" purpose and to signal that the user has come to the end of the page.

![Footer](https://github.com/lucyrush/readme-template/blob/master/media/love_running_footer.png) ### GLÖM EJ ####

### Features Left to Implement
- On the home page i want to implement a way so that you can see the top trending posts aswell as the top trending authors.

- I also want to implement a better search system so you can search for everything not just titles.

- more ? 

## Testing 

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your project’s features and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.


### Validator Testing 

- HTML
  - No errors were returned when passing through the official [W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcode-institute-org.github.io%2Flove-running-2.0%2Findex.html)
- CSS
  - No errors were found when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fvalidator.w3.org%2Fnu%2F%3Fdoc%3Dhttps%253A%252F%252Fcode-institute-org.github.io%252Flove-running-2.0%252Findex.html&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en#css)

### Unfixed Bugs
There will be a few unfixed bugs, becase I couldnt complete the project in time for the deadline. This has been really hard to grasp and to understand fully. Im not expecting a pass on this subject and would happyily redo it as soon as possible.
Nevertheless I'l list all the bugs here.
- Edit profile at this moment in time does not work. Cant post it or make the information stick to the database.
- Profile page is not complete. i could not get the posts from the user and showed on a list view. under the bio description.
- There are issues with the login function which i couldnt solve. Allauth seems more suitable for social authentication.
- The website is not made to a responsive design to this point. I was focusing on getting the django logic to work.

I know this will result in a fail. im aware of that.

## Deployment
The web application is deployed using heroku.

- The site was deployed to GitHub pages. The steps to deploy are as follows: 
  - In the GitHub repository, navigate to the Settings tab 
  - From the source section drop-down menu, select the Master Branch
  - Once the master branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment. 

The live link can be found here - https://code-institute-org.github.io/love-running-2.0/index.html 


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
- Bootstrap was used for layout of the pages.

### Media

- The image on the homepage is taken from [https://unsplash.com/photos/k_Am9hKISLM]

Congratulations on completing your Readme, you have made another big stride in the direction of being a developer! 

## Other General Project Advice

Below you will find a couple of extra tips that may be helpful when completing your project. Remember that each of these projects will become part of your final portfolio so it’s important to allow enough time to showcase your best work! 

- One of the most basic elements of keeping a healthy commit history is with the commit message. When getting started with your project, read through [this article](https://chris.beams.io/posts/git-commit/) by Chris Beams on How to Write  a Git Commit Message 
  - Make sure to keep the messages in the imperative mood 

- When naming the files in your project directory, make sure to consider meaningful naming of files, point to specific names and sections of content.
  - For example, instead of naming an image used ‘image1.png’ consider naming it ‘landing_page_img.png’. This will ensure that there are clear file paths kept. 

- Do some extra research on good and bad coding practices, there are a handful of useful articles to read, consider reviewing the following list when getting started:
  - [Writing Your Best Code](https://learn.shayhowe.com/html-css/writing-your-best-code/)
  - [HTML & CSS Coding Best Practices](https://medium.com/@inceptiondj.info/html-css-coding-best-practice-fadb9870a00f)
  - [Google HTML/CSS Style Guide](https://google.github.io/styleguide/htmlcssguide.html#General)

Getting started with your Portfolio Projects can be daunting, planning your project can make it a lot easier to tackle, take small steps to reach the final outcome and enjoy the process! 
