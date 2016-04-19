# Booksy

Dependencies:
Flask
Hypothes.is


## index.py

This sets up the basic Flask app. It does so by building three routes (links): one for the index page, one for the comments page, and one for the actual pdf-view itself. For the comments page, it goes through a file containing the list of all usernames, and passes this list to the comments.html jinja2 template.

## templates/pdfview.html

This sets up the pdf viewer using a combination of the pdf.js and hypothes.is libraries. 

## templates/comments.html

This dis