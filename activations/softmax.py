"""Softmax activation."""

from activations.activation import Activation
import numpy as np
import numpy.typing as npt


class Softmax(Activation):
    """Implements the Softmax activation function. Derives from `Activation`."""

    def __call__(self, z: npt.ArrayLike) -> npt.ArrayLike:
        """
        Compute the activation of the softmax function on z.

        Parameters:
        z: dot(weights, inputs) + bias

        Return:
        The activation output.
        """
        return self._apply(z)

    def prime(self, z: npt.ArrayLike) -> npt.ArrayLike:
        """
        Compute the output of the derivative of softmax function on z.

        Parameters:
        z: dot(weights, inputs) + bias

        Return:
        The output of the derivative of the activation function given z.
        """
        #  z = np.dot(weight, activation) + bias
        z = self._apply(z)
        z = np.reshape(z, (1, -1))
        # Diagflat is the same as z * np.identity(z)
        z = np.diagflat(z) - np.dot(z, np.transpose(z))
        return z

    def _apply(self, z: npt.ArrayLike) -> npt.ArrayLike:
        exps = np.exp(z)
        z = exps / exps.sum()
        return z
