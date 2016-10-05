# UNUI
Physical environment computational abstraction, camera control, actor/entity tracking. Think "inside out video game engine" to make the 'game map' that the computer can 'play reality' with via the outputs like lights and climate controls and so on.

This is a test project given by IUNU (the project title is that name spelled backwards) to test my coding skills.  Since I'm wrapping this up and it's something that seems interesting and like it could have practical applications, whether I get this job or not, I'm putting some thought into it and making it usable by myself, or possibly others, later on, as a graphics workhorse package for a set of functionality useful for building digital abstractions of real physical environments with actors <entities with behavior>, some event handling, and some physical geometry calculation abilities- nothing too heavy, but figuring out distances between points and so on.  {idea for later- google earth or google maps integration?}

Paradigms: IUNU was founded as a digital plant-growing light company, to produce and market a very cool digitally spectrum-controlled plasma light that changes the color of the light depending on what the plant it is growing needs- for example, marijuana growers need more blue-shifted light for the early part of the growing season and a more red-shifted light for later in the season.  As part of that, they have camera sensors that detect the plants to figure out the correct light spectrum to shine and so on, and these cameras are starting to be used more on their own to track the growth of individual plants, down to the individual leaves. And of course, you can optimize quite a lot quite well this way. It's very cool.

initial docspec:
	there's a camera mounted on a pair of servos. For purposes of this exercise, those servos each have a pair of external functions, one for setting its rotation, one for reading its rotation. Given the position of the camera as locally defined constant as one element in an array of the positions of all the cameras in the room, and a (X,Y,Z) target coordinate, determine if this camera is the closest on any side of the target, and if so, aim at the target and at a synchronized time, take a picture.

 	proper python project setup, tests, with gitbhub repo and commits that make sense.

	 Asking questions is encouraged. Finding hidden requirements is half the battle of building software. Getting software working, then refactoring is the other. Show me how you think through a problem.
