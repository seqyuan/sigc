from pkg_resources import get_distribution, DistributionNotFound

try:
    __version__ = get_distribution("sigc").version
except DistributionNotFound:
    pass
