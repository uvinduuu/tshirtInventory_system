# T-shirt Inventory Q&A System

This repository contains a Streamlit application designed to manage a T-shirt inventory system through natural language processing (NLP). The system utilizes LangChain and OpenAI's GPT models to interpret user questions, generate SQL queries, and provide accurate responses based on the inventory data.

## Features

- **NLP-Driven Q&A:** Users can ask natural language questions regarding the T-shirt inventory, and the system responds with precise answers generated from corresponding SQL queries.
- **Streamlit Interface:** Provides an intuitive and user-friendly web interface for inputting questions and viewing answers.
- **Few-Shot Learning:** The model is trained using a few-shot learning approach, enhancing its ability to handle specific types of queries effectively.

## Project Overview

### Few-Shot Learning with OpenAI

Few-shot learning is a technique where a model learns to perform a task from a small number of examples. In this project, we utilize few-shot learning to train the model with specific examples of inventory-related questions and their corresponding SQL queries. This helps the model understand and generate appropriate SQL queries for similar questions in the future.

### LangChain and OpenAI Integration

LangChain is a powerful tool that integrates with various NLP and machine learning libraries. In this project, we use LangChain to connect OpenAI's GPT models with our SQL database. The workflow involves:
1. Receiving a user question from the Streamlit interface.
2. Using the LangChain model to interpret the question and generate an SQL query.
3. Executing the SQL query against the inventory database.
4. Returning the results to the user through the Streamlit interface.

## Files

- `few_shots.py`: Contains example questions, their corresponding SQL queries, expected results, and answers to train the model.
- `langchain_helper.py`: Sets up the environment and defines functions to create a few-shot database chain using LangChain and OpenAI.
- `main.py`: Streamlit application that provides the web interface and integrates the NLP model with the SQL database.
- `db_creation_atliq_t_shirts.sql`: SQL file containing the database schema and initial data for the T-shirt inventory.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/uvinduuu/tshirtInventory_system.git
   ```

2. Navigate to the directory
   ```bash
   cd tshirtInventory_system
   ```
3. Set up the SQL database:

Ensure you have MySQL installed and running on your machine.
Create a database and import the provided SQL file:

```bash
mysql -u your_username -p your_password -h your_host -e "CREATE DATABASE tshirt_inventory;"
mysql -u your_username -p your_password -h your_host tshirt_inventory < tshirt_inventory.sql
```

4. Set up environment variables in a .env file:

```makefile
OPENAI_API_KEY=your_openai_api_key
DB_HOST=your_host
DB_USER=your_username
DB_PASSWORD=your_password
DB_NAME=tshirt_inventory
```

5. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
bash

6. Set up environment variables in a .env file:

```makefile
OPENAI_API_KEY=your_openai_api_key
```

7. Run the Streamlit application

```bash
streamlit run main.py
```

- Enter your inventory-related question in the input box.
= View the generated answer based on the inventory data.

*Example Questions
"How many T-shirts do we have left for Nike in XS size and white color?"
"How much is the total price of the inventory for all S-size T-shirts?"
"If we sell all Levi’s T-shirts today with applied discounts, how much revenue will our store generate?"*
