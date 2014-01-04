from hashlib import md5

def email_hash(request):
    user = request.user

    if user.is_authenticated():
        return {'email_hash': md5(user.email.lower()).hexdigest()}
    return {'email_hash': 'default'}

def full_name(request):
    user = request.user

    if user.is_authenticated():
        return {'full_name': user.first_name + ' ' + user.last_name}
    return {'full_name': 'Nume Prenume'}
 
