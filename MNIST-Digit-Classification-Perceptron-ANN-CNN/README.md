# MNIST Digit Classification using Perceptron, ANN and CNN

## 📌 Project Overview

This project focuses on **handwritten digit classification using neural networks**. The **MNIST handwritten digit dataset** is used to train and evaluate three different deep learning approaches:

1. **Perceptron / Single-Layer Neural Network**
2. **Artificial Neural Network (ANN)**
3. **Convolutional Neural Network (CNN)**

The main objective of this project is not only to classify handwritten digits from **0 to 9**, but also to understand how different neural network architectures perform when working with image data.

The project demonstrates the complete workflow of an image classification problem, including:

* Loading the dataset
* Understanding the dataset structure
* Checking for missing values
* Data preprocessing
* Pixel normalization
* Reshaping image data
* One-hot encoding of target labels
* Building neural network models
* Training and validation
* Model evaluation
* Comparing model performance
* Visualizing training accuracy and loss

---

## 🎯 Objectives

The major objectives of this project are:

* To understand the structure of the MNIST handwritten digit dataset.
* To preprocess image pixel data for neural network training.
* To implement a simple neural network as a baseline model.
* To build an ANN for handwritten digit classification.
* To implement a CNN specifically designed for image classification.
* To compare the performance of the three approaches.
* To understand the advantage of convolution and pooling operations for image data.

---

## 📊 Dataset

The project uses the **MNIST handwritten digit dataset** in CSV format.

Two files are used:

```text
mnist_train.csv
mnist_test.csv
```
🔗 Dataset Source

The complete dataset can be accessed from the following link:

MNIST Dataset – Dataset Link

