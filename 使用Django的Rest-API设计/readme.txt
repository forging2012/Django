ѧϰ����:
https://blog.laisky.com/p/django-rest/


ע�⣺Django �Դ���api��̨,��flask���ӵ�

��װ����:
pip install djangorestframework 

RESTful�ܹ�ʵ�ʵ�6��ԭ��:

1)Uniform Interface: ͳһ�ӿڣ�������˺Ϳͻ���ͨ��ͳһ�ӿڽ���ͨ�ţ������ÿͻ��˺ͷ�����ܶ���������
2��Stateless�� ��״̬�������������ͻ�����ȫͨ�����ֲ�ʵ�֣�
3��Cacheable�� �ɻ����
4�� Client-Server�� �ͻ��˺ͷ���˷��루�ͻ��˰������ݣ�����˲������û�״̬��
5��Layered System: �ֲ�ϵͳ
6��Code on Demand��������룬����˺Ϳͻ��˶���ͳһ�Ľӿڽ���ͨ�ţ����Է���˺Ϳͻ��˿������Լ�ϲ���ı�����Ա�д��


#########################
Django REST framework�кܶ��֡��÷�����������÷��ǣ�

1. ������Դ����Դ��python���󣨱���model���󣩽��и��롢��װ��������Ҫ���л���serialize)�����ݡ����˻�����Resource�����⣬��ܻ��ṩ��FormResource��ModelResource���Ա��ڶ�Form��Model�Ĵ���Resource������View�еĴ�����Ȼ��Ҳ���Բ�ʹ��Resource,����View��ȥָ��Ҫ���л������ݡ�

2. ������ͼ����ͼ�Ƕ�django View�ķ�װ�����������л�����ϵ�л��ȷ�����ͬʱͨ��Mixin��֧����ʵ��get,post,put,delete�Ȳ��������������ModelView����ModelResource���ʹ�÷ǳ��򵥷��㡣

3. ����url����������ʽƥ���View���as_view�������÷����᷵��django��view������