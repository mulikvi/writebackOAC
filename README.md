# OAC Writeback Gateway

<b>Overview</b><br>

Oracle Analytics Cloud (OAC) enables powerful reporting capabilities, including direct manipulation of database data from reports. However, a limitation arose due to the lack of an encrypted data gateway, which posed security and compliance risks.

To address this, the OAC Writeback Gateway script was developed. This solution involves a Flask application hosted on a Unix server that leverages OAC's Rest API functionality through a Go-URL to securely update database data. The application uses the jaydebeapi and jpype libraries for interacting with the database via microservices.

<b>Features</b><br>

Secure Database Updates: Enables secure writeback functionality from OAC to the database.<br>
Custom API Integration: Utilizes Flask and REST APIs for data updates.<br>
Real-Time Processing: Instantly updates the database upon user action in OAC.<br>
Flexible Architecture: Easily adaptable for different database systems using JDBC drivers.<br>
Role-Based Control: Ensures secure and controlled data manipulation.<br>

<b>Solution Architecture</b><br>

1. Components

	Oracle Analytics Cloud (OAC): The reporting platform, configured to interact with external APIs via Go-URL.<br>
	Flask Application: A lightweight Python-based web framework hosted on a Unix server.<br>
	Jaydebeapi and JPype Libraries: Provide a bridge for Python to connect with Java-based JDBC drivers for secure database access.<br>
	Unix Server: The hosting environment for the Flask application.<br>
	Oracle Database: The target database for updates triggered via OAC reports.<br>

2. Workflow

	Trigger: A user interacts with an OAC report, initiating a Go-URL API call.<br>
	API Call: The Go-URL sends a REST API request to the Flask application with the required payload.<br>
	Processing: The Flask application parses the payload and validates the request.<br>
	Database Update: Using jaydebeapi and jpype, the application securely connects to the database and performs the required data manipulation.<br>
	Response: The Flask application returns a status message (success or error) back to OAC for user feedback.<br>

<b>Prerequisites</b><br>

Oracle Analytics Cloud: Configure Go-URLs in OAC to trigger API calls.<br>
Unix Server: Set up a Unix server with Python installed.<br>
Oracle Database: Ensure JDBC drivers are available and accessible on the server.<br>
Python Libraries: Install the following Python libraries:<br>
Flask<br>
Jaydebeapi<br>
Jpype<br>
Secure Communication: Ensure HTTPS is configured for secure communication between OAC and the Flask application.<br>


The OAC Writeback Gateway project bridges the gap between Oracle Analytics Cloud and secure database manipulation, leveraging modern web technologies to meet business needs efficiently and securely.
