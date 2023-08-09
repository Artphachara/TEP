###########
# Imports #
###############################################################################

from importlib.metadata import version, PackageNotFoundError

#############
# Constants #
###############################################################################

try:
    __version__ = version('TEP')
except PackageNotFoundError:
    pass

###############################################################################
