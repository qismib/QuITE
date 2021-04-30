from qiskit import *
from qiskit.extensions import Initialize
from qiskit.visualization import *
from qiskit.quantum_info import *
import numpy as np
import random

def Bell_pair(circuit, qr) :
    circuit.h(qr[1])
    circuit.cx(qr[1],qr[2])

    circuit.barrier()

def create_a_random_state0(circuit, qr) :
    vec = random_statevector(2) #creo un generico vettore a base 2
    #al qubit 0 do le ampiezze del generico vettore
    circuit.initialize(vec.data, qr[0])

    plot_bloch_multivector(vec)

    circuit.barrier()

def create_a_random_state1(circuit, qr) :
    #prendo degli agoli generici
    a = random.random()
    b = random.random()

    theta = a*2*np.pi
    phi = b*2*np.pi

    #la trasformazione che porta da |0> a |psi> può essere sempre riscritta cosi
    circuit.ry(theta, qr[0])
    circuit.rz(phi, qr[0])

    circuit.barrier()


def Alice_operations(circuit, qr) :
    circuit.cx(qr[0],qr[1])
    circuit.h(qr[0])

    circuit.barrier()

def Alice_measurements(circuit, qr, Alice_cr0, Alice_cr1) :
    circuit.measure(qr[0], Alice_cr0)
    circuit.measure(qr[1], Alice_cr1)


    circuit.barrier()

def Bob_operations(circuit, qr, Alice_cr0, Alice_cr1) :
     circuit.x(qr[2]).c_if(Alice_cr1, 1)
     circuit.z(qr[2]).c_if(Alice_cr0, 1)
