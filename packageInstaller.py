import click
import json
import pip

def installPackage(packageName, version):
    print("Installing: "+packageName+"=="+str(version))
    output = pip.main(['install', packageName+"=="+version])

    return output

@click.command()
@click.argument('packages_list_file')
def packageInstaller(packages_list_file):

    successful = 0
    failedPackages = dict()
    with open(packages_list_file) as json_file:
        data = json.load(json_file)
        dependencies = data["Dependencies"]
        keys = dependencies.keys()
        for packageName in keys:
            value = installPackage(packageName, dependencies[packageName])
            if(value==1):
                failedPackages[packageName] = dependencies[packageName]
            successful = successful+value

    if(successful == 0):
        print("Installation is Succesfull")
    else:
        print("Package Installation Failed are:")
        for key in failedPackages.keys():
            print(key+"=="+failedPackages[key])


if (__name__ == '__main__'):
    packageInstaller()






