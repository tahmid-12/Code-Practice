var compareVersion = function(version1, version2) {
    const versionPart1 = version1.split('.');
    const versionPart2 = version2.split('.');

    const maxLength = Math.max(versionPart1.length,versionPart2.length);

    for(let index = 0; index < maxLength; index++){
        const revisionNumber1 = Number(versionPart1[index]) || 0;
        const revisionNumber2 = Number(versionPart2[index]) || 0;

        if (revisionNumber1 < revisionNumber2) {
            return -1;
        }

        if (revisionNumber1 > revisionNumber2) {
            return 1;
        }
    }
    return 0;
};