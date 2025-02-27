# FASTA Sequence Analysis with Streamlit

This Streamlit app allows users to analyze DNA sequences from FASTA files. It provides sequence statistics, GC content, transcribed RNA bases, reverse complementary bases, and nucleotide frequency visualization.

## Features
- Upload a custom FASTA file or use the default **E. coli genome**.
- View sequence ID and length.
- Calculate GC content.
- Display the first 50 transcribed RNA bases.
- Display the first 50 reverse compliment bases
- Generate a **Nucleotide Frequency Plot**.

## Demo
- https://dna-sequence-analysis-2.streamlit.app/

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/kichyoo/fasta-sequence-analysis.git
   cd fasta-sequence-analysis
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the App Locally

Run the following command:
```bash
streamlit run streamlit_app.py
```

## Deploying on Streamlit Cloud
1. Push your code to **GitHub**.
2. Go to [Streamlit Cloud](https://share.streamlit.io/).
3. Click **'New App'**, select your repository, and deploy!
---

