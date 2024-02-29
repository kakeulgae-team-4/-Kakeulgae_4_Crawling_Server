url_repository = {
    'base': 'https://www.jobkorea.co.kr/recruit/joblist?menucode=local&localorder=1#anchorGICnt_1',
}

path_repository = {
    'body': '/html/body',
    'category_major_button': '/html/body/div[5]/div[1]/div/div[2]/div[1]/div[2]/div/div[1]/dl[1]/dt/p',
    'category_middle_button': '/html/body/div[5]/div[1]/div/div[2]/div[1]/div[2]/div/div[1]/dl[1]/dd[2]/div[2]/dl[1]/dd/div[1]/ul/li[6]/label/span',
    'category_button': '/html/body/div[5]/div[1]/div/div[2]/div[1]/div[2]/div/div[1]/dl[1]/dd[2]/div[2]/dl[2]/dd/div[1]/ul[2]/li[{i}]/label/span',
    'category_sub_button': '/html/body/div[5]/div[1]/div/div[2]/div[1]/div[2]/div/div[1]/dl[1]/dd[2]/div[2]/dl[2]/dd/div[1]/ul[2]/li[1]/label/span',
    'search_button': '/html/body/div[5]/div[1]/div/div[2]/div[1]/div[2]/div/div[3]/div/dl[1]/dd[2]/button',
    'order_tab': '/html/body/div[5]/div[1]/div/div[2]/div[4]/div/div[2]/div[5]/div[2]/div[1]/select',
    'order_tab_optional': '/html/body/div[5]/div[1]/div/div[2]/div[4]/div/div[2]/div[5]/div[2]/div[1]/select/option[2]',
    'num_of_list_btn': '/html/body/div[5]/div[1]/div/div[2]/div[4]/div/div[2]/div[5]/div[2]/div[2]/select',
    'num_50_of_list_btn': '/html/body/div[5]/div[1]/div/div[2]/div[4]/div/div[2]/div[5]/div[2]/div[2]/select/option[5]',
    'page_button_pattern': '/html/body/div[5]/div[1]/div/div[2]/div[4]/div/div[6]/div/ul/li[{}]/a',
    'page_next_button_pattern': '/html/body/div[5]/div[1]/div/div[2]/div[4]/div/div[6]/div/p[{}]/a',
    'page_next_button': '/html/body/div[5]/div[1]/div/div[2]/div[4]/div/div[6]/div/p/a',
    'row': {
        'one': '/html/body/div[5]/div[1]/div/div[2]/div[4]/div/div[5]/table/tbody/tr[{idx}]/td[2]/div/strong/a',
        'company_name': '/html/body/div[5]/div[1]/div/div[2]/div[4]/div/div[5]/table/tbody/tr[{idx}]/td[1]/a',
        'post_name': '/html/body/div[5]/div[1]/div/div[2]/div[4]/div/div[5]/table/tbody/tr[{idx}]/td[2]/div/strong/a',
        'url': '/html/body/div[5]/div[1]/div/div[2]/div[4]/div/div[5]/table/tbody/tr[{idx}]/td[2]/div/strong/a',
        'tag': '/html/body/div[5]/div[1]/div/div[2]/div[4]/div/div[5]/table/tbody/tr[{idx}]/td[2]/div/p[1]/span[{span_idx}]',
        'work_type': '/html/body/div[5]/div[1]/div/div[2]/div[4]/div/div[5]/table/tbody/tr[{idx}]/td[2]/div/p[2]',
        'created_at': '/html/body/div[5]/div[1]/div/div[2]/div[4]/div/div[5]/table/tbody/tr[{idx}]/td[4]/span[1]',
        'deadline': '/html/body/div[5]/div[1]/div/div[2]/div[4]/div/div[5]/table/tbody/tr[{idx}]/td[4]/span[2]'
    }
}
