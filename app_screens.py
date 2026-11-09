import streamlit as st
import csv
from datetime import datetime
stems = ["груст", "печал", "тоск", "одинок", "опустош", "обид", "злост", "злюсь", "злой", "злая", "сердит", "раздраж", "бесит", "страх", "страш", "боюсь", "испуг", "тревог", "тревож", "паник", "нервнич", "беспоко", "волнуюсь", "отвращен", "противно", "мерзко", "удивл", "шокирован", "в шоке", "радост", "радуюсь", "счастлив", "спокой", "умиротвор", "благодар", "надежд", "облегчен", "виноват", "стыд", "смущ", "растерян", "запутал", "устал", "вымотан", "измотан", "перегруж", "стресс", "скучно", "зависть", "завидую", "ревн", "разочаров", "оцепенен", "безразлич", "апати", "уныни", "ожидан", "неопределенн", "неопределённ", "весел"]
risk_words = ["суицид", "убить себя", "покончить с собой", "хочу умереть", "не хочу жить", "не хочу больше жить", "причинить себе вред", "навредить себе", "хочу исчезнуть", "лучше бы меня не было"]
if "screen" not in st.session_state:
    st.session_state["screen"] = 1
step = st.session_state["screen"]
if step <= 5:
    st.caption(f"Шаг {step} из 5")
if st.session_state["screen"] == 1:
    st.title("Здесь и сейчас")
    st.info("Это учебный прототип для моего исследования: я изучаю, как людям удаётся называть свои чувства. Это не терапия. Займёт около 2 минут.")
    st.write("Правильных ответов здесь нет, отвечай как чувствуешь. Ответы сохраняются без имени, для личного проекта.")
    st.write("Что ты чувствуешь прямо сейчас?")
    if st.button("Радость"):
        st.session_state["chosen"] = "радость"
        st.session_state["screen"] = 2
        st.rerun()
    if st.button("Грусть"):
        st.session_state["chosen"] = "грусть"
        st.session_state["screen"] = 2
        st.rerun()
    if st.button("Злость"):
        st.session_state["chosen"] = "злость"
        st.session_state["screen"] = 2
        st.rerun()
    if st.button("Страх"):
        st.session_state["chosen"] = "страх"
        st.session_state["screen"] = 2
        st.rerun()
    if st.button("Отвращение"):
        st.session_state["chosen"] = "отвращение"
        st.session_state["screen"] = 2
        st.rerun()
    if st.button("Удивление"):
        st.session_state["chosen"] = "удивление"
        st.session_state["screen"] = 2
        st.rerun()
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
        st.session_state["screen"] = 2
        st.rerun()
elif st.session_state["screen"] == 2:
    text = st.session_state.get("text", "")
    found = st.session_state.get("found", [])
    chosen = st.session_state.get("chosen", "")
    if text:
        st.write("Твой текст: ", text)
        if found:
            st.write("Вот что я вижу. Чувства: ", ", ".join(found))
            if chosen:
                st.write(f'Выбрано: {chosen}, а в твоих словах я вижу: {", ".join(found)}. Всё это может быть рядом.')
        else:
            st.write("Здесь больше о событиях. А что ты чувствуешь сейчас, пока это пишешь?")
    else:
        st.write(f'Выбрано: «{chosen}»')
    body = st.text_input("Где ты чувствуешь это в теле прямо сейчас?")
    if st.button("Дальше"):
        st.session_state["body"] = body
        st.session_state["screen"] = 3
        st.rerun()
elif st.session_state["screen"] == 3:
    changed = st.radio("Что сейчас с этим чувством?", index=None, options=["Стало сильнее", "Стало слабее", "Не изменилось"])
    if st.button("Дальше"):
        st.session_state["changed"] = changed
        st.session_state["screen"] = 4
        st.rerun()
elif st.session_state["screen"] == 4:
    situation = st.radio("Что повлияло на это чувство?", index=None, options=["Что-то произошло", "Человек", "Мысль или беспокойство", "Тело (усталость, напряжение)", "Не знаю"])
    situation_text = st.text_input("Расскажи подробнее, если хочешь")
    if st.button("Дальше"):
        st.session_state["situation"] = situation
        st.session_state["situation_text"] = situation_text
        st.session_state["screen"] = 5
        st.rerun()
elif st.session_state["screen"] == 5:
    hard = st.radio("Было ли трудно понять и назвать, что ты чувствуешь?", index=None, options=["Легко", "Немного трудно", "Очень трудно"])
    bridge = st.radio("Спасибо за твои ответы. Хочется ли тебе поделиться этим с кем-то из близких?", index=None, options=["Да, с кем-то близким", "Нет, справлюсь сам(а)", "Пока не знаю"])
    if st.button("Завершить"):
        st.session_state["hard"] = hard
        st.session_state["bridge"] = bridge
        with open("sessions_ru.csv", "a", newline="", encoding="utf-8-sig") as f:
                writer = csv.writer(f)
                writer.writerow([datetime.now(), st.session_state.get("chosen", ""), st.session_state.get("text", ""), ','.join(st.session_state.get("found", [])), st.session_state.get("body", ""), st.session_state.get("changed", ""),  st.session_state.get("situation", ""), st.session_state.get("situation_text", ""), st.session_state.get("hard", ""), st.session_state.get("bridge", "")])
        st.session_state["screen"] = 6
        st.rerun()
elif st.session_state["screen"] == 6:
    st.write("Спасибо, что поучаствовал(а) в тестировании!")
