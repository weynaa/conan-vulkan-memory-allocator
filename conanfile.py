from conans import ConanFile
from conans.tools import download,unzip
from distutils.dir_util import copy_tree
import os
import shutil

class VulkanMemoryAllocator(ConanFile):
    """Build VulkanMemoryAllocator"""
    name = "VulkanMemoryAllocator"
    version = "2.3.0"
    url = "https://github.com/GPUOpen-LibrariesAndSDKs/VulkanMemoryAllocator"
    author = "AMD"
    license = "MIT"
    settings = "os", "arch", "compiler", "build_type"
    generators = ["cmake","cmake_multi"]
    exports = "*"
    description = "VulkanMemoryAllocator library"
    requires = (
    )
    options = {"shared": [True, False]}
    default_options = {
        "shared": False
    }
    exports_sources = "cmake/*", "config/*", "include/*", "config/*", "src/*", "CMakeLists.txt"
    def source(self):
        zipName = "v"+self.version+".zip"
        download("https://github.com/GPUOpen-LibrariesAndSDKs/VulkanMemoryAllocator/archive/"+zipName,zipName)
        unzip(zipName)
        #shutil.move("VulkanMemoryAllocator-"+self.version, "VulkanMemoryAllocator")
        copy_tree("VulkanMemoryAllocator-"+self.version+"/",".")
        os.unlink(zipName)
        shutil.rmtree("VulkanMemoryAllocator-"+self.version+"/")
    def package(self):
        self.copy("src/vk_mem_alloc.h","include",keep_path=False)
        if self.settings.compiler == "Visual Studio":
            self.copy("src/vk_mem_alloc.natvis","src",keep_path=False)

    def package_info(self):
        self.info.header_only()
        if self.settings.compiler == "Visual Studio":
            self.cpp_info.srcdirs.append("src")

    