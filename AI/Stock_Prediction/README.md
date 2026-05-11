Got you — here’s a cleaned up, professional version of all three pieces. You can copy these straight into your repo.

---

### **README.md**

# **Stock Price Predictor**

Time-series forecasting for stock prices using classical ML and deep learning models.

## **Table of Contents**
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Models](#models)
5. [Metrics](#metrics)
6. [Project Structure](#project-structure)
7. [Contributing](#contributing)
8. [License](#license)

## **Introduction**
This project predicts future stock prices using historical market data. It implements and compares a baseline Linear Regression model with an LSTM neural network to capture temporal dependencies. The goal is to benchmark performance and provide a reproducible pipeline for time-series forecasting.

**Disclaimer**: This tool is for educational purposes only and not financial advice.

## **Installation**
1. Clone the repository:
```bash
git clone https://github.com/your-username/stock-price-predictor.git
cd stock-price-predictor
```

2. Create a virtual environment and install dependencies:
```bash
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## **Usage**
Run the full training and evaluation pipeline:
```bash
python main.py --ticker AAPL --model lstm
```

**CLI Arguments**
| Argument | Description | Default |
| --- | --- | --- |
| `--ticker` | Stock ticker symbol to predict | `AAPL` |
| `--model` | Model type: `linear` or `lstm` | `lstm` |
| `--epochs` | Training epochs for LSTM | `50` |
| `--predict` | Run inference only using saved model | `False` |

## **Models**
1. **Linear Regression**: Baseline model using lag features and technical indicators
2. **LSTM**: Long Short-Term Memory network to model sequential patterns and long-range dependencies

## **Metrics**
Model performance is evaluated using:
- **Mean Squared Error (MSE)**: Penalizes large errors
- **Mean Absolute Error (MAE)**: Interpretable average error in price units
- **R-squared (R²)**: Proportion of variance explained by the model

## **Project Structure**
```
stock-price-predictor/
├── data/ # Raw and processed datasets - not tracked by git
├── models/ # Saved model weights - not tracked by git
├── utils/ # Feature engineering and data loaders
├── main.py # Training and inference entry point
├── requirements.txt
└── README.md
```

## **Contributing**
Contributions are welcome. Please follow these steps:
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/add-model`
3. Follow the commit message guidelines below
4. Submit a pull request with a clear description of changes

## **License**
This project is licensed under the MIT License. See `LICENSE` for details.

---

### **.gitignore**
Your current one ignores too much. This version ignores what should be ignored, but keeps `requirements.txt` and `README.md` tracked:

```
# Byte-compiled / optimized files
__pycache__/
*.py[cod]
*$py.class

# Environments
.env
.venv
env/
venv/
ENV/

# Data and model artifacts
data/
models/
*.h5
*.pkl
*.csv
*.parquet

# IDEs
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Logs
*.log
```

**Key fixes**:
1. `*.pyc` and `pycache` → changed to `__pycache__/` and `*.py[cod]` to catch all bytecode
2. Removed `requirements.txt` and `README.md` — you want those in git
3. Added model file extensions and OS/IDE files

---

### **Commit Message Guidelines**
Follow conventional commits for clarity:

1. **Format**: `<type>: <subject>`
   - Types: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`
2. **Imperative mood**: `Add LSTM model` not `Added LSTM model`
3. **Concise subject**: Keep under 50 characters
4. **Present tense**: `Update data loader` not `Updated data loader`
5. **Body optional**: Wrap at 72 characters if you add details

**Examples**:
```
feat: Add LSTM model with 2 layers
fix: Correct data leakage in train/test split
docs: Update README installation steps
refactor: Move feature engineering to utils
```

---

### **API Documentation Guidelines**
When documenting functions/classes:

1. **Clear language**: Explain *what* and *why*, not just *how*
2. **Parameters**: Name, type, description, and default value
3. **Returns**: Type and description of output
4. **Example**: Include a short usage snippet

**Example docstring**:
```python
def load_stock_data(ticker: str, start_date: str, end_date: str) -> pd.DataFrame:
    """
    Load historical stock data from Yahoo Finance.

    Args:
        ticker: Stock symbol, e.g. "AAPL"
        start_date: Start date in "YYYY-MM-DD" format
        end_date: End date in "YYYY-MM-DD" format

    Returns:
        DataFrame with Date index and OHLCV columns

    Example:
        >>> df = load_stock_data("AAPL", "2020-01-01", "2023-01-01")
    """
```

Want me to add a `LICENSE` file, sample `requirements.txt`, or GitHub Actions CI template next?
