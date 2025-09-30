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
| Clicking on "Add to Bag" button | should add that item with the quantity selected to the bag and a message shows the confirmation of the adding in the messages container |Pass- as expected the button adds the item with the quantity selected and a massage shows in the messages area |

`My Bag Page`

| Scenario        | Expected           | result  |
| ------------- |:-------------:| -----:|
| Updating the quantities in the quantity form using +/- buttons | should update the quantity in the input filed |Pass- as expected the buttons update the quantities accordingly|
| Clicking on "Update" button | should update the quantity for that product in the bag and a message confirms that |Pass- as expected the buttons update the quantities of the products accordingly and the message confirms that|
| Clicking on "Remove Item" button | should remove the product from the bag and a message confirms that |Pass- as expected the buttons removes the product from the bag and the message shows|
| Clicking on "Secure Checkout" button | should navigate to checkout page |Pass- as expected the buttons works and navigate to the secure checkout page|


`Checkout Page and test secure payment with Stripe`

| Scenario        | Expected           | result  |
| ------------- |:-------------:| -----:|
| Clicking the "Complete order" button without filling the required fields or provide an invalid details| should not complete and a message under the field explains the issue  |Pass- as expected the operation not complete and a message appears under each fiels descripes the issue|
| Filling the card field with an invalid card number| should not complete and a message under the payment card field shows that the card number is invalid |Pass- as expected the operation not complete and a message appears under the payment card field says that  the card number is invalid|

| Filling the card field with an invalid expiry-date/post-code/cvc | should not complete and a message under the payment card field shows that the expiry-date/post-code/cvc are invalid |Pass- as expected the operation not complete and a message appears under card that the expiry-date/post-code/cvc are invalid|

| Filling the checkout form with a complete details and a valid card number | should complete the order and navigates to checkout-success page and a message of confirmation apeears |Pass- as expected the operation completes and navigates to the checkout-success page with a message of confirmation|

| Checkout-Success page | after completing the order and navigating to checkout-success page the success message shows with the order summary|Pass- as expected the operation completes and navigates to the checkout-success page with a message of confirmation and order summary|





`Signing in`

| Scenario        | Expected           | result  |
| ------------- |:-------------:| -----:|
| username empty| If the username is blank prompts the user to fill the field |Pass - as expected, if the username field is blank, message prompts user to fill the username field | 
| password field| 1. only a valid password corresponding to the username should get accepted. 2. if the user name or password was entered incorrectly, a message should prompt the user to check his entry. |1. Pass - as expected, only a valid password corresponding to the user was accepted. 2. Pass - as expected, a message "The username and/or password you specified are not correct." displayed to user stating his entry is incorrect. | 

`Sign out`

| Scenario        | Expected           | result  |
| ------------- |:-------------:| -----:|
| click on log out button in navbar | 1. Should prompt the user to confirm the logout. 2. on confirm by clicking signout. User should get signedout. 3. user cannot access booking list after signout | 1. Pass - as expected, user is prompted to confirm his logout. 2. Pass - as expected, when the signout button clicked the user gets signed out from his account. 3. Pass - as expected, user was unable to access the booking history after signout. | 





<u>[Back To README.md](/README.md)</u>

<u>[Back To Top](#table)</u>

