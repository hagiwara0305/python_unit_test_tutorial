from bottle import route, run, template, post, request

# indexページ
@route('/')
def index():
    return template('form.html')

@post('/')
def item_post():
    print(request.forms.get('name'))
    print(request.forms.get('gender'))
    print(request.forms.get('date'))
    json_object = {
        'name' : request.forms.get('name'),
        'gender' : request.forms.get('gender'),
        'date' : request.forms.get('date'),
    }
    try:
        return json_object
    except:
        return "<p>500 Error</p><a href="">Index前の画面に戻る</a>"

# webサーバ実行
run(host='localhost', port=8080, debug=True, reloader=True)