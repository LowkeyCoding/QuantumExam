from dataclasses import dataclass
from qiskit import QuantumCircuit,QuantumRegister, ClassicalRegister, transpile
import numpy as np

@dataclass
class User:
    basis: [str]
    key: [int]
    qc: QuantumCircuit
    qr: QuantumRegister
    cr: ClassicalRegister
    n: int
    name: str


def create_basis(user):
    user.basis = []
    for index in range(len(user.qr)):
        if 0.5 < np.random.random():   # 50% chance
            user.qc.h(user.qr[index])         # change to diagonal basis
            user.basis.append('X')    # character for diagonal basis
        else:
            user.basis.append('Z')

def send_state(a, b):
    qc = a.qc.copy()
    qc.compose(b.qc, inplace=True)
    for index in range(len(a.qr)): 
        qc.measure(a.qr[index], a.cr[index])
    return qc

def execute(qc, backend, shots =1):
    # Transpile circuit to work with the current backend.
    qc_compiled = transpile(qc, backend)
    # Run the job
    # This will cause a pop where you have to authenticate with azure.
    job_sim = backend.run(qc_compiled, shots = shots)

    # Get the result
    return job_sim.result().get_counts(qc_compiled)

def get_shared_key(a, b, sim = 1, debug = False, simp = False):
    keep = []
    discard = []
    for qubit, basis in enumerate(zip(a.basis, b.basis)):
        if basis[0] == basis[1]:
            if debug and not simp: 
                print(f"Same choice for qubit: {qubit}, basis: {basis[0]}") 
            keep.append(qubit)
        else:
            if debug and not simp:
                print(f"Different choice for qubit: {qubit}, {a.name} has {basis[0]}, {b.name} has {basis[1]}")
            discard.append(qubit)
    acc = 0
    for bit in zip(a.key, b.key):
        if bit[0] == bit[1]:
            acc += 1

    if not simp:
        print('Percentage of qubits to be discarded according to table comparison: ', len(keep)/a.n)
        print('Measurement convergence by additional chance: ', acc/a.n)   
        
    new_key_a = [a.key[qubit] for qubit in keep]
    new_key_b = [b.key[qubit] for qubit in keep]

    acc = 0
    for bit in zip(new_key_a, new_key_b):
        if bit[0] == bit[1]:
            acc += 1        
    if not simp:
        print('Percentage of similarity between the keys: ', acc/len(new_key_a))
    x = False
    if (acc//len(new_key_a) >= sim):
        if not simp:
            print("Key exchange has been successfull")
            print(f"New {a.name}'s key: ", "".join(new_key_a))
            print(f"New {b.name}'s key: ", "".join(new_key_b))
        x = True
    else:
        if not simp:
            print("Key exchange has been tampered! Check for eavesdropper or try again")
            print(f"New {a.name}'s key is invalid: ", "".join(new_key_a))
            print(f"New {b.name}'s key is invalid: ", "".join(new_key_b))
    return (new_key_a, new_key_b, x)