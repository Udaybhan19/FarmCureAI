
# FarmCureAI
## An AI-powered mobile decision support system for real-time, multi-crop plant disease detection and lesion segmentation using real-world field images. Accepted at IEEE INDICON 2026.


## Abstract

Plant diseases rarely appear in the clean and controlled form, yet existing mobile-based approaches are predominantly developed and evaluated on controlled, single-leaf datasets, limiting their reliability under diverse real-world field conditions. In this work, we present a segmentation-based mobile plant disease diagnosis framework that moves beyond conventional image-level classification by explicitly localizing disease-affected regions, supporting more informative disease diagnosis under complex field conditions. We combine three publicly available field agricultural datasets, namely PlantSeg, NLB, and Rice Disease, organize them into 12 essential food-crop categories, together with an unknown-crop category covering 20 common diseases across diverse plant species. Using InternImage as the segmentation backbone, the framework achieves an average 68.39% mIoU and 78.94% mAcc across the 12 food-crop categories, while the unknown-crop category achieves 62.18% mIoU and 76.51% mAcc. The resulting framework provides a practical benchmark for evaluating segmentation-based plant disease diagnosis across diverse crops and field conditions, while the mobile deployment demonstrates a practical pathway from agricultural vision models to real-world, field-ready applications. At the end, we further identify key challenges in field deployment and outline future directions for more robust, scalable, and farmer-centric plant disease diagnosis systems.

---

## Key Features

- **Disease Segmentation:** Explicitly identifies and localizes disease-affected regions in plant images.
- **Multi-Crop Support:** Covers 12 essential food-crop categories.
- **Unknown-Crop Recognition:** Includes an additional category covering 20 common diseases across diverse plant species.
- **Multiple Agricultural Datasets:** Integrates PlantSeg, NLB, and Rice Disease datasets.
- **InternImage Backbone:** Utilizes InternImage as the segmentation backbone.
- **Mobile Deployment:** Demonstrates the practical deployment of the proposed framework in a mobile application.
- **Reproducibility:** Provides code for dataset selection, preparation, model training, and inference.

---

## Repository Structure

The repository is organized as follows:

```text
FarmCureAI/
│
├── All_Disease_Dataset/
│   ├── Cropwise_Disease_Dataset/
│   ├── Test/
│   └── Train/
│
├── InternImage/
│   └── segmentation
│
├── data_processing.ipynb
│
├── model_training_inference.ipynb
│
└── README.md
```


---

## Dataset Preparation

The proposed framework integrates three publicly available agricultural datasets:

1. **PlantSeg**
2. **NLB**
3. **Rice Disease**

### Step 1: Download the Datasets

Download the PlantSeg, NLB, and Rice Disease datasets from their respective publicly available sources.

Ensure that the downloaded datasets are accessible from the paths specified in the data processing notebook.

### Step 2: Dataset Processing

Open and execute:

```text
data_processing.ipynb
```

This notebook performs the required data processing and organization steps.

The downloaded datasets are processed and separated according to the corresponding crop types and disease categories. The resulting dataset is organized under the `All_Disease_Dataset` directory and its associated dataset folders.

The processed dataset structure is used by the subsequent model training and inference pipeline.

---

## Dataset Composition

The prepared dataset consists of 12 food-crop categories and one additional unknown-crop category covering 20 common diseases.

