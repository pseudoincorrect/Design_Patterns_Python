class CodeBuilder:
    def __init__(self, root_name):
        self.class_name = root_name
        self.fields = []

    def add_field(self, type, name):
        self.fields.append([type, name])
        return self

    def __str_fields(self):
        fields_str = ""
        if self.fields == []:
            return ' ' * 2 + 'pass\n'
        fields_str += ' ' * 2 + 'def __init__(self):\n'
        for i in self.fields:
            fields_str += ' ' * 4 + 'self.{} = {}\n'.format(i[0], i[1])
        return fields_str

    def __str__(self):
        return 'class {}:\n'.format(self.class_name) \
            + self.__str_fields()



if __name__ == '__main__':
    cb = CodeBuilder('Person') \
            .add_field('name', '""') \
            .add_field('age', '0')

    print(cb)
    # class Person():
    #     __init__(self):
    #         self.name = ""
    #         self.age = 0