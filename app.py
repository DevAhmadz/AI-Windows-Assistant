from pin_check import verify_pin
import streamlit as st
from intent_matcher import get_intent
from command_router import run_command
from logger import log_action


st.set_page_config(page_title="AI Windows Assistant", page_icon="🤖")

st.title("🤖 Offline AI IT Support Assistant")
st.markdown("Ask a system-related question like:")
st.markdown("- *'Why is my internet not working?'*")
st.markdown("- *'Start menu isn’t responding'*")
st.markdown("---")

user_input = st.text_input("💬 Your issue:")

if user_input:
    intent = get_intent(user_input)
    if intent:
        st.success(f"🧠 Detected issue: `{intent}`")
        with st.expander("🔐 Enter PIN to confirm execution"):
            pin_input = st.text_input("Enter 4-digit PIN", type="password")
            if st.button("✅ Run Fix"):
                if verify_pin(pin_input):
                    result = run_command(intent)
                    log_action(user_input, intent, result)
                    st.success("✅ PIN correct — fix executed.")
                    st.info(result)
            else:
                st.error("❌ Incorrect PIN. Action not allowed.")


    else:
        st.warning("❓ I couldn't match that to any known issue. Try rephrasing.")
