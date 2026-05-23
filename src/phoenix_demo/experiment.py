from phoenix.client import Client
from phoenix.client.experiments import run_experiment

from src.agent.agent import agent

client = Client(base_url='http://localhost:6006')

dataset = client.datasets.get_dataset(dataset='benchmark')

def task(input):
    output = agent.invoke({'messages': ('human', f'{input["input"]}')})
    return output

run_experiment(
    dataset=dataset,
    task=task,
    experiment_name='Base Experiment'
)