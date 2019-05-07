import getpass


def get_my_api_key():
    username = getpass.getuser()
    if username == 'sampanna':
        return 'AIzaSyBG_1zyVQwCKnqFoPyz7IjAKCS0xu_KXG0'
    #elif username == 'naman':
        #return 'AIzaSyBU2AZtVmel0wV_NMhPTFKmChVHxb6_30Q'
    else:
        return 'AIzaSyBG_1zyVQwCKnqFoPyz7IjAKCS0xu_KXG0'
