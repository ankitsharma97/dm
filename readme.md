# Endpoint
# Bank List Endpoint
`https://dm-89bh.onrender.com/banks/`

# Branch Search Endpoint 
`https://dm-89bh.onrender.com/branch-search/?branch_name=kak`


## Prerequisites

- Python 3.7+
- Git
- Virtualenv

## Setup Instructions

1. **Install Python:** [Download and install Python](https://www.python.org/downloads/).

2. **Create a Virtual Environment:**

    ```bash
    python -m venv venv
    ```

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

3. **Clone the Project:**

    ```bash
    git clone https://github.com/ankitsharma97/dm
    cd dm
    ```

4. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```


    ```
5. **Run the Server:**

    ```bash
    python manage.py runserver
    ```

# dm

# API Testing with Postman and cURL

## 1. Using Postman

Postman is a popular tool for testing APIs.

### Download Postman
[Postman Download](https://www.postman.com/downloads/)

### Bank List Endpoint

1. Create a new request.
2. Set the request type to **GET**.
3. Enter the URL: `http://127.0.0.1:8000/banks/`
4. Click **Send** to see the response, which should return a list of unique banks.

### Branch Search Endpoint

1. Create a new request.
2. Set the request type to **GET**.
3. Enter the URL: `http://127.0.0.1:8000/branch-search/?branch_name=<branch_name>/?ifsc=<IFSC_code>`
4. Replace `<branch_name>` with the name of the branch you're searching for.
5. Click **Send** to see the response, which should return details of the specific branch.

## 2. Using cURL

cURL is a command-line tool for making HTTP requests.


### Bank List Endpoint
`curl -X GET "http://127.0.0.1:8000/banks/"`

# Branch Search Endpoint 
`curl -X GET "http://127.0.0.1:8000/branch-search/?branch_name=<branch_name>"`

```bash