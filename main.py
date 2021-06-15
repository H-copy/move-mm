from flask import Flask, url_for, request
from model.response import Response

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False
# app.jinja_env.auto_reload = True
# app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def root():
  return 'hello world !!!'

'''

标签列表分页查询
url: get /tags
query: 
  - pageSize
  - pageNo
  - name
  - code

response:
  - msg
  - code
  - result
    - id
    - name
    - color

新增标签
url: post /tags
params:
  - name
  - color

response: 
  - msg
  - code

修改标签
url: put /tags/id
params:
  - name
  - color
  - id


response: 
  - msg
  - code
  

删除标签
url: delete /tags/id

response: 
  - msg
  - code

'''

@app.route('/tags', methods=['POST'])
def tags_creat():
  print('create tags',  type(request.json))
  return Response.success().dict()
  

@app.route('/tags', methods=['GET'])
def tags_list():
  return Response.success(
    name='惊悚',
    color='orange'
  ).dict()


@app.route('/tags', methods=['PUT'])
def tags_update():
  pass


@app.route('/tags', methods=['DELETE'])
def tags_delete():
  pass
  


app.run(
  host='localhost',
  port=8080,
  debug=True
)
