# Booksy
Created by Jim Tse, Vatsal Jayaswal, and Sumit Shyamsukha.

## Notes:

Mockup images are courtesy Medium -- the UI will be modeled in a very similar manner.
Flowchart describes how the major components fit in with each other. Readme describes these components.

## Major Components of Booksy

* [Landing Page](#landing-page)
* [User Interface](#user-interface)
* [User Accounts](#user-accounts)
* [Reputation System](#reputation-system)
* [Quality Control](#quality-control)
* [Aggregation](#aggregation)


## Landing Page <a id="landing-page"></a>

The landing page shows the user sign-up and login buttons, along with some promotional content about Booksy. Once the user has logged in or signed up, the user sees the main Booksy dashboard.


** Point Value: 2 **

## User Interface <a id="user-interface"></a>

The user interface consists of several subparts:

### Dashboard

The Booksy dashboard allows the user to search for textbooks to read, and displays their current reading list and their recently-read books list.

Potential additions include a feed to display what their followers are reading, provide book recommendations, and so on.

### Reading Interface

The reading interface displays the actual text of a book, allowing the user to perform inline annotations such as highlighting, strikeout, underline, as well as the added ability to comment on a particular part of the text.

A user can toggle between reading in private mode and public mode -- all annotations made in private mode will only be visible to the user.

### Displaying Annotations

When reading a book in public mode, users will be able to view comments associated with a particular part of the text made by other users. The way this would work is: a user could hover over part of a text, and would have the option of viewing all the annotations associated with that part of the text.

The user will also have the ability to add their own comments in the form of a conversational "thread."

### Account Information and Settings

A user will be able to access their account information: reading list, recently read books, followers, and following.

In addition to account information, users will also be able to edit their account settings.

** Point Value: 3 **

## User Account System <a id="user-accounts"></a>

The user will be able to create an account that stores the information describes above. Users will be able to follow other users.

Each user's account will store information about their annotations: this includes public and private annotations, as well as comments, etc.

Certain users will have a verified status associated with their accounts: this generally includes people who are verified experts on a particular topic i.e people with PhDs, professors, and the like. Verification can be done by designated moderators.

** Point Value: 3 **

## Reputation System <a id="reputation-system"></a>

What does reputation do?

A Booksy user's reputation is a part of their identity on the site. It indicates, to an extent, a user's expertise and knowledge, as well as the amount that other users value a particular user's content.

All users start at with a reputation of unity. This is the minimum reputation value. If a user's reputation sinks below this value, their reputation is automatically reset.

A user gains reputation when:

* one of their comments is upvoted by a regular user: +5 points
* one of their comments is upvoted by a verified user: +10 points
* a downvote on their comments is removed: +2 points
* a comment they downvote is removed: +1 point

A user loses reputation when:

* one of their comments is downvoted by any user: -2 points
* one of their comments is flagged for spam by a verified user: -20 points
* one of their comments is flagged for spam by a critical mass of regular users: -10 points
* one of their verified answers loses its status: -10 points

** Point Value: 3 **

## Quality Control <a id="quality-control"></a>

The reputation system essentially plays the most vital role in quality control.

Quality control for comments will work similarly:

* All comments can be upvoted or downvoted by any user.
* A comment that receives a critical mass of downvotes will be displayed as a highly downvoted comment.
* A comment can also be flagged as spam. Comments flagged as spam will also be displayed so.
* Each comment will have associated with it a score value. This score value will be determined based on a certain statistic: lower bound of Wilson score confidence interval for a Bernoulli parameter. [Credit: http://www.evanmiller.org/how-not-to-sort-by-average-rating.html]

The Quality Control is split between the Aggregator and the Comment classes. The Comment class allows the user to mark a comment as spam, and the Aggregator, while printing comments, takes care of displaying "flagged as spam" for the comments that have been marked as spam.

** Point Value: 4 **

## Aggregation <a id="aggregation"></a>

Comments are displayed based on the following set of rules:
* The top three comments are those that are recommended by the most verified users.
* All other comment threads will be displayed by using a "Display All Comments" button. These comments will be displayed based on the ranking system that is described in the QC module above.
* Comments flagged as spam will be displayed as flagged as spam, but the user will have the ability to still click and view them.

The Aggregator class aggregates all of the comments and displays them with their "score" value. The "score" value is calculated based on the lower bound of the Wilson interval. The Comment class has a "_confidence" helper method to achieve this.

** Point Value: 4 **

