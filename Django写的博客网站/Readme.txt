(1)Djangoʹ�����ݿ��API �������ݿ����ɾ�Ĳ��ԭ��:

ע��;Django�����ݿ�api ������Django���õ����ݿ���﷨ ���Բ������е����ݿ⡣��Ҳ��������ʹ��DJango��ģ�Ͷ����� import MySQLdb����ʮ����Ĳ�����,���ǲ��� from django.db import models  ��ܵ�ģ��


����ͼ�н������ݿ��ѯ�ı�����

�����������ϸ���ܵ��Ǹ�����ͼ����� HTML �ı�������ͨ������ͼ����ı�ֱ��Ӳ����HTML��������ͼ��Ҳ�б��������Դ����ݿ��л�ȡ���ݡ� �ܼ򵥣� �����е��κ� Python ���ִ��һ�� SQL ��ѯ���Խ������һЩ����

�ڱ�������ͼ�У�����ʹ���� MySQLdb ��⣨���Դ� http://www.djangoproject.com/r/python-mysql/ ��ã������� MySQL ���ݿ⣬ȡ��һЩ��¼���������ṩ��ģ������ʾһ����ҳ��

#coding:utf8
from django.shortcuts import render_to_response    #����������Ⱦ��htmlҳ�漴��
import MySQLdb

def book_list(request):
    db = MySQLdb.connect(user='me', db='mydb', passwd='secret', host='localhost')
    cursor = db.cursor()  #�����α�
    cursor.execute('SELECT name FROM books ORDER BY name')
    names = [row[0] for row in cursor.fetchall()]
    db.close()
    return render_to_response('book_list.html', {'names': names})

����������ã����ܿ�һЩ���⽫����������ǰ��

���ǽ����ݿ����Ӳ���Ӳ�б����ڴ���֮�С� ��������£���Щ����Ӧ�������� Django �����С�

���ǲ��ò��ظ�ͬ���Ĵ��룺 �������ݿ����ӡ��������ݿ��αꡢִ��ĳ����䡢Ȼ��ر����ݿ⡣ ��������£���������ҪӦ��ֻ��ָ������Ľ����

��������˨���� MySQL ֮�ϡ� �������ʱ�䣬����Ҫ�� MySQL ���� PostgreSQL���Ͳ��ò�ʹ�ò�ͬ�����ݿ������������� psycopg ������ MySQLdb �����ı����Ӳ��������� SQL �������Ϳ��ܻ�Ҫ�޸�SQL �� ��������£�Ӧ����ʹ�õ����ݿ���������г�������һ��ֻ��һ���޸ļ��ɱ任���ݿ�������� ����������ڽ���һ����Դ��DjangoӦ�ó������������ø�����ʹ�õĻ�����������Ƿǳ��ʵ��ġ���

���������ڴ��ģ�Django���ݿ�����������ڽ����Щ���⡣ ������ǰ��ʾ�����ʹ�� Django ���ݿ� API ��д֮ǰ�ĸ���ͼ��

from django.shortcuts import render_to_response
from mysite.books.models import Book

def book_list(request):
    books = Book.objects.order_by('name')
    return render_to_response('book_list.html', {'books': books})
���ǽ��ڱ����Ժ�ĵط�������δ��롣 Ŀǰ���ԣ���������и����µ���ʶ��

(2) �����Ľ��ͺͲ�������:

http://docs.30c.org/djangobook2/chapter05/


�������˾��� �����õ��������ݿ� ����ֱ����ԭ����import mysqldb�� �򵥲���ѧ�����е����ݿ��api���������������е����ݿ�api�Ĳ�����������Ҳ����ʵ�ָ��ӵ�sql���� �洢���̵ı�д.