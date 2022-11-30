from pkg_resources import get_distribution, DistributionNotFound
import sigc
try:
    __version__ = get_distribution("sigc").version
except DistributionNotFound:
    pass
