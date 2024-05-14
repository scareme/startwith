# Get started
1. git clone https://github.com/scareme/startwith.git
2. startwith/scripts/init.sh demo

```bash
conda deactivate
conda env remove -n dev-startwith
conda env create -f environment.yml
conda activate dev-startwith
```

# Testing
1. pytest
    ```bash
    coverage run -m pytest -v
    coverage report
    coverage html
    ```
2. [safety](https://github.com/pyupio/safety)
    ```bash
    safety check
    ```



