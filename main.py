# main.py

from utils import read_log_file
from log_parser import parse_log_lines
from data_processing import clean_data
from plotter import plot_metrics

def main():
    # Здесь можно задать путь к файлу логов
    log_file = "ignite_short.log"
    lines = read_log_file(log_file)

    # Парсим лог
    raw_records = parse_log_lines(lines)
    # print('Raw records = ')
    # print(raw_records)
    # Очищаем и нормализуем данные
    cleaned_records = clean_data(raw_records)

    # Если хотим построить графики
    if cleaned_records:
        plot_metrics(cleaned_records)
        print("Plots have been saved successfully.")
    else:
        print("No data found to plot.")

if __name__ == "__main__":
    main()
