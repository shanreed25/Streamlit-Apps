### Streamlit App template

1. `uv init`
2. `uv add streamlit`
3. **Navigation:** Configure Streamlit application to hide the multi-page navigation menu from the client's view
    - add `config.toml` file to  `.streamlit` folder
    - the `.streamlit` folder is the designated location where Streamlit looks for global configuration files for your specific project
    ```python
    # config.toml file
    [client]
    showSidebarNavigation = false
    ```
    **Useful For**
    - custom navigation and do not want the default sidebar menu to interfere or appear redundant - single-page apps that are designed to operate entirely within a single script without needing multi-page functionality
    - cleaner interface by removing visual clutter for users when the application's design benefits from a more minimalist layout
    - backward compatibility because it provides a simple way to revert to the pre-multi-page app appearance if you prefer the classic Streamlit layout
    - `modules/navigation.py` creates a custom navigation menu