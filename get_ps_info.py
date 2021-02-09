# -*- coding: utf-8 -*-


def get_ps_info():
    ps_info = """
    RSP0/CPUO:>%: sh ps
    
    power shelf 0 info
    =====================
    power module 0 present
    -----------------------
    input power: 654.73 W
    output power: 554.43 W
    
    power module 1 present
    ------------------------
    input power: 622.73 W
    output power: 511.43 W
    
    
    power shelf 1 info
    ===========================
    power module 0 present
    --------------------------
    input power: 552.67 W
    output power: 513.23 W
    """

    ps_info_list = ps_info.split('power module')
    ps_info_list = ps_info_list[1:]

    userdict = {}
    userdict['order_info'] = [('ps0', 'm0'), ('ps0', 'm1'), ('ps1', 'm0')]
    pm_info_dict = {}
    for pm in userdict['order_info']:
        ps_name = pm[0]
        pm_name = pm[1]
        pm_info_dict[(ps_name, pm_name)] = {}
        pm_index = userdict['order_info'].index((ps_name, pm_name))
        ps_info = ps_info_list[pm_index]
        each_ps_info_list = ps_info.split('\n')
        for each in each_ps_info_list:
            if ':' in each:
                pm_info_dict[(ps_name, pm_name)][each.split(':')[0].strip()] = each.split(':')[1].strip()
    return pm_info_dict


pm_info_dict = get_ps_info()
print(pm_info_dict)
