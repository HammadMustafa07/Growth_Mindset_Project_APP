# import streamlit as st

# st.header("✅Growth Mindset Challange")
# st.subheader("Welcome to the Growth Mindset App — where comfort zones end and real growth begins. Challenge yourself, break limits, and become the person you were meant to be. It all starts here.")

# reason = st.text_input("Write the Reason You are here", "Type Here..")

# if(st.button("Submit")):
#     st.success("If you think that then you are at the right place")

# practises = st.text_input("Did you practises what u learnt Yesterday?", "Type Here in one word")


# # practises = st.text_input("Did you practice? (yes/no)")

# if practises.lower() == "yes":
#     st.success("Then we can move to the next question!")
# elif practises:
#     st.error("Then complete the revision first.")


# learnings = st.text_input("what did you learn today?", "Type Here")

# if(st.button("submit")):
#     st.success("Your learnings have been recorded keep going")

# st.info("“Growth begins at the edge of your comfort zone.”")
# st.info("“A path for Heaven feels like hell and the path for Hell feels like Heaven”")

# # or use st.success / st.warning for different vibes

# goal = st.text_input("what's your Goal for today?")

# if(st.button("Set")):
#     st.success("Your Goal has been set keep going")
#     st.success("Set your goals high and work hard — even if you fail, you'll fall above everyone else's success.")
#     st.success("The world’s champions were once beginners.")
    
# st.info("See You tomorrow Champ!")






import streamlit as st

st.header("✅ **Growth Mindset Challenge** 💪")
st.subheader("Welcome to the **Growth Mindset App** — where comfort zones end and real growth begins. 🌱 Challenge yourself, break limits, and become the person you were meant to be. It all starts here. 🚀")

reason = st.text_input("📝 **Why are you here?**", "Type Here..")

if(st.button("submit")):
    st.success("✅ **If you think that, you're in the right place!**")

practises = st.text_input("💪 **Did you practice what you learned yesterday?**", "Type Here in one word")

if practises.lower() == "yes":
    st.success("🔥 **Awesome! Let's move on to the next question!**")
elif practises:
    st.error("❗ **Finish your revision first, then let's move forward!**")

learnings = st.text_input("📚 **What did you learn today?**", "Type Here")

if(st.button("Submit")):
    st.success("📈 **Your learnings have been recorded. Keep going!**")

st.info("✨ **“Growth begins at the edge of your comfort zone.”**")
st.info("💭 **“A path to Heaven feels like hell, and the path to Hell feels like Heaven.”**")

goal = st.text_input("🎯 **What's your goal for today?**")

if(st.button("Set")):
    st.success("✅ **Your goal has been set. Keep pushing forward!**")
    st.success("🚀 **Set your goals high and work hard — even if you fail, you'll land higher than others' success.**")
    st.success("🌟 **The world’s champions were once beginners.**")

st.info("👋 **See you tomorrow, Champ!**")
