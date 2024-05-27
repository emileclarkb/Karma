# TODO: Remove this (use pip instead)
import os, sys
sys.path.append(f'{os.getcwd()}\\..\\..\\Coma\\Repo')

from Coma import Coma
from Coma.Providers import GitHub, GitLab, BitBucket

from Coma.Requirements.Formats.Version import Version



'''
Constaints:
    - delimiter must be a single character (otherwise it will be interpretted
        as multiple delimiters that are all value, ie "abc" -> ["a","b","c"])
    - for delimiter "." use "\." instead to avoid regex issues
    - prefix and postfix cannot contain digits
'''
def main():
    version_postfixes = ['-alpha', '-beta', '-alphA', '-release']
    version_format = Version(prefixes = ['v'],
                             prefix_optional = True,
                             prefix_case_sensitive = False,
                             version_numbers = 3, 
                             max_version_digits = 3,
                             delimiter = '\.',
                             postfixes = version_postfixes,
                             postfix_optional = True)
    
    version = 'V1.2.3-Alpha'
    result = version_format.Validate(version)
    print(f'Success: {result.success}')
    print(f'Reason: {result.reason}')
    print()
    if not result.success: return 1
    print(f'String: {result.value.string}')
    print(f'Versions: {result.value.versions}')
    print(f'Prefix: {result.value.prefix}')
    print(f'Postfix: {result.value.postfix}')
    
    '''
    coma = Coma([GitHub(), GitLab(), BitBucket()])
    # component = coma.NewComponent('mkiol', 'dsnote')
    component = coma.NewComponent('emileclarkb', 'Kara')
    coma.FillProviders(component)
    for provider in component.providers.values():
        if provider is None: continue
        print(f'{provider.name}')

    for branch in coma.providers['GitHub'].GetBranches(component):
        print(branch)

    print('#'*15)
    for release in coma.providers['GitHub'].GetReleases(component):
        print(release)
        '''
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
