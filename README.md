# MovieReviewsClassification
*Предсказание рейтинга по тексту отзыва на английском*

[Отчет по решению](https://github.com/c-nemo/MovieReviewsClassification/blob/main/report/%D0%9E%D1%82%D1%87%D0%B5%D1%82_%D0%93%D1%80%D0%B8%D0%BD%D0%B0%D1%82%D0%BE%D0%BC.pdf)

## Пример работы сайта

![image](https://github.com/c-nemo/MovieReviewsClassification/assets/86519457/0739d001-17b6-43f9-a1b7-e296dd1276aa)


## Структура репозитория

- streamlit_app - веб-приложение streamlit
- dataset_generation_notebooks - генерация датасетов из папки

  - make_csv_from_folder.ipynb - генерация первичного датасета
  - make_multi.ipynb - функция для undersampling-а доминирующих классов и функция создания multilabel-датасета для ordinal classification 
  
- model_training_notebooks - обучение моделей
  - Reviews_classification_binary_tree.ipynb - fine-tuning "bert-base-uncased" for classification on balanced dataset, with binary-tree approach to prediction, 2 epochs
  - under-multi-2.ipynb - fine-tuning "bert-base-uncased" fot multilabel classification, 2 epochs
  
- django_site - веб-приложение django

- results - результаты на тестовой выборке

- report - отчет о выборе и обучении моделей, анализ датасета
