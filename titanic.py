import pandas as pd  # подключаем библиотеку pandas для работы с таблицами и данными 
import matplotlib.pyplot as plt  # подключаем библиотеку matplotlib для построения графиков

df = pd.read_parquet("titanic.parquet") # чтение исходного parquet файла
df.to_csv("titanic.csv", index=False) # сохранение данных в формат csv
df_csv = pd.read_csv("titanic.csv") # чтение сохраненного csv файла для проверки

quantity_passengers = df_csv.groupby("Pclass").size() # подсчет общего количества пассажиров для каждого класса
survived = df_csv[df_csv["Survived"] == 1].groupby("Pclass").size() / quantity_passengers * 100 # вычисление процента выживших
not_survived = df_csv[df_csv["Survived"] == 0].groupby("Pclass").size() / quantity_passengers * 100 # вычисление процента погибших

survival_data = pd.DataFrame({ # создание таблицы данных для графика
    "выжившие": survived,
    "не выжившие": not_survived
})

ax = survival_data.plot(kind="bar", stacked=True, color=["green", "red"]) # построение столбчатой диаграммы
ax.set_xlabel("класс билета") # название оси x
ax.set_ylabel("доля пассажиров (%)") # название оси y
ax.set_title("выживаемость пассажиров в зависимости от класса билета") # заголовок графика
ax.legend(title="статус") # добавление легенды

plt.show() # отображение графика