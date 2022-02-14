# AWS S3 File Upload using boto3 with and without multi-threading

Follow the steps below to run this project:

1.  Make sure you have the following development environment:

    1.  Python 3.8.10 (You can be flexible with the version but, Implementation is tested with this version only).
    2.  Django 4.0.1 (You can be flexible with the version but, Implementation is tested with this version only).
    3.  Any IDE or text editor of your choice.
    4.  Access to Command-Line or Terminal.

1.  Clone this repository.
1.  Open the terminal or command line.
1.  Navigate to the location where you cloned this repository
1.  Install the dependencies by typing following command:
  
      `pip install -r requirements.txt`
      
1.  Go to s3_file_upload folder and run the Django server by entering following command:

      `python manage.py runserver`
      
Now, the project should be up and running. By default django server runs in <b>localhost:8000</b> and you should be able to access the

- simple_file_upload app by typing http://localhost:8000/simple-file-upload address in the address bar of the browser.
- multipart_upload app by typing http://localhost:8000/multipart-upload address in the address bar of the browser.


Visit [File Upload Time Improvement with AWS S3 Multipart Parallel Upload](https://muneebshahid.com/improvement-with-s3-multipart-parallel-upload/) for detailed explanation.

Have Fun :smile:
