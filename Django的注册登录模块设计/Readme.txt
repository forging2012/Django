��1��
V1 û��ʹ��װ���� ���Գ�ʦ����.ֻ��������ת���ܷ��ʵĽ��滹�ǿ��Է���


��2��V2 �汾ʹ��װ������������

��django��Ŀ�У������ῴ�����������Ĵ��룺

from django.contrib.auth.decorators import login_required  
 
@login_required  
def my_view(request):  
    ...  

������һ��@login_required��ǩ�������þ��Ǹ��߳���ʹ�����������Ҫ���û���¼�ġ�
1.����û���û�е�¼��Ĭ�ϻ���ת����/accounts/login/�������ֵ������settings�ļ���ͨ��LOGIN_URL�������趨�������滹���Զ������������url��Ϊ��¼����ת�ĵ�ַ���磺 /accounts/login/?next=/polls/3/ ��¼���֮�󣬻�ȥ����/poll/3��

2.����û���¼�ˣ���ô�÷����Ϳ�������ִ��