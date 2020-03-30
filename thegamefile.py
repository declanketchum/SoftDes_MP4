"""
Micro Project 4
"""

import pygame
import cv2

# this is the main file for the project with all of the classes and functions that will be called

# hypothetical x positions of lanes.
global LEFT_LANE = 50
global MIDDLE_LANE = 100
global RIGHT_LANE = 150
global top_y = 0

class Runner():
#creates a class for the character in the game
    def __init__(self, screen, x = middle_lane, y = 150, lives = 3):
        #initilizes the character with a starting x position. y position is at the
        #bottom of the page because the background moves not the character.
        pass
    def draw(self):
        #draws the character on the screen
        pass
    def move(self):
        #Moves runner in the direction specified by the OpenCV camera
        #feedback. Changes the x location of the character to one of the
        #three global lane variables.
        pass
    def minus_life(self):
        #Subtracts one from life of the Runner.
        pass

class Obstacles():
#creates a class that for the obstacles
    def __init__(self, screen, x, y=0):
        #initilizes each obstacle with an x (one of the three lanes) & y
        #position
        pass
    def draw(self):
        #draws obstacle on the screen
        pass
    def move(self):
        #keeps obstacle on the same lane while increasing the y position so it
        #moves down the screen towards the player.
        pass

def redrawWindow():
    '''
    redraws elements so that it can update every frame

    draws the following:
    background
    Runner
    for every obstacle in the obstacles list, draw it in the window.
    '''
    #code drawing stuff.
    pygame.display.update()
    pass

obstacles = [] #This stores all obstacles in a list and loops through the list
#to draw each one
pygame.time.set_timer(USEREVENT+1, random.randrange(2000, 3500)) # Will trigger
# every 2 - 3.5 seconds. This is the timer that sets off obstacle generation.

class Game():
    def __init__(self):
        '''
        initializes attributes of the game:

        frames per second
        Clock
        background
        size of screen
        creates Runner class
        creates Obstacles class
        '''
    def run(self):
        '''
        runs the game.
        '''
        RUNNING = true
        while RUNNING:

            #if lives is less than 0, then RUNNING becomes false

            redrawWindow() # updates frame with all of the sprites

            #moves runner based on direction of open cv arrows

            #generate obstacles if userevent timer is true.
            if event.type == USEREVENT+1:
            r = random.randrange(0,2)
            if r == 0:
                obstacles.append(saw(810, 310, 64, 64))
            elif r == 1:
                obstacles.append(spike(810, 0, 48, 310))

            #moves obstacles: updates obstacle position or removes it if it
            #goes off the screen.
            for obstacle in obstacles:
                 obstacle.y += 1.4
                 if obstacle.x < obstacle.width * -1:
                     # If our obstacle is off the screen we will remove it
                     obstacles.pop(obstacles.index(obstacle))

            # insert code that manages collisions: if it touches the player
            # then the obstacle deletes, the player loses a life, the player's
            # turn starts over



def read_card():
    "if open cv reads left arrow"
        return "left"
    "if open cv reads right arrow"
        return "right"
    "if open cv does not read anything"
        return "stay"
    pass

def generate_obstacles():
    "randomly generates obsticals for the runner to dodge"
    "as time passes it creates more obsticals"

    if
    pass


def crash():
    "when runner hits an obstical with 0 lives the game ends and the end screen shows"
    pass

test = True

class Camera(): #not finished but close, lol
    '''
    Class containing all gathering of data from the Camera feed.
    designed to have minimal interpreting in this class and instead interface
    with another class to find the meaning in the image data.
    '''
    def __init__(self, left, right):

        # initalize the feed
        self.cap = cv2.VideoCapture(0)

        # create the ORB data from images to check the feed with
        self.leftORB = init_templates(left)
        self.rightORB = init_template(right)

        # check that camera is available
        if not (self.cap.isOpened()):
            print('No camera detected,\n please run with a Camera')

        # generate the ORBs templates for the left and right pointing arrows

    def init_templates(self, temp, orbs):
        # save the template image
        self.img = cv2.imread(temp, 0)

        # Initiate ORB detector
        orb = cv.ORB_create()

        # find the keypoints with ORB
        keypoints = orb.detect(img, None)

        # compute the descriptors with ORB
        keypoints, descriptor = orb.compute(img, keypoints)

        # draw only keypoints location,not size and orientation
        orbtemplate = cv.drawKeypoints(img, keypoints, None, color=(0,255,0), flags=0)

        return orbtemplate

    def get_feed(self):
        '''
        This function returns the vidnumORBseo feed after converting it to a grayscale for further interpreting
        '''

        # while the camera may be on, the camera could be reading a file or feed type
        # that it cannot handle this double checks that the input type is correct.
        self.everythingGood, self.frame = cap.read()
        if self.everythingGood == True:

            # Converting the Video frame into a grayscale image
            grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            return grayscale

    def image_converter(self, image, EdgeThres = (100, 255), pMatches = 300, OrbThres = 90):

            # using the CannyEdge Detector to simply image and store it
            self.edge = cv2.Canny(image, EdgeThres[0], EdgeThres[1])

            # using ORBs detection to
            self.orbprocessed =

            # Since this uses a lot of external input a testing function is made to clarify
            # what it is that the edge dectectors are finding
            if test:
                # Unfiltered Video Feed
                cv2.imshow('Real', frame)
                # Filtered Video Feed
                cv2.imshow('Edge', edge)
                # ORB filtered Video Feed
                cv2.imshow('ORBs', orbprocessed)
                # Escape the Video feed, and properly(?) close the windows/camera
                if cv2.waitKey(20) == ord('q'):
                break



    def get_feed(self, EdgeThres = (100, 255), pMatches = 300, OrbThres = 90, t = True):
        '''
        By inputing the desired threshold for the Canny Edge detector,
        as well as the number of ORBs for the templates, and the
        threshold for the number of matches needed for a positive fit.

        This function will return the data of the video feed converted into the
        '''

        everythingGood, frame = cap.read()
        # while the camera may be on, the camera could be reading a file or feed type
        # that it cannot handle this double checks that the input type is correct.
        if everythingGood == True:

            # Converting the Video frame into a grayscale image
            grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # using the Cannyedge Detector package in the OpenCV Library to simply image
            edge = cv2.Canny(grayscale, 50, 220)

            # Since this uses a lot of external input a testing function is made to clarify
            # what it is that the edge dectectors are finding
            if t:
                # Unfiltered Video Feed
                cv2.imshow('Real', frame)
                # Filtered Video Feed
                cv2.imshow('Edge', edge)
                # Escape the Video feed, and properly(?) close the windows/camera
                if cv2.waitKey(20) == ord('q'):
                break
def __main__():
    cam = Camera()
