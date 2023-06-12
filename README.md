```
# Django REST Framework CRUD Project

This project demonstrates how to build a simple CRUD (Create, Read, Update, Delete) API using Django REST Framework.

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/iamakhildabral/DjangoCURD.git
   ```

2. Navigate to the project directory:

   ```
   cd DjangoCURD
   ```

3. Create a virtual environment:

   ```
   python -m venv env
   ```

4. Activate the virtual environment:

   - For Windows:

     ```
     env\Scripts\activate
     ```

   - For macOS/Linux:

     ```
     source env/bin/activate
     ```

5. Install the dependencies:

   ```
   pip install -r requirements.txt
   ```

6. Run the database migrations:

   ```
   python manage.py migrate
   ```

## Usage

1. Start the development server:

   ```
   python manage.py runserver
   ```

2. Open your web browser and navigate to `http://localhost:8000/` to access the API.

3. The API endpoints available are:

   - `api/v1/companies/`: Retrieve a list of all companies.
   - `api/v1/employees/`: Retrieve a list of all employees.
  


4. You can use tools like Django REST app or Postman to interact with the API.

## Customization

- If you want to customize the project further, you can modify the Django models in the `models.py` file.
- You can also define additional views, serializers, or authentication classes based on your requirements.
- Remember to run database migrations (`python manage.py migrate`) whenever you make changes to the models.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.
```

Feel free to modify and add more information to this README file based on your specific project requirements.
