from app import create_app, db, pk
import os

app = create_app()

class TextForFirstPage(db.Model):
    __tablename__ = 'text_for_first_page'
    id = pk.db.Column(pk.db.Integer, primary_key=True)
    description = pk.db.Column(pk.db.String(255), nullable=False)

class TextForHiddenPage(db.Model):
    __tablename__ = 'text_for_hidden_page'
    id = pk.db.Column(pk.db.Integer, primary_key=True)
    description = pk.db.Column(pk.db.String(255), nullable=False)

class BlockForHardSkills(db.Model):
    __tablename__ = 'block_for_hard_skills'
    id = pk.db.Column(pk.db.Integer, primary_key=True)
    description = pk.db.Column(pk.db.String(255), nullable=False)
    img = pk.db.Column(pk.db.String(255), nullable=True)
    url = pk.db.Column(pk.db.String(255), nullable=True)

class BlockForSoftSkills(db.Model):
    __tablename__ = 'block_for_soft_skills'
    id = pk.db.Column(pk.db.Integer, primary_key=True)
    img = pk.db.Column(pk.db.String(255), nullable=True)
    url = pk.db.Column(pk.db.String(255), nullable=True)

with app.app_context():
    pk.db.create_all()
    print("created))")

    data_for_first_page = [
        'я денчик @тг',
        'я ваще на питоне пишу, но хочу в идеале понять плюсы и быть очень умным',
        'ща, я стараюсь дропать все задачи/проекты, которые у меня есть, на гитхаб'
    ]
    for text in data_for_first_page:
        new_line_db1 = TextForFirstPage(description=text)
        pk.db.session.add(new_line_db1)

    data_for_second_page = [
        'я, ваще, стараюсь делать какие-то задачи где по кайфу',
        'мне нравится чет писать/программировать, потому что это круто, что-то автоматизировать, да и логику хорошо грейдит',
        'там степик проблемы на литкоде я на всяких подобных сайтах',
        'короче стараюсь'
    ]
    for text in data_for_second_page:
        new_line_db2 = TextForHiddenPage(description=text)
        pk.db.session.add(new_line_db2)

    data_hard_skills = [
        ('interview/static/images/leet.png', 'тут я решаю проблемы когда понимаю, что надо улучшить свое понимание алгоритмов', 'https://leetcode.com/'),
        ('interview/static/images/stepik.png', 'а здесь я делаю, когда понимаю, что минимум, я не знаю, или забыл', 'https://stepik.org/'),
        ('interview/static/images/git.png', 'сюда я стараюсь выкладывать все, что пишу, ибо интересно как я пишу', 'https://github.com/')
    ]
    for path, description, url in data_hard_skills:
        img_path = os.path.abspath(path)
        new_line_db3 = BlockForHardSkills(description=description, img=img_path, url=url)
        pk.db.session.add(new_line_db3)

    data_soft_skills = [
        ('interview/static/images/hh.png', 'https://novosibirsk.hh.ru'),
        ('interview/static/images/link.png', 'https://www.linkedin.com/'),
        ('interview/static/images/habr.png', 'https://career.habr.com/')
    ]
    for path, url in data_soft_skills:
        img_path = os.path.abspath(path)
        new_line_db4 = BlockForSoftSkills(img=img_path, url=url)
        pk.db.session.add(new_line_db4)

    pk.db.session.commit()
    print("data added))")