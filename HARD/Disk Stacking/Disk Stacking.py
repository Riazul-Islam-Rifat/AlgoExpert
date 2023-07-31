def diskStacking(disks):
    # Sort the given input according to height
    disks.sort(key=lambda disk: disk[2])
    # Create an array where each index contains the max height keeping the disk at the bottom
    height = [disk[2] for disk in disks]
    # Create another array to keep tracj the used disks
    sequence = [None for disk in disks]
    # This variable is basically used to keep track the last used disk
    maxHeight = 0

    for i in range(1, len(disks)):
        cw = disks[i][0]
        cd = disks[i][1]
        ch = disks[i][2]

        for j in range(0, i):
            ow = disks[j][0]
            od = disks[j][1]
            oh = disks[j][2]

            if ow < cw and od < cd and oh < ch:
                if height[i] <= ch + height[j]:
                    height[i] = ch + height[j]
                    # When we add any disk to the height[i], we keep track of that index
                    sequence[i] = j
        if height[i] >= height[maxHeight]:
            maxHeight = i  # Takes the last used disk

    # Extract the used disks
    ans = []

    while maxHeight is not None:
        ans.append(disks[maxHeight])
        maxHeight = sequence[maxHeight]

    return list(reversed(ans))
