from qiskit import *
from qiskit.quantum_info import *
from qiskit.extensions import Initialize
from qiskit.visualization import plot_bloch_multivector
import numpy as np

def Bell_pair(circuit, qr) :
    circuit.h(qr[1])
    circuit.cx(qr[1],qr[2])

    circuit.barrier()

def create_a_random_state0(circuit, qr) :
    vec = random_statevector(2) #creo un generico vettore a base 2
    #al qubit 0 do le ampiezze del generico vettore
    psi = circuit.initialize(vec.data, qr[0])

    plot_bloch_multivector(vec)

    circuit.barrier()
    return psi

def create_a_random_state1(circuit, qr) :
    #definisco i range di alpha beta e gamma da 0 a 2pi
    alpha_range = np.arange(0, 2*np.pi, np.pi/20)
    beta_range = np.arange(0, 2*np.pi, np.pi/20)
    gamma_range = np.arange(0, 2*np.pi, np.pi/20)

    #prendo degli agoli generici
    alpha = np.random.choice(alpha_range)
    beta = np.random.choice(beta_range)
    gamma = np.random.choice(gamma_range)

    #la trasformazione che porta da |0> a |psi> può essere sempre riscritta cosi
    circuit.rz(gamma, qr[0])
    circuit.ry(beta, qr[0])
    circuit.rz(alpha, qr[0])

    circuit.barrier()


def Alice_operations(circuit, qr, Alice_cr) :
    #gates
    circuit.cx(qr[0],qr[1])
    circuit.h(qr[0])

    circuit.barrier()

    #misure
    circuit.measure(qr[0], Alice_cr[0])
    circuit.measure(qr[1], Alice_cr[1])

    #print(Alice_cr)

    circuit.barrier()

def Bob_operations(circuit, qr, Alice_cr) :
     #non posso usare if (Alice_cr[0] == 1)

     #potrei usare c_if ma

     #dopo le misure, i qubit saranno o 0 o 1 posso utilizzare cx e cz
     circuit.cx(qr[1], qr[2])
     circuit.cz(qr[0], qr[2])
