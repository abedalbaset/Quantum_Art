# Import the Qiskit SDK
#36d56bc391ac1cbfa7e9f81200eab8aed0fff6265efb8ce7dae914672f5aee111d46f72b98943fb2afba77d672dc928fa5670adb8d527f819788d11990bf9ce3
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute, Aer
from qiskit import IBMQ

# Create a Quantum Register with 2 qubits.
q = QuantumRegister(1)
# Create a Classical Register with 2 bits.
c = ClassicalRegister(1)
# Create a Quantum Circuit
qc = QuantumCircuit(q, c)

# Add a H gate on qubit 0, putting this qubit in superposition.
qc.h(q[0])
# Add a CX (CNOT) gate on control qubit 0 and target qubit 1, putting
# the qubits in a Bell state.
#qc.cx(q[0], q[1])
# Add a Measure gate to see the state.
qc.measure(q, c)

#IBMQ.save_account('MY-IBMQ-API')
IBMQ.load_accounts()
print("Available backends:")
IBMQ.backends()

from qiskit.backends.ibmq import least_busy

large_enough_devices = IBMQ.backends(filters=lambda x: x.configuration()['n_qubits'] > 3 and
                                                       not x.configuration()['simulator'])
backend = least_busy(large_enough_devices)
print("The best backend is " + backend.name())

#from qiskit.wrapper.jupyter import *
#qiskit_job_status
shots = 1           # Number of shots to run the program (experiment); maximum is 8192 shots.
max_credits = 3        # Maximum number of credits to spend on executions. 
for x in range(6):
	job_exp = execute(qc, backend=backend, shots=shots, max_credits=max_credits)
	result_real = job_exp.result()
	v=result_real.get_counts(qc)
	newstr = "".join((str(v), '\n'))
	print(newstr)
	f = open('result_randon_q', 'a')
	f.write(newstr)  # python will convert \n to os.linesep
	f.close()  


