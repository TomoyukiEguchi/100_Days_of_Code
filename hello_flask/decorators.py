# from datetime import datetime
#
#
# def not_during_the_night(func):
#     def wrapper():
#         if 7 <= datetime.now().hour < 22:
#             func()
#         else:
#             pass
#     return wrapper
#
# def say_whee():
#     print("wow whee!")
#
# say_wow_whee = not_during_the_night(say_whee)
# say_wow_whee()


class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper

@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")

new_user = User("Tomo")
new_user.is_logged_in = True
create_blog_post(new_user)
