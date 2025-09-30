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

![](/media/readme/testing/landing-page-test.png)

**About page**

![](/media/readme/testing/about-page-test.png)

**Faqs page**

![](/media/readme/testing/faqs-page-test.png)

**Reviews page**

![](/media/readme/testing/reviews-page-test.png)


**Products page**

![](/media/readme/testing/products-page-test.png)


**Product-Details  page**

![](/media/readme/testing/productdetails-page-test.png)


**Checkout page**

![](/media/readme/testing/checkout-page-test.png)

Here I found only 1 warning about the empty "h1" tag as it is filled out with a spinner and I can't write text inside

**Checkout-Success page**

![](/media/readme/testing/checkout-success-page-test.png)


**Bag page**

![](/media/readme/testing/bag-page-test.png)+++++++++++++++++


**Profile page**

![](/media/readme/testing/profile-page-test.png)


**Add Product page**

![](/media/readme/testing/addproduct-page-test.png)


**Edit Product page**

![](/media/readme/testing/editproduct-page-test.png)











**Login page**

![](/media/readme/testing/login-page-test.png)


**Logout page**

![](/media/readme/testing/logout-page-test.png)

**Forget Password page**

![](/media/readme/testing/forgetpass-page-test.png)


**Signup page**

![](/media/readme/testing/login-page-test.png)++++++++++++++



**CSS**

