# llm-demo: Exploring Large Language Models with Python

This folder, located within the `100-Days-Challenge-GenerativeAI` repository, contains Python scripts demonstrating how to interact with various Large Language Models (LLMs) through their respective APIs and libraries.

**📌 Purpose:**

The primary goal of this folder is to provide practical examples and code snippets for accessing and utilizing different LLMs. This serves as a learning resource for understanding the capabilities, functionalities, and implementation details of these models.

For a detailed blog post explaining different LLMs and how to use them, check out this blog post **[Exploring Different LLM Models: A Hands-on Guide](https://dev.to/sharsha315/exploring-different-llm-models-a-hands-on-guide-part-2-3d0h)**.

**📁 Contents:**

This folder includes Python files, each dedicated to showcasing a specific LLM or platform. You'll find examples covering:
- `awstitan_model.py` - Access and use **AWS Titan** from **Amazon Bedrock**
- `llama3_model.py` - Load and use models from **Hugging Face Transformers**
- `anthropic_model.py` - Interact with **Claude models** from Anthropic
- `mistral_model.py` - Use **Mistral models** for various text-based tasks
- `gemini_model.py` - Access **Gemini (Bard)** models 
- `cohere_model.py` - Work with **Cohere's language models**
- `deepseek_model.py` - Run **DeepSeek-R1 model** using **Amazon Bedrock**
- `groq_model.py` - Access various LLMs using **Groq** platform

**🚀 Requirements:**

Before running the scripts, ensure you have the following prerequisites:

1.  **Python:** Python 3.6 or later is recommended.
2.  **Required Libraries:** Install the necessary Python libraries using `pip`:

    ```bash
    pip install -r requirements.txt
    ```
3.  **API Keys/Credentials:** Obtain API keys or service account credentials from the respective LLM providers (AWS, Google Cloud, etc.). **Keep these credentials secure!**

**🚀 Usage:**

1.  **Clone the Repository:** Clone the repository to your local machine.
```bash
git clone https://github.com/sharsha315/100-Days-Challenge-GenerativeAI.git
```
2.  **Navigate to the `llm-demo` Folder:** Change your directory to the `llm-demo` folder.
3.  **Set API Keys/Credentials:** Create the `.env` file and add the API keys or credentials.
For Example:
   ```bash
   HF_TOKEN='"your_hugging_face_token"'
   MISTRAL_API_KEY="your_mistral_api_key"
   GOOGLE_API_KEY="your_google_api_key"
   GROQ_API_KEY="your_groq_api_key"
   AWS_ACCESS_KEY="your_aws_access_key"
   AWS_SECRET_KEY="your_aws_secret_key"
   COHERE_API_KEY="your_cohere_api_key"
   ANTHROPIC_API_KEY="your_anthropic_api_key"
   ```
4.  **Run the Scripts:** Execute the Python scripts using the Python interpreter:

    ```bash
    python anthropic_model.py
    python gemini_model.py
    # ... and so on
    ```
5.  **Explore and Modify:** Feel free to modify the scripts, experiment with different prompts, and explore the various parameters of the LLMs.

**Important Notes:**

* API costs may apply. Be mindful of your usage and monitor your spending.
* Rate limiting is common. Handle rate limits gracefully in your code.
* Model selection is crucial. Choose the model that best suits your specific needs.
* Ethical considerations are paramount. Use LLMs responsibly and avoid generating harmful or biased content.
* Refer to the specific LLM providers' documentation for the most accurate and up-to-date information.

**Contributions:**

Contributions to this folder are welcome! If you have any improvements, bug fixes, or new examples, feel free to submit a pull request.

**📜 License:**
This project is open-source and available under the **MIT License**.

**Author:** 
[Harsha S](https://www.x.com/sharsha315)

Happy Coding! 🚀💡