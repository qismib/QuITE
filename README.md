# QuITE
Quantum Information Teleported on the IBM quantum Experience

**Overview**
The aim of the thesis is the study and implementation of the quantum teleportation protocol on an IBM quantum computer. Quantum teleportation is a useful protocol for transmitting a generic quantum state |Ψ> without the physical transfer of the information carrier. For the transmission to take place, the sender must have a second qubit in a state that is maximally entangled to a receiver’s qubit.

The protocol dictates the application, performed by the sender, of quantum gates both to his entangled qubit and to the |Ψ> state. The sender applies a CNOT using |Ψ> as control and his entangled qubit as the target, after he applies a Hadamard-gate to the |Ψ> state, obtaining the following state:


So when the sender measures his qubits, communicates the results to the receiver. Thanks to the nonlocality of the entanglement the receiver know exactly in which state is his qubit, so he can apply the suitable quantum gate: the receiver applies an X-gate if the result are  01, a Z-gate if the results are 10 and ZX-gates if the results are 11. In this way, the receiver reconstructs the |Ψ> state.

**Simulation**

We simulate this protocol first in the Qasm simulator:

![ ](https://github.com/qismib/QuITE/blob/main/images/qasm_simulator/circuit_with_check.png  "circuit_simulator")


We first create the generic state with two rotational gates, after, in order to verify the correct implementation, we apply the rotational gate to the last qubit. As expected we obtain always 0 from the measurement of the last qubit.
![ ](https://github.com/qismib/QuITE/blob/main/images/qasm_simulator/result_simulator.png  "simulato_results")




**Real Devices**

For the implementation on real devices we have to know that, with the current hardware, we can’t have measurements in the middle of the circuit. We can use the deferred measurements principle, which state we can always postpone the measurements at the end of the circuit without any effect on the probability distribution of the outcomes:
![ ](https://github.com/qismib/QuITE/blob/main/images/real_device/circuit_real_device.png  "circuit_real_device")



We obtain these results on the ibmq_quito:

![ ](https://github.com/qismib/QuITE/blob/main/images/real_device/result_quito.png  "results_quito")



As we can see, we have some probabilities of obtaining 1 in the last qubit, due to the noise of the real device. We can compare the results with a much more noisy device:
![ ](https://github.com/qismib/QuITE/blob/main/images/real_device/result_yorktown.png  "results_yorktown")
