#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

from conans import ConanFile, CMake, tools, RunEnvironment
import os


class TestPackageConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        mpiexec = os.path.join(os.environ['MPI_BIN'], 'mpiexec.exe')
        with tools.environment_append(RunEnvironment(self).vars):
            command = '%s -n 2 %s' % (mpiexec, os.path.join("bin", "test_package"))
            self.run(command)
