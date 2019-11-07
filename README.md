# Assessment
Coding language python django framework
To run the project from command prompt please run the command python manage.py runserver
for contact us please change the following statments in DjangoTutorial->settings.py 
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASS')
by adding it to environment variable


https://github.com/AlishaChopra/Assessment/blob/master/users/views.py
Please change the email id in emailSend method

for part 3
select user_name, activity_name, max(occurrence) as 'Last Occurrence' , min(occurrence) as 'First Occurrence', amount 
from user_activity ua
inner join user ua ON ua.user_id = u.u_id
inner join activity a ON ua.activity_id = a.activityid
where extract(Month(occurence)) = 'Oct'
