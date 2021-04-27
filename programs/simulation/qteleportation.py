from qiskit import *
from funzioni import *
import matplotlib
import matplotlib.pyplot as plt
from qiskit.visualization import plot_histogram
from qiskit.quantum_info import *
from qiskit.extensions import Initialize



#loading my IBMQ account
provider = IBMQ.load_account()

#configuaration
qr = QuantumRegister(3)
Alice_cr = ClassicalRegister(2)
Bob_cr = ClassicalRegister(1)
circuit = QuantumCircuit(qr, Alice_cr, Bob_cr)

#trasformo il primo qubit in un generico stato |psi> che voglio teletrasportare
create_a_random_state0(circuit, qr)
#create_a_random_state1(circuit, qr)

#creo l'entanglement tra il secondo e terzo qubit
Bell_pair(circuit, qr)

#alice applica le sue porte e misura i suoi qubits
Alice_operations(circuit, qr, Alice_cr)

print('Alice sta comunicando i risultati a Bob')

#bob applica l'operazione corretta
Bob_operations(circuit, qr, Alice_cr)

#misura finale
circuit.measure(qr[2], Bob_cr)


simulator = Aer.get_backend('qasm_simulator')
result = execute(circuit,backend = simulator, shots = 1000).result()

counts = result.get_counts(circuit)

plot_histogram(counts)
print(counts)

circuit.draw(output = 'mpl')
plt.show()
