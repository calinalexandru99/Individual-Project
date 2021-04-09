const regex = /(.+)@(.+)$/;

/**
 * Given an NPM Package, get the name and version
 *
 * @param npmPackage NPM Package string
 *
 * @return Name and version of the given package
 */
const getPackageNameAndVersion = (npmPackage: string): [string, string] => {
    const name = npmPackage.replace(regex, "$1");
    const version = npmPackage.replace(regex, "$2");

    return [name, version];
};

/**
 * Processes a libraries json, returning an array of Library objects
 *
 * @param libraries Libraries json to process
 *
 * @return Array of Library objects
 */
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