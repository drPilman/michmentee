@bot.message_handler(commands=["gen"])
@log
def cmd_gen(message):
    db.create()
    db.gen()
    bot.send_message(message.chat.id, "gen")


def create():
    session.flush()
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    session.commit()


"""
def get(chat_id):
    result = session.query(User).filter(User.chat_id == chat_id).first()
    if result:
        logging.debug(f"{chat_id} is {result}")
    else:
        result = User(chat_id=chat_id)
        session.add(result)
        session.commit()
    return result"""
mm = ('лекция', 'практика', 'лабараторная', 'физ.занятие')

mtime = ((9, 30), (11, 20), (13, 10), (15, 25), (17, 15))

subj_list = {
    "алгем (лекция)": "Андрей Валентинович Куприн",
    "алгем (практика)": "Андрей Валентинович Куприн",
    "выч.тех. (лабараторная)": "Анастасия Андреевна Изотова",
    "выч.тех. (лекция)": "Симонов Сергей Евгеньевич",
    "выч.тех. (практика)": "Анастасия Андреевна Изотова",
    "выш.мат. (лекция)": "Ирина Васильевна Гетманская",
    "выш.мат. (практика)": "Ирина Васильевна Гетманская",
    "инф.тех. (лабараторная)": "Павликов Артем",
    "инф.тех. (лекция)": "Городничев Михаил Геннадьевич",
    "инф.тех. (практика)": "Грач Маратович",
    "инф.экология (лабараторная)": "Курбатов Валерий Александрович",
    "инф.экология (лекция)": "Шакиров Кирилл Фаридович",
    "ин.яз. (практика)": "Анна Юрьевна Москалёва",
    "комп.граф. (лекция)": "Рывлина Александра Александровна",
    "комп.граф. (практика)": "Ирина Ивановна Пискарёва",
    "физ-ра (физ.занятие)": "Наталья Николаевна Г.",
    "философия (лекция)": "Кораблева Елена Валентиновна",
    "философия (практика)": "Попов Антон Павлович",
}

raspis = ((
              ('инф.тех.|2|ВЦ127|11', 'выч.тех.|3|314|12',
               'ин.яз.|2|404,301б|19',
               'комп.граф.|2|223|16', ''),
              ('физ-ра|4||17', 'философия|2|318|21', '', '', ''),
              (
                  '', '', '', 'инф.тех.|2|ВЦ116|11',
                  'инф.тех.|2|ВЦ116|11'),
              ('инф.экология|1|347|18', 'выч.тех.|1|310|20',
               'комп.граф.|1|126|15', '', ''),
              ('', 'инф.экология|3|339|18', 'выш.мат.|2|504а|13',
               'физ-ра|4||17',
               'алгем|2|508|14'),
          ),
          (
              ('инф.тех.|2|ВЦ127|11', 'выч.тех.|2|314|12',
               'ин.яз.|2|404,301б|19',
               'комп.граф.|2|223|16', ''),
              ('физ-ра|4||17', 'философия|2|318|21', '', '', ''),
              ('выш.мат.|1|522|13', 'алгем|1|347|14',
               'инф.тех.|1|517|11', '', ''),
              ('философия|1|514|21', 'выч.тех.|1|310|20', '', '', ''),
              ('', '', 'выш.мат.|2|504а|13', 'физ-ра|4||17',
               'алгем|2|508|14'),
          )
)


def gen():
    for subj, teacher in subj_list.items():
        session.add(Subject(name=subj))
        session.add(Teacher(full_name=teacher, subject=subj))
    session.commit()

    for weekn, t in enumerate(raspis):
        for dayn, d in enumerate(t):
            for timen, s in enumerate(d):
                if s:
                    subj, type_id, room, teacher_id = s.split('|')
                    t = mtime[timen]
                    session.add(TimeTable(week=weekn,
                                          day=dayn,
                                          subject=f"{subj} ({mm[int(type_id) - 1]})",
                                          room=room,
                                          start_time=t[0] * 100 + t[1]))
    session.commit()
