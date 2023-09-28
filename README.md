# Automated BeCode "push the button" script
## Project Description

This project contains a Python script designed to automate attendance recording for a [My BeCode platform](https://my.becode.org/dashboard). The script utilizes the BeCode API to record attendance based on a predefined schedule and the student's current location (at home or on-site).
## Features

- **Automatic Attendance Recording:** The script automates the process of recording attendance at specified times of the day, considering whether the student is at home or on-site.

- **Customizable Schedule:** The script allows you to configure the schedule for attendance recording, taking into account specific days of the week and time periods.

- **Location-Based Recording:** Attendance is recorded differently depending on whether the student is at home or on-site, ensuring accurate tracking.
## Workflow Integration

This project includes a GitHub Actions workflow that triggers the script based on a schedule defined in the workflow configuration. The workflow runs the script, records attendance, and logs the results.
## Usage

To use this script make a fork of [this repository](https://github.com/MykolaSenko/becode_check.in.out_button_automatization). 
In order to authenticate with the BeCode API, you need to provide your personal access token for the BeCode platform as a secret in your GitHub repository settings. The script will use this token for authentication when making API requests. You can find your personal access token at **mybecode --> inspect --> network --> fetch/xhr --> name (graph.becode.org) --> headers (request headers) --> authorization**.
Copy your personal access token and paste it into the **Value** field in the workflow configuration, using this [Tutorial](https://github.com/Azure/actions-workflow-samples/blob/master/assets/create-secrets-for-GitHub-workflows.md). Give a name to your secret **"TOKEN"**. The script will use this token for authentication when making API requests.
You are set! The script will run automatically according to the schedule you defined in the workflow configuration.

Voilà.
### Dependencies

This script depends on the following Python libraries:

- `requests`: Used for making HTTP requests to the BeCode API.
- `enum`: Used to define constants for attendance time periods.
- `datetime`: Used for working with date and time values.
- `os`: Used for accessing environment variables.
- `logging`: Used for generating log files for script execution.
## Timeline

This project was finished on September 29, 2023.
## The Team

The project was made by Junior AI & Data Engineers:
    
**Andreia Heringer Negreira**: [LinkedIn](https://www.linkedin.com/in/andreiahnegreira/), [GitHub](https://github.com/andreia-negreira)
    
**Mykola Senko**: [LinkedIn](https://www.linkedin.com/in/mykola-senko-683510a4), [GitHub](https://github.com/MykolaSenko)
## License

This project is under [GNU General Piblic License](./LICENSE) which allows to make modification to the code and use it for commercial purposes.

Gent, Belgium
September 29, 2023
