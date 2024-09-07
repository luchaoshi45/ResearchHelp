from abc import ABC, abstractmethod
from package.common_file import CommonFile
from resolve.resolve import Resolve


class CommonCore(ABC):
    def __init__(self, resolve: Resolve, package: CommonFile):
        self.resolve = resolve
        self.package = package
    
    @abstractmethod
    def run(self):
        pass
    
    def info(self):
        print(50 * "-")
        print(f"Repo Remote: {self.resolve.repo_url}")
        print(f"Repo Local Dir: {self.resolve.repo_dir}")
        # print(f"Repo Tree: {self.resolve.tree}")
        
        print(f"Output Dir: {self.package.out_dir}")
        print(f"Output File Name: {self.package.file_name}")
        print(f"File Header: {self.package.COMMON_FILE_HEADER}")
        
        print("\033[95mCore: {}\033[00m".format(self))
            
        print(50 * "-")