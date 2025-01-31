# 作業想法與過程敘述
## 觀察資料
1. 資料擷取：`training data` 共計50個csv檔，分屬50戶用戶用電需求及太陽能板產電量。
2. 讀入資料：每筆csv檔內有共3欄：分別為timestamp、generation以及consumption，資料筆數統計為5832筆，時間戳記顯示取樣日期為2018年1/1~8/31，且頻率為1小時1次，共有5832/24=243天。另本案 `training data` 檢查無缺失值，故不做插補等補值流程。
3. 定義資料：觀察上述原始資料，除時間外，後兩欄產量及用量皆為小數型態，3個欄位分別以時間戳記、浮點數、浮點數作宣告。
4. 儲存資料：吾人希望觀察8個月中，季節變化對光照產電之變化，故先針對每筆資料分段(以24個sample為週期)，而後抽取彙整同一日期之數據為相同dataframe，最終將243個dataframe存為單一list變數。
7. 觀察資料：完成上述步驟後，產出list型態之變數 `train_data` 。地球日照最長為 **「夏至」** 日期約**6/21**左右，反之最短則為 **「冬至」** 日期約落在**12/22**，因 `train_data` 並無12月份資料，故以1/1資料代替觀察目標。

## 數據前處理
將單日電量數據plot繪圖(橫軸為時間vs.縱軸為電量)，綠色折線表示產電，藍色為用電。繪製如下圖1/1以及6/21分別50戶用戶的電力情形。
![1to25_Jan1](https://user-images.githubusercontent.com/117910213/203584383-feaddea1-9d97-4a71-8851-366d8fdbe693.png)
<center>1/1產電及用電情形(用戶No.0~No.24)</center>

![26to50_Jan1](https://user-images.githubusercontent.com/117910213/203584408-bce1d542-ee03-4336-82ee-b04f30597c2f.png)
<center>1/1產電及用電情形(用戶No.25~No.49)</center>

![1to25_Jun21](https://user-images.githubusercontent.com/117910213/203583711-0da20865-281f-4913-9308-6721a6ac9dfa.png)
<center>6/21產電及用電情形(用戶No.0~No.24)</center>

![26to50_Jun21](https://user-images.githubusercontent.com/117910213/203583715-ce765cf2-c9c6-4f64-a613-f558d557c090.png)
<center>6/21產電及用電情形(用戶No.25~No.49)</center>

## 模型訓練
1. 藉由觀察，50戶用戶單日產電量之產電高峰皆落在PM12:00左右，且上升及下降趨勢皆近似，惟用電量特徵則有大致群組特徵，故下一步試圖將類似用電特徵之用戶歸類並做regression。
2. 標準差在統計上用以衡量一組數據的離散程度，依據每個數據點與平均值的差異程度而定。在此選用標準差及平均值來表達電能產量與用量的波動程度與量。
3. 繪製每戶資料之「平均值vs.標準差」圖，可以看出數據點的分別集中情形，在此使用 `K-means` 做clustering並指定分2群。
4. 將同群合併為同一變數並以高斯函數做fitting，便可得出得出2類用戶對應之2個函數(fitting model)。
![1280px-Normal_distribution_pdf](https://user-images.githubusercontent.com/117910213/203588379-5b9d04d2-97d5-46fd-90e8-a220f7f1e371.png)

## 趨勢預測
1. 根據前7天資料帶入高斯函數取殘差，殘差小者變為該類用戶。
