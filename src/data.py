
problem_type_to_model_type_dict = {
    "Classification": ["XGBoost", "CatBoost", "LightGBM", "RandomForest", "LogisticRegression", "SVC", "KNeighborsClassifier", "GaussianNB"],
    "Regression": ["XGBoost", "CatBoost", "LightGBM", "RandomForest", "LinearRegression", "Ridge", "Lasso", "ElasticNet"],
    "Clustering": ["KMeans", "AgglomerativeClustering", "DBSCAN", "OPTICS"],
    "Anomaly Detection": ["XGBoost", "CatBoost", "LightGBM", "RandomForest"]
}

problem_specific_model_description_dict = {
    "Classification": {
        "XGBoost": "XGBoost 在分類問題中通常用於處理大規模、高維度或不平衡的數據集。",
        "CatBoost": "CatBoost 在分類問題中特別適用於處理具有很多類別型特徵的數據。",
        "LightGBM": "LightGBM 在分類問題中提供了高度優化的速度和效果，尤其適用於大數據集。",
        "RandomForest": "隨機森林是一種經典的分類算法，適用於各種數據集，尤其在特徵維度高的情況下。",
        "LogisticRegression": "邏輯回歸在二元或多類別分類問題中是一個基礎但卻很實用的模型。",
        "SVC": "支持向量機（SVC）在分類問題中特別適用於處理線性不可分和高維數據。",
        "KNeighborsClassifier": "k-近鄰算法（KNeighborsClassifier）是一種基於實例的學習，適用於小至中等規模的數據集。",
        "GaussianNB": "高斯朴素貝葉斯（GaussianNB）是一個基於機率的分類器，特別適用於具有連續特徵的數據集。"
    },
    "Regression": {
        "XGBoost": "XGBoost 在回歸問題中通常用於實現高度準確的預測模型。",
        "CatBoost": "CatBoost 在回歸問題中特別適用於處理具有類別特徵的數據，並提供強大的自動特徵工程能力。",
        "LightGBM": "LightGBM 在回歸問題中提供了高度優化的速度和效果，適用於大規模和高維數據集。",
        "RandomForest": "隨機森林在回歸問題中能有效地處理非線性關係和高度集成的數據。",
        "LinearRegression": "線性回歸是一個基本但強大的回歸工具，通常用作基線模型。",
        "Ridge": "Ridge 回歸在具有多重共線性的回歸數據中表現良好。",
        "Lasso": "Lasso 回歸用於特徵選擇和處理高度相關的特徵，通常用於維度減少。",
        "ElasticNet": "ElasticNet 回歸結合了 Ridge 和 Lasso 的優點，對於具有多重共線性或高維數據集特別有用。"
    },
    "Clustering": {
        "KMeans": "K均值是一種經典的聚類算法，適用於找出數據中的隱藏模式或分組。",
        "DBSCAN": "DBSCAN 非常適用於發現具有任意形狀的聚類。",
        "AgglomerativeClustering": "AgglomerativeClustering 是一種自底向上的聚類方法，適用於發現數據中的層次結構。",
        "OPTICS": "OPTICS 是一種基於密度的聚類算法，適用於發現具有不同密度和形狀的聚類。"
    },
    "Anomaly Detection": {
        "XGBoost": "XGBoost 可用於異常檢測，特別是在需要考慮多個特徵來識別異常的情況下。",
        "RandomForest": "隨機森林是一個有效的異常檢測工具，因為它能捕捉到數據中複雜的結構。",
        "CatBoost": "CatBoost 也可用於異常檢測，特別是當數據集中有類別型特徵時。",
        "LightGBM": "LightGBM 可以高效地處理大規模數據集，因此也適用於需要快速識別異常的場景。"
    }
}

