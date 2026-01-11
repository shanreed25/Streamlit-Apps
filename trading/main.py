import streamlit as st
from modules.navigation import SidebarNav

def main():
    SidebarNav()
    st.title("Trading")
    st.markdown("#### Trading is the act of buying and selling financial assets like stocks, currencies, or commodities with the goal of making a profit from price changes.")
    st.markdown("* often involves active, short-to-medium term strategies like day trading or swing trading, contrasting with long-term investing.")
    st.markdown("* requires understanding market movements and managing risk.")
    st.markdown("* uses strategies like technical analysis (chart patterns) or fundamental analysis (company health) to profit from price volatility")
    
    st.header("Key Characteristics")
    st.markdown("* **Profit Goal:** To buy low and sell high (or vice versa with short selling)")
    st.markdown("* **Active vs. Passive:** Active trading involves frequent buying and selling to capitalize on short-term market movements, while passive trading focuses on long-term investment strategies with less frequent transactions.")
    st.markdown("* **Timeframes:** Varies from minutes or hours (day trading) to several days or weeks (swing trading)")
    st.markdown("* **Risk Management:** Essential to protect capital through techniques like stop-loss orders and position sizing.")

    st.header("What is Traded?")
    st.markdown("* Stocks, shares of public companies")
    st.markdown("* Forex (Currencies), foreign exchange market, trading  global currency pairs (e.g., EUR/USD)")
    st.markdown("* Commodities, raw materials like gold, oil, and agricultural products")
    st.markdown("* Cryptocurrencies, digital or virtual currencies using cryptography for security (e.g., Bitcoin, Ethereum)")
    st.markdown("* Derivatives, financial contracts whose value is derived from an underlying asset, such as futures or options")

    st.header("Types of Trading")
    st.markdown("* **Day Trading:** Opening and closing positions within the same day.\n    * Suited for individuals who thrive in a fast-paced, high-pressure environment and can dedicate full attention to the markets during trading hours  ")
    st.markdown("* **Swing Trading:** Holding positions for several days or weeks to capture price swings.\n    * Suitable for beginners or those with other commitments (like a full-time job) because it allows for a more relaxed pace and more time for analysis.")
    st.markdown("* **Scalping:** Making many small profits from tiny price changes.")
    st.markdown("* **Position Trading:** Holding for months or years, similar to investing but with active management. ")




if __name__ == "__main__":
    main()
