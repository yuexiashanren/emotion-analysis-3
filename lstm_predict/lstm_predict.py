import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import LSTM, Dense, Activation

#split：训练比
def load_data(file_name, sequence_length=10, split=0.8):
    df = pd.read_csv(file_name, sep=',', usecols=[1])
    data_all = np.array(df).astype(float)
    scaler = MinMaxScaler()
    data_all = scaler.fit_transform(data_all)
    data = []
    for i in range(len(data_all) - sequence_length - 1):
        data.append(data_all[i: i + sequence_length + 1])
    reshaped_data = np.array(data).astype('float64')
    np.random.shuffle(reshaped_data)
    # 对x进行统一归一化，而y则不归一化
    x = reshaped_data[:, :-1]
    y = reshaped_data[:, -1]
    split_boundary = int(reshaped_data.shape[0] * split)
    train_x = x[: split_boundary]
    test_x = x[split_boundary:]

    train_y = y[: split_boundary]
    test_y = y[split_boundary:]

    return train_x, train_y, test_x, test_y, scaler


def build_model():
    # input_dim是输入的train_x的最后一个维度，train_x的维度为(n_samples, time_steps, input_dim)
    model = Sequential()
    model.add(LSTM(input_dim=1, output_dim=50, return_sequences=True))
    print(model.layers)
    model.add(LSTM(100, return_sequences=False))
    model.add(Dense(output_dim=1))
    model.add(Activation('linear'))

    model.compile(loss='mse', optimizer='rmsprop')
    return model


def train_model(train_x, train_y, test_x, test_y):
    model = build_model()
    #模型训练成功
    try:
        model.fit(train_x, train_y, batch_size=16, nb_epoch=30, validation_split=0.1)
        predict = model.predict(test_x)
        predict = np.reshape(predict, (predict.size, ))
    #模型训练失败
    except KeyboardInterrupt:
        print("实际结果1：", test_y)
        print("预测结果1：", predict)
    
    return predict, test_y


if __name__ == '__main__':
    train_x, train_y, test_x, test_y, scaler = load_data('stu_value.csv')
    train_x = np.reshape(train_x, (train_x.shape[0], train_x.shape[1], 1))
    test_x = np.reshape(test_x, (test_x.shape[0], test_x.shape[1], 1))
    predict_y, test_y = train_model(train_x, train_y, test_x, test_y)
    predict_y = scaler.inverse_transform([[i] for i in predict_y])
    test_y = scaler.inverse_transform(test_y)
    
    print("实际结果2：", test_y)
    print("预测结果2：", predict_y)
    x = [x for x in range(1, len(test_y)+1)]
    plt.figure("对比")
    plt.plot(x, predict_y, 'g:', label='pred')
    plt.plot(x, test_y, 'r-', label='real')
    plt.legend() # 显示图例
    #plt.plot(x,y)
    plt.xlabel("time")#X轴标签
    plt.ylabel("value")#Y轴标签 
    plt.show()

