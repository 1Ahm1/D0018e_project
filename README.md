D0018e_project
This is a project repository for the D0018e course at Luleå University of Technology.

Project description
The project is focused on developing a web application for managing tasks and projects, aimed at small teams and individuals. The application will allow users to create projects, add tasks, set deadlines, assign tasks to team members, and track progress. It will also include features such as notifications, chat, and file sharing.

Installation and setup
To run the application locally, follow these steps:

Clone the repository to your local machine.
Install the necessary dependencies by running npm install in the project directory.
Set up the database by running the scripts in the db_scripts folder.
Create a .env file in the project directory with the following environment variables:
makefile
Copy code
DB_HOST=<your_database_host>
DB_PORT=<your_database_port>
DB_NAME=<your_database_name>
DB_USER=<your_database_username>
DB_PASSWORD=<your_database_password>
Start the server by running npm start.
Access the application at http://localhost:3000 in your web browser.
Contributing
We welcome contributions to the project. If you find a bug or have a feature request, please open an issue in the GitHub repository. If you would like to contribute code, please follow these steps:

Fork the repository to your own GitHub account.
Create a new branch for your changes.
Make your changes and commit them to your branch.
Push your branch to your forked repository.
Open a pull request in the original repository with your changes.
License
This project is licensed under the MIT License. See the LICENSE file for details.
