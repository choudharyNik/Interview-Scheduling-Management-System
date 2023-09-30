# from django.contrib.auth.management.commands import createsuperuser
# from django.core.exceptions import ValidationError

# class Command(createsuperuser.Command):
#     help = 'Create a superuser with separate username, email, and password'

#     def add_arguments(self, parser):
#         super().add_arguments(parser)
#         parser.add_argument(
#             '--username',
#             dest='username',
#             required=False,
#             help='Specifies the username for the superuser.'
#         )
#         parser.add_argument(
#             '--password',
#             dest='password',
#             required=False,
#             help='Specifies the password for the superuser.'
#         )

#     def handle(self, *args, **options):
#         username = options['username']
#         email = options['email']
#         password = options['password']

#         if not username:
#             raise ValidationError('Username is required for superusers.')

#         if not password:
#             raise ValidationError('Password is required for superusers.')

#         # Remove the 'username' and 'password' options from the options dictionary
#         options.pop('username', None)
#         options.pop('password', None)

#         # Set the 'username' field for the superuser
#         options['username'] = username

#         super().handle(*args, **options)
