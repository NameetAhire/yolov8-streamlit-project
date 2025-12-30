# **YOLOv8 Object Detection Web App (Streamlit)**



This project is a Streamlit web application that uses YOLOv8 deep learning models to perform real-time object detection on images.

It supports multiple custom-trained models such as fire detection, Accident detection, weapon detection, and more.



##### **📁 Project Structure**

streamlit/

│

├── mp.py                     # Main Streamlit application

├── f.py                      # Helper / model logic file

├── answer\_phone.py           # Additional processing script

├── requirements.txt          # Python dependencies

├── links.txt                 # Reference links

│

├── input/                    # YOLO model files

│   ├── yolov8n.pt

│   ├── fire.pt

│   ├── fall.pt

│   ├── w.pt

│   └── c.pt

│

├── uploads/                  # Uploaded images (runtime)

│

├── downloaded\_image.jpg      # Sample image

├── BE\_project (1).pdf        # Project report

├── mjpr-3.pptx               # Project presentation

└── certif.pdf                # Certificate



##### **Features**



* &nbsp;Upload images via web interface
* &nbsp;Detect objects using YOLOv8
* &nbsp;Fire detection
* &nbsp;Fall detection
* &nbsp;Accident Detection
* &nbsp;Weapon Detection
* &nbsp;Simple and interactive Streamlit UI





##### **Requirements**



Python 3.8 or above



Virtual environment (recommended)





##### **Install dependencies using:**



*pip install -r requirements.txt*





##### **How to Run the Project**



Navigate to the project directory



*cd streamlit*





Run the Streamlit app



*streamlit run mp.py*





Open your browser



*http://localhost:8501*





##### **Models Used**



* yolov8n.pt – Base YOLOv8 model
* fire.pt – Fire detection model
* fall.pt – Fall detection model
* w.pt, c.pt – Custom-trained object models



All models are loaded dynamically from the input/ folder.





##### **Output**



Detected objects are displayed with:



* Bounding boxes
* Class labels
* Confidence scores
* Processed image shown directly on the web app





##### **Documentation**



* Project Report: BE\_project (1).pdf
* Presentation: mjpr-3.pptx
* Certificate: certif.pdf





##### **Future Enhancements**



* Cloud deployment
* Mobile-friendly UI
* Detection analytics dashboard





##### **Author**



Nameet Ahire

Computer Vision \& Deep Learning using YOLOv8


Note : In mp.py there are some error because of twilio and email password conflict with git. So to run the project properly you need to modify the mp.py file or you can completly remove the email and twilio function completely.
