#if [[ $CREATE_SUPERUSER ]];
#then
#  python newspaper/manage.py createsuperuser --no-input
#fi