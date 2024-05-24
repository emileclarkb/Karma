# TODO: Remove this (use pip instead)
import os, sys
sys.path.append(f'{os.getcwd()}\\..\\..\\Coma\\Repo')

from Coma import Coma
from Coma.Providers import GitHub, GitLab, BitBucket


def main():
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
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
