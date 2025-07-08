import json 

DEBUG = True

def show_diff(vulns1, vulns2):
    """ Show the differences and write changes into changes.md """

    cve_list1 = [ vuln.get('cveID') for vuln in vulns1 ]
    cve_list2 = [ vuln.get('cveID') for vuln in vulns2 ]

    diffs = list(set(cve_list1) - set(cve_list2))
    print(f'{diffs = } [{len(diffs)}]')
    print(f'')

    details = [ v for cve in diffs for v in vulns1 if v.get('cveID') == cve ]

    mk = '# CISA KEV (Diff)\n'
    mk += f'\n'
    mk += f'| Date | Vendor | Product | CVE |\n'
    mk += f'| ---- | ------ | ------- | --- |\n'

    for detail in details:
        print(f'')
        print(f' - {detail.get("cveID")}')
        print(f' - {detail.get("vendorProject")}/{detail.get("product")}')
        print(f' - {detail.get("vulnerabilityName")}/{detail.get("dateAdded")}')
        print(f' - {detail.get("shortDescription")}')
        mk += f'| {detail.get("dateAdded")} '
        mk += f'| {detail.get("vendorProject")} '
        mk += f'| {detail.get("product")} '
        mk += f'| {detail.get("cveID")} |\n'

    #print(mk)
    with open('changes.md', 'w') as fd:
        fd.write(mk)


def json_diff(file1_path, file2_path):
    """ Open the 2 files and check the differences """

    with open(file1_path, 'r') as f1, open(file2_path, 'r') as f2:
        json1 = json.load(f1)
        json2 = json.load(f2)

    count1 = json1.get('count')
    count2 = json2.get('count')

    vulns1 = json1.get('vulnerabilities')
    vulns2 = json2.get('vulnerabilities')

    if count1 == count2:
        print("JSON files are identical.")
        exit 0
    else:
        print(f' * {file1_path} : {count1}/{len(vulns1)}')
        print(f' * {file2_path} : {count2}/{len(vulns2)}')

        if DEBUG:
            show_diff(vulns1,vulns2)
            print(f'')
        exit 1


json_diff('cisa_kev-download.json', 'cisa_kev-old.json')

