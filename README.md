# Fractal-Dimension-Project
This project estimates the fractal dimension of India's coastline using the box-counting method, demonstrating the self-similarity and complexity of natural geographic boundaries.

📌 Objectives
Apply fractal geometry to a real-world object: India's coastline.

Use image processing techniques to extract the coastline boundary.

Implement the box-counting algorithm in Python to calculate the fractal (Hausdorff) dimension.

Visualize the scaling relationship between box size and box count on a log-log plot.

🔧 Tools & Libraries
NumPy, Pandas – Numerical computation

matplotlib – Data visualization

📈 Method
Preprocess the coastline image (grayscale → binary → edge detection).

Overlay square grids of varying sizes.

Count how many boxes contain a part of the coastline for each grid size.

Plot log(N) vs log(1/ε) and determine the slope as the fractal dimension.

📊 Results
Estimated Fractal Dimension: ≈ 1.198

Indicates that the Indian coastline has a structure more complex than a straight line but less than a plane.

📎 Applications
Geographical analysis

Pattern recognition

Environmental modeling
