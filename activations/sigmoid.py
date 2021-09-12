from activations.activation import Activation
import numpy as np
import numpy.typing as npt


class Sigmoid(Activation):
    def call(self, z: npt.ArrayLike) -> npt.ArrayLike:
        return self._apply(z)

    def prime(self, z: npt.ArrayLike) -> npt.ArrayLike:
        return self._apply(z) * (1 - self._apply(z))

    def _apply(self, z: npt.ArrayLike) -> npt.ArrayLike:
        return 1.0 / (1.0 + np.exp(-z))
