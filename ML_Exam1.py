questions = [
  {
    "id": 1,
    "category": "ML Overview - Training/Test Phases",
    "question": "What is the primary purpose of splitting data into training and test sets?",
    "options": [
      "To ensure equal representation of all classes",
      "To evaluate model performance on unseen data and detect overfitting",
      "To speed up the training process",
      "To make the dataset smaller and easier to process"
    ],
    "explanation": "The training/test split allows us to train the model on one portion of data and evaluate its generalization ability on unseen test data, helping detect overfitting.",
    "answer": "b"
  },
  {
    "id": 2,
    "category": "ML Overview - Basic Concepts",
    "question": "In machine learning terminology, what is a 'feature vector'?",
    "options": [
      "The numerical representation of all input attributes for one instance",
      "A single data point in the dataset",
      "The target variable we're trying to predict",
      "The error between predicted and actual values"
    ],
    "explanation": "A feature vector is the numerical representation of all input attributes (features) for a single instance/example in the dataset.",
    "answer": "a"
  },
  {
    "id": 3,
    "category": "ML Overview - Taxonomy",
    "question": "Which of the following best describes the difference between classification and regression?",
    "options": [
      "Classification uses labeled data, regression uses unlabeled data",
      "Classification is supervised, regression is unsupervised",
      "Classification is faster than regression",
      "Classification predicts discrete categories, regression predicts continuous values"
    ],
    "explanation": "Classification predicts discrete categories/classes (e.g., spam/not spam), while regression predicts continuous numerical values (e.g., house prices).",
    "answer": "d"
  },
  {
    "id": 4,
    "category": "ML Overview - Learning Types",
    "question": "What characterizes semi-supervised learning?",
    "options": [
      "Using only labeled data for training",
      "Using reinforcement signals for training",
      "Using both labeled and unlabeled data for training",
      "Using only unlabeled data for training"
    ],
    "explanation": "Semi-supervised learning uses a combination of labeled and unlabeled data, typically with a small amount of labeled data and a large amount of unlabeled data.",
    "answer": "c"
  },
  {
    "id": 5,
    "category": "ML Overview - Reinforcement Learning",
    "question": "In reinforcement learning, what is the agent trying to optimize?",
    "options": [
      "Cumulative reward over time",
      "Prediction accuracy on a test set",
      "Classification error rate",
      "Feature correlation"
    ],
    "explanation": "In reinforcement learning, an agent learns to take actions in an environment to maximize cumulative reward over time through trial and error.",
    "answer": "a"
  },
  {
    "id": 6,
    "category": "Data Preprocessing - Variable Types",
    "question": "What is the main difference between ordinal encoding and one-hot encoding for categorical variables?",
    "options": [
      "One-hot encoding is faster than ordinal encoding",
      "Ordinal encoding creates more features than one-hot encoding",
      "One-hot encoding only works with numerical data",
      "Ordinal encoding preserves order relationships, one-hot encoding doesn't"
    ],
    "explanation": "Ordinal encoding assigns integers that preserve order (e.g., low=1, medium=2, high=3), while one-hot encoding creates binary columns without assuming order.",
    "answer": "d"
  },
  {
    "id": 7,
    "category": "Data Preprocessing - Scaling",
    "question": "When should you use standardization (z-score normalization) instead of min-max scaling?",
    "options": [
      "When the data has outliers or unknown distribution bounds",
      "When you want values between 0 and 1",
      "When you have categorical variables",
      "When the dataset is very small"
    ],
    "explanation": "Standardization (mean=0, std=1) is more robust to outliers than min-max scaling and doesn't require knowing the data bounds.",
    "answer": "a"
  },
  {
    "id": 8,
    "category": "Data Preprocessing - Missing Data",
    "question": "Which approach for handling missing data is generally NOT recommended?",
    "options": [
      "Mean/median imputation",
      "Deleting rows with missing values",
      "Using algorithms that handle missing values naturally",
      "Ignoring missing values completely"
    ],
    "explanation": "Completely ignoring missing values can lead to errors and biased results. The other approaches are valid strategies depending on the context.",
    "answer": "d"
  },
  {
    "id": 9,
    "category": "Model Evaluation - Overfitting",
    "question": "What does a learning curve that shows training error much lower than validation error indicate?",
    "options": [
      "The model is underfitting",
      "The data is corrupted",
      "The model is overfitting",
      "The model is perfectly fitted"
    ],
    "explanation": "A large gap between low training error and high validation error is a classic sign of overfitting - the model memorizes training data but doesn't generalize.",
    "answer": "c"
  },
  {
    "id": 10,
    "category": "Model Evaluation - Cross Validation",
    "question": "What is the main advantage of k-fold cross-validation over the holdout method?",
    "options": [
      "It provides more robust performance estimates by using all data for both training and validation",
      "It's faster to compute",
      "It uses less memory",
      "It only works with large datasets"
    ],
    "explanation": "K-fold cross-validation uses all data for both training and validation across different folds, providing more robust and reliable performance estimates.",
    "answer": "a"
  },
  {
    "id": 11,
    "category": "Model Evaluation - Stratified Sampling",
    "question": "When is stratified sampling particularly important?",
    "options": [
      "When the dataset is very large",
      "When features are highly correlated",
      "When using linear regression",
      "When there is class imbalance in the target variable"
    ],
    "explanation": "Stratified sampling ensures each fold maintains the same proportion of samples for each target class, crucial when dealing with imbalanced datasets.",
    "answer": "d"
  },
  {
    "id": 12,
    "category": "Model Evaluation - Regression Metrics",
    "question": "What is the main difference between RMSE and MAE for regression evaluation?",
    "options": [
      "RMSE is always larger than MAE",
      "RMSE penalizes large errors more heavily than MAE",
      "MAE is more computationally expensive",
      "RMSE only works with linear models"
    ],
    "explanation": "RMSE (Root Mean Square Error) squares errors before averaging, giving more weight to larger errors, while MAE (Mean Absolute Error) treats all errors equally.",
    "answer": "b"
  },
  {
    "id": 13,
    "category": "Model Evaluation - Classification Metrics",
    "question": "In a confusion matrix for binary classification, what does precision measure?",
    "options": [
      "True positives / (True positives + False negatives)",
      "True negatives / (True negatives + False positives)",
      "(True positives + True negatives) / Total predictions",
      "True positives / (True positives + False positives)"
    ],
    "explanation": "Precision = TP/(TP+FP), measuring the proportion of positive predictions that were actually correct. It answers 'Of all positive predictions, how many were right?'",
    "answer": "d"
  },
  {
    "id": 14,
    "category": "Model Evaluation - Classification Metrics",
    "question": "What does recall (sensitivity) measure in binary classification?",
    "options": [
      "True positives / (True positives + False positives)",
      "True negatives / (True negatives + False negatives)",
      "True positives / (True positives + False negatives)",
      "False positives / (False positives + True negatives)"
    ],
    "explanation": "Recall = TP/(TP+FN), measuring the proportion of actual positives that were correctly identified. It answers 'Of all actual positives, how many did we find?'",
    "answer": "c"
  },
  {
    "id": 15,
    "category": "Model Evaluation - F1 Score",
    "question": "When is the F1-score particularly useful?",
    "options": [
      "When you need to balance precision and recall",
      "When you only care about accuracy",
      "When the dataset is perfectly balanced",
      "When you're doing regression"
    ],
    "explanation": "F1-score is the harmonic mean of precision and recall, useful when you need to balance both metrics, especially with imbalanced datasets.",
    "answer": "a"
  },
  {
    "id": 16,
    "category": "Linear Regression - Basic Concepts",
    "question": "In the linear regression equation y = β₀ + β₁x₁ + β₂x₂ + ε, what does β₀ represent?",
    "options": [
      "The slope of the regression line",
      "The error term",
      "The y-intercept when all predictors equal zero",
      "The correlation coefficient"
    ],
    "explanation": "β₀ (beta-zero) is the intercept term, representing the predicted value of y when all predictor variables equal zero.",
    "answer": "c"
  },
  {
    "id": 17,
    "category": "Linear Regression - Assumptions",
    "question": "Which of the following is NOT a key assumption of linear regression?",
    "options": [
      "Linear relationship between predictors and target",
      "Target variable must be categorical",
      "Homoscedasticity (constant variance of residuals)",
      "Independence of residuals"
    ],
    "explanation": "Linear regression assumes a continuous target variable, not categorical. The other options are key assumptions of linear regression.",
    "answer": "b"
  },
  {
    "id": 18,
    "category": "Linear Regression - Model Quality",
    "question": "What does an R² value of 0.85 indicate?",
    "options": [
      "The model is 85% accurate",
      "There's an 85% chance the model is correct",
      "The model has an 85% error rate",
      "85% of the variance in the target variable is explained by the model"
    ],
    "explanation": "R² (coefficient of determination) represents the proportion of variance in the dependent variable explained by the independent variables. 0.85 means 85% of variance is explained.",
    "answer": "d"
  },
  {
    "id": 19,
    "category": "Linear Regression - Multiple Variables",
    "question": "Why might adjusted R² be preferred over regular R² in multiple regression?",
    "options": [
      "It's easier to calculate",
      "It's always higher than regular R²",
      "It only works with categorical variables",
      "It penalizes the addition of irrelevant predictors"
    ],
    "explanation": "Adjusted R² accounts for the number of predictors, penalizing models that add predictors without meaningful improvement in explanatory power.",
    "answer": "d"
  },
  {
    "id": 20,
    "category": "Linear Regression - Categorical Variables",
    "question": "When using categorical variables in linear regression, why is one-hot encoding typically preferred over ordinal encoding?",
    "options": [
      "It doesn't impose artificial ordering on categories",
      "It uses less memory",
      "It's faster to compute",
      "It always improves model accuracy"
    ],
    "explanation": "One-hot encoding avoids imposing artificial numerical ordering on categories that may not have inherent order (e.g., colors, cities).",
    "answer": "a"
  },
  {
    "id": 21,
    "category": "Linear Regression - Gradient Descent",
    "question": "What is the main advantage of gradient descent over the analytical solution for linear regression?",
    "options": [
      "It's always more accurate",
      "It's simpler to understand",
      "It can handle very large datasets that don't fit in memory",
      "It always finds the global minimum"
    ],
    "explanation": "Gradient descent can work with datasets too large for memory and is scalable, while analytical solutions require computing matrix inverses of the full dataset.",
    "answer": "c"
  },
  {
    "id": 22,
    "category": "Linear Regression - Regularization",
    "question": "What is the primary purpose of regularization in linear regression?",
    "options": [
      "To increase model complexity",
      "To speed up training",
      "To handle missing data",
      "To prevent overfitting by penalizing large coefficients"
    ],
    "explanation": "Regularization adds a penalty term to prevent overfitting by discouraging large coefficient values, leading to simpler, more generalizable models.",
    "answer": "d"
  },
  {
    "id": 23,
    "category": "Linear Regression - Ridge vs LASSO",
    "question": "What is the key difference between Ridge and LASSO regression?",
    "options": [
      "Ridge uses L2 penalty, LASSO uses L1 penalty",
      "Ridge uses L1 penalty, LASSO uses L2 penalty",
      "Ridge is for classification, LASSO is for regression",
      "Ridge is faster than LASSO"
    ],
    "explanation": "Ridge regression uses L2 penalty (sum of squared coefficients), while LASSO uses L1 penalty (sum of absolute coefficients). LASSO can drive coefficients to exactly zero.",
    "answer": "a"
  },
  {
    "id": 24,
    "category": "Linear Regression - LASSO Properties",
    "question": "What unique property does LASSO regression have compared to Ridge regression?",
    "options": [
      "It always has better performance",
      "It works better with categorical variables",
      "It doesn't require regularization parameter tuning",
      "It can perform automatic feature selection by setting coefficients to zero"
    ],
    "explanation": "LASSO's L1 penalty can drive some coefficients to exactly zero, effectively performing automatic feature selection by eliminating irrelevant features.",
    "answer": "d"
  },
  {
    "id": 25,
    "category": "Data Preprocessing - Feature Transforms",
    "question": "When might you apply nonlinear feature transforms in linear regression?",
    "options": [
      "When the relationship between predictors and target is nonlinear",
      "When you want to make the model more complex",
      "When you have too many features",
      "When the target variable is categorical"
    ],
    "explanation": "Nonlinear transforms (like polynomial features, log transforms) can help capture nonlinear relationships while still using linear regression methods.",
    "answer": "a"
  },
  {
    "id": 26,
    "category": "Model Evaluation - Class Imbalance",
    "question": "Why is accuracy not always a good metric for imbalanced datasets?",
    "options": [
      "It's too hard to calculate",
      "It doesn't work with neural networks",
      "A model can achieve high accuracy by simply predicting the majority class",
      "It requires too much computational power"
    ],
    "explanation": "In imbalanced datasets (e.g., 95% class A, 5% class B), a model predicting all samples as class A achieves 95% accuracy but fails to identify class B instances.",
    "answer": "c"
  },
  {
    "id": 27,
    "category": "Model Evaluation - Dummy Classifier",
    "question": "What is the purpose of a dummy classifier in model evaluation?",
    "options": [
      "To replace the actual model in production",
      "To handle missing data",
      "To speed up training",
      "To provide a baseline for comparison with more sophisticated models"
    ],
    "explanation": "A dummy classifier provides a simple baseline (e.g., always predict majority class) to ensure your model performs better than naive strategies.",
    "answer": "d"
  },
  {
    "id": 28,
    "category": "Linear Regression - Residual Analysis",
    "question": "What should the histogram of residuals look like in a well-fitted linear regression model?",
    "options": [
      "Uniformly distributed",
      "Normally distributed and centered around zero",
      "Right-skewed",
      "Bimodal"
    ],
    "explanation": "Residuals should be normally distributed around zero, indicating that the model's errors are random and unbiased.",
    "answer": "b"
  },
  {
    "id": 29,
    "category": "Linear Regression - Outliers",
    "question": "How can linear regression help identify outliers in your data?",
    "options": [
      "By looking at the R² value",
      "By checking the intercept term",
      "By examining residuals - points with very large residuals may be outliers",
      "By looking at the correlation matrix"
    ],
    "explanation": "Large residuals (differences between predicted and actual values) can indicate outliers that don't fit the general pattern captured by the model.",
    "answer": "c"
  },
  {
    "id": 30,
    "category": "Linear Regression - Elastic Net",
    "question": "What does Elastic Net regression combine?",
    "options": [
      "Ridge and LASSO penalties",
      "L1 and L3 penalties",
      "Linear and logistic regression",
      "Training and validation sets"
    ],
    "explanation": "Elastic Net combines both Ridge (L2) and LASSO (L1) penalties, getting benefits of both: feature selection from LASSO and stability from Ridge.",
    "answer": "a"
  },
  {
    "id": 41,
    "category": "ML Overview - Supervised Learning",
    "question": "True or False: In supervised learning, the model learns from labeled data.",
    "options": [
      "True",
      "False"
    ],
    "explanation": "Supervised learning requires labeled data to train the model on the correct output for given inputs.",
    "answer": "a"
  },
  {
    "id": 42,
    "category": "Data Preprocessing - Scaling",
    "question": "True or False: Standardization always scales values between 0 and 1.",
    "options": [
      "True",
      "False"
    ],
    "explanation": "Standardization transforms data to have a mean of 0 and a standard deviation of 1, but the range is not bounded.",
    "answer": "b"
  },
  {
    "id": 43,
    "category": "Model Evaluation - Cross Validation",
    "question": "True or False: K-fold cross-validation helps reduce overfitting by using each data point for both training and testing.",
    "options": [
      "True",
      "False"
    ],
    "explanation": "K-fold cross-validation gives more reliable estimates by ensuring each instance is used for both training and validation.",
    "answer": "a"
  },
  {
    "id": 44,
    "category": "Linear Regression - Regularization",
    "question": "True or False: LASSO regression uses the L2 penalty and shrinks all coefficients toward zero without eliminating any.",
    "options": [
      "True",
      "False"
    ],
    "explanation": "LASSO uses the L1 penalty and can shrink some coefficients all the way to zero, effectively removing them.",
    "answer": "b"
  },
  {
    "id": 45,
    "category": "Unsupervised Learning - Clustering",
    "question": "True or False: Clustering requires labeled data to form distinct groups.",
    "options": [
      "True",
      "False"
    ],
    "explanation": "Clustering is an unsupervised learning method that finds patterns and groupings in data without needing labels.",
    "answer": "b"
  }
]



# Print answer distribution for verification
def print_answer_distribution():
    answer_counts = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
    for q in questions:
        answer_counts[q['answer']] += 1
    
    total = len(questions)
    print(f"Answer Distribution (Total: {total} questions):")
    for option in ['a', 'b', 'c', 'd']:
        count = answer_counts[option]
        percentage = (count / total) * 100
        print(f"Option {option.upper()}: {count} questions ({percentage:.1f}%)")

print_answer_distribution()