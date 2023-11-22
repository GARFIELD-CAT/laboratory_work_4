import json
import yaml


def convert_file_from_yaml_to_json(yaml_file_path: str):
    with open(yaml_file_path, 'r', encoding='utf-8') as yaml_file:
        data = yaml.safe_load(yaml_file)

    raw_path, _ = yaml_file_path.split('.')
    _, file_name = raw_path.split('/')
    json_file_path = f'json_results/{file_name}.json'

    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json_file.write(json.dumps(data, ensure_ascii=False))


if __name__ == '__main__':
    # Введите путь к вашему файлу. Он должен лежать в папке 'yaml_examples'
    example_path = 'yaml_examples/people.yaml'
    convert_file_from_yaml_to_json(example_path)
