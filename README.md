
# Crowd Funding App Python

#### Mid-Course Python Project in 9-Months Scholarship ITI 
Crowd-Funding console app Crowdfunding is the practice of funding a project or venture by raising small amounts of money from a large number of people, typically via the Internet. Crowdfunding is a form of crowdsourcing and alternative finance. In 2015, over US$34 billion was raised worldwide by crowdfunding.

## Make Your Configuration
In Package helpers -> email_utils.py  
Setup 2 variables: 
```python
    sender_email = "< ur email >" 
    #In sendEmail function
    password ="< password of sender email >" 
```
Adjust your SMTP domain and port
## Features

- Register a new user with info <br>
        1. id (unique, auto-generated)<br>
        2. First Name <br>
        3. Last Name <br>
        4. Unique Email <br>
        5. Password (confirmed) <br>
        6. Egyption Phone <br>

- Send Random Verifcation Code by Email to new user to activate account
- Login with
    - Email and Password
- User Can:
    1. Create a Project with:
        - id (unique, auto-generated)
        - title
        - details
        - totalTarget
        - startDate
        - endDate
        - ownerID (login user id)
    2. Read all Projects in App
    3. Update Project (only create by login user)
    4. Delete Project (only create by login user)
    5. Search for a Project by Date


