����Django1.9֮ǰ�ģ�

���� 

(1)python manage.py syncdb  ������DJango�Դ��ĺ�̨��һЩ��.


(2)Ȼ��ͨ�� python manage.py makemigrations blog  ����ģ��������ݱ�

Django 1.7֮��,����������South��migration���ܣ��޸�Model������ڲ�Ӱ���������ݵ�ǰ�����ؽ���ṹ��
����Ŀ¼�»����� migrations����¼��ĸ���.

(3)Ȼ��ͬ��ģ�͵����ݿ������.
python manage.py syncdb 

��4��

�����ٴδ���һ������һ��.

��models���涨���.Ȼ��ʹ��python manage.py makemigrations blog

��� python manage.py syncdb  �����ݿ�ɹ���.

ԭ��blog_blogspost  �ı�Ҳû��ɾ��.





���ǻ���Ϊʲôһ��Ҫͬ��model�����ݿ��ˣ�
ԭ��:

(1)��Django��ormΪ���� ��ֻ��ά��model�Ķ��壬 Ȼ��makemigrations��
migrate/syncdb�Ϳ��԰Ѷ�model�ĸ���ͬ�������ݿ�.

(2)�������ֱ�ӿͻ��˹���ȥ ��Ҫά������һ����mysqlһ��model��ֵά��һ����̨�����á�

