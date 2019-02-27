#实际与预测比较
from sklearn.metrics import recall_score  

def loadY():   
    y = [line.strip()  for line in open('./recallData/y.txt', 'r', encoding='utf-8').readlines() ]   
    return y
def loadYPre():   
    y_pred = [line.strip()  for line in open('./recallData/y_pre.txt', 'r', encoding='utf-8').readlines() ]   
    return y_pred

y_true = loadY()  
y_pred = loadYPre()
print("y_true",y_true)
print("y_pred",y_pred)
r = recall_score(y_true, y_pred, average='macro')   
print(r)