| Crop Name | Total Images | Train / Test Images | No. of Diseases | Disease Names |
|---|---:|---:|---:|---|
| **Unknown** | 12,058 | 9,736 / 2,322 | 20 | Rust; Rot; Mosaic; Scab; Spot; Downy mildew; Blight; Anthracnose; Mold; Powdery mildew; Blotch; Smut; Leaf streak; Leaf curl; Scorch; Bacterial wilt; Blast; Pocket disease; Leafroll; Mummy berry |
| **Apple** | 579 | 454 / 115 | 4 | Black rot; Mosaic virus; Rust; Scab |
| **Grape** | 493 | 395 / 98 | 4 | Black rot; Downy mildew; Leaf spot; Leafroll |
| **Rice** | 609 | 487 / 122 | 3 | Blast; Blight; Brown spot |
| **Wheat** | 1,791 | 1,454 / 357 | 8 | Bacterial leaf streak (black chaff); Head scab; Leaf rust; Loose smut; Powdery mildew; Septoria blotch; Stem rust; Stripe rust |
| **Soybean** | 788 | 630 / 158 | 6 | Bacterial blight; Brown spot; Downy mildew; Frog-eye leaf spot; Mosaic; Rust |
| **Corn** | 615 | 1,338 / 222 | 4 | Gray leaf spot; Northern leaf blight; Rust; Smut |
| **Tomato** | 900 | 719 / 181 | 7 | Bacterial leaf spot; Early blight; Late blight; Leaf mold; Mosaic virus; Septoria leaf spot; Yellow leaf curl virus |
| **Banana** | 573 | 459 / 114 | 6 | Anthracnose; Black leaf streak; Bunchy top; Cigar-end rot; Cordana leaf spot; Panama |
| **Potato** | 243 | 195 / 48 | 2 | Early blight; Late blight |
| **Cabbage** | 276 | 220 / 56 | 3 | Alternaria leaf spot; Black rot; Downy mildew |
| **Bean** | 229 | 183 / 46 | 3 | Halo blight; Mosaic virus; Rust |
| **Cucumber** | 478 | 382 / 96 | 3 | Angular leaf spot; Bacterial wilt; Powdery mildew |

**Note:** The Corn row contains a discrepancy in the supplied figures: the total image count is 615, whereas the training and testing counts sum to 1,560. Please verify these values against the final dataset split before publication.

---

## Model Training and Inference

After completing dataset preparation, proceed with the model training and inference notebook.

### Step 1: Open the Notebook

```text
model_training_inference.ipynb
```

### Step 2: Environment Setup

Execute the notebook cells sequentially.

The notebook is configured to:

- Create and configure the required Python environment.
- Install the necessary dependencies.
- Configure the InternImage-based segmentation framework.
- Prepare dataset loaders for individual crop categories.

### Step 3: Model Training

Once the environment and dataset loaders are configured, execute the training cells to train the segmentation model using the prepared crop-specific datasets.

### Step 4: Model Inference

The notebook also provides the inference workflow for evaluating the trained model and generating disease segmentation predictions.

Ensure that the dataset paths and trained model checkpoint paths are correctly configured before running inference.

---

## Experimental Results

The proposed framework is evaluated across 12 food-crop categories and an additional unknown-crop category. The crop-wise segmentation performance is reported using mean Intersection over Union (mIoU) and mean Accuracy (mAcc).

### Crop-wise Segmentation Performance

| Crop | No. of Diseases | mIoU (%) | mAcc (%) |
|---|---:|---:|---:|
| Unknown Crop | 20 | 62.18 | 76.51 |
| Apple | 4 | 70.07 | 77.47 |
| Grape | 4 | 68.24 | 81.30 |
| Rice | 3 | 71.48 | 79.59 |
| Wheat | 8 | 62.35 | 73.64 |
| Soybean | 6 | 80.45 | 90.00 |
| Corn | 4 | 70.91 | 78.91 |
| Tomato | 7 | 48.31 | 62.21 |
| Banana | 6 | 71.61 | 79.20 |
| Potato | 2 | 71.48 | 80.00 |
| Cabbage | 3 | 67.74 | 78.61 |
| Bean | 3 | 72.48 | 84.24 |
| Cucumber | 3 | 71.80 | 84.54 |
| **Average (12 Food Crops)** | — | **68.39** | **78.94** |

The framework achieves an average **68.39% mIoU** and **78.94% mAcc** across the 12 food-crop categories. For the additional unknown-crop category, it achieves **62.18% mIoU** and **76.51% mAcc**.

---

## InternImage Original Repository

https://github.com/OpenGVLab/InternImage

---

## Citation

**FarmCureAI: An AI-Powered Mobile Decision Support System for Real-Time Plant Disease Detection and Segmentation**

```bibtex
@inproceedings{farmcureai,
    title={FarmCureAI: An AI-Powered Mobile Decision Support System for Real-Time Plant Disease Detection and Segmentation},
    author={Udaybhan Rathore, Amit Shakya, Rupesh Kumar, Lalit Sharma},
    booktitle={23rd IEEE India Council International Conference (INDICON 2026)},
    year={2026}
}
```


## License

Please refer to the original licenses and usage terms of the PlantSeg, NLB, and Rice Disease datasets, as well as the InternImage framework.
