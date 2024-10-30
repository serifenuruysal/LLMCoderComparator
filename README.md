<img width="1268" alt="Screenshot 2024-10-30 at 10 05 33" src="https://github.com/user-attachments/assets/4b4788ee-36d9-47af-b8f2-c9ae5d0cd5cd">


1. **Create a `.env` File**:  
   In your project directory, create a `.env` file with the following keys and placeholders for your API keys:

    ```plaintext
    MISTRAL_API_KEY='your_mistral_api_key'
    OPENAI_API_KEY='your_openai_api_key'
    GROQ_API_KEY='your_groq_api_key'
    ANTHROPIC_API_KEY='your_anthropic_api_key'
    ```

    > *Tip:* Replace each placeholder with your actual API keys!

2. **Install Required Libraries**:  
   Install all necessary dependencies by running:

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Application**:  
   Start the app using Streamlit:

    ```bash
    streamlit run app.py
    ```

4. **Enjoy the Experience!** 🎉  
   Once the app starts, head to the local URL provided to interact with your new project.
