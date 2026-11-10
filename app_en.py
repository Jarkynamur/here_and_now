import streamlit as st
import csv
from datetime import datetime
stems = ["sad", "angry", "afraid", "disgust", "despond", "anticipat", "uncertain", "cheerful", "scared", "panic", "surpris", "happy", "joy", "fear", "anger", "calm", "envious", "peaceful", "glad", "lonely", "empty", "hurt", "annoy", "frustrated", "guilty", "ashamed", "embarrassed", "confused", "overwhelmed", "stressed", "anxi", "nervous", "worr", "excit", "hopeful", "gratef", "relieved", "shocked", "disappointed", "jealous", "envy", "resentful", "bored", "tired", "sleepy", "restless", "distracted", "unmotivated", "apathetic", "indifferent"]
risk_words = ["suicide", "kill myself", "want to die", "hurt myself", "don't want to live"]
SAVE_ANSWERS = False
if "screen" not in st.session_state:
    st.session_state["screen"] = 1
step = st.session_state["screen"]
if step <= 5:
    st.caption(f"Step {step} of 5")
if st.session_state["screen"] == 1:
    st.title("Here and Now")
    st.info("This is a learning prototype for my research: I'm exploring how people can name their feelings. This is not therapy. It will take about 2 minutes.")
    st.success("There are no right answers, just answer how you feel right now. This is a demo version: your answers are not saved.")
    st.write("**What are you feeling right now?**")
    if st.button("Joy"):
        st.session_state["chosen"] = "joy"
        st.session_state["screen"] = 2
        st.rerun()
    if st.button("Sadness"):
        st.session_state["chosen"] = "sadness"
        st.session_state["screen"] = 2
        st.rerun()
    if st.button("Anger"):
        st.session_state["chosen"] = "anger"
        st.session_state["screen"] = 2
        st.rerun()
    if st.button("Fear"):
        st.session_state["chosen"] = "fear"
        st.session_state["screen"] = 2
        st.rerun()
    if st.button("Disgust"):
        st.session_state["chosen"] = "disgust"
        st.session_state["screen"] = 2
        st.rerun()
    if st.button("Surprise"):
        st.session_state["chosen"] = "surprise"
        st.session_state["screen"] = 2
        st.rerun()
    user_text = st.text_area("Can't choose? Write in your own words, however you can")
    if st.button("Send"):
        chosen = st.session_state.get("chosen", "")
        for phrase in risk_words:
            if phrase in user_text.lower():
                st.write("This sounds important. I can't help with this here. Please talk to a trusted person or contact a local support service.")
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
        st.write("Your text: ", text)
        if found:
            st.write("Here is what I see. Feelings: ", ", ".join(found))
            if chosen:
                st.write(f'You chose: {chosen}, and in your words I see: {", ".join(found)}. All of this can be here at once.')
        else:
            st.write("This is more about events. What do you feel right now, while you are writing this?")
    else:
        st.write(f'You chose: "{chosen}"')
    body = st.text_input("Where do you feel this in your body right now?")
    if st.button("Next"):
        st.session_state["body"] = body
        st.session_state["screen"] = 3
        st.rerun()
elif st.session_state["screen"] == 3:
    changed = st.radio("Is this feeling stronger, weaker, or the same as at the beginning?", index=None, options=["Stronger", "Weaker", "The same"])
    if st.button("Next"):
        st.session_state["changed"] = changed
        st.session_state["screen"] = 4
        st.rerun()
elif st.session_state["screen"] == 4:
    situation = st.radio("What influenced this feeling?", index=None, options=["Something happened", "A person", "A thought or worry", "My body (tired, tense)", "I don't know"])
    situation_text = st.text_input("Tell me more, if you want")
    if st.button("Next"):
        st.session_state["situation"] = situation
        st.session_state["situation_text"] = situation_text
        st.session_state["screen"] = 5
        st.rerun()
elif st.session_state["screen"] == 5:
    hard = st.radio("Was it hard to understand and name what you feel?", index=None, options=["Easy", "A bit hard", "Very hard"])
    bridge = st.radio("Thank you for your answers. Is there someone you want to share this with?", index=None, options=["Yes, with someone close", "No, not now", "Not sure yet"])
    if st.button("Finish"):
        st.session_state["hard"] = hard
        st.session_state["bridge"] = bridge
        if SAVE_ANSWERS:
            with open("sessions_en.csv", "a", newline="", encoding="utf-8-sig") as f:
                    writer = csv.writer(f)
                    writer.writerow([datetime.now(), st.session_state.get("chosen", ""), st.session_state.get("text", ""), ','.join(st.session_state.get("found", [])), st.session_state.get("body", ""), st.session_state.get("changed", ""),  st.session_state.get("situation", ""), st.session_state.get("situation_text", ""), st.session_state.get("hard", ""), st.session_state.get("bridge", "")])
        st.session_state["screen"] = 6
        st.rerun()
elif st.session_state["screen"] == 6:
    st.write("Thank you for participating in the testing!")
