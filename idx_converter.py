import re


class IDXConverter:
    def __init__(self, path):
        self.path = path

    def converting(self):

        with open(self.path, 'r') as f:
            data = f.readlines()

        format_data = []
        out_data = []

        for row in data:
            row = row.replace('\n', '')
            row = row.replace('\t', '')
            row_list = row.split(',')
            result = re.match(r'\d+', row_list[0])
            if result and len(row_list) == 8:
                format_data.append(row)

        for row in format_data:
            row_list = row.split(',')
            row_list.pop(-1)
            row_list.pop(-1)
            row_list.pop(-1)
            row_list.pop(0)
            row_list[0] = row_list[0].replace('"', '')
            out_data.append(row_list)

        return out_data
