from conans import ConanFile
import os


class MSMPIConan(ConanFile):
    name = "msmpi"
    version = "9.0"
    description = "Keep it short"
    url = "Microsoft MPI (MS-MPI) is a Microsoft implementation of the Message Passing Interface standard for " \
          "developing and running parallel applications on the Windows platform"
    homepage = "https://msdn.microsoft.com/en-us/library/bb524831%28v=vs.85%29.aspx"
    license = "Microsoft"
    settings = {"os": ["Windows"], "arch": ["x86", "x86_64"]}

    def source(self):
        url = 'https://github.com/SSE4/microsoft_mpi.git'
        self.run('git clone --depth 1 --branch %s %s' % (self.version, url))

    def package(self):
        self.copy(pattern="*", dst="license", src=os.path.join("microsoft_mpi", "License"))
        self.copy(pattern="*", dst="include", src=os.path.join("microsoft_mpi", "Include"), keep_path=True)
        self.copy(pattern="*.exe", dst="bin", src=os.path.join("microsoft_mpi", "Bin"), keep_path=False)
        self.copy(pattern="*.man", dst="bin", src=os.path.join("microsoft_mpi", "Bin"), keep_path=False)
        if self.settings.arch == "x86":
            self.copy(pattern="*.dll", dst="bin", src=os.path.join("microsoft_mpi", "Bin", "X86"), keep_path=False)
            self.copy(pattern="*", dst="lib", src=os.path.join("microsoft_mpi", "Lib", "x86"), keep_path=False)
        elif self.settings.arch == "x86_64":
            self.copy(pattern="*.dll", dst="bin", src=os.path.join("microsoft_mpi", "Bin", "x64"), keep_path=False)
            self.copy(pattern="*", dst="lib", src=os.path.join("microsoft_mpi", "Lib", "x64"), keep_path=False)

    def package_info(self):
        self.env_info.MPI_HOME = self.package_folder
        mpi_bin = os.path.join(self.package_folder, 'bin')
        self.env_info.MPI_BIN = mpi_bin
        self.env_info.PATH.append(mpi_bin)
        self.cpp_info.libs = ['msmpi']
