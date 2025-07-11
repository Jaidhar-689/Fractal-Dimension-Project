import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

# Load image
f1 = 'outline-map-united-kingdom.jpg' # For reference because it's a well known value
f2 = 'india-outline-map.jpg'

for f in [f1,f2]:
    img = Image.open(f).convert('L')  # 'L' mode = grayscale

    # Convert to numpy array
    img_array = np.array(img)

    # Binarize the image (threshold)
    threshold = 128 # 256/2 = 128
    binary_array = (img_array < threshold).astype(int)

    # Convert to DataFrame
    df = pd.DataFrame(binary_array)

    # Box counting function
    def boxcount(df, k):
        rows = np.arange(0, df.shape[0], k)
        cols = np.arange(0, df.shape[1], k)

        count = 0
        for r in rows:
            for c in cols:
                block = df.iloc[r:r+k, c:c+k]
                if block.values.sum() > 0:
                    count += 1
        return count

    # Different box sizes
    min_dim = min(df.shape)
    sizes = 2**np.array(range(int(np.log2(min_dim)), 1, -1))

    counts = []
    for size in sizes:
        counts.append(boxcount(df, size))
    
    y = np.log(counts)
    x = np.log(1/sizes)

    # Linear fit
    coeffs = np.polyfit(np.log(1/sizes), np.log(counts), 1)
    fractal_dimension = coeffs[0]
    print(f"Estimated fractal dimension of {f}: {fractal_dimension:.4f}")

    # Log-log plot
    # plt.figure(figsize=(8,6))
    plt.plot(x, coeffs[0]*x+ coeffs[1])
    plt.plot(x, y, 'o-')
    plt.grid(True)
    plt.xlabel('log(1/box size)')
    plt.ylabel('log(number of boxes)')
    plt.title(f'Fractal Dimension of {f}')


    plt.show()
