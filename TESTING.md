# Introduction.

Automatedmanual and testing are crucial in ensuring software quality, while manual testing excels in 
exploratory testing, automated testing shines in performance, and load testing.  
the choice between them depands on factors like the timelines, budget, project requirements
and the nature of the application being tested.

The time I had was not enougph to perform an automated testing, so I tested the project manualy and here are the results:

<h2 id="table">Table of contents</h2>

- [Code Validation](#code)
- [Lighthouse](#lighthouse)
- [Responsiveness Testing](#responsive)
- [Browser compatibility Testing](#compatibility)
- [User story Testing](#user)

<hr/>

<h3 id="code">Code Validation</h3>

**HTML**  
The Html code was tested using the [W3C Validator](https://validator.w3.org/).
The Validation was done for each page bei copying the source code using 'Direct Input'.

Below the screenshots for each page:

**Landing page**

![](/static/images/testing/test-landingpage.png)

**Home page**

![](/static/images/testing/test-homepage.png)

**Bookings page**

![](/static/images/testing/test-reservations.png)

**Edit booking page**

![](/static/images/testing/test-edit.png)

**Delete booking page**

![](/static/images/testing/test-delete.png)

**Delete booking page**

![](/static/images/testing/test-delete.png)

**Login page**

![](/static/images/testing/test-login.png)
![](/static/images/testing/test-login2.png)

**Logout page**

![](/static/images/testing/test-logout.png)

**Signup page**

![](/static/images/testing/test-signup.png)



**CSS**

CSS code was tseted using the [W3C CSS Validator Service](https://jigsaw.w3.org/css-validator/)

![](/static/images/testing/test-css.png)

<u>[Back To Top](#table)</u>

**JavaScript**

Js Code was tseted using the [Jshint Tool](https://jshint.com/) and found only one warning about the  
function within foor loop.

![](/static/images/testing/test-js.png)


<u>[Back To Top](#table)</u>

**Python**

Python Code was tested usint the [Code Institute's Python Linter](https://pep8ci.herokuapp.com/)  

Results for all 'Python' files:

**settings.py**

![](/static/images/testing/test-settings.png)

The warnings in the image are related to Django code and was not changed.

**urls.py**

![](/static/images/testing/test-urls.png)

**admin.py**

![](/static/images/testing/test-admin.png)

**booking.urls.py**

![](/static/images/testing/test-booking.urls.png)

**forms.py**

![](/static/images/testing/test-forms.png)

**models.py**

![](/static/images/testing/test-models.png)

**views.py**

![](/static/images/testing/test-views.png)

<u>[Back To Top](#table)</u>

<hr/>

<h3 id="lighthouse">Lighthous Testing</h3>

A Lighthouse testing was done in the local enviroment using Chrome DevTools in incognito mode  
to check the performance, accessibility, best practice and SEO.

**Landing page**
- mobile

  ![](/static/images/testing/light-mobile-landing.png)

- desktop

  ![](/static/images/testing/light-desktop-landing.png)

**Home page**
- mobile

  ![](/static/images/testing/light-mobile-home.png)

- desktop

  ![](/static/images/testing/light-desktop-home.png)

**Bookings list page**
- mobile

  ![](/static/images/testing/light-mobile-bookings.png)

- desktop

  ![](/static/images/testing/light-desktop-bookings.png)

**Edit Bookings page**
- mobile

  ![](/static/images/testing/light-mobile-edit.png)

- desktop

  ![](/static/images/testing/light-desktop-edit.png)

**Make booking page**
- mobile

  ![](/static/images/testing/light-mobile-make.png)

- desktop

  ![](/static/images/testing/light-desktop-make.png)

**Delete booking page**  
When I tested the page that contains a 'modal' I got the next result:
- mobile

  ![](/static/images/testing/light-mobile-delete.png)

- desktop

  ![](/static/images/testing/light-desktop-delete.png)

**Sign in page**
- mobile

  ![](/static/images/testing/light-mobile-signin.png)

- desktop

  ![](/static/images/testing/light-desktop-signin.png)

  **Logout page**
- mobile

  ![](/static/images/testing/light-mobile-logout.png)

- desktop

  ![](/static/images/testing/light-desktop-logout.png)


  **Sign up page**
- mobile

  ![](/static/images/testing/light-mobile-signup.png)

- desktop

  ![](/static/images/testing/light-desktop-signup.png)


<u>[Back To Top](#table)</u>

<hr/>

<h3 id="responsive">Responsiveness Testing</h3>

The site is responsive for mobiles, tablets, labtops and extra screen sizes, it was tested  
manualy using Chrome DevTools and using the [Am I Responsive tool](https://ui.dev/amiresponsive)

iPhone SE:  
![](/static/images/testing/iPhone-SE.png)

Mobile Galaxy-s8:  
![](/static/images/testing/Galaxy-S8.png)

iPad Mini:  
![](/static/images/testing/iPad-Mini.png)

Desktop:  
![](/static/images/testing/desktop.png)

![](/static/images/main.png)

<u>[Back To Top](#table)</u>

<hr/>

<h3 id="compatibility">Browser compatibility Testing</h3>

I tested the site on Chrome, Edge and Firefox and it was working good:

`Chrome`

![](/static/images/testing/chrome.png)

`Edge`

![](/static/images/testing/edge.png)

`Firefox`

![](/static/images/testing/firefox.png)


<u>[Back To Top](#table)</u>

<hr/>

<h3 id="user">User story Testing</h3>

As mentioed in the 'README.md' in Agile Methadology,
The User stories were created in GitHub issues and guided throughout the way for this project,  
these were tested manually to confirm that it passes and achieve the goal for each.

Some of the text test was copied from the [Restaurant Project](https://github.com/Pramilashanmugam/Restaurant)  
but the functionality was tested and validated as the time was critical.

I tested the 'Python' code which was applied to the buttons to check the functionality, usability,  
and data management.

`Navbar`

| Scenario        | Expected           | result  |
| ------------- |:-------------:| -----:|
| click on brand name | should navigate to home page  |Pass- as expected navigates to homepage |
| click on home  | should navigate to home page  |Pass- as expected navigates to homepage | 
| click on register | should navigate to registration page  |Pass- as expected navigates to sign up page|
| click on login  | should navigate to sign in page  |Pass- as expected navigates to sign in page|
| click on logout | should navigate to sign out page  |Pass- as expected navigates to sign out page |

`Social links in Footer`

| Scenario        | Expected           | result  |
| ------------- |:-------------:| -----:|
| click on facebook icon  | should opens facebook site in new tab  |Pass- as expected navigates to a new window and opens facebook |
| click on twitter icon  | should opens twitter site in new tab  |Pass- as expected navigates to a new window and opens twitter |
| click on youtube icon  | should opens youtube site in new tab  |Pass- as expected navigates to a new window and opens youtube |
| click on instagram icon  | should opens instagram site in new tab  |Pass- as expected navigates to a new window and opens instagram |

`Click on Buttons on home page`

| Scenario        | Expected           | result  |
| ------------- |:-------------:| -----:|
| click on 'Book for a meal' button | 1. should navigate to make booking page. 2. should display a form to fill |1. Pass- as expected navigates to make booking page 2. Pass -  as expected a form is shown to fillout |
| click on 'My Bookings' button | 1. should navigate to the list of bookings related to the loggedin user 2. when there is no bookings for that specific user, should show text that there is no bookings |1. Pass- as expected navigates to the list of bookings for the specific user 2. Pass - as expected if user has no bookings it says that 'you have no bookings'|

`Click on Buttons on My Bookings page`

The 'Edit' and 'Delete' buttons are assigned a dynamic data attribute that responds to user interactions  
and apply an action using [Javascript](/static/js/script.js) code and was also tested manually:

| Scenario        | Expected           | result  |
| ------------- |:-------------:| -----:|
| Click on 'Edit booking' button | 1. should navigate to a new page with the selected booking details 2. should be able to change any particular field detail  | 1. Pass- as expected when clicked navigates to new page with the selected booking details  2. Pass - as expected the user is able to change every detail in any field| 
| Click on 'Delete booking' button | should display a modal with a confirm message | Pass- as expected when clicked a modal appears for confirmation|


`Click on Buttons on Modal`

The 'Delete' button on modal also have a dynamic [Javascript](/static/js/script.js) code and  
was tested manually:

| Scenario        | Expected           | result  |
| ------------- |:-------------:| -----:|
| Click on 'Close' button|should do nothing and stays in the same page| Pass - as expected if the button clicked nothing haben and the user is still in the current page|
| Click on 'Delete' button|1. should delete the booking from the list and stays in the same page 2. A successfull message should show to inform the user that the booking is deleted successfully | 1. Pass - as expected if the button clicked the booking is deleted from the list and user is still in the current page 2. Pass - as expected a successfull message of deletion is shown|

` Make booking form`

| Scenario        | Expected           | result  |
| ------------- |:---------------:| -----:|
| name field |1. should accept only alphabets 2. should not allow the user to left blank because its required| 1. Pass - as expected it accepts only alphabets no numbers or spaces allowed 2. Pass - as expected when the field is blank the transaction can't be saved and prompts the user to enter avalid name|
| date field |1. should accept a valid date entry only and displays apropriate message when the entry in not valid 2. should not allow the user to left blank because its required 3. should allow only bookings within one month|  1. Pass - as expected the field accepts only valid date entry and warns if the date is not valid  2. Pass - as expected when the field is blank the transaction can't be saved and prompts the user to enter a valid date 3. Pass - as expected the only dates allowed are in one month and a message is shown when trying to select a date like yesterday and after one month|
| time field |the time field is mandatory and displays a list of the current times|Pass - as expected the field shows a list of times and cann't be lefted |
| email field |1. the field is required and cann't be lefted blank 2. the field has a validation of correct email format | 1. Pass - as expected the field is required and cann't be lefted blank  2. Pass - as expected there is a validation on the field to accept only valid email format|
| notes field |the field is not required and can be blank| Pass - as expected the user can leave the form without notes and the transaction can be saved |


`Click on other Buttons 'Home' 'Back' 'Save' 'Update'`

| Scenario        | Expected           | result  |
| ------------- |:-------------:| -----:|
| click on 'Home' button | should navigate to home page  |Pass- as expected navigates to home page |
| click on 'Back' button | should navigate to previous page  |Pass- as expected navigates to previous page |
| click on 'Save' button | 1. should save the transaction and display a message of successful 2. should take the user back to bookings page |1. Pass- as expected the transaction is saved and the message successful is shown 2. Pass - as expected the page navigates back to bookings page.|
| click on 'Update' button | 1. should update the transaction and display a message of successful update 2. should take the user back to bookings page|1. Pass- as expected the transaction is saved and the message successful update is shown 2. Pass - as expected the page navigates back to bookings page.|

`User Registration`

| Scenario        | Expected           | result  |
| ------------- |:-------------:| -----:|
|username empty| If the username is blank prompts the user to fill the field | Pass - as expected, if the username field is blank, message shows to fill the username field |
| email field is optional| the form will accepted without email address  |Pass - as expected, the form  accepted without email address as it is optional field|
| Password field| 1. password can’t be too similar to  other personal information. 2. password must contain at least 8 characters. 3. password can’t be a commonly used password. 4.  password can’t be entirely numeric.| 1.Pass - as expected, when password entered was similar to the user id, message asking to enter a different password appears. 2. Pass - as expected, characters less than 8 are not expected and prompt the user to enter a minimum 8 characters. 3.Pass - as expected, password like testing0123 is not accepted and advises the user to choose a different password. 4.Pass - as expected, if the password entered is fully numeric like 1122334455, a message saying the password is fully numeric is displayed.
| Signup button| Signup button should accept the valid data and get logged in and the user is redirected to home page| Pass - as expected, after valid data received signed in as the useruser and redirected to main page| 


`Signing in`

| Scenario        | Expected           | result  |
| ------------- |:-------------:| -----:|
| username empty| If the username is blank prompts the user to fill the field |Pass - as expected, if the username field is blank, message prompts user to fill the username field | 
| password field| 1. only a valid password corresponding to the username should get accepted. 2. if the user name or password was entered incorrectly, a message should prompt the user to check his entry. |1. Pass - as expected, only a valid password corresponding to the user was accepted. 2. Pass - as expected, a message "The username and/or password you specified are not correct." displayed to user stating his entry is incorrect. | 

`Sign out`

| Scenario        | Expected           | result  |
| ------------- |:-------------:| -----:|
| click on log out button in navbar | 1. Should prompt the user to confirm the logout. 2. on confirm by clicking signout. User should get signedout. 3. user cannot access booking list after signout | 1. Pass - as expected, user is prompted to confirm his logout. 2. Pass - as expected, when the signout button clicked the user gets signed out from his account. 3. Pass - as expected, user was unable to access the booking history after signout. | 


`Django Admin administration`

| Scenario        | Expected           | result  |
| ------------- |:-------------:| -----:|
| Can login only Superuser| 1. Should accept only the super user user id and password. 2. If a non superuser try to access a message  should display| 1. Pass - as expected, only the superuser user id and password is accepted. 2. Pass - as expected, when a non superuser try to log in the admin a message "Please enter the correct username and password for a staff account. Note that both fields may be case-sensitive." displayed.| 
| All reservations| Superuser/admin can see all reservations like with name, date and time.| Pass - when he login he sees the reservation model and when clicked the reservations lis shows all reservations with name, date and time. | 
|    | Superuser/admin can filter reservations by date and name..|  Pass - he can do the filtering as mentioned | 
|  | Superuser/admin can search for a reservation by name. | Pass - he can search for a reservation by name. | 
| | Superuser/admin can create new reservation |  Pass - when click on add reservation he can fill in all fields and save the transaction  | 
|  |Superuser/admin can delete a reservation | Pass - he can delete a given one | 
|  |Superuser/admin can update a reservation | Pass - he can update all fields for a given one | 
|  |changes reflected in the reservations list | Pass - after updating or deleting, all changes are reflected | 



<u>[Back To README.md](/README.md)</u>

<u>[Back To Top](#table)</u>

