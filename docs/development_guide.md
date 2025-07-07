# IBM Data Analyst Capstone - Development Guide

## Introduction

This guide is intended for developers who want to contribute to the IBM Data Analyst Capstone project. It provides information on the project structure, development workflow, and best practices.

## Project Structure

The project is organized as follows:

```
ibm-data-analyst-capstone/
├── docs/                  # Documentation
│   ├── user_guide.md      # User guide
│   ├── api_reference.md   # API reference
│   └── development_guide.md # Development guide
├── examples/              # Example data and notebooks
├── src/                   # Source code
│   ├── excel/             # Excel-related modules
│   ├── visualization/     # Visualization modules
│   ├── business_intelligence/ # Business intelligence modules
│   ├── sql/               # SQL-related modules
│   ├── data_analyst_platform.py # Main platform module
│   └── main_platform.py   # Command-line interface
├── tests/                 # Tests
│   ├── test_platform.py   # Unit tests
│   └── performance_test.py # Performance tests
├── LICENSE                # License file
├── README.md              # Project README
└── requirements.txt       # Dependencies
```

## Development Workflow

### Setting Up the Development Environment

1. Clone the repository:
   ```bash
   git clone https://github.com/galafis/ibm-data-analyst-capstone.git
   ```

2. Navigate to the project directory:
   ```bash
   cd ibm-data-analyst-capstone
   ```

3. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

5. Install the development dependencies:
   ```bash
   pip install -r requirements-dev.txt
   ```

### Running Tests

To run the unit tests:

```bash
python -m unittest discover tests
```

To run a specific test:

```bash
python -m unittest tests.test_platform
```

To run the performance tests:

```bash
python tests/performance_test.py
```

### Code Style

We follow the [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide for Python code. You can use tools like `flake8` and `black` to check and format your code:

```bash
flake8 src tests
black src tests
```

### Documentation

We use Markdown for documentation. The documentation is organized as follows:

- `README.md`: Project overview and quick start guide.
- `docs/user_guide.md`: Detailed user guide.
- `docs/api_reference.md`: API reference.
- `docs/development_guide.md`: Development guide.

### Commit Messages

We follow the [Conventional Commits](https://www.conventionalcommits.org/) specification for commit messages. The commit message should be structured as follows:

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

Types:
- `feat`: A new feature
- `fix`: A bug fix
- `docs`: Documentation only changes
- `style`: Changes that do not affect the meaning of the code (white-space, formatting, etc.)
- `refactor`: A code change that neither fixes a bug nor adds a feature
- `perf`: A code change that improves performance
- `test`: Adding missing tests or correcting existing tests
- `chore`: Changes to the build process or auxiliary tools and libraries

Examples:
- `feat: add pivot table export feature`
- `fix: correct calculation of revenue growth`
- `docs: update user guide with new examples`

### Pull Requests

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes.
4. Run the tests to ensure they pass.
5. Commit your changes with a descriptive commit message.
6. Push your branch to your fork.
7. Create a pull request.

## Best Practices

### Code Quality

- Write clean, readable, and maintainable code.
- Follow the [SOLID](https://en.wikipedia.org/wiki/SOLID) principles.
- Use meaningful variable and function names.
- Add comments to explain complex logic.
- Write docstrings for all functions and classes.

### Testing

- Write unit tests for all new features.
- Ensure all tests pass before submitting a pull request.
- Use test-driven development (TDD) when appropriate.
- Write performance tests for performance-critical code.

### Documentation

- Update the documentation when adding new features or changing existing ones.
- Write clear and concise documentation.
- Include examples in the documentation.
- Keep the API reference up to date.

### Performance

- Be mindful of performance when working with large datasets.
- Use efficient algorithms and data structures.
- Profile your code to identify bottlenecks.
- Write performance tests to ensure performance does not degrade over time.

## Troubleshooting

### Common Issues

#### ImportError: No module named 'src'

This error occurs when Python cannot find the `src` module. To fix it, add the project directory to the Python path:

```python
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
```

#### ModuleNotFoundError: No module named 'statsmodels'

This error occurs when the required dependencies are not installed. To fix it, install the dependencies:

```bash
pip install -r requirements.txt
```

#### AttributeError: module 'pandas' has no attribute 'DataFrame'

This error occurs when there is a conflict with another module named `pandas`. To fix it, check your Python path and remove any conflicting modules.

### Getting Help

If you encounter any issues or have questions, please open an issue on GitHub.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
