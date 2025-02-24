import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import datetime
import json
import math
import time

class Calculate:

    # Calculates least square regression and returns all variables used.
    def leastSquareRegression(self, x: list, y: list) -> tuple:
        start_time = time.perf_counter()

        m, b = np.polyfit(x, y, 1)
        u = np.mean(y)
        s1 = np.std(y)
        s2 = np.var(x)
        cv = (s1 / u)
        regression = (m * x + b)

        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f"LQR\nCompute Time: {(elapsed_time * 1000):.2f}ms.\nSlope: {m:.2f}\nIntercept: {b:.2f}\nMean: {u:.2f}\nStandard Deviation: {s1:.2f}\nVariance: {s2:.2f}\nCoefficient Variation: {cv:.2f} | {(cv * 100):.2f}%\n")

        return {
            'm': m,
            'x': x,
            'b': b,
            'u': u,
            's1': s1,
            's2': s2,
            'cv': cv,
            'regression': regression
        }

    # Calculates exponential moving average (EMA) and returns smoothed-out data points.
    def exponentialMovingAverage(self, data: dict, period) -> any:
        start_time = time.perf_counter()

        ema = data.ewm(span=period, adjust=False).mean()

        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f"EMA\nCompute Time: {(elapsed_time * 1000):.2f}ms.\nResults:\n{ema}\n")

        return ema

    # Plots data analysis and saves graph.
    def _visualize(self, item: any,  x: any, y: any, lsr: any, ema: any) -> None:
        today = datetime.date.today()
        x = [today - datetime.timedelta(days=i) for i in range(90, 0, -1)]

        # Formatting. Colors @ https://matplotlib.org/stable/_images/sphx_glr_named_colors_003.png
        plt.style.use('dark_background')
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
        plt.xticks(fontsize=8)

        # Plotting
        plt.plot(x, y, marker="o", markersize=2, color="cornflowerblue", alpha=1, label="Raw Data")
        plt.plot(x, ema.values, color="cornflowerblue", markersize=1, alpha=.5, label="7-Day Epo. Moving Avg.")
        plt.plot(x, lsr['regression'], color="fuchsia", alpha=.5,label="Least Square Regression")
        plt.fill_between(x, lsr['regression'] - lsr['s1'], lsr['regression'] + lsr['s1'], color='fuchsia', alpha=.1, label=f'±1 Std Dev ({lsr['s1']:.2f})')

        # Labels
        plt.suptitle(f"GEMW 90-Day Analysis")
        plt.title(f"Item: {item} | Date: {today}", fontsize=10)
        plt.xlabel("Past 90 Days")
        plt.ylabel("Item Price (GP)")
        plt.legend()

        # Save & Display
        plt.savefig(f"./data/MatPlotLib_Analysis/MPLA_{item}_{today}.jpg")
        plt.show()

    # Coordinates calculation process to return data insights.
    def trends(self, identifier: any) -> any:
        date_today = datetime.date.today()
        file_path = f"./data/GEMW_past_90_days/GEMW_{identifier}_{date_today}.json"

        with open(file_path, "r") as f:
            data = json.load(f)
            data = data[identifier]

        data_y = {
            'prices': list(entry['price'] for entry in data),
            'volumes': list(entry['volume'] for entry in data),
        }
        data_x = np.array(range(1, len(data) + 1))
        data_x_and_y = pd.Series(data_y['prices'], index=data_x)

        lqr_results = self.leastSquareRegression(x=data_x, y=data_y['prices'])
        ema_results = self.exponentialMovingAverage(data=data_x_and_y, period=7)

        self._visualize(item=identifier, x=data_x, y=data_y['prices'], lsr=lqr_results, ema=ema_results)