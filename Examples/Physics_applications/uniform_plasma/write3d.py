import numpy as np
import openpmd_api as io

size = 32

data = np.arange(size*size*size, dtype = np.double).reshape(32,32,32)

series = io.Series("diags/diag1/test.h5", io.Access.create)

rho = series.write_iterations()[0]. \
    meshes["rho"][io.Mesh_Record_Component.SCALAR]

dataset = io.Dataset(data.dtype, data.shape)

rho.reset_dataset(dataset)

series.flush()
rho[()] = data
series.write_iterations()[0].close()
series.close()