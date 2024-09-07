from core.common_core import CommonCore
from package.common_file import CommonFile
from resolve.resolve import Resolve

class AiCore(CommonCore):
    def __init__(self, resolve: Resolve, package: CommonFile, ai):
        super().__init__(resolve, package)
        self.ai = ai
    
    def construct(self):
        pass
        
if __name__ == '__main__':
    ai_core = AiCore()
    print(ai_core.ai) # None