required_parameters_dict = {
    "Classification": {
        "XGBoost": ["objective", "eval_metric", "eta", "max_depth", "min_child_weight", "subsample", "colsample_bytree"],
        "CatBoost": ["loss_function", "iterations", "depth", "learning_rate", "cat_features"],
        "LightGBM": ["objective", "metric", "learning_rate", "num_leaves", "min_data_in_leaf"],
        "RandomForest": ["n_estimators", "criterion", "max_depth", "min_samples_split"],
        "LogisticRegression": ["penalty", "C", "solver"],
        "SVC": ["C", "kernel", "degree", "gamma"],
        "KNeighborsClassifier": ["n_neighbors", "weights", "algorithm"],
        "GaussianNB": ["var_smoothing"]
    },
    "Regression": {
        "XGBoost": ["objective", "eval_metric", "eta", "max_depth", "min_child_weight", "subsample", "colsample_bytree"],
        "CatBoost": ["loss_function", "iterations", "depth", "learning_rate"],
        "LightGBM": ["objective", "metric", "learning_rate", "num_leaves", "min_data_in_leaf"],
        "RandomForest": ["n_estimators", "criterion", "max_depth", "min_samples_split"],
        "LinearRegression": ["fit_intercept", "normalize"],
        "Ridge": ["alpha", "fit_intercept", "normalize"],
        "Lasso": ["alpha", "fit_intercept", "normalize"],
        "ElasticNet": ["alpha", "l1_ratio", "fit_intercept", "normalize"]
    },
    "Clustering": {
        "KMeans": ["n_clusters", "init", "n_init", "max_iter"],
        "AgglomerativeClustering": ["n_clusters", "affinity", "linkage"],
        "DBSCAN": ["eps", "min_samples", "metric"],
        "OPTICS": ["min_samples", "max_eps", "metric"]
    },
    "Anomaly Detection": {
        "XGBoost": ["objective", "eval_metric", "eta", "max_depth", "min_child_weight", "subsample", "colsample_bytree"],
        "CatBoost": ["loss_function", "iterations", "depth", "learning_rate"],
        "LightGBM": ["objective", "metric", "learning_rate", "num_leaves", "min_data_in_leaf"],
        "RandomForest": ["n_estimators", "criterion", "max_depth", "min_samples_split"]
    }
}

