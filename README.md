**Objective**
The objective of this assignment is to create a basic Vehicle Management System using the Django framework. The system will allow users to collect vehicle information along with the D.C. (Delivery Challan) number and P.O. (Purchase Order) number. With the entered P.O. number, the system will retrieve vendor data and product information. The security department will conduct quality checks, and finally, the vehicle will be checked out.
Requirements:
User Authentication: Implement a user authentication system to allow only authenticated users to access the system.

**Vehicle Information Form**
Create a form to collect vehicle information including:
Vehicle number
Vehicle type
Delivery Challan (D.C.) number
Purchase Order (P.O.) number
Validate the form data to ensure correctness and completeness.
Vendor and Product Information:
Create models for Vendor and Product.
Associate vendors with products using Foreign Key relationships.
When a P.O. number is entered, retrieve vendor data and associated product information.

**Quality Check**
Implement a quality check system.
The security department should have access to mark the quality check as pass/fail.
Display quality check status on the vehicle details page.

**Check-Out Process**
Implement a check-out process for vehicles.
Display relevant details of the vehicle including vendor information and quality check status.
Allow the security department to initiate the check-out process.

**Proper Flow**
Ensure that the system follows a proper flow:
User logs in
The user enters vehicle information
The system retrieves vendor and product information based on the P.O. number
Quality check is conducted
The vehicle is checked out

**Database Integration**
Utilize Django's ORM to interact with the database.
Design an appropriate database schema to store vehicle, vendor, and product information.

**Documentation**
Provide clear documentation on how to run the project.
Include explanations for each component and functionality.
Document all endpoints, request methods, request parameters, and response formats.
Create a Postman collection that includes pre-defined requests for all API endpoints.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/nikhilrai-tech/Vehicle-Management-System-with-Django.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd main
    ```

3. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

4. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Run migrations:**

    ```bash
    python manage.py migrate
    ```
