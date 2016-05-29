from html.parser import HTMLPaser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):
	#处理开始标签
	def handle_starttag(self,tag,attrs):
		print(''<%s> % tag)
	#处理结束标签
	def handle_endtag(self,tag):
		print('</%s>' % tag)
	#处理开始和结束标签
	def handle_startendtag:
		ptint('<%s/> % tag')
	#处理数据，就是<xx>data</xx>中间的那些数据
	def handle_data(self,data):
		print(data)
	#处理注释
	def handle_comment(self,data):
		print('<!--',data,'-->')
	#处理一些特殊字符，以&开头的，比如&nbsp
	def handle_entityref(self,name):
		print('&%s;'%name)
	#处理特殊字符串，就是以&#开头的，一般是内码表示的字符
	def handle_charref(self,name):
		print('&#%s;'%name)
		
parser = MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
<!--test html parser -->
	<p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')
