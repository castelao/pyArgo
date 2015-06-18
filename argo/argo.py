# -*- coding: utf-8 -*-

try:
    from netCDF4 import Dataset
except:
    from pupynere import netcdf_file as Dataset





filename = 'test_data/D20150316_prof.nc'


def extract_profile(filename, pid=None):
    """ Extract ARGO profiles from a netCDF file

        If n is not given, extract all profiles.
    """
    nc = Dataset(filename)

    if pid is None:
        try:
            pid = range(len(nc.dimensions['N_PROF']))
        except:
            pid = range(nc.dimensions['N_PROF'])
    elif type(pid) is int:
        pid = [pid]

    output = [ARGO() for n in pid]

    for v in nc.variables:
        if 'N_PROF' not in nc.variables[v].dimensions:
            for n in range(len(pid)):
                #if nc.variables[v].typecode() == 'c':
                #    output[n].attributes[v] = "".join(nc.variables[v][:]).strip()
                #else:
                output[n].attributes[v] = nc.variables[v][:]
        # Different values for each profile
        else:
            dims = list(nc.variables[v].dimensions)
            ax = dims.index('N_PROF')
            dims.remove('N_PROF')

            if nc.variables[v].shape[0] != 0:
                " Sometimes N_HISTORY is zero, so there is no data"

                pvar = nc.variables[v][:].swapaxes(ax, 0)

                for n, p in enumerate(pid):
                    if 'N_LEVELS' not in dims:
                        output[n].attributes[v] = pvar[p]
                    else:
                        output[n].data[v] = pvar[p].swapaxes(0, dims.index('N_LEVELS'))
    return output


class ARGO(object):    
    def __init__(self):

        self.data = {}
        self.attributes = {}

    def keys(self):
        return self.data.keys()

    def __getitem__(self, key):
        return self.data[key]
