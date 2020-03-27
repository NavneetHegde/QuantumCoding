
#1. reference qiskit
import qiskit
from qiskit import (IBMQ, 
                    QuantumRegister, 
                    ClassicalRegister, 
                    QuantumCircuit, 
                    execute)

#2.  setting account using token
IBMQ.enable_account('ACCOUNT TOKEN')

#3. print qiskit version
print("Qiskit Version : ", qiskit.__qiskit_version__.get('qiskit'))

#4 init quantum register with 1 qubit
quantumReg = QuantumRegister(1, 'qreg')

#5 init classic register with 1 bit
classicalReg = ClassicalRegister(1, 'creg')

#6 init circuit
circuit = QuantumCircuit(quantumReg, classicalReg)

####### GATE LOGIC GOES HERE #########

######################################

#7 measure qubit
circuit.measure(quantumReg,classicalReg)

#8 Execute the circuit on the qasm simulator
provider = IBMQ.get_provider(hub='ibm-q')
backend = provider.get_backend('ibmq_qasm_simulator')
job = execute(circuit, backend, shots=1024)

#9 get the results
result = job.result()

#10 print results
counts = result.get_counts(circuit)
print("\nTotal count for 0 is:",counts)



