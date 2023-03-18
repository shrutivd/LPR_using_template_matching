# LPR_using_template_matching
The project contains logic that reads the license plate and returns the owner name and state to which the license plate is registered.

To Run Application: $ python3 app.py <IMAGE_FILE_NAME>

To Run a Faster Version of The Application: $ python3 app.py --fast <IMAGE_FILE_NAME>

To Run Frontend (Please use images in static/images or add an image to static/images to use): $ python3 flaskApp.py

To Test Application: $ python3 test.py

WARNING: This application may run into errors with accuracy when running it on MacOS.
This is due to an issue with the glob library compatibility with MacOS.
If the license plate characters are being identified as mostly 1’s, try running on an MCECS Windows Remote Lab computer at https://intranet.cecs.pdx.edu/remote_lab/remotelab.php.
This should fix the issue.