import os
from datetime import datetime


def rename_abimagefile(instance, filename):
    upload_to = f'media/ab_images/'
    ext = filename.split('.')[-1]
    current_time = datetime.now()
    
    filename ='{}.{}'.format(current_time, ext)
    
    return os.path.join(upload_to, filename)


def rename_cafeimagefile(instance, filename):
    upload_to = f'media/cafe_images/'
    ext = filename.split('.')[-1]
    current_time = datetime.now()
    
    filename ='{}.{}'.format(current_time, ext)
    
    return os.path.join(upload_to, filename)


def rename_imagefile(instance, filename):
    upload_to = f'media/images/'
    ext = filename.split('.')[-1]
    current_time = datetime.now()
    
    filename ='{}.{}'.format(current_time, ext)
    
    return os.path.join(upload_to, filename)


def rename_searchimagefile(instance, filename):
    upload_to = f'media/search_images/'
    ext = filename.split('.')[-1]
    current_time = datetime.now()
    
    filename ='{}.{}'.format(current_time, ext)
    
    return os.path.join(upload_to, filename)