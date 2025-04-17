from qiskit import QuantumCircuit
from qiskit_aer.primitives import SamplerV2 as Sampler
import bluequbit
import matplotlib.pyplot as plt

# Load the circuit from QASM
qc = QuantumCircuit.from_qasm_file('P4_golden_mountain.qasm')

qc.h(range(48))

qc.cz(0, 1)  # Example oracle (customize this to your oracle)

# Apply the Grover Diffusion Operator (Amplitude Amplification)
qc.h(range(48))
qc.x(range(48))
qc.h(range(48))

# Oracle (again): Typically, the oracle is applied before and after the diffusion operator.
qc.cz(0, 1)  # Example oracle (you should customize this based on your problem)

qc.h(range(48))
qc.x(range(48))
qc.h(range(48))
# Apply the Oracle to the circuit

qc.measure_all()

# Initialize BlueQubit
bq = bluequbit.init("6Qr8Hh3RPXHArEBaOONswy8st02wTLCH")

result = bq.run(qc, device='quantum', shots=2000)

# Retrieve and display the counts
# counts = result.get_counts()

print(result)
