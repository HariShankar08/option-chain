# option-chain

## Usage

```bash
pip install -r requirements.txt
```
Before you start running. Virtual Environment recommended.

Activate the Virtual Environment, and in the terminal, run the following to ensure everything worked fine:

```bash
python data_generator.py -h
```

## Running

Get the Option Data with
```bash
python data_generator.py -eq {stock_name}
```

Can also specify expiry date with `-exp`, but will not run if the expiry date does not exist. Not fully implemented this.