(https://www.kaggle.com/datasets/oddrationale/mnist-in-csv)



## The training dataset contains:

* **60,000 images**
* **785 columns**

  * 1 column: `label`
  * 784 columns: pixel values
* Each image is originally represented as a **28 × 28 grayscale image**.

The notebook confirms that the training dataset has **60,000 rows and 785 columns**.

The dataset columns contain a target column named:

```text
label
```

followed by pixel columns ranging from:

```text
1x1 → 28x28
```

The notebook also verifies that there are **no missing values** in the dataset.

### Dataset Representation

Each image can be represented as:

```text
28 × 28 pixels
```

Therefore:

```text
28 × 28 = 784 pixels
```

Each pixel contains an intensity value representing the grayscale information of the handwritten digit.

---

## 🔄 Project Workflow

```text
MNIST Dataset
      ↓
Load CSV Files
      ↓
Data Exploration
      ↓
Check Missing Values
      ↓
Separate Features & Labels
      ↓
Normalize Pixel Values
      ↓
Reshape Images
      ↓
One-Hot Encode Labels
      ↓
 ┌───────────────┬───────────────┬───────────────┐
 ↓               ↓               ↓
Perceptron       ANN             CNN
 ↓               ↓               ↓
Training         Training        Training
 ↓               ↓               ↓
Evaluation       Evaluation      Evaluation
 └───────────────┴───────────────┴───────────────┘
                    ↓
             Model Comparison
```

---

# 🧹 Data Preprocessing

## 1. Separating Features and Labels

The `label` column is separated from the pixel values.

```python
X_train = df.drop("label", axis=1).values
y_train = df["label"].values

X_test = df_test.drop("label", axis=1).values
y_test = df_test["label"].values
```

Here:

* `X_train` → training image pixels
* `y_train` → training labels
* `X_test` → testing image pixels
* `y_test` → testing labels

This preprocessing step is implemented directly in the notebook.

---

## 2. Pixel Normalization

The pixel values are converted to `float32` and divided by `255`.

```python
X_train = X_train.astype("float32") / 255.0
X_test = X_test.astype("float32") / 255.0
```

This converts the pixel range from:

```text
0 – 255
```

to:

```text
0 – 1
```

Normalization helps neural networks train more effectively.

---

## 3. Reshaping the Images

For the basic neural-network models, the images are represented as:

```text
28 × 28
```

For the CNN, an additional channel dimension is introduced:

```text
28 × 28 × 1
```

The `1` represents the single grayscale channel.

```python
X_train_cnn = X_train.reshape(-1, 28, 28, 1)
X_test_cnn = X_test.reshape(-1, 28, 28, 1)
```

This format is required for the convolutional layers used by the CNN.

---

## 4. One-Hot Encoding

The digit labels are converted into categorical format using:

```python
y_train_cat = to_categorical(y_train, 10)
y_test_cat = to_categorical(y_test, 10)
```

Since MNIST contains ten classes:

```text
0, 1, 2, 3, 4, 5, 6, 7, 8, 9
```

each label is represented using a 10-element one-hot encoded vector.

---

# 🤖 Models Implemented

## 1. Perceptron / Single-Layer Neural Network

The first model is used as a simple baseline.

### Architecture

```text
Input Image (28 × 28)
        ↓
Flatten
        ↓
Dense Layer (10 neurons)
        ↓
Softmax
        ↓
Digit Prediction
```

Implementation:

```python
perceptron = Sequential([
    Flatten(input_shape=(28,28)),
    Dense(10, activation="softmax")
])
```

The model uses:

* **SGD optimizer**
* **Categorical Cross-Entropy loss**
* **Accuracy as evaluation metric**
* **5 epochs**
* **Batch size = 32**

The model achieved a test accuracy of approximately:

### **88.08%**

---

# 2. Artificial Neural Network (ANN)

The second model is a deeper fully connected neural network.

### Architecture

```text
Input Image (28 × 28)
        ↓
Flatten
        ↓
Dense (128 neurons, ReLU)
        ↓
Dense (64 neurons, ReLU)
        ↓
Dense (10 neurons, Softmax)
        ↓
Digit Prediction
```

Implementation:

```python
ann = Sequential([
    Flatten(input_shape=(28,28)),
    Dense(128, activation="relu"),
    Dense(64, activation="relu"),
    Dense(10, activation="softmax")
])
```

The ANN uses:

* **Adam optimizer**
* **Categorical Cross-Entropy loss**
* **Accuracy metric**
* **5 epochs**
* **Batch size = 32**

The final reported test accuracy is approximately:

### **95.97%**

---

# 3. Convolutional Neural Network (CNN)

The main model in this project is the **Convolutional Neural Network**.

CNNs are particularly useful for image classification because convolutional layers can learn spatial patterns and visual features from images.

### CNN Architecture

```text
Input Image
28 × 28 × 1
      ↓
Conv2D
32 filters
3 × 3 kernel
ReLU
      ↓
MaxPooling2D
2 × 2
      ↓
Conv2D
64 filters
3 × 3 kernel
ReLU
      ↓
MaxPooling2D
2 × 2
      ↓
Flatten
      ↓
Dense
128 neurons
ReLU
      ↓
Dropout
0.5
      ↓
Dense
10 neurons
Softmax
      ↓
Digit Prediction
```

The implemented CNN is:

```python
cnn = Sequential([
    Conv2D(32, kernel_size=(3,3),
           activation="relu",
           input_shape=(28,28,1)),

    MaxPooling2D(pool_size=(2,2)),

    Conv2D(64, kernel_size=(3,3),
           activation="relu"),

    MaxPooling2D(pool_size=(2,2)),

    Flatten(),

    Dense(128, activation="relu"),

    Dropout(0.5),

    Dense(10, activation="softmax")
])
```

The CNN uses:

* **Adam optimizer**
* **Categorical Cross-Entropy loss**
* **Accuracy metric**
* **5 epochs**
* **Batch size = 32**
* **Dropout = 0.5**

---

# 📈 Results

The three implemented models were evaluated on the MNIST test dataset.

| Model      | Test Accuracy |
| ---------- | ------------: |
| Perceptron |    **88.08%** |
| ANN        |    **95.97%** |
| CNN        |    **98.76%** |

The CNN achieved the highest test accuracy among the models implemented in this notebook, with a reported accuracy of approximately **98.76%**.

### Performance Summary

The progression demonstrates how model architecture affects image classification performance:

```text
Perceptron  →  88.08%
      ↓
ANN         →  95.97%
      ↓
CNN         →  98.76%
```

The CNN training logs show validation accuracy increasing from approximately **97.96% in the first epoch to 98.76% by the fifth epoch**.

---

# 📉 Training Visualization

The notebook includes a function for visualizing:

* Training accuracy
* Validation accuracy
* Training loss
* Validation loss

This allows the training behaviour of each model to be inspected across epochs.

The visualization function plots accuracy and loss curves from the training history.

---

# 🛠️ Technologies & Libraries

The project is implemented in **Python** using the following libraries:

| Technology / Library | Purpose                                     |
| -------------------- | ------------------------------------------- |
| Python               | Programming language                        |
| NumPy                | Numerical operations                        |
| Pandas               | Dataset handling                            |
| Matplotlib           | Visualization                               |
| Seaborn              | Data visualization                          |
| Scikit-learn         | Machine learning utilities and evaluation   |
| TensorFlow / Keras   | Neural network and CNN implementation       |
| Google Colab         | Development and experimentation environment |

The notebook imports TensorFlow/Keras components such as `Sequential`, `Dense`, `Conv2D`, `Flatten`, `MaxPooling2D`, `Dropout`, and `to_categorical`.

---

# 📁 Project Structure

A recommended GitHub repository structure is:

```text
MNIST-CNN-Classification/
│
├── CNN.ipynb
├── mnist_train.csv
├── mnist_test.csv
├── README.md
└── requirements.txt
```

> **Note:** The CSV files are the dataset files used by the notebook. If they are too large for normal GitHub storage, consider using Git LFS or provide the original dataset source instead of committing the large files directly.

---

# ⚙️ Installation

Clone the repository

Install the required libraries:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn tensorflow
```

---

# ▶️ How to Run

### Option 1 — Google Colab

1. Open `CNN.ipynb` in Google Colab.
2. Upload `mnist_train.csv` and `mnist_test.csv`.
3. Run the notebook cells sequentially.
4. Review the preprocessing steps.
5. Train the Perceptron, ANN, and CNN models.
6. Compare their test accuracies.
7. Observe the training accuracy and loss plots.

### Option 2 — Jupyter Notebook

Install the dependencies and place the following files in the same directory:

```text
CNN.ipynb
mnist_train.csv
mnist_test.csv
```

Then launch Jupyter:

```bash
jupyter notebook
```

Open `CNN.ipynb` and run the cells.

---

# 🧠 Key Concepts Demonstrated

This project helped demonstrate several important concepts in machine learning and deep learning:

### Machine Learning

* Classification
* Training and testing
* Model evaluation
* Accuracy

### Neural Networks

* Dense layers
* Activation functions
* Softmax classification
* ReLU activation
* Categorical cross-entropy
* Gradient-based optimization

### Computer Vision

* Image representation
* Pixel normalization
* Convolution
* Feature extraction
* Pooling
* Flattening
* Dropout

### Deep Learning

* ANN architecture
* CNN architecture
* Model training
* Validation performance
* Training and loss curves

---

# 🔍 Why CNN for Image Classification?

A traditional fully connected neural network treats the image primarily as a collection of input values after flattening it.

A CNN, on the other hand, processes the image while preserving its spatial structure through convolutional operations.

In this project, the CNN uses:

```text
Conv2D → MaxPooling → Conv2D → MaxPooling
```

before flattening the learned features and passing them to dense layers.

This architecture allows the network to learn image-related patterns before making the final digit classification.

---

# 📌 Limitations

Although the CNN achieved high accuracy on the MNIST test set, this project has some limitations:

* The experiment uses a relatively simple grayscale digit dataset.
* Training was performed for only **5 epochs**.
* No extensive hyperparameter tuning was performed.
* No data augmentation was implemented.
* The CNN was evaluated primarily using accuracy.
* The model was not tested on handwritten digits from external real-world sources.

Therefore, the reported performance should be interpreted specifically in the context of the MNIST test dataset.

---

# 🚀 Future Improvements

The project can be extended in several ways:

* Implement **data augmentation**.
* Experiment with different CNN architectures.
* Add **Batch Normalization**.
* Perform systematic **hyperparameter tuning**.
* Increase the number of training epochs.
* Add **Early Stopping**.
* Generate and analyze a **confusion matrix**.
* Calculate **precision, recall and F1-score** for individual digit classes.
* Test the model on user-provided handwritten images.
* Build an interactive digit recognition application using **Streamlit** or **Gradio**.
* Deploy the trained model as a web application or API.

---

# 💡 Learning Outcome

Through this project, I developed a practical understanding of how neural network architectures can be applied to image classification problems.

The comparison between the Perceptron, ANN, and CNN also provided hands-on experience in understanding how progressively more suitable architectures can be designed for image-based tasks.

The project particularly strengthened my understanding of:

**Data preprocessing → Neural Network Design → Model Training → Evaluation → Performance Comparison**

---

# 👩‍💻 Author

**Swastika Mukherjee**

Final-Year Computer Science & Engineering Student
Interested in **Data Science, Machine Learning and Artificial Intelligence**

---

# ⭐ Acknowledgement

This project was developed as part of my learning journey in **Machine Learning and Deep Learning**, with a focus on understanding neural networks and CNN-based image classification.

---

## 📜 License

This project is intended for **educational and learning purposes**.
