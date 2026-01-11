import streamlit as st
from modules.navigation import SidebarNav

def main():
    SidebarNav()
    st.title("Trading")
    st.markdown("#### Trading is the act of buying and selling financial assets like stocks, currencies, or commodities with the goal of making a profit from price changes, often involving active, short-to-medium term strategies like day trading or swing trading, contrasting with long-term investing.")
    st.markdown("*The primary difference between day trading and swing trading is the holding period for a position. Day traders open and close positions within the same trading day to profit from small, frequent price movements, while swing traders hold positions for several days to a few weeks to capture larger price 'swings'.*")
    st.markdown("#### Day Trading")
    st.markdown("*Suited for individuals who thrive in a fast-paced, high-pressure environment and can dedicate full attention to the markets during trading hours*")

    st.markdown("#### Swing Trading")
    st.markdown("*Suitable for beginners or those with other commitments (like a full-time job) because it allows for a more relaxed pace and more time for analysis. Many traders use a combination of both styles depending on market conditions*")

    st.markdown("##### Many traders use a combination of both styles depending on market conditions")
if __name__ == "__main__":
    main()
