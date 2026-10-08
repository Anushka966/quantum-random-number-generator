
# Quantum Random Number Generator (QRNG)

## Qiskit Fall Fest 2026 — Foundation Track F1

### Project Overview
This project implements a Quantum Random Number Generator using Qiskit and compares its output with Python's classical pseudorandom number generator.

The objective is to demonstrate quantum measurement-based randomness and evaluate the resulting bit sequences using statistical tests.

### Technologies
- Python
- IBM Qiskit
- Matplotlib
- Qiskit BasicSimulator

### How It Works
1. Initialize a qubit in state |0>.
2. Apply a Hadamard gate to create superposition.
3. Measure the qubit to obtain a 0 or 1.
4. Repeat for 4,096 shots.
5. Generate 4,096 classical pseudorandom bits.
6. Compare both datasets statistically.

### Randomness Tests
- Bit balance: proportion of zeros and ones.
- Chi-square goodness-of-fit test.
- P-value analysis for bit balance.
- Visual comparison of bit distributions.

### How to Run

Install dependencies:

    pip install -r requirements.txt

Run the project:

    python main.py

### Outputs
- Statistical comparison printed in terminal.
- bit_distribution_comparison.png
- bit_sequence_preview.png

### Practical Applications
Random number generation is important for simulations, sampling, gaming, and cryptographic systems.

### Limitations
This prototype uses a quantum circuit simulator, not physical quantum hardware.

The simulator does not provide certified physical quantum randomness.

Statistical tests alone cannot establish that a generator is secure or truly random. Passing the chi-square test does not prove randomness.

Python's random module is also not suitable for cryptographic security.

### Conclusion
This project demonstrates the principles of quantum random number generation using Qiskit and provides a reproducible comparison with classical pseudorandom bit generation.
