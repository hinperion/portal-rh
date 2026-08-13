from functools import wraps

from django.core.exceptions import PermissionDenied
def hr_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        user = request.user
        
        if user.is_superuser or user.role in ["HR", "CEO"]:
            return view_func(request, *args, **kwargs)
        
        raise PermissionDenied
    
    return wrapper
            
                                              
                                             
    