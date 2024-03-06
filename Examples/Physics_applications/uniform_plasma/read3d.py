import openpmd_api as io
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    series = io.Series("diags/diag1/openpmd.h5",io.Access.read_only)
    series2 = io.Series("diags/diag1/test.h5", io.Access.read_only)
    iterations = np.asarray(series.iterations)

    eV = -1.602*10**(-19)


    it = series.iterations[0]
    it2 = series2.iterations[0]

    rho = it.meshes["rho"]
    rho_scalar = rho[io.Record_Component.SCALAR]
    rho_data = rho_scalar.load_chunk()

    rho2 = it2.meshes["rho"]
    rho_scalar2 = rho2[io.Record_Component.SCALAR]
    rho_data2 = rho_scalar2.load_chunk()


    series.flush()


    print(rho_data[:10,0,0])
    print(rho_data2[:10,0,0])



    # series2 = io.Series("diags/diag1/test.h5", io.Access.create)
    #
    # rho_test = series2.write_iterations()[0]. \
    #     meshes["rho"][io.Mesh_Record_Component.SCALAR]
    #
    # dataset = io.Dataset(rho_data.dtype, rho_data.shape)
    # rho_test.reset_dataset(dataset)
    # series2.flush()
    #
    # rho_test.store_chunk(rho_data)
    # series2.flush()
    # print(rho_test[:10,0,0])
    #
    # series2.write_iterations()[0].close()
    #
    # series2.close()

    # series3 = io.Series("diags/diag1/test.h5", io.Access.read_only)
    # it3 = series3.iterations[0]
    # rho3 = it3.meshes["rho"]
    # rho_scalar3 = rho3[io.Record_Component.SCALAR]
    # rho_data3 = rho_scalar3.load_chunk()
    # print(rho_data3)
    #
    # series3.close()


    # rho_x = []
    # rho_y = []
    # rho_z = []
    # for i in range(32):
    #     for j in range(32):
    #         for k in range(32):
    #             rho_x.append(rho_data[i,j,k] / eV)
    #             rho_y.append(rho_data[0,i,0] / eV)
    #             rho_z.append(rho_data[0,0, i] / eV)




    # rho_x = rho_data[:32,0,0]
    # rho_y = rho_data[0,:32,0]
    # rho_z = rho_data[0,0, :32]

    # print(rho_x)
    #
    # fig = plt.figure()
    # ax = fig.add_subplot(projection = '3d')
    # ax.scatter(rho_x, rho_y, rho_z)
    # plt.show()

    series.close()