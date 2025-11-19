import torch
from torch import nn


if __name__ == "__main__":
   # 入力のtensorの定義
   in_tensor = torch.ones(32, 3, 128, 128)

   #modelインスタンスの生成
   model =  ExcrciseModel()
    
   #  実行結果の確認
   out = model(in_tensor)
   print(f"in : {repr(in_tensor.shape)}")
   print(f"out : {repr(out.shape)}")