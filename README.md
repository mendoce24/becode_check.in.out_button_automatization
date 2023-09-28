UNDER THE CONSTRUCTION!!!!


# Automatised "push the button" code

## Usage

### Important

- If you follow those steps, keep in mind that your code will be running locally. It means that your terminal will be open showing the task running and it relays on your computer to be turned on and not be in sleep mode.

- In case you just want to run it locally, but is not interested on your terminal displaying the log, take a look at the method BackgroundScheduler (apscheduler).

- You can also store and run this code in a EC2 instance, feel free.

1. Install all the requirements
2. Change the becode token
3. Run the code

Voilà.


## Project Description

### Overview

This project contains a Python script designed to automate attendance recording for a learning institution, specifically designed for use with the BeCode platform. The script utilizes the BeCode API to record attendance based on a predefined schedule and the student's current location (at home or on-site).

### Features

- **Automatic Attendance Recording:** The script automates the process of recording attendance at specified times of the day, considering whether the student is at home or on-site.

- **Customizable Schedule:** The script allows you to configure the schedule for attendance recording, taking into account specific days of the week and time periods.

- **Location-Based Recording:** Attendance is recorded differently depending on whether the student is at home or on-site, ensuring accurate tracking.

### Workflow Integration

This project includes a GitHub Actions workflow that triggers the script based on a schedule defined in the workflow configuration. The workflow runs the script, records attendance, and logs the results.

### Usage

To use this script, you need to provide your personal access token for the BeCode platform as a secret in your GitHub repository settings. The script will use this token for authentication when making API requests.

Please refer to the setup and usage instructions in the [**Usage Guide**](USAGE.md) for detailed information on how to configure and run the script.

### Dependencies

This script depends on the following Python libraries:

- `requests`: Used for making HTTP requests to the BeCode API.
- `enum`: Used to define constants for attendance time periods.
- `datetime`: Used for working with date and time values.
- `os`: Used for accessing environment variables.
- `logging`: Used for generating log files for script execution.

### Contributing

If you would like to contribute to this project, feel free to fork the repository and submit pull requests. We welcome contributions, bug fixes, and feature enhancements.

### License

This project is licensed under the [MIT License](LICENSE.md). You are free to use, modify, and distribute this script as long as you adhere to the terms of the license.

### Contact

For any questions or inquiries related to this project, please contact [Your Name] at [your.email@example.com].
