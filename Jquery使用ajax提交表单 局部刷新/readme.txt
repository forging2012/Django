��飺

ע�⣺js����ʵ��ajax����ֻ����Jquery  ��ajax���� ���ӷ���ͼ�

AJAX����Asynchronous Javascript And XML�����첽JavaScript��XML������ָһ�ִ�������ʽ��ҳӦ�õ���ҳ����������ͨ���ں�̨������������������ݽ�����

AJAX ����ʹ��ҳʵ���첽���¡�����ζ�ſ����ڲ����¼���������ҳ������£�����ҳ��ĳ���ֽ��и��¡�

Jquery��һ�������Javascript�����⡣���ݸ��������ʹ�û��ܸ�����ش���HTML��events��ʵ�ֶ���Ч�������ҷ����Ϊ��վ�ṩAJAX������

����������ʵ�������Աȣ�һ���Ǽ�����һ����JS������ơ�



ajax�ύ������jQuery ȥʵ�֣��ǳ��򵥣�����ԭ����js��


�ύ������ݲ�����get��ʽһ������ַ�г���.���õ����첽�ύ

��1��
ͨ�� jQuery��������ѡȡ����ѯ��query�� HTML Ԫ�أ���������ִ��"����"��actions����

�����﷨�� $(selector).action()

��Ԫ���Ŷ��� jQuery

ѡ�����selector��"��ѯ"��"����" HTML Ԫ��

jQuery �� action() ִ�ж�Ԫ�صĲ���

ʵ��:
$(this).hide() - ���ص�ǰԪ��
$("p").hide() - �������� <p> Ԫ��
$("p.test").hide() - �������� class="test" �� <p> Ԫ��
$("#test").hide() - �������� id="test" ��Ԫ��

(2)
ѧϰ��ַ�� http://www.runoob.com/jquery/jquery-ajax-get-post.html

jQuery get() �� post() ��������ͨ�� HTTP GET �� POST ����ӷ������������ݡ�

�����ڿͻ��˺ͷ������˽�������-��Ӧ�ĳ��÷����ǣ�GET �� POST��
GET - ��ָ������Դ��������
POST - ��ָ������Դ�ύҪ���������


��2.1��
jQuery $.get() ����
$.get() ����ͨ�� HTTP GET ����ӷ��������������ݡ�

�﷨��
$.get(URL,callback);
����� URL �����涨��ϣ������� URL��
��ѡ�� callback ����������ɹ�����ִ�еĺ�������

���������ʹ�� $.get() �����ӷ������ϵ�һ���ļ���ȡ�����ݣ�
ʵ��
$("button").click(function(){
  $.get("demo_test.php",function(data,status){
    alert("Data: " + data + "nStatus: " + status);
  });
});

��2.2��

jQuery $.post() ����

$.post() ����ͨ�� HTTP POST ����ӷ��������������ݡ�
�﷨:
$.post(URL,data,callback);
����� URL �����涨��ϣ������� URL��
��ѡ�� data �����涨��ͬ�����͵����ݡ�
��ѡ�� callback ����������ɹ�����ִ�еĺ�������

���������ʹ�� $.post() ��ͬ����һ�������ݣ�
ʵ��
$("button").click(function(){
  $.post("demo_test_post.html",
  {
    name:"Donald Duck",
    city:"Duckburg"
  },
  function(data,status){
    alert("Data: " + data + "nStatus: " + status);
  });
});