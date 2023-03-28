# MovieReviewsClassification
*Предсказание рейтинга по тексту отзыва на английском*

## Протестировать модель можно по ссылке:
https://captainnemo.pythonanywhere.com/app/prediction

## Структура репозитория

- dataset_generation_notebooks - генерация датасетов из папки

  - make_csv_from_folder.ipynb - генерация первичного датасета
  - make_multi.ipynb - функция для undersampling-а доминирующих классов и функция создания multilabel-датасета для ordinal classification 
  
- model_training_notebooks - обучение моделей
  - Reviews_classification_binary_tree.ipynb - fine-tuning "bert-base-uncased" for classification on balanced dataset, with binary-tree approach to prediction, 2 epochs
  - under-multi-2.ipynb - fine-tuning "bert-base-uncased" fot multilabel classification, 2 epochs
  
- django_site - веб приложение

- results - результаты на тестовой выборке