CSS code was tseted using the [W3C CSS Validator Service](https://jigsaw.w3.org/css-validator/)


 - Basestyle.css
 ![](/media/readme/testing/base-css-test.png)

  No errors found only some warnings

  - Checkout.css
 ![](/media/readme/testing/base-css-test.png)

  No errors found only 1 warnings about the -webkit-transition which is not a vendor extension

  - Profiles.css
 ![](/media/readme/testing/profile-css-test.png)

 - Support.css
 ![](/media/readme/testing/support-css-test.png)

<u>[Back To Top](#table)</u>

**JavaScript**

Js Code was tseted using the [Jshint Tool](https://jshint.com/) and found the next results:

- stripe_elements.js

 ![](/media/readme/testing/elemens-js-test.png)

- countryField.js

 ![](/media/readme/testing/countryfield-js-test.png)

 - quantity_script

 ![](/media/readme/testing/-js-test.png)


 I tested all the "Scripts" inside all "HTML" documents and found no errors.


<u>[Back To Top](#table)</u>

**Python**

Python Code was tested usint the [Code Institute's Python Linter](https://pep8ci.herokuapp.com/)  

Results for all 'Python' files:

**settings.py**

![](/media/readme/testing/urls-py-test.png)

The warnings in the image are related to Django code and was not changed.

**urls.py**

![](/media/readme/testing/urls-py-test.png)

 I tested all thee "urls.py" files for all "apps" and found no errors.

**admins.py**

- about.admin.py

  ![](/media/readme/testing/about-admin-test.png)

- checkout.admin.py

  ![](/media/readme/testing/checkout-admin-test.png)

- products.admin.py

  ![](/media/readme/testing/products-admin-test.png)

- profiles.admin.py

  ![](/media/readme/testing/profiles-admin-test.png)

- reviews.admin.py

  ![](/media/readme/testing/reviews-admin-test.png)

- support.admin.py

  ![](/media/readme/testing/faqs-admin-test.png)


**forms.py**

- collaborate-form

  ![](/media/readme/testing/collaborate-form-test.png)

- order-form

  ![](/media/readme/testing/order-form-test.png)

- products-form

  ![](/media/readme/testing/products-form-test.png)

- profiles-form

  ![](/media/readme/testing/profiles-form-test.png)




**models.py**

- about-model

![](/media/readme/testing/about-model-test.png)

- checkout-model

![](/media/readme/testing/checkout-model-test.png)

- products-model

![](/media/readme/testing/products-model-test.png)

- profiles-model

![](/media/readme/testing/profiles-model-test.png)

- reviews-model

![](/media/readme/testing/reviews-model-test.png)

- faqs-model

![](/media/readme/testing/faqs-model-test.png)




**views.py**

- about-views

![](/media/readme/testing/about-view-test.png)

- bag-views

![](/media/readme/testing/bag-view-test.png)

- checkout-views

![](/media/readme/testing/checkout-view-test.png)

- home-views

![](/media/readme/testing/home-view-test.png)

- products-views

![](/media/readme/testing/products-view-test.png)

- profiles-views

![](/media/readme/testing/profiles-view-test.png)

- reviews-views

![](/media/readme/testing/reviews-view-test.png)

- faqs-views

![](/media/readme/testing/faqs-view-test.png)



<u>[Back To Top](#table)</u>

<hr/>

<h3 id="lighthouse">Lighthous Testing</h3>

A Lighthouse testing was done in the local enviroment using Chrome DevTools in incognito mode  
to check the performance, accessibility, best practice and SEO.

**Landing page**

- mobile

  ![](/media/readme/testing/landing-page-mobile-test.png)

- desktop

  ![](/media/readme/testing/landing-page-desktop-test.png)

**About page**

- mobile

  ![](/media/readme/testing/about-page-mobile-test.png)

- desktop

  ![](/media/readme/testing/about-page-desktop-test.png)

**Faqs page**

- mobile

  ![](/media/readme/testing/faqs-page-mobile-test.png)

- desktop

  ![](/media/readme/testing/faqs-page-desktop-test.png)

**Reviews page**

- mobile

  ![](/media/readme/testing/reviews-page-mobile-test.png)

- desktop

  ![](/media/readme/testing/reviews-page-desktop-test.png)

**Products page**

- mobile

  ![](/media/readme/testing/products-page-mobile-test.png)

- desktop

  ![](/media/readme/testing/products-page-desktop-test.png)

**Product-details page**

- mobile

  ![](/media/readme/testing/productdetails-page-mobile-test.png)

- desktop

  ![](/media/readme/testing/productdetails-page-desktop-test.png)

**Add-product page**

- mobile

  ![](/media/readme/testing/addproduct-page-mobile-test.png)

- desktop

  ![](/media/readme/testing/addproduct-page-desktop-test.png)

**Edit-product page**

- mobile

  ![](/media/readme/testing/editproduct-page-mobile-test.png)

- desktop

  ![](/media/readme/testing/editproduct-page-desktop-test.png)

**Profiles page**

- mobile

  ![](/media/readme/testing/profile-page-mobile-test.png)

- desktop

  ![](/media/readme/testing/profile-page-desktop-test.png)

**Checkout page**

- mobile

  ![](/media/readme/testing/checkout-page-lighthouse-test.png)

- desktop

  ![](/media/readme/testing/checkout-page-lighthouse-test.png)

  I found an issue for Accessibility that there is an element with "[aria-hidden="true"]" contain focusable descendents, which is the card element and prevent those interactive elements from being available to users of assistive, I searched and asked th "AI" and found that I don’t need to (and shouldn’t) fix this.
  That hidden <input> is part of Stripe’s accessibility implementation. It’s used internally for security and autofill handling. Stripe marks it aria-hidden="true" and opacity: 0 to keep screen readers away, while routing real focus to the secure iframe.

**Checkout-success page**

- mobile

  ![](/media/readme/testing/checkout-success-page-mobile-test.png)

- desktop

  ![](/media/readme/testing/checkout-success-page-desktoptest.png)











**Sign in page**

- mobile

  ![](/media/readme/testing/signin-page-mobile-test.png)


- desktop

  ![](/media/readme/testing/signin-page-desktop-test.png)


  **Logout page**

- mobile

  ![](/media/readme/testing/signout-page-mobile-test.png)

- desktop

  ![](/media/readme/testing/signout-page-desktope-test.png)


  **Sign up page**
- mobile

  !![](/media/readme/testing/register-page-mobile-test.png)

- desktop

  ![](/media/readme/testing/register-page-desktop-test.png)


<u>[Back To Top](#table)</u>

<hr/>

<h3 id="responsive">Responsiveness Testing</h3>

The site is responsive for mobiles, tablets, labtops and extra screen sizes, it was tested  
manualy using Chrome DevTools and using the [Am I Responsive tool](https://ui.dev/amiresponsive)



Mobile Galaxy-s8:  
![](/media/readme/testing/galaxy.png)

iPad Mini:  
![](/media/readme/testing/ipadmini-pro.png)

Desktop:  
![](/media/readme/testing/desktop.png)

![](/media/readme/testing/home-page.png)

<u>[Back To Top](#table)</u>

<hr/>

<h3 id="compatibility">Browser compatibility Testing</h3>

I tested the site on Chrome, Edge and Firefox and it was working good:




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
| click on About  | should navigate to about page  |Pass- as expected navigates to aboutpage |
| click on Reviews  | should navigate to reviews page  |Pass- as expected navigates to reviewspage |
| click on Faqs  | should navigate to faqs page  |Pass- as expected navigates to faqspage |
| click on All-Products  | should navigate to products page  |Pass- as expected navigates to productspage |
| Sort products by price/rating/brand  | should sort the products by this key   |Pass- as expected the products appears sorted according to the key selected |
| Filter products a specific brand | should show only products related to that specific brand |Pass- as expected the results shows only the products related to that specific brand|
| Filter Special offers by Deals/Clearance | should show only products in that offer |Pass- as expected the results shows only the products in the  specific offer|
| Use the search form to search for a specific product name or processor model | should show only products with that name or processor model |Pass- as expected the results shows only the products with that name or processor model|
| click on register | should navigate to registration page  |Pass- as expected navigates to sign up page|
| click on login  | should navigate to sign in page  |Pass- as expected navigates to sign in page|
| click on logout | should navigate to sign out page  |Pass- as expected navigates to sign out page |
| click on Bag icon | should navigate to my bag page  |Pass- as expected navigates to my bag page |

`Links in Footer`

| Scenario        | Expected           | result  |
| ------------- |:-------------:| -----:|
| click on Social-facebook icon  | should opens business-facebook site in new tab  |Pass- as expected navigates to a new window and opens the business-facebook page|
| click on Subscribe button with an email  | should show the message "Thank you for subscribing!"  |Pass- as expected the form works and displays the desired message|
| click on Privacy Policy icon  | should opens the privacy policy of the website in a new tab|Pass- as expected navigates to a new window and opens th privacy policy of the websitetube |

`About Form`

| Scenario        | Expected           | result  |
| ------------- |:-------------:| -----:|
| Filling the form and click on Submit button  | should submit and the message "Thank you for your collaboration..."  appears in the top upper right |Pass- as expected the form submits and the message shows|

`Buttons on Reviews/Faqs Pages`

| Scenario        | Expected           | result  |
| ------------- |:-------------:| -----:|
| Clicking the button Keep Shopping  | should navigate to products page |Pass- as expected the button navigates to products page|

`Product-Details Page`

| Scenario        | Expected           | result  |
| ------------- |:-------------:| -----:|
| Clicking on any product  | should navigate to that specific product page |Pass- as expected the button navigates to the specific product page|
| Increment/decrement quantity using the -/+ buttons | should update the quantity in the input field accordingly |Pass- as expected the buttons increments/decrements and the quantity updates accordingly in the input field |







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

