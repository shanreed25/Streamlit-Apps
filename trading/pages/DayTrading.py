import streamlit as st
from modules.navigation import SidebarNav


def dayTrading():
    st.title("Day Trading")
    st.markdown("*Suited for individuals who thrive in a fast-paced, high-pressure environment and can dedicate full attention to the markets during trading hours*")
    st.markdown("* buy and sell financial securities (like stocks, currencies, or options) within the same trading day")
    st.markdown("* aiming to profit from small, short-term price fluctuations and intraday market volatility, rather than holding investments overnight to avoid risk")
    st.markdown("* involves rapid, frequent trades using technical analysis and news to capitalize on momentary price swings")
    st.markdown("* extremely risky and can lead to substantial losses")
    st.markdown("* demands deep market understanding, quick decision-making, and discipline ")

    st.markdown("### Key Characteristics")
    st.markdown("* Short-Term Focus")
    st.markdown("* Intraday")
    st.markdown("* High Risk, High Reward")
    st.markdown("* Requires Skill")

    st.markdown("*The primary difference between day trading and swing trading is the holding period for a position. Day traders open and close positions within the same trading day to profit from small, frequent price movements, while swing traders hold positions for several days to a few weeks to capture larger price 'swings'.*")
    st.markdown("*Many traders use a combination of both styles depending on market conditions*")


def main():
    SidebarNav()
    dayTrading()

if __name__ == "__main__":
    main()
