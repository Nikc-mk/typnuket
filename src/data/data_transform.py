import pandas


def concat_raw_data():
    data_train = pandas.read_csv(
        "../../data/raw/train.csv", index_col="row_id"
    )
    data_test = pandas.read_csv("../../data/raw/test.csv", index_col="row_id")
    data_train.drop(columns=["user_id"], inplace=True)
    data_end = data_train._append(other=data_test)
    data_end.to_csv("../../data/interim/data_all.csv")


def create_public_train():
    data_train = pandas.read_csv(
        "../../data/raw/train.csv", index_col="row_id"
    )
    data_train.drop(columns=["timestamp", "gate_id"], inplace=True)
    data_train.to_csv("../../data/interim/target.csv")


if __name__ == "__main__":
    concat_raw_data()
    create_public_train()
