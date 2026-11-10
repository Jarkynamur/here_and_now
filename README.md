# Here and Now

Demo video: https://drive.google.com/drive/folders/10oO9NVvlpZ0EOpElwPYt7Rbx4fwrx3Ad?usp=sharing 

## What is this
This is a small prototype to understand one idea: can a short exercise help  people name what they feel right now? It is a pilot for a larger research project with three directions: 1. Real connection, 2.  Professional support, 3. AI as a mirror. This prototype tests a simple version of the third one, a "mirror" without AI

## How to run it
The prototype is built with Python and Streamlit. Firstly, you need to install Streamlit, then run the prototype from the project folder. A page opens in the browser.

Install Streamlit:
```bash
pip3 install streamlit
```

Run the Russian version: 

```bash
cd /path/to/the/project
python3 -m streamlit run app_screens.py
```

Run the English version: 

```bash
python3 -m streamlit run app_en.py
```

## Why I made it

In my survey, about one third of respondents share their thoughts with AI, and most of them named fear of judgment as a barrier to sharing with people. In Gestalt practice an exercise often starts with the question: " What are you feeling right now?". During my Gestalt training, I noticed that many people find it hard to answer this question at first. If it's hard to name a feeling, it is even harder to share it with someone.

My hypothesis: naming a feeling can be easier first step before sharing it with another person. This prototype tests whether an exercise helps people do it.

## How it works

The first screen explains the purpose of the exercise. The prototype is built with a rule-based mirror and no AI yet. 

Step 1. 
- The user can chooses one of six basic feelings. If  it's hard to choose, they can describe feelings in their own words (alternative flow). 

Step 2. 
- The mirror reflects the choice or the text back and asks a question about their body, to check whether the feeling fits.

Step 3. 
- The prototype asks "Where do you feel this in your body right now?". The person chooses: stronger, weaker, the same. I want to see if the feeling changes when a person pays attention on it.

Step 4.
- The person answers "What influences this feeling?". This gives context based on the results of pilot 1, when one person wanted to explain the situation.

- An optional field to tell more.

Step 5.
- The person says how hard it was to name the feeling.

- "Is there someone you want to share this with?". The user can also choose "No, not now". This question is the base of my idea: the exercise should lead toward a person only when the user wants it. 

The prototype says thank you, so people know the exercise is over.

Both flows (buttons and own words) are the same after step 2.

Safety:
If the user writes some risky words such as "hurt myself" or "don't want to live", the prototype stops the exercise and shows a message: "talk to a trusted person or contact a local support service". This is a first, minimal step toward direction 2, professional support. The word list is basic and can miss cases.

## Pilot results

Pilot 1

The first version was one long page. People didn't understand what the exercise was for and expected a survey. Also some people read "Where was it hard?" as a question about the interface. For the two people who wrote text, the program didn't find feeling words, because their  words weren't in my list. After the pilot I added a more detailed intro, separate screens, a direct question about how hard it was to name the feeling, an optional sharing step and new words.

Pilot 2

The exercise was clear to everyone. 
The first person didn't have any difficulties. 
The second asked if it was anonymous and said the question "What is happening with this feeling now?" needed a small clarification. She also noticed the feeling became stronger because she thought about it again. 
The third person describe positive feelings and felt the last question about sharing is only relevant for negative emotions. 

Two of three people mentioned anonymity and one said it kept her from opening up fully, even though I told her only I would see the answers.

**What I would change**

Make anonymity clearer and rewrite the sharing question so it works for positive feelings. Also to clarify the "what is happening now" question.


## What doesn't work yet

I tested only a few people, so the results are early.

The mirror idea follows simple rules. It only finds feeling words from my list and doesn't understand things like "not sad".

There is no AI yet. AI as the mirror is the next step.

## What is next

Next I want to test the prototype with more people and make anonymity clearer. Later, I want use AI as a tool to help people reflect their emotions and feelings. 

## How I worked

The idea, the research question, the flow, the questions, the tests and the notes are mine. I wrote the code in Python myself. I used Claude Code as a learning tool, like a talking textbook. It explained concepts, suggested next steps and helped me fix errors. I checked every change by running the prototype locally (localhost preview). I made a Russian copy of the English version for testing with users.

I also used Claude's help to create a .gitignore file, so participants' answers are not published. Two of the three people in pilot 2 mentioned anonymity.


### Testing

I ran 3 test sessions on version 1 and 3 test sessions on version 2 and took notes. After each round I improved the prototype based on my notes. For example, after round 1, I added an introduction explaining the purpose of this exercise, a question about what influenced the feeling, and the option "I can handle it myself." After the second session I changed the "I can handle it myself" to "No, not now" to make the option more flexible, not only regarding negative emotions.
