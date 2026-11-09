import streamlit as st
import csv
from datetime import datetime
stems = ["груст", "печал", "тоск", "одинок", "опустош", "обид", "злост", "злюсь", "злой", "злая", "сердит", "раздраж", "бесит", "страх", "страш", "боюсь", "испуг", "тревог", "тревож", "паник", "нервнич", "беспоко", "волнуюсь", "отвращен", "противно", "мерзко", "удивл", "шокирован", "в шоке", "радост", "радуюсь", "счастлив", "спокой", "умиротвор", "благодар", "надежд", "облегчен", "виноват", "стыд", "смущ", "растерян", "запутал", "устал", "вымотан", "измотан", "перегруж", "стресс", "скучно", "зависть", "завидую", "ревн", "разочаров", "оцепенен", "безразлич", "апати"]
risk_words = ["суицид", "убить себя", "покончить с собой", "хочу умереть", "не хочу жить", "не хочу больше жить", "причинить себе вред", "навредить себе", "хочу исчезнуть", "лучше бы меня не было"]
st.title("Здесь и сейчас")
st.info("Это учебный прототип для моего исследования: я изучаю, как людям удаётся называть свои чувства. Это не терапия. Займёт около 2 минут.")
st.write("Правильных ответов здесь нет, отвечай как чувствуешь. Ответы сохраняются без имени, для личного проекта.")
st.write("Что ты чувствуешь прямо сейчас?")
if st.button("Радость"):
    st.write('Выбрано: «радость». Где ты чувствуешь это в теле прямо сейчас?')
    st.session_state["chosen"] = "радость"
if st.button("Грусть"):
    st.session_state["chosen"] = "грусть"
    st.write('Выбрано: «грусть». Где ты чувствуешь это в теле прямо сейчас?')
if st.button("Злость"):
    st.session_state["chosen"] = "злость"
    st.write('Выбрано: «злость». Где ты чувствуешь это в теле прямо сейчас?')
if st.button("Страх"):
    st.session_state["chosen"] = "страх"
    st.write('Выбрано: «страх». Где ты чувствуешь это в теле прямо сейчас?')
if st.button("Отвращение"):
    st.write('Выбрано: «отвращение». Где ты чувствуешь это в теле прямо сейчас?')
    st.session_state["chosen"] = "отвращение"
if st.button("Удивление"):
    st.write('Выбрано: «удивление». Где ты чувствуешь это в теле прямо сейчас?')
    st.session_state["chosen"] = "удивление"
user_text = st.text_area("Не получается выбрать? Напиши своими словами, как можешь")
if st.button("Отправить"):
    chosen = st.session_state.get("chosen", "")
    for phrase in risk_words:
        if phrase in user_text.lower():
            st.write("Это звучит очень важно. Здесь я не могу с этим помочь. Пожалуйста, поговори с близким человеком или обратись в местную службу помощи.")
            st.stop()
    found = []
    for word in stems:
        if word in user_text.lower():
            found.append(word)
    st.session_state["sent"] = True
    st.session_state["text"] = user_text.strip()
    st.session_state["found"] = found
if st.session_state.get("sent"):
    text = st.session_state.get("text", "")
    found = st.session_state.get("found", [])
    chosen = st.session_state.get("chosen", "")
    st.write("Твой текст: ", text)
    if found:
        st.write("Вот что я вижу. Чувства: ", ", ".join(found))
        if chosen:
            st.write(f'Выбрано: {chosen}, а в твоих словах я вижу: {", ".join(found)}. Всё это может быть рядом.')
    else:
        st.write("Здесь больше о событиях. А что ты чувствуешь сейчас, пока это пишешь?")
    changed = st.text_input("Что-то изменилось? Что?")
    if st.button("Дальше"):
        st.session_state["changed"] = changed
        st.session_state["next_done"] = True
    if st.session_state.get("next_done"):
        hard = st.text_input("Где было сложно? Что было непонятно?")
        bridge = st.text_input("Спасибо, за твои ответы. Кому из близких можно было бы об этом рассказать?")
        if st.button("Завершить"):
            st.session_state["hard"] = hard
            st.session_state["bridge"] = bridge
            st.write("Спасибо!")
            with open("sessions_ru.csv", "a", newline="", encoding="utf-8-sig") as f:
                    writer = csv.writer(f)
                    writer.writerow([datetime.now(), st.session_state.get("chosen", ""), st.session_state.get("text", ""), ','.join(st.session_state.get("found", [])), st.session_state.get("changed", ""), st.session_state.get("hard", ""), st.session_state.get("bridge", "")])