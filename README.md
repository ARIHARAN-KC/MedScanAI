# MedScanAI - Advanced Medical Image Classification

[image](https://github.com/user-attachments/assets/c62b48c1-91cc-4efa-946a-fa405e9189fd)


**AI-powered diagnostics for faster, more accurate medical image analysis.**  
Upload X-ray, CT, MRI scans, or skin images, and get quick and highly accurate results.

---

## 📋 Table of Contents
- [About](#about)
- [How It Works](#how-it-works)
- [Why Choose MedScanAI?](#why-choose-medscanai)
- [Supported Conditions](#supported-conditions)

---

## ⚡️ How It Works
1. **Upload Your Image**  
    Drag and drop or select your medical image (X-ray, CT scan, MRI, etc.)  
   ![image](https://github.com/user-attachments/assets/7a56a37c-f415-4f01-b980-975d36f3cb56)

2. **AI Analysis**  
    Our deep learning model analyzes the image for potential abnormalities.  


3. **Get Results**  
    Receive a detailed report with findings and probability scores for different conditions.  
   ![image](https://github.com/user-attachments/assets/6d143e9b-5e2d-4020-a8e1-0ea1b2dedf0a)

---

## ✅ Why Choose MedScanAI?

| Feature           | Details |
|---------------------|---------|
| ⚡️ **Fast Analysis**           | Results within seconds using advanced AI. |
| 🎯 **High Accuracy**           | Achieves >95% precision across medical image types. |
| 🔒 **Secure & Private**        | All medical data is encrypted and never stored permanently. |
| 🩺 **Easy to Use**              | Simple drag, drop, and review results workflow. |

---

## 🩺 Supported Conditions
| Condition       | Supported Imaging | Details |
|-----------------|------------------|---------|
| 🫁 Chest Disease     | Chest X-ray      | High precision detection of lung infections.![image](https://github.com/user-attachments/assets/e0f9c06a-ca41-4aa9-8b0c-34badf29ad78)
| 🧠 Brain Tumor   | MRI              | Identifies abnormal growths in brain scans. !![image](https://github.com/user-attachments/assets/299ba87c-b732-4e1c-98c2-b39452be693c)
| 🩺 Kidney Disease | CT / MRI / X-ray| Detects kidney-related anomalies. ![image](https://github.com/user-attachments/assets/d722c216-2f9d-4669-9931-9c71f5d7fa54)
| 🩹 Skin Disease  | Skin Images      | Detects and classifies skin conditions. !![image](https://github.com/user-attachments/assets/a3af6f4b-1762-426e-b5f6-c4a7683dc053)

---
## ⚙️ Installation

### Prerequisites

* Python 3.9 or 3.10
* git
* virtualenv

### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/MedScanAI.git
   cd MedScanAI
   ```
2. Create a virtual environment and activate it:

   ```bash
   python -m venv env
   .\env\Scripts\activate    # Windows
   source env/bin/activate    # macOS/Linux
   ```
3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```
4. (Optional) Install GPU support if needed. See the relevant deep learning framework installation guides.

---

## 🚀 Usage

1. Run database migrations:

   ```bash
   python manage.py migrate
   ```
2. Start the Django development server:

   ```bash
   python manage.py runserver
   ```
3. Open the app in your browser:

   ```
   http://127.0.0.1:8000/
   ```
4. Upload an image and get the results.

---

## 🛠 Technologies Used

* **Backend:** Django, Python
* **Machine Learning:** TensorFlow / PyTorch
* **Database:** SQLite 
* **UI Framework:** TailwindCSS
* **Tools:** Git, GitHub, Visual Studio Code

---

## Author
https://github.com/ARIHARAN-KC
