# test-element8

Our client is planning to automate their shareholder’s outstanding details using a web application.
Here is the plan to float shares to different buyers.
1. Add shareholders to the system
2. For each shareholder - Define due amount, duration, installment type, Date on which the
installment starts
3. Display a summary list of all shareholder, their total due amount, their total paid amount, their
total outstanding amount
4. Display a detail list of an individual shareholder to see the details of his/her share details, payment
schedule and outstanding amount
5. Search for a shareholder and get details
A shareholder can have multiple shares.
Share duration can be 1 to 5 year.
Share Payment option is: monthly(12), Quarterly(4), half-yearly(2), annual(1) or custom (customisable
period and amount)
Search share details (search for a shareholder details by entering his email address)
Excel Report based on search result
It is desirable that you come up with a good layout, especially for the listing and reports
   
### How to setup:

- Install python version: 3.x (tested on 3.9) 
- Optional: Setup and activate virtualenv
- `pip install -r requirements.txt`
- `python manage.py createsuperuser` (Only super users are allows to log in)

### Dependencies


- `Django==3.2.5`
- `django-countries==7.2.1`
- `django-crispy-forms==1.12.0`
- `django-phonenumber-field==5.2.0`
- `django-tables2==2.4.0`
