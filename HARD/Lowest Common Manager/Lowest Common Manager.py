def getLowestCommonManager(topManager, reportOne, reportTwo):
    return getOrgInfo(topManager, reportOne, reportTwo).lowestCommonManager


# The recursive function
def getOrgInfo(manager, reportOne, reportTwo):
    numOfReports = 0
    for report in manager.directReports:
        orgInfo = getOrgInfo(report, reportOne, reportTwo)
        if orgInfo.lowestCommonManager is not None:
            return orgInfo
        numOfReports += orgInfo.numOfReports
    if manager == reportOne or manager == reportTwo:
        numOfReports += 1

    lowestCommonManager = manager if numOfReports == 2 else None
    return OrgInfo(lowestCommonManager, numOfReports)


# Track the variables
class OrgInfo:
    def __init__(self, lowestCommonManager, numOfReports):
        self.lowestCommonManager = lowestCommonManager
        self.numOfReports = numOfReports


# This is an input class. Do not edit.
class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []
