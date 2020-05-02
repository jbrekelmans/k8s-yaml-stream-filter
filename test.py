import yaml

to_delete = {
    ('v1', 'Secret', 'mysecret2', 'mynamespace'): 1,
}
with open('test.yaml', 'rb') as file_obj:
    resources_bytes = file_obj.read()
resources = yaml.safe_load_all(resources_bytes)
resources_filtered = []
for resource in resources:
    metadata = resource['metadata']
    key = (resource['apiVersion'], resource['kind'], metadata['name'], metadata['namespace'])
    if key not in to_delete:
        resources_filtered.append(resource)
with open('test2.yaml', 'w') as file_obj:
    yaml.safe_dump_all(resources_filtered, file_obj)
