# from qiskit import QuantumCircuit
# from qiskit_aer.primitives import SamplerV2 as Sampler
# import bluequbit

# qc = QuantumCircuit.from_qasm_file('P2_swift_rise.qasm')

# # print(qc)

# qc.measure_all()


# bq = bluequbit.init("Y4qP1EX3zRMb0VXP5V4I2GameCdg2dKh")
# result = bq.run(qc, device='cpu', shots=100) # <-- Quantum Magic
# # print(result.get_counts())
# counts = result.get_counts()

# most_frequent_outcome = max(counts, key=counts.get)
# highest_occurrence = counts[most_frequent_outcome]
# print(f"\nThe outcome with the highest occurrence is: {most_frequent_outcome}")
# print(f"It occurred {highest_occurrence} times.")

s = "0000000000000000000000000000000000000000000"
n = len(s)

lister = []
for i in range(48):
    if i == 23:
        lister.append("1")
    else:
        lister.append("0")
print("".join(lister))