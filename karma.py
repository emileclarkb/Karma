# TODO: Remove this (use pip instead)
import os, sys
sys.path.append(f'{os.getcwd()}\\..\\..\\Coma\\Repo')

from Coma import Coma

def main():
    coma = Coma()
    # component = coma.NewComponent('mkiol', 'dsnote')
    component = coma.NewComponent('emileclarkb', 'Kara')
    coma.FillProviders(component)
    for provider in component.providers.values():
        print(f'{provider.name}: {provider.exists}')
        
    for branch in coma.PROVIDERS['GitHub'].GetBranches(component):
        print(branch)
        
    print('#'*15)
    for release in coma.PROVIDERS['GitHub'].GetReleases(component):
        print(release)
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
