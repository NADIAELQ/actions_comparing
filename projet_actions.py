import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Télécharger les données avec des dates explicites
start_date = "2023-07-01"
end_date = "2023-10-01"

try:
    data = yf.download(
        ["AAPL", "MSFT"],
        start=start_date,
        end=end_date,
        interval="1d",
        group_by="ticker"
    )
except Exception as e:
    print(f"Erreur lors du téléchargement : {e}")
    exit()

# Préparer les données
apple = data["AAPL"]["Close"].rename("Apple")
microsoft = data["MSFT"]["Close"].rename("Microsoft")
df = pd.DataFrame({"Apple": apple, "Microsoft": microsoft})

# Supprimer les lignes avec des NaN (au cas où)
df.dropna(inplace=True)

# Tracer le graphique
plt.figure(figsize=(12, 6))
plt.plot(df.index, df["Apple"], label="Apple (AAPL)", color="blue")
plt.plot(df.index, df["Microsoft"], label="Microsoft (MSFT)", color="green")
plt.title("Évolution des Prix de Clôture : Apple vs Microsoft (Juillet 2023 - Octobre 2023)")
plt.xlabel("Date")
plt.ylabel("Prix (USD)")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.7)
plt.tight_layout()
plt.savefig("comparaison_actions.png")
plt.show()

# Calculer les performances
perf_apple = ((df["Apple"].iloc[-1] - df["Apple"].iloc[0]) / df["Apple"].iloc[0] * 100)
perf_microsoft = ((df["Microsoft"].iloc[-1] - df["Microsoft"].iloc[0]) / df["Microsoft"].iloc[0] * 100)

print(f"\nPerformance entre {start_date} et {end_date} :")
print(f"- Apple : {perf_apple:.2f}%")
print(f"- Microsoft : {perf_microsoft:.2f}%")

if perf_apple > perf_microsoft:
    print("\nConclusion : Apple a mieux performé que Microsoft.")
else:
    print("\nConclusion : Microsoft a mieux performé que Apple.")