hyperparameter_range_dict = {
    "Classification": {
        "XGBoost": {
            "objective": (["binary:logistic", "multi:softmax", "multi:softprob"], "list"),
            "eval_metric": (["logloss", "merror", "mlogloss"], "list"),
            "eta": ((0.01, 0.3), "tuple"),
            "max_depth": ((3, 10), "tuple"),
            "min_child_weight": ((1, 6), "tuple"),
            "subsample": ((0.5, 1.0), "tuple"),
            "colsample_bytree": ((0.5, 1.0), "tuple")
        },
        "CatBoost": {
            "loss_function": (["Logloss", "CrossEntropy"], "list"),
            "iterations": ((100, 1000), "tuple"),
            "depth": ((4, 10), "tuple"),
            "learning_rate": ((0.01, 0.3), "tuple"),
            "cat_features": (["column_1", "column_2"], "list")
        },
        "LightGBM": {
            "objective": (["binary", "multiclass"], "list"),
            "metric": (["binary_error", "multi_error"], "list"),
            "learning_rate": ((0.01, 0.3), "tuple"),
            "num_leaves": ((15, 50), "tuple"),
            "min_data_in_leaf": ((20, 200), "tuple")
        },
        "RandomForest": {
            "n_estimators": ((50, 200), "tuple"),
            "criterion": (["gini", "entropy"], "list"),
            "max_depth": ((None, 10), "tuple"),
            "min_samples_split": ((2, 10), "tuple")
        },
        "LogisticRegression": {
            "penalty": (["l1", "l2", "elasticnet", "none"], "list"),
            "C": ((0.1, 10.0), "tuple"),
            "solver": (["newton-cg", "lbfgs", "liblinear", "sag", "saga"], "list")
        },
        "SVC": {
            "C": ((0.1, 10.0), "tuple"),
            "kernel": (["linear", "poly", "rbf", "sigmoid"], "list"),
            "degree": ((2, 5), "tuple"),
            "gamma": (["scale", "auto"], "list")
        },
        "KNeighborsClassifier": {
            "n_neighbors": ((1, 20), "tuple"),
            "weights": (["uniform", "distance"], "list"),
            "algorithm": (["auto", "ball_tree", "kd_tree", "brute"], "list")
        },
        "GaussianNB": {
            "var_smoothing": ((1e-9, 1e-6), "tuple")
        }
    },
    "Regression": {
        "XGBoost": {
            "objective": (["reg:squarederror", "reg:linear", "reg:logistic"], "list"),
            "eval_metric": (["rmse", "mae", "logloss"], "list"),
            "eta": ((0.01, 0.3), "tuple"),
            "max_depth": ((3, 10), "tuple"),
            "min_child_weight": ((1, 6), "tuple"),
            "subsample": ((0.5, 1.0), "tuple"),
            "colsample_bytree": ((0.5, 1.0), "tuple")
        },
        "CatBoost": {
            "loss_function": (["RMSE", "MAE", "Quantile"], "list"),
            "iterations": ((100, 1000), "tuple"),
            "depth": ((4, 10), "tuple"),
            "learning_rate": ((0.01, 0.3), "tuple")
        },
        "LightGBM": {
            "objective": (["regression", "regression_l1", "huber", "fair"], "list"),
            "metric": (["rmse", "mae"], "list"),
            "learning_rate": ((0.01, 0.3), "tuple"),
            "num_leaves": ((15, 50), "tuple"),
            "min_data_in_leaf": ((20, 200), "tuple")
        },
        "RandomForest": {
            "n_estimators": ((50, 200), "tuple"),
            "criterion": (["mse", "mae"], "list"),
            "max_depth": ((None, 10), "tuple"),
            "min_samples_split": ((2, 10), "tuple")
        },
        "LinearRegression": {
            "fit_intercept": ([True, False], "list"),
            "normalize": ([True, False], "list")
        },
        "Ridge": {
            "alpha": ((0.1, 10.0), "tuple"),
            "fit_intercept": ([True, False], "list"),
            "normalize": ([True, False], "list")
        },
        "Lasso": {
            "alpha": ((0.1, 10.0), "tuple"),
            "fit_intercept": ([True, False], "list"),
            "normalize": ([True, False], "list")
        },
        "ElasticNet": {
            "alpha": ((0.1, 10.0), "tuple"),
            "l1_ratio": ((0, 1), "tuple"),
            "fit_intercept": ([True, False], "list"),
            "normalize": ([True, False], "list")
        }
    },
    "Clustering": {
        "XGBoost": {  # 注意，XGBoost通常不用於聚類問題，這些參數只是做為示例
            "objective": (["reg:squarederror", "binary:logistic"], "list"),
            "eval_metric": (["rmse", "logloss"], "list"),
            "eta": ((0.01, 0.3), "tuple"),
            "max_depth": ((3, 10), "tuple"),
            "min_child_weight": ((1, 6), "tuple"),
            "subsample": ((0.5, 1.0), "tuple"),
            "colsample_bytree": ((0.5, 1.0), "tuple")
        },
        "KMeans": {
            "n_clusters": ((2, 10), "tuple"),
            "init": (["k-means++", "random"], "list"),
            "n_init": ((10, 20), "tuple"),
            "max_iter": ((100, 500), "tuple")
        },
        "AgglomerativeClustering": {
            "n_clusters": ((2, 10), "tuple"),
            "affinity": (["euclidean", "manhattan", "cosine"], "list"),
            "linkage": (["ward", "complete", "average", "single"], "list")
        },
        "DBSCAN": {
            "eps": ((0.1, 1.0), "tuple"),
            "min_samples": ((5, 20), "tuple"),
            "metric": (["euclidean", "manhattan", "cosine"], "list")
        },
        "OPTICS": {
            "min_samples": ((5, 20), "tuple"),
            "max_eps": ((1.0, 5.0), "tuple"),
            "metric": (["euclidean", "manhattan", "cosine"], "list")
        }
    },
    "Anomaly Detection": {
        "XGBoost": {
            "objective": (["reg:squarederror", "binary:logistic"], "list"),
            "eval_metric": (["rmse", "logloss"], "list"),
            "eta": ((0.01, 0.3), "tuple"),
            "max_depth": ((3, 10), "tuple"),
            "min_child_weight": ((1, 6), "tuple"),
            "subsample": ((0.5, 1.0), "tuple"),
            "colsample_bytree": ((0.5, 1.0), "tuple")
        },
        "CatBoost": {
            "loss_function": (["RMSE", "MAE", "Quantile"], "list"),
            "iterations": ((100, 1000), "tuple"),
            "depth": ((4, 10), "tuple"),
            "learning_rate": ((0.01, 0.3), "tuple")
        },
        "LightGBM": {
            "objective": (["regression", "regression_l1", "huber", "fair"], "list"),
            "metric": (["rmse", "mae"], "list"),
            "learning_rate": ((0.01, 0.3), "tuple"),
            "num_leaves": ((15, 50), "tuple"),
            "min_data_in_leaf": ((20, 200), "tuple")
        },
        "RandomForest": {
            "n_estimators": ((50, 200), "tuple"),
            "criterion": (["mse", "mae"], "list"),
            "max_depth": ((None, 10), "tuple"),
            "min_samples_split": ((2, 10), "tuple")
        }
    }
}

seaborn_datasets = [
    'anscombe',
    'attention',
    'brain_networks',
    'car_crashes',
    'diamonds',
    'dots',
    'exercise',
    'flights',
    'fmri',
    'gammas',
    'geyser',
    'iris',
    'mpg',
    'penguins',
    'planets',
    'tips',
    'titanic'
]

dataset_name_list = []

dataset_discrb_dict = {}

data_process_dict_pycaret = {
    "Classification": {},
    "Regression": {},
    "Clustering": {},
    "Time Series": {},
}