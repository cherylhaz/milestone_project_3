# ![alt text](./static/images/Recipe_Box.jpg "Recipe Box logo")

The site, Recipe Box, is an easy to use online portal to store your favourite recipes.  Many people, myself included, have numerous cookbooks that
we keep for just one or two recipes along with old handwritten pieces of paper with recipes handed down from other people. Storing this information in our 
kitchens adds to clutter and it can be difficult to find something when you are looking for it.  This site offers a solution to input the recipes you have on hand
and store them for easy access.

Online recipes have seen an explosion of growth the past number of years as bloogers aided by Pinterest and Instagram contine to share recipes 
and many people have begun online collections which are easy to use and find what you are looking for.  The old favourites which are stored on hard copies
can be impossible to integrate into this system as most people don't have their own blog or website where they can share them.  This site aims to solve this problem 
and will enable everyone to store their recipes electronically, saving time, space and frustration.  

## UX

The main goal was an easy to use site to sort and organize random recipes I have around my kitchen.  Having this issue myself, I am sure that it is a common problem with many people.
Often recipes are ripped out of magazines, copied down from friends cookbooks or passed down from generation to generation by scribbling something down on a scrap piece of paper.

*To add a recipe:* 
The link in in the main navigation bar and the form is easy to complete and use.  This saves this recipe in the collection and can be edited or deleted at a later date.
A confirmation screen appears after the recipe is submitted to reassure the user that the recipe has been saved. 

*To make changes to a current recipe:*
When the recipe in located, sometimes input errors are caught at a later date.  When looking at the recipe, an edit button is conviently there to allow for instant changes.

*To find a recipe:*
The main page is the search feature and allows the user to narrow down recipes by category.  These categories are the most common ones, often you are looking for an idea to make for dinner, 
so it makes sense to group all the dinner recipes together.  By clicking on the button, all recipes within that category are listed.

**Database Structure**
The database structure is outlined below and was created with MongoDB.  It was designed for future enhancements to the search functionality and to allow for links to affiliate programmmes.

* recipe_box
  + recipes
    + _id
    + title
    + ingredients
    + method
    + required_tools
    + source
    + cooking_time
    + category
    + sub_category
  + categories
    + _id
    + title
    + image_url
    + slug
  + sub_categories
    + _id
    + title
    + image_url
  + required_tools
    + _id
    + name
    + purchase_url

**MockUp**  
Mockups were completed using Balsamiq Mockups 3 and can be viewed [here](./static/mockups/RecipeSite.pdf")

## Features
In this section, you should go over the different parts of your project, and describe each in a sentence or so.

### Existing Features
**Navigation bar**  
The Navbar is located at the top to easily move around the site and to access all other parts of the site.  The feature is mobile
friendly.  

**[Search by Category Page]()**  
The main page or search page is divided by category and allows the user to easily find the recipes they are looking for broken down by meal.
Typically when searching for recipes you are looking for a dessert to make or something for dinner.  This is the easiest way to divide the recipes for easiest access for the user.
The features left to implement section describes additional search capability that would be added in the future. 

**[Add Recipe]()**  
This page was kept simple and straightforward on purpose so it would appeal to a large number of users.
Only title, ingredients, method, cooking time and category are required fields so that entering a recipe is not overly cumbersome. 

**Confirmation of Added Recipe**  
A page which appears after a recipe is added to reassure the user that the recipe has been saved and added to the database.

**Edit and Delete Recipe**  
Mistakes happen and things change so it is easy to edit a recipe or delete the entire record.  Both of these features are accesssible via the recipe modal which are accessible through the search page.

### Features Left to Implement
Future enhancements would include: 
1.  User log in and personalized experience
2.  Greater search capability, including search by keywords, ingredients, cooking time
3.  Sharing tools so recipes could be shared on Pinterest or other social media sites
4.  Links to sites to purchase required tools or ingredients to support revenue stream for site owner. 

## Technologies Used
**[HTML](https://html.spec.whatwg.org/multipage/)**  
  The basic structure and all pages were created using HTML.

**[CSS](https://www.w3.org/Style/CSS/Overview.en.html)**  
  Design and enhancement of user experience was done with CSS to make it a site that is both easy to read and navigate. 

**[JavaScript](http://www.ecmascript.org/)**  
  Some of the bootstrap elements use JavaScript to function.

**[JQuery](https://jquery.com/)**  
  Some of the bootstrap elements use jQuery to function.

**[Bootstrap](https://getbootstrap.com/)**  
Used for the framework of the site, including the layout, the forms, modals, navbar, footers.

**[MongoDB](https://www.mongodb.com/)**  
Hosts the database for the project. 

**[Canva](https://www.canva.com/)**  
Is a free website and was used for the logo creation. 

## Testing
In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

Contact form:
Go to the "Contact Us" page
Try to submit the empty form and verify that an error message about the required fields appears
Try to submit the form with an invalid email address and verify that a relevant error message appears
Try to submit the form with all inputs valid and verify that a success message appears.
In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Deployment
This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:

Different values for environment variables (Heroku Config Vars)?
Different configuration files?
Separate git branch?
In addition, if it is not obvious, you should also describe how to run your code locally.

## Credits
### Content & Media
Sources of recipes are listed as a database field, all other written content is original work. 

Images used are from [UnSplash](https://unsplash.com/)

### Acknowledgements
1. Design inspiration came from [AWWWARDS](https://www.awwwards.com/sites/outdoor-dreams)

2. Other inspiration came from the project submitted by Nico as shared on LinkedIn
https://github.com/Frozenaught/homechopped

3. Footer code was from [Free Code Camp](https://www.freecodecamp.org/news/how-to-keep-your-footer-where-it-belongs-59c6aa05c59c/)

Special thank you to my mentor Akshat Garg and to Code Institute Support who assisted me in getting through a rough patch on the project.
