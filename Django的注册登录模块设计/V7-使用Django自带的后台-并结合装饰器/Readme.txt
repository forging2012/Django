ʹ��Django�Դ��ĺ�̨��¼���з��ʣ����Ĵ������£�

if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():                          ##У���û���������
            #��ȡ���û�����
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #��ȡ�ı�������dj�ֵ��auth����бȽ�
            user = auth.authenticate(username=username,password=password)
		.......
	
##########################################

## ��ʹ��װ������ʹ�÷���
def list(request):
##��֤ʧ��,��������ҳ��
    if not  request.user.is_authenticated():
        return HttpResponseRedirect('http://127.0.0.1:8000/static/login_error.html')
    else:
        return render_to_response('list.html')


#ʹ��װ�����ķ���
@login_required
def list2(request):
    return render_to_response('list2.html')


###############################################################

