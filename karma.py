# TODO: Remove this (use pip instead)
import os, sys
sys.path.append(f'{os.getcwd()}\\..\\..\\Coma\\Repo')

from Coma import Coma
from Coma.Requirements import Format
from Coma.Providers import GitHub, GitLab, BitBucket





'''
Constaints:
    - delimiter must be a single character (otherwise it will be interpretted
        as multiple delimiters that are all value, ie "abc" -> ["a","b","c"])
    - for delimiter "." use "\." instead to avoid regex issues
    - prefix and postfix cannot contain digits
'''
def main():
    '''
    # version_postfixes = ['-alpha', '-beta', '-release']
    version_prefixes = ['Alpha-', 'Beta-', 'Release-']
    version_format = Version(prefixes = version_prefixes,
                             prefix_optional = True,
                             prefix_case_sensitive = False,
                             version_numbers = 2, 
                             max_version_digits = 1,
                             delimiter = '\.',
                             postfixes = [],
                             postfix_optional = False)
    '''
    version_postfixes = ['-alpha', '-beta', '-release']
    version_format = Format.Version(prefixes = ['v'],
                                    prefix_optional = False,
                                    prefix_case_sensitive = False,
                                    version_numbers = 3, 
                                    max_version_digits = 3,
                                    delimiter = '\.',
                                    postfixes = version_postfixes,
                                    postfix_optional = True,
                                    postfix_case_sensitive = True)
    
    metadata_format = Format.Map({
        'description': Format.String(max_length=30),
        'maintained': Format.Boolean(),
        'latest_version': version_format,
        'versions': Format.Array(version_format)
    })
    
    # component = coma.NewComponent('mkiol', 'dsnote')
    
    coma = Coma([GitHub()])
    coma.RequireFile('module.json', 'json', format=metadata_format)
    component = coma.NewComponent('emileclarkb', 'KarmaTemplate')
    result = coma.IsPackage(component)
    print(result)
    
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
