import sys

sys.path.append('.')
sys.path.append("/database")

print(sys.path)
from database import data_handler

obj = data_handler.MyData()
obj.view()



