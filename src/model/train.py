import glob
import os

import click
import mlflow
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

SELECTED_COLUMNS = (
    "Pregnancies",
    "PlasmaGlucose",
    "DiastolicBloodPressure",
    "TricepsThickness",
    "SerumInsulin",
    "BMI",
    "DiabetesPedigree",
    "Age",
)


# define functions
def train(training_data, reg_rate):
    mlflow.autolog()

    # read data
    df = get_csvs_df(training_data)

    # split data
    x_train, _, y_train, y_test = split_data(df)

    # train model
    train_model(reg_rate, x_train, y_train)


def get_csvs_df(path):
    if not os.path.exists(path):
        raise RuntimeError(f"Cannot use non-existent path provided: {path}")
    csv_files = glob.glob(f"{path}/*.csv")
    if not csv_files:
        raise RuntimeError(f"No CSV files found in provided data path: {path}")
    return pd.concat((pd.read_csv(f) for f in csv_files), sort=False)


def split_data(df):
    x = df[list(SELECTED_COLUMNS)].values
    y = df["Diabetic"].values
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30, random_state=0)
    return x_train, x_test, y_train, y_test


def train_model(reg_rate, x_train, y_train):
    # train model
    LogisticRegression(C=1 / reg_rate, solver="liblinear").fit(x_train, y_train)


@click.command()
@click.option("--training_data", required=True, help="path to folder with training data", type=str)
@click.option("--reg_rate", default=0.01, help="reg_rate for LogisticRegression", type=float)
def main(training_data, reg_rate):
    # add space in logs
    print("\n\n")
    print("*" * 60)

    # run main function
    train(training_data, reg_rate)

    # add space in logs
    print("*" * 60)
    print("\n\n")


if __name__ == "__main__":
    main()  # pylint: disable=no-value-for-parameter
