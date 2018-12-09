# Grovers-Algorithm
A simulation of Grover's quantum algorithm for a classical computer.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

This only requires numpy to run. If you want to visualise aspects of the algorithm (such as superposition collapse probabilities) you will need matplotlib too. To install open terminal/command line and type the following commands.

```
pip install numpy
pip install matplotlib
```

## Running the tests

Explain how to run the automated tests for this system

### Running Grovers Algorithm

This creates 16-dimensional computational basis and attempts to find x from the basis.

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

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Me, Myself and I
* (also Lov Grover)
