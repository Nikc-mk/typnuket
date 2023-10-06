Typnuket
==============================
Проект посвящен решению конкурсной задачи https://ods.ai/tracks/linear-models-autumn23/competitions/gates_autumn_2023

Турникеты 2.0: Чей это след?
Кто там? Предскажите, кто вошел в здание по времени и турникету. Но теперь легче: мы знаем, что "след" через турникеты принадлежит "Х". Кто этот "Х" предстоит вычислить по данным, которые нам известны. А ID юзеров известны по обучающей выборке (кроме нескольких новых!).
Чтобы попасть в здание, нужно пройти через турникет. Чтобы открыть парковку, нужно открыть шлагбаум. Чтобы попасть на этаж, нужно приложить “таблетку”. Все это фиксируется - кто, в какую дату, в какое время.
Сможем ли мы выучить кому конкретно принадлежит след прохода через турникеты? Теперь мы знаем, что это был кто-то, кто уже был. (Правда, есть и несколько - не больше 10% - новых).
“8 утра понедельник, турникет 4? Директор.” “11 утра суббота? Гриша. Но Гриша в последний день месяца никогда не приходит.”  Какие есть паттерны в настоящих данных?
В тестовой выборке id посетителей заменены на слова, которые встречались в курсе "Линейные модели": aucroc, binary, blue, categorical и т.п.
Ваша задача в этом раунде составить таблицу вида:

user_word	preds

aucroc	49

binary	12

blue	55

categorical	-999

coefficient	15

где user_word - index, preds - колонка с соответствующими id. Таблицу нужно запомнить как csv (см. пример в секции Data). -999 – id нового посетителя, которого раньше не было.
Каждому слову сопоставлен вес, который зависит от того, насколько трудно предсказать id. Баллы набираются как взвешенная по весам сумма правильных ответов. Чем сложнее вы отгадали слово, тем больше баллов.

Отгадали все? Забирайте 560 баллов и становитесь победителем.

Для курса "Линейные модели" - используем только линейную (логистическую) регрессию.
Для курса "Деревья и их ансамбли" - используем деревья и ансамбли.
Ну и если вы знаете нейросети, SVM, и все-все-все, то используйте все, но для оценки в курсе будем смотреть на методы, которые вы использовали, и, соответственно, корректировать оценку. Ведь курсы - учебные, значит надо осваивать то, что было на курсе.

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── outpute        <- Data for submit.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
