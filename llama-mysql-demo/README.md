# llama-mysql-demo

## Overview
This project demonstrates how to set up a MySQL database and interact with it using Python. It includes scripts for installing MySQL, creating a database, and setting up a `users` table. The main application file showcases how to use the `llama-index` library to interact with the database.

## Project Structure
```
llama-mysql-demo
├── src
│   ├── setup_mysql.py        # Script to install MySQL and set up the database
│   ├── llama_index_demo.py   # Main application demonstrating database interaction
│   └── utils.py              # Utility functions for database operations
├── requirements.txt          # List of dependencies
└── README.md                 # Project documentation
```

## Installation Instructions
1. **Install MySQL**: 
   - Follow the instructions for your operating system to install MySQL. You can find the installation guide on the [MySQL official website](https://dev.mysql.com/doc/refman/8.0/en/installing.html).

2. **Set Up the Database**:
   - Run the `setup_mysql.py` script located in the `src` directory. This script will create a database named `test_db` and a `users` table with appropriate fields.

3. **Install Dependencies**:
   - Use the following command to install the required Python packages:
     ```
     pip install -r requirements.txt
     ```

## Usage
- After setting up the database and installing the dependencies, you can run the main application using:
  ```
  python src/llama_index_demo.py
  ```

## Contributing
Feel free to submit issues or pull requests if you have suggestions or improvements for this project.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.