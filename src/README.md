# Booksy

Dependencies:
Flask
Hypothes.is
pdf.js


## index.py

This sets up the basic Flask app. It does so by building three routes (links): one for the index page, one for the comments page, and one for the actual pdf-view itself. For the comments page, it goes through a file containing the list of all usernames, and passes this list to the comments.html jinja2 template.

## templates/index.html

This displays a very basic front-end to allow the user to add his/her username and then access a sample book and view the comments of other users. 

## templates/pdfview.html

This sets up the pdf viewer using a combination of the pdf.js and hypothes.is libraries. 

## templates/comments.html

This displays the list of users that have commented on some part of the book. It does so by retrieving the data passed by the Flask route and uses a for loop in the jinja2 template to display these usernames as an unordered list, with two radio buttons for upvoting and downvoting users.


## TODO:
* Connect the quality control module with the back-end
* Make the UI a little prettier
* Improve the upvote/downvote system to perhaps be on a different page
