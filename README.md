# Secure Pipeline For Machine Learning With Homomorphic Encryption

In this modern world of technology, a vast amount of personal data is required to perform computations. This data can be vulnerable to attack by third-party intruders or malicious actors. To eliminate this problem, we are using Homomorphic Encryption to develop a pipeline for securing individual data. Our main aim is to secure the data instead of the model. Secure Machine Learning includes growing and enforcing device studying fashions which are proof against assaults and making sure the confidentiality, integrity, and availability of the statistics and fashions used. The encrypted data goes to the model which then gets trained on it. The model predicts the result and then performs decryption. In this system, neither the developer nor the model is aware of the authentic data.

## Introduction

According to studies, different countries like USA, Sweden, Japan, Singapore etc. People residing there, are willing to donate their data. The percentage of these people is about
70-90 percent. But of course, they have some concerns about their data privacy. Due to the sensitive nature of data of any individual, it is vital to offer safety for his data. It
can be misused if it comes in the wrong hands. Machine learning algorithms often require big datasets that could include personal, financial, or scientific information, which may be liable to assaults by hackers, cybercriminals, or different malicious actors. To conquer this hassle we use Homomorphic Encryption. This technique enables data to remain encrypted while performing computations on it. This is particularly useful for preserving privacy and security in scenarios where sensitive data needs to be processed by third parties.

### Objectives

1. Protecting sensitive data
2. Enhancing privacy
3. Improving security
4. Enabling more data sharing
 
# Homomorphic Encryption

Homomorphic encryption is a encryption technique that allows computation on encrypted data without decrypting it allowing data to be kept private and secure even while processing. The goal is to enable secure and private computation on sensitive data. There are three main types of homomorphic encryption:

1. Partially Homomorphic Encryption (PHE)
2. Somewhat Homomorphic Encryption (SHE)
3. Fully Homomorphic Encryption (FHE)

We will be implementing Partially Homomorphic Encryption (PHE) as well as Fully Homomorphic Encryption (FHE) to conclude best of our results. Below is this working flow of our project:

![WF](https://github.com/tahawar/Secure-Pipeline-For-Machine-Learning-With-Homomorphic-Encryption/blob/2db7d8dfbdad2cd1e74060ecfe18facaecd7418b/Flow%20Diagram.png)

# Paillier Cryptosystem

The Paillier cryptosystem is an asymmetric (public-key) cryptosystem that is widely used for secure computations, especially in the context of privacy-preserving protocols and homomorphic encryption. It uses Partially Homomorphic Encryption (PHE). It involves:

1. Key Generation
2. Encryption
3. Decryption

![M1](https://github.com/tahawar/Secure-Pipeline-For-Machine-Learning-With-Homomorphic-Encryption/blob/a5c1ff8ce2a617426f15b259846f8bcafcdc8b14/Methodology%201.png)

It is simple to implement. However, PHE is very limited to operations such as either addition or multiplication, but not both. Moreover, it is not well-suited for scenarios where complex computations are required. Additionally, it has some performance overhead which may impact the speed of computations, making it less desirable for real-time applications.

# TenSEAL

TenSEAL is an open-source library that provides homomorphic encryption functionalities in Python. It uses Fully Homomorphic Encryption (FHE). It’s designed to work with the PyTorch machine learning framework, allowing users to perform privacy-preserving computations on encrypted data. It’s constructed on Microsoft SEAL, a C++ library enforcing the BFV and CKKS homomorphic encryption schemes. Moreover, it provides ease of use through a Python API, while preserving efficiency by implementing most of its operations using C++, so TenSEAL is a C++ library with a Python interface.

![M2](https://github.com/tahawar/Secure-Pipeline-For-Machine-Learning-With-Homomorphic-Encryption/blob/acd2a66ca89362123e6ded6ea19595c0e8a3afa3/Methodology%202.png)

FHE offers secure machine learning on encrypted data more efficiently. Furthermore, it provides end-to-end encryption ensuring more privacy. At last, both operations such as addition and multiplication can be applied. Hence, it can make complex computations as well.

# Constraints

The main constraints of this projects are:

1. Performance
2. Algorithm compatibility
3. Data Preprocessing
   
There is a trade-off between security and performance which prioritizes security at the expense of performance. Certain algorithms may not be suitable with Homomorphic Encryption, and the processing of extensive data is a limitation when preserving privacy.

# Tools Used

1. TenSEAL
2. Jupyter Notebook
3. TensorFlow
4. Python
5. PyTorch

### Dataset 1 (Employee Dataset)

Collecting data sets was quite challenging because of the privacy issues of people. This dataset is about the employees in a company. We have downloaded the data set from [kaggle](https://www.kaggle.com/datasets/varungitboi/employee-salary-dataset). The length of dataset is 1000 rows and 5 columns.

![D1](https://github.com/tahawar/Secure-Pipeline-For-Machine-Learning-With-Homomorphic-Encryption/blob/eb77c4ad9b9fe083081daa129ee5c0111a691f8e/D1.png)

### Dataset 2 (CHD Dataset)

This dataset is about the people having coronary heart disease (CHD). We have downloaded the data set from [kaggle](https://www.kaggle.com/datasets/dileep070/heart-disease-prediction-using-logistic-regression). The length of dataset is 4238 rows and 16 columns.

![D2](https://github.com/tahawar/Secure-Pipeline-For-Machine-Learning-With-Homomorphic-Encryption/blob/eb77c4ad9b9fe083081daa129ee5c0111a691f8e/D2.png)

# Conclusion

Between both approaches, it was concluded that TenSEAL was more preferable as it could complex computations efficiently and generated more reasonable results.

# Future Work

We’ve created a pipeline with Homomorphic Encryption. In future work, it can be enhanced by incorporating Differential Privacy and Federated Learning to further prioritize data privacy and enable decentralized model training.

