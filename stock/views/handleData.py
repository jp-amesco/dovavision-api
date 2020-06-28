import pandas as pd
import pandas_datareader as pdr

class HandlerData(object):

    def get_data(name, start, end):
        data = pdr.data.get_data_yahoo(name, start=start, end=end)
        
        return data.reset_index()

    def get_labels(data):
        return data['Open'] < data['Close']


    def get_inputs(labels):
        return labels[len(labels) - 31: len(labels) - 1]

    def format_date(dates):
        day_list = list()
        for i in range(len(dates)): 
            day_list.append(dates[i].timetuple().tm_yday)
        
        return day_list

    def get_move(data):
        return data['Open'] < data['Close']

    def save_model(model, local):
        model.save(local)
    