#################################################################################################################################
# You should not modify this part.
def config():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--consumption", default="./sample_data/consumption.csv", help="input the consumption data path")
    parser.add_argument("--generation", default="./sample_data/generation.csv", help="input the generation data path")
    parser.add_argument("--bidresult", default="./sample_data/bidresult.csv", help="input the bids result path")
    parser.add_argument("--output", default="output.csv", help="output the bids path")

    return parser.parse_args()


def output(path, data):
    import pandas as pd

    df = pd.DataFrame(data, columns=["time", "action", "target_price", "target_volume"])
    df.to_csv(path, index=False)

    return
# You should not modify this part.
#################################################################################################################################

if __name__ == "__main__":
    args = config()

    # data = [["2018-09-01 00:00:00", "buy", 2.5, 3],
    #         ["2018-09-01 01:00:00", "sell", 3, 5],
    #         ["2018-09-01 01:00:00", "buy", 2.5, 5]]
    data = [["2022-11-22 00:00:00", "buy", 1.64, 0.25],
            ["2022-11-22 01:00:00", "buy", 1.64, 0.25],
            ["2022-11-22 02:00:00", "buy", 1.64, 0.25],
            ["2022-11-22 03:00:00", "buy", 1.64, 0.25],
            ["2022-11-22 04:00:00", "buy", 1.64, 0.25],
            ["2022-11-22 05:00:00", "buy", 1.64, 0.25],
            ["2022-11-22 06:00:00", "buy", 1.64, 0.25],
            ["2022-11-22 07:00:00", "buy", 1.64, 0.25],
            ["2022-11-22 08:00:00", "buy", 1.64, 0.25],
            ["2022-11-22 09:00:00", "sell", 4, 0.2],
            ["2022-11-22 10:00:00", "sell", 3, 0.5],
            ["2022-11-22 11:00:00", "sell", 2, 0.7],
            ["2022-11-22 12:00:00", "sell", 1.5, 0.9],
            ["2022-11-22 13:00:00", "sell", 1, 1.2],
            ["2022-11-22 14:00:00", "sell", 0.5, 1.4],
            ["2022-11-22 15:00:00", "sell", 1, 1.2],
            ["2022-11-22 16:00:00", "sell", 1.5, 0.6],
            ["2022-11-22 17:00:00", "buy", 1.6, 0.1],
            ["2022-11-22 18:00:00", "buy", 1.7, 0.1],
            ["2022-11-22 19:00:00", "buy", 1.8, 0.2],
            ["2022-11-22 20:00:00", "buy", 1.9, 0.3],
            ["2022-11-22 21:00:00", "buy", 2, 0.4],
            ["2022-11-22 22:00:00", "buy", 2.1, 0.5],
            ["2022-11-22 23:00:00", "buy", 2.25, 0.6]]

    output(args.output, data)

# print("hello")
