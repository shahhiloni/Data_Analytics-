import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
prices = [150, 155, 148, 160, 170, 168, 175]

plt.figure(figsize=(10, 5))
plt.plot(
    days,
    prices,
    color="blue",
    marker="o",
    linewidth=2,
    markersize=8,
    label="Stock Price"
)

plt.title("Weekly Stock Price Trend", fontsize=16)
plt.xlabel("Days", fontsize=12)
plt.ylabel("Price (₹)", fontsize=12)
plt.grid(True)
plt.legend()
plt.show()