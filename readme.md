# Face Recognition Application

FRA is a face recognition application built using the Kivy framework. It allows users to perform user registration, login using facial recognition, and check the status of their device's camera.

## Features

- **User Registration:** Users can sign up by providing their full name and email. The registration data is stored in an SQLite database.

- **Face Recognition:** After registration, users can log in using facial recognition. The application uses saved facial data for recognition.

- **Camera Status Check:** Users can check the status of their device's camera to ensure it's functioning correctly.

## Installation

Follow these steps to install and run FRA on your local machine:

### 1. Clone the Repository

Use Git to clone this repository to your local machine.

```shell
git clone https://github.com/your_username/FRA.git
cd FRA
```

### 2. Create a Virtual Environment (Optional but Recommended)

We recommend creating a virtual environment to isolate the dependencies for this project. If you don't have `virtualenv` installed, you can install it using `pip`:

```shell
pip install virtualenv
```

Create a virtual environment and activate it:

```shell
virtualenv venv
source venv/bin/activate      # On Windows, use: venv\Scripts\activate
```

### 3. Install Dependencies

Install the required dependencies using the provided `requirements.txt` file:

```shell
pip install -r requirements.txt
```

### 4. Database Setup

The application uses SQLite for the database. You can use the default database name 'FRA.db' or specify a custom one. Make sure to create a new database or adjust the name in the `Database` class if needed.

### 5. Run the Application

Run the app using Python:

```shell
python main.py
```

### 6. Using the App

Once the app is running, you can use the "Sign Up" button to register a new user, the "Login" button to log in with facial recognition, and the "Check Camera" button to verify your device's camera status.

## Additional Notes

- This application is a sample and may require additional setup for facial recognition, such as configuring the facial recognition libraries and models.

- The database schema can be customized by modifying the `create_table` method in the `Database` class.

- Please ensure that your device has a functional camera for face recognition to work.

- Feel free to modify and extend the application to suit your specific requirements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

In this README, I've added instructions for creating a virtual environment, which is a good practice for isolating project dependencies. Users can follow these steps to set up the environment and install the necessary packages from the `requirements.txt` file.
