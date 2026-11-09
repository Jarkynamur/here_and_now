import streamlit as st
import csv
from datetime import datetime
stems = ["sad", "angry", "afraid", "disgust", "scared", "panic", "surpris", "happy", "joy", "fear", "anger", "calm", "envious", "peaceful", "glad", "lonely", "empty", "hurt", "annoy", "frustrated", "guilty", "ashamed", "embarrassed", "confused", "overwhelmed", "stressed", "anxi", "nervous", "worr", "excit", "hopeful", "gratef", "relieved", "shocked", "disappointed", "jealous", "envy", "resentful", "bored", "tired", "sleepy", "restless", "distracted", "unmotivated", "apathetic", "indifferent"]
risk_words = ["suicide", "kill myself", "want to die", "hurt myself", "don't want to live"]
st.title("Here and Now")
st.write("This is a learning prototype, not therapy")
st.write("What are you feeling right now?")
if st.button("Joy"):
    st.write('You chose "joy". Where do you feel it in your body right now?')
    st.session_state["chosen"] = "joy"
if st.button("Sadness"):
    st.session_state["chosen"] = "sadness"
    st.write('You chose "sadness". Where do you feel it in your body right now?')
if st.button("Anger"):
    st.session_state["chosen"] = "anger"
    st.write('You chose "anger". Where do you feel it in your body right now?')
if st.button("Fear"):
    st.session_state["chosen"] = "fear"
    st.write('You chose "fear". Where do you feel it in your body right now?')
if st.button("Disgust"):
    st.write('You chose "disgust". Where do you feel it in your body right now?')
    st.session_state["chosen"] = "disgust"
if st.button("Surprise"):
    st.write('You chose "surprise". Where do you feel it in your body right now?')
    st.session_state["chosen"] = "surprise"
user_text = st.text_area("Can't choose? Write in your own words, however you can")
if st.button("Send"):
    chosen = st.session_state.get("chosen", "")
    for phrase in risk_words:
        if phrase in user_text.lower():
            st.write("What you wrote sounds important. I can't help with this here. Please talk to someone close to you or contact a local helpline.")
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
    st.write("You wrote: ", text)
    if found:
        st.write("Here is what I see. Feelings: ", ", ".join(found))
        if chosen:
            st.write(f'You chose {chosen} and in your words I see: {", ".join(found)}. Both can be here at the same time.')
    else:
        st.write("You told me about events. What do you feel right now, while you are writing this?")
    changed = st.text_input("Did anything change? What?")
    if st.button("Next"):
        st.session_state["changed"] = changed
        st.session_state["next_done"] = True
    if st.session_state.get("next_done"):
        hard = st.text_input("Where was it hard? What was unclear?")
        bridge = st.text_input("Thank you for sharing. Who close to you could you tell about this?")
        if st.button("Finish"):
            st.session_state["hard"] = hard
            st.session_state["bridge"] = bridge
            st.write("Thank you!")
            with open("sessions.csv", "a", newline="", encoding="utf-8") as f:
                    writer = csv.writer(f)
                    writer.writerow([datetime.now(), st.session_state.get("chosen", ""), st.session_state.get("text", ""), ','.join(st.session_state.get("found", [])), st.session_state.get("changed", ""), st.session_state.get("hard", ""), st.session_state.get("bridge", "")])