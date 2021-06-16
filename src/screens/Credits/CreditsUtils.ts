const regex = /(.+)@(.+)$/;

const getPackageNameAndVersion = (npmPackage: string): [string, string] => {
    const name = npmPackage.replace(regex, "$1");
    const version = npmPackage.replace(regex, "$2");

    return [name, version];
};

const getPackagesArray = (libraries: Record<string, LicenseInfo>): Library[] => {
    return Object.keys(libraries).map((key) => {
        const [name, version] = getPackageNameAndVersion(key);

        return {
            name,
            version,
            licenseInfo: libraries[key],
        };
    });
};

export { getPackageNameAndVersion, getPackagesArray };