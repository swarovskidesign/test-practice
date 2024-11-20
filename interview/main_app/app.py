from flask import Flask, render_template
import __init__ as pk

def create_app():
    app = Flask(
        __name__, 
        template_folder="../templates", 
        static_folder="../static"
    )
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1337@localhost:1315/postgres'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    pk.db.init_app(app)
    return app

app = create_app()

@app.route('/')
def home():
    first_page_data = pk.take_data_for_first_page()
    second_page_data = pk.take_data_for_second_page()
    third_page_data = pk.take_data_for_three_page()
    fourth_page_data = pk.take_data_for_four_page()
    txt_for_tri_page = [
        ('я уже писал, что мне нравятся плюсы, но я хочу изначально понять, \
         как работает ит работа, чтобы было понимание, \
         в каком направлении мне развиваться на плюсах... \
         а питон я выбрал, потому что он универсальный и простой')
    ]
    txt_for_four_page = [
        ('все профили пустые'),
        ('не потому что я не знаю что писать, а потому что не хватает навыков'),
        ('но...))')
    ]
    return render_template(
        'data.html',
        first_page_data = first_page_data,
        second_page_data = second_page_data,
        third_page_data = third_page_data,
        fourth_page_data = fourth_page_data,
        txt_for_tri_page = txt_for_tri_page,
        txt_for_four_page = txt_for_four_page
    )

if __name__ == '__main__':
    app.run(debug=True)