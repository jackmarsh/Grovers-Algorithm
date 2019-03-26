# Grovers-Algorithm
A simulation of Grover's quantum search algorithm for a classical computer.

## Abstract

Quantum algorithms are proving important to many fields as they repeatedly display, often expo- nential, speed up over their classical counterparts. In this paper, we discuss Grover’s algorithm which provides quadratic speed up over its classical alternative of searching for an element in an unstruc- tured database. It provides the mathematical grounding necessary to understand the algorithm while touching on the proof for the quadratic speed up in time complexity. With the main limitations of quantum algorithms coming from hardware specific decoherence problems, this paper hopes to generate excitement about the future prospects of this young yet growing area of Computer Science. There is no question that this algorithm will be instrumental in changing the future world.

## Getting Started

These instructions explain how to get a classical simulation of Grovers quantum search algorithm running on your local machine.

### Prerequisites

This only requires numpy to run. If you want to visualise aspects of the algorithm (such as superposition collapse probabilities) you will need matplotlib too. To install open terminal/command line and type the following commands.

```
pip install numpy
pip install matplotlib
```

### Running Grovers Algorithm

Run grovers.py to run the algorithm. The Jupyter notebook contains detailed mathematical explanations.

Running grovers.py like below creates 16-dimensional computational basis and attempts to find x from the basis.

It returns result and state, where result is the index of the found state in register 1 and state is the found state.

```
n = 16 # Number of vectors in computational basis
x = 3  # The value you want to find (should be in the computational basis)
register1 = computational_basis(n)
register2 = [register1[x]]

result, state = grovers(register1, register2)
```

## Authors

* **Jack Marsh** - *Initial work* - [Me](https://github.com/jackmarsh)

## License

This project is licensed under the MIT License

## Acknowledgments

* Me, Myself and I
* (also Lov Grover)
