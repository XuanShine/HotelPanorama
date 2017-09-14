from pyexcel_ods3 import get_data
import yaml
import pdb


def ods_to_yaml(ods_file, sheet_name=None, return_dict=False):
    """ Get ods_file return yaml output in utf-8
    Input Table:
    x0 x1 x2 x3
    y0 y1 y2 y3
    z0 z1 z2 z3

    Output Yaml:
    y0:
        x1: y1
        x2: y2
        x3: y3
    z0:
        x1: z1
        x2: z2
        x3: z3
    """
    ods = get_data(ods_file)
    assert len(ods.keys()) > 0
    data = ods[sheet_name] if sheet_name else ods[list(ods.keys())[0]]

    type_rooms = data[0][1:]
    tarifs = data[1:]

    assert type(type_rooms) == list
    assert type(tarifs) == list
    assert type(tarifs[0]) == list

    result = dict()

    for tarif in tarifs:
        if len(tarif) == 0:
            continue
        date = tarif[0]
        prices = tarif[1:]
        result[date] = {room: price
                        for (room, price) in zip(type_rooms, prices)}
    if return_dict:
        return result
    return yaml.dump(result, default_flow_style=False)


def file_ods_to_yaml(ods_file='price.ods', yaml_file='price.yaml', mode='wa'):
    with open(yaml_file, mode) as f_out:
        f_out.write(ods_to_yaml(ods_file))


def ods_file_update_yaml(ods_file, yaml_file):
    # TODO save file before modify
    with open(yaml_file, 'r') as f_yaml_in:
        actual_tarif = yaml.load(f_yaml_in.read())
    # with open(ods_file, 'r') as f_ods_in:
    new_tarif = ods_to_yaml(ods_file, return_dict=True)
    actual_tarif.update(new_tarif)
    with open(yaml_file, 'w') as f_out:
        f_out.write(yaml.dump(actual_tarif, default_flow_style=False))
