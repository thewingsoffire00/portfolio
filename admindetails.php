<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Edit Admin Page</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            margin: 0;
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100vh;
            background-image: url('img/loginpage.jpg'); /* Add your image URL here */
            background-size: cover;
        }

        .signup-container {
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100vh;
        }

        .signup-form {
            background-color: rgba(255, 255, 255, 0.8); /* Add a semi-transparent white background */
            padding: 70px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            width: 500px; /* Adjust the width as needed */
        }

        h1 {
            text-align: center;
            color: #333;
        }

        form {
            display: flex;
            flex-direction: column;
        }

        .form-group {
            margin-bottom: 15px;
        }

        label {
            color: #555;
        }

        input {
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 3px;
        }

        button {
            padding: 10px;
            background-color: #007BFF;
            color: #fff;
            border: none;
            border-radius: 3px;
            cursor: pointer;
        }

        button:hover {
            background-color: #0056b3;
        }

        .clearfix {
            clear: both;
        }

        .link-text {
            text-align: center;
            margin-top: 15px;
        }

        .link-text a {
            color: #007BFF;
            text-decoration: none;
        }
    </style>
</head>




<script>
    // Push a new state to the history whenever the page is loaded
    history.pushState(null, null, document.URL);

    // Disable the back and forward buttons
    window.addEventListener('popstate', function (event) {
      history.pushState(null, null, document.URL);
    });
  </script>

<body>

<?php
// Fetch user details based on user ID
$userId = 12; // Set the user ID to 12

// Connect to the database
$con = mysqli_connect("localhost", "admin", "admin", "miniproject");

if (mysqli_connect_errno()) {
    die("Database connection failed: " . mysqli_connect_error());
}

// Fetch user details based on user ID
$userData = mysqli_query($con, "SELECT * FROM customer_details WHERE id='$userId'");
$userDetails = ($userData) ? mysqli_fetch_array($userData) : [];

if (isset($_POST['submit'])) {
    // Update the customer_details table
    $mt1 = $_POST['email'];
    $mt2 = $_POST['password']; // Note: Handle password hashing securely in production

    $updateQuery = "UPDATE customer_details SET 
                    email = '$mt1',
                    password = '$mt2'
                    WHERE id = '$userId'";

    $updateResult = mysqli_query($con, $updateQuery);

    if ($updateResult) {
        echo "<script>alert('Profile updated successfully');</script>";
        header('location: adminpage.php');
        exit;
    } else {
        echo "<script>alert('Error updating profile: " . mysqli_error($con) . "');</script>";
    }
}
?>

<!-- Your HTML form goes here -->

<div class="signup-container">
    <div class="signup-form">
        <h1>Update Profile</h1>
        <form method="post" enctype="multipart/form-data">
            <!-- Add the left side of the form -->
            <div class="left-side">
                <div class="form-group">
                    <label for="first-name"><i class="fas fa-user"></i> Name/Email</label>
                    <input type="text" id="first-name" name="email" value="<?php echo isset($userDetails['email']) ? htmlspecialchars($userDetails['email']) : ''; ?>" required>
                </div>
                <!-- Add other left side form elements here -->
            </div>

            <!-- Add the right side of the form -->
            <div class="right-side">
                <div class="form-group">
                    <label for="middle-name"><i class="fas fa-lock"></i> New Password</label>
                    <input type="password" id="password" name="password" value="<?php echo isset($userDetails['password']) ? htmlspecialchars($userDetails['password']) : ''; ?>">
                </div>
                <!-- Add other right side form elements here -->
            </div>

            <!-- End of the right side -->
            <div class="clearfix"></div>
            <button type="submit" name="submit">Update Details</button>
        </form>
        <p class="link-text">
            <a href="adminpage.php"><i class="fas fa-home"></i> Back to Home</a>
        </p>
    </div>
</div>




</body>
</html>
