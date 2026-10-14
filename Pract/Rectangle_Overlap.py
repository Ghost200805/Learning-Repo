def isRectangleOverlap(
    r1x1: int, r1y1: int, r1x2: int, r1y2: int,
    r2x1: int, r2y1: int, r2x2: int, r2y2: int
) -> bool:
    if max(r1x1,r2x1)<min(r1x2,r2x2) and max(r1y1,r2y1)<min(r1y2,r2y2):
        return True
    else:
        return False
print(isRectangleOverlap(r1x1= 0,r1y1= 0,r1x2= 2,r1y2= 2,r2x1= 1,r2y1= 1,r2x2= 3,r2y2= 3))