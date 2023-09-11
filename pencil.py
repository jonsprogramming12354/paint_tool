import pygame

def roundline(canvas, color, start, end, radius=1):
    Xaxis = end[0]-start[0]
    Yaxis = end[1]-start[1]
    distance = max(abs(Xaxis), abs(Yaxis))
    for i in range (distance):
        x = int(start[0]+float(i)/distance*Xaxis)
        y = int(start[1]+float(i)/distance*Yaxis)
        pygame.draw.circle(canvas, color, (x, y), radius)