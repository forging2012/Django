(1)
��ʱ����post��ʽ��csrf���о����鷳����ȻҲ����ȡ�����£�
��settings.py������


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
   # 'django.middleware.csrf.CsrfViewMiddleware',                 #ȡ��post��ʽ��csrf
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)


(2)��HttpResponse �����ĵ�ʱ��Ҫ���� u"��������"����Ȼ��ʾ��Ҫdecode.
