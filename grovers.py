import math
import numpy as np
from matplotlib import pyplot as plt

def normalise(*qubits):
    """Create superposition state with equal amplitudes"""
    result = np.zeros(qubits[0].shape)
    for qubit in qubits:
        result += qubit/np.linalg.norm(qubits)
    return result

def computational_basis(n):
    return np.hsplit(np.eye(n),n)

def H(qubit):
    """Returns qubit passed through H"""
    lg2 = int(math.log(qubit.shape[0], 2))
    h = np.array([[1]])
    for i in range(0, lg2):
        h = np.vstack((np.hstack((h, h)), np.hstack((h, -h))))
    
    hadamard = 1./np.sqrt(qubit.shape[0]) * h
    return np.dot(hadamard, qubit)

def kron_prod(*qubits):
    #Calculate a Kronecker product over a variable number of inputs
    result = np.array([[1.0]])
    for qubit in qubits:
        result = np.kron(result, qubit)
    return result

def cnot(qubit):
    X = np.eye(qubit.shape[0])[::-1]
    return np.dot(X, qubit)

def measure(state):
    ps = []
    cb = computational_basis(state.shape[0])
    for i in range(state.shape[0]):
        ps.append(np.dot(cb[i],cb[i].T))
    
    identity = np.eye(state.shape[0])
    
    rho = np.dot(state, state.T)
    
    result = 0
    r = np.random.uniform(0, sum(np.diag(rho)))
    for p in np.diag(rho):
        r -= p
        if r <= 0:
            break
        result += 1
    
    result_state = normalise(np.dot(np.dot(ps[result], identity), state))
    
    
    return result, result_state

def f(i, j):
    if i is j:
        return 1
    return 0

def oracle(i, j):
    return ((-1)**f(i,j))*i*j

def G(psi, target):
    return ((2**(target.shape[0]-2))-1)/(2**(target.shape[0]-2))*psi + (2/np.sqrt(2**target.shape[0]))*target

def grovers(register1, register2, vis = False):
    
    psi = normalise(*register1)
    target = H(*register2)
    
    psi = oracle(psi, target)
    psiG = G(psi, *register2)
    
    iterations = int((np.pi/4)*np.sqrt(2**target.shape[0]))
    for i in range(iterations): # Set to 4 iterations
        psi = oracle(psiG, target)
        psiG = G(psi, *register2)
    return measure(psiG)

n = 16
register1 = computational_basis(n)
register2 = [register1[8]]

probs = [0 for s in register1]

for i in range(1000):
    result, state = grovers(register1, register2)
    probs[result] += 1
    
print(probs)

probs /= np.sum(probs)

fig, ax = plt.subplots()

index = np.arange(n)
bar_width,opacity = 0.8, 0.4

rects = ax.bar(index, probs, bar_width,
                alpha=opacity, color='b')

ax.set_xlabel('Vector of Computational Basis')
ax.set_ylabel('Probability of Finding State')
ax.set_title('Grovers Algorithm')
ax.set_xticks(index)
ax.set_xticklabels([r'$\left|{'+str(s)+r'}\right\rangle$' for s in range(n)])

fig.tight_layout()
plt.show()
