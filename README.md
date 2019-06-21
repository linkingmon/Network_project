# Network_project<br>

## Usage<br>
1. run "bash setup.sh" to install all packages<br> 
2. run "pip3 install tensorflow==1.13" if you have no cuda；otherwise, run “pip3 install tensorflow-gpu==1.13”<br>
3. Download our pretrained model from https://drive.google.com/open?id=1CRMeaL2TP9zSEB3m-OUv9C_sKKzqqGjw <br>
4. run "python3 app.py 0" for closing face detection & "python3 app.py 1" for opening face detection<br><br>

## Update<br>
- (6/7)  Apply frame rate control on server side<br>
- (5/31) 修正他人打字，自己的字會被刷掉的錯誤<br>
- (5/31) 支援"中文"聊天<br>
- (5/30) 聊天室與直播排版完成<br>
- (5/26) chatroom done<br>
- (5/25) face detection done<br><br>

## Description<br>
- 要下載很多套件<br>
- 下載keras >= 2.2.4<br>
- Flask-SQLAlchemy一定要裝2.1(pip3 install flask_sqlalchemy==2.1.0)<br>
- model檔案下載：https://drive.google.com/open?id=1CRMeaL2TP9zSEB3m-OUv9C_sKKzqqGjw <br>
- 只有人臉辨識找到人臉位置時，才會進行表情辨識<br>
