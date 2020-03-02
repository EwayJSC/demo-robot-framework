# Run test

```bash
$ docker-compose up --build -d
```

# Check result

```bash
$ open results/log.html
```

# Run Browser test

```bash
$ cd robot
$ pip install -r requirements.txt
$ robot -d manual_results tests/WebBrowser/
```
