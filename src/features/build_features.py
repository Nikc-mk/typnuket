import math

import pandas as pd


def create_features():
    data = pd.read_csv("../../data/interim/data_all.csv", index_col="row_id")
    print(data.columns)
    data["timestamp"] = data["timestamp"].astype("datetime64[ns]")

    data["timestamp_lag_1"] = data.groupby("gate_id")["timestamp"].shift(1)
    data["timestamp_lag_2"] = data.groupby("gate_id")["timestamp"].shift(2)
    data["timestamp_lag_3"] = data.groupby("gate_id")["timestamp"].shift(3)
    data["timestamp_lag_4"] = data.groupby("gate_id")["timestamp"].shift(4)
    data["timestamp_lag_5"] = data.groupby("gate_id")["timestamp"].shift(5)

    data["diff_time_gate_lag_1"] = (
        data["timestamp"] - data["timestamp_lag_1"]
    ) / pd.Timedelta(seconds=1)
    data["diff_time_gate_lag_2"] = (
        data["timestamp"] - data["timestamp_lag_2"]
    ) / pd.Timedelta(seconds=1)
    data["diff_time_gate_lag_3"] = (
        data["timestamp"] - data["timestamp_lag_3"]
    ) / pd.Timedelta(seconds=1)
    data["diff_time_gate_lag_4"] = (
        data["timestamp"] - data["timestamp_lag_4"]
    ) / pd.Timedelta(seconds=1)
    data["diff_time_gate_lag_5"] = (
        data["timestamp"] - data["timestamp_lag_5"]
    ) / pd.Timedelta(seconds=1)

    data.fillna(value=0, inplace=True)

    data["hour"] = data["timestamp"].dt.hour
    data["minute"] = data["timestamp"].dt.minute
    data["second"] = data["timestamp"].dt.second
    data["day"] = data["timestamp"].dt.day
    data["dayofweek"] = data["timestamp"].dt.dayofweek
    data["is_weekend"] = data["dayofweek"] > 4
    data["is_weekend"] = data["is_weekend"].apply(int)
    data["time_to_sec"] = (
        data["hour"] * 3600 + data["minute"] * 60 + data["second"]
    )

    data["dayweek"] = data["dayofweek"]
    data = pd.get_dummies(
        data, columns=["dayofweek", "gate_id", "hour"], dtype="int8"
    )
    data["hour"] = data["timestamp"].dt.hour

    lst_features = data.drop(
        columns=[
            "timestamp",
            "timestamp_lag_1",
            "timestamp_lag_2",
            "timestamp_lag_3",
            "timestamp_lag_4",
            "timestamp_lag_5",
            "diff_time_gate_lag_1",
            "diff_time_gate_lag_2",
            "diff_time_gate_lag_3",
            "diff_time_gate_lag_4",
            "diff_time_gate_lag_5",
            "dayofweek_0",
            "dayofweek_1",
            "dayofweek_2",
            "dayofweek_3",
            "dayofweek_4",
            "dayofweek_5",
            "dayofweek_6",
        ]
    ).columns
    print(lst_features)

    for i in lst_features:
        for j in range(1, 6):
            data[f"{i}_lag_{j}"] = data[f"{i}"].shift(j)

    data["diff_time_to_sec"] = data["time_to_sec"].diff(1)
    data["diff_time_to_sec_2"] = data["time_to_sec"].diff(2)
    data["diff_time_to_sec_3"] = data["time_to_sec"].diff(3)
    data["diff_time_to_sec_4"] = data["time_to_sec"].diff(4)
    data["diff_time_to_sec_5"] = data["time_to_sec"].diff(5)

    data = pd.get_dummies(data, columns=["day"], dtype="int8")

    data.to_csv("../../data/outpute/public_train_features_5.csv")


if __name__ == "__main__":
    create_features()
