import streamlit as st
from modules.navigation import SidebarNav

def swingTrading():
    st.title("Swing Trading")
    st.markdown("* buy and hold financial securities for several days to weeks")
    st.markdown("* aiming to profit from expected upward or downward market shifts over a medium-term period")
    st.markdown("* involves less frequent trades compared to day trading, relying on technical and fundamental analysis")
    st.markdown("* carries moderate risk, balancing potential rewards with holding positions overnight")
    st.markdown("* requires patience, market knowledge, and the ability to analyze trends and patterns")

    st.markdown("### Key Characteristics")
    st.markdown("* Medium-Term Focus")
    st.markdown("* Days to weeks")

    st.markdown("*The primary difference between day trading and swing trading is the holding period for a position. Day traders open and close positions within the same trading day to profit from small, frequent price movements, while swing traders hold positions for several days to a few weeks to capture larger price 'swings'.*")

    st.markdown("*The primary difference between day trading and swing trading is the holding period for a position. Day traders open and close positions within the same trading day to profit from small, frequent price movements, while swing traders hold positions for several days to a few weeks to capture larger price 'swings'.*")
    st.markdown("*Many traders use a combination of both styles depending on market conditions*")

def main():
    SidebarNav()
    swingTrading()

if __name__ == "__main__":
    main()
