import streamlit as st
from Bio import SeqIO
import matplotlib.pyplot as plt
import pandas as pd
import io

st.title("FASTA Sequence Analysis")

# Handle file upload
if st.button("Use Default FASTA File"):
    uploaded_file = "ecoli_genome.fasta"
else:
    uploaded_file = st.file_uploader("Upload a FASTA file", type=["fasta"])

if uploaded_file:
    if isinstance(uploaded_file, str):  # Default file case
        with open(uploaded_file, "r") as file:
            record = next(SeqIO.parse(file, "fasta"))
    else:  # Uploaded file case
        uploaded_file.seek(0)
        record = next(SeqIO.parse(io.StringIO(uploaded_file.getvalue().decode("utf-8")), "fasta"))

    dna_sequence = str(record.seq)

    # Display sequence info
    st.write(f"**Sequence ID:** {record.id}")
    st.write(f"**Sequence Length:** {len(dna_sequence)} bases")

    # Calculate GC Content
    gc_count = dna_sequence.count("G") + dna_sequence.count("C")
    at_count = dna_sequence.count("A") + dna_sequence.count("T")
    total_bases = len(dna_sequence)
    gc_percent = (gc_count / total_bases) * 100
    at_gc_ratio = (at_count / gc_count) if gc_count > 0 else float('inf')

    st.write(f"**GC Content:** {gc_percent:.2f}%")
    st.write(f"**AT/GC Ratio:** {at_gc_ratio:.2f}")

    # Nucleotide counts
    nucleotide_counts = {base: dna_sequence.count(base) for base in "ATGC"}

    # Transcribe to RNA
    rna_sequence = dna_sequence.replace("T", "U")
    st.write("**First 50 RNA bases:**", rna_sequence[:50])

    # Reverse Complement
    reverse_complement = str(record.seq.reverse_complement())
    st.write("**First 50 Reverse Complement bases:**", reverse_complement[:50])

    # Nucleotide Distribution Graph with Smaller Figure Size
    fig, ax = plt.subplots(figsize=(4, 3))  # Reduce overall figure size
    ax.bar(nucleotide_counts.keys(), nucleotide_counts.values(), color=['blue', 'red', 'green', 'orange'])
    ax.set_xlabel("Nucleotide")
    ax.set_ylabel("Count")
    ax.set_title("Nucleotide Frequency")
    st.pyplot(fig)

