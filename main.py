import random
import math
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit
from qiskit.providers.basic_provider import BasicSimulator

SHOTS = 4096

# -----------------------------
# STEP 1: Quantum circuit
# -----------------------------
qc = QuantumCircuit(1, 1)
qc.h(0)
qc.measure(0, 0)

simulator = BasicSimulator()
job = simulator.run(qc, shots=SHOTS, memory=True)
quantum_bits = job.result().get_memory()

# -----------------------------
# STEP 2: Classical bits
# -----------------------------
classical_bits = [str(random.getrandbits(1)) for _ in range(SHOTS)]

# -----------------------------
# STEP 3: Analysis function
# -----------------------------
def analyze(bits):
    zeros = bits.count("0")
    ones = bits.count("1")
    total = len(bits)
    expected = total / 2

    chi_square = ((zeros - expected) ** 2 / expected) + ((ones - expected) ** 2 / expected)
    p_value = math.erfc(math.sqrt(chi_square / 2))

    return {
        "zeros": zeros,
        "ones": ones,
        "total": total,
        "chi_square": chi_square,
        "p_value": p_value
    }

q_result = analyze(quantum_bits)
c_result = analyze(classical_bits)

print("Quantum Result:", q_result)
print("Classical Result:", c_result)

# -----------------------------
# STEP 4: Bar chart
# -----------------------------
labels = ["Quantum Zeros", "Quantum Ones", "Classical Zeros", "Classical Ones"]
values = [
    q_result["zeros"],
    q_result["ones"],
    c_result["zeros"],
    c_result["ones"]
]

plt.figure(figsize=(10, 6))
plt.bar(labels, values)
plt.title("Quantum vs Classical Random Bit Distribution")
plt.ylabel("Count")
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig("bit_distribution_comparison.png")
plt.show()

# -----------------------------
# STEP 5: First 50 bits preview
# -----------------------------
quantum_preview = [int(bit) for bit in quantum_bits[:50]]
classical_preview = [int(bit) for bit in classical_bits[:50]]

plt.figure(figsize=(12, 4))
plt.plot(range(50), quantum_preview, marker='o', label='Quantum Bits')
plt.plot(range(50), classical_preview, marker='x', label='Classical Bits')
plt.title("First 50 Bits: Quantum vs Classical")
plt.xlabel("Bit Position")
plt.ylabel("Bit Value")
plt.yticks([0, 1])
plt.legend()
plt.tight_layout()
plt.savefig("bit_sequence_preview.png")
plt.show()

print("\nGraphs saved successfully:")
print("1. bit_distribution_comparison.png")
print("2. bit_sequence_preview.png")