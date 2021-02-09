# -*- coding: utf-8 -*-
import re

global sys_slot_info
global processor_info
global processor_type
global processor0
global processor1
global processor0_con
global processor1_con
global processor0_aux
global lc_info
global ps_info

def get_specified_slot_info(sys_slot_info,
                            main_module_name=None,
                            child_module_name=None):
    """

    :param sys_slot_info:
    :param main_module_name:
    :param child_module_name:
    :return:
    """
    slot_info_list = []
    for slot_name in sys_slot_info:
        single_slot_info_list = []
        child_slot_info_list = []
        if re.match(main_module_name, slot_name):
            if sys_slot_info[slot_name]['exist']:
                single_slot_info_list.append(slot_name)
            else:
                continue
        else:
            continue
        if child_module_name:
            for child_slot_name in sys_slot_info[slot_name]:
                if isinstance(child_slot_name, bool):
                    continue
                if re.match(child_module_name, child_slot_name) and sys_slot_info[slot_name][child_slot_name]['exist']:
                    child_slot_info_list.append(child_slot_name)
            child_slot_info_list.sort()
        single_slot_info_list.extend(child_slot_info_list)
        single_slot_info_list = tuple(single_slot_info_list)
        slot_info_list.append(single_slot_info_list)
    slot_info_list.sort()
    return slot_info_list


def add_order_info_to_global():

    config_file = open('CHASSIS0.txt', 'r')
    with config_file:
        config_str = config_file.read()
        slot_info = eval(config_str)
        sys_slot_info = slot_info
        processor_info = get_specified_slot_info(sys_slot_info=sys_slot_info, main_module_name='RSP')
        lc_info = get_specified_slot_info(sys_slot_info=sys_slot_info, main_module_name='LC', child_module_name='EP')
        ft_info = get_specified_slot_info(sys_slot_info=sys_slot_info, main_module_name='FAN')
        ps_info = get_specified_slot_info(sys_slot_info=sys_slot_info, main_module_name='PS', child_module_name='m')
        config_file.close()

        print('processor_info: {}'.format(processor_info))
        print('lc_info: {}'.format(lc_info))
        print('ft_info: {}'.format(ft_info))
        print('ps_info: {}'.format(ps_info))

        if len(processor_info) == 2:
            processor0 = processor_info[0][0]
            processor1 = processor_info[1][0]
            processor_type = re.search(r'[^\d]+', processor0).group()
            processor0_con = processor0 + '_CON'
            processor1_con = processor1 + '_CON'
            processor0_aux = processor0 + '_AUX'
        elif len(processor_info) == 1:
            processor0 = processor_info[0][0]
            # processor1 = processor_info[1][0]
            processor_type = re.search(r'[^\d]+', processor0).group()
            processor0_con = processor0 + '_CON'
            processor1_con = 'RSP1' + '_CON'
            print('processor1_con: {}'.format(processor1_con))
            processor0_aux = processor0 + '_AUX'
        else:
            raise ValueError('Route process quantity is not right, pls check!')
        return


add_order_info_to_global()
