# Project: Feed

A Full-Stack Web App
By
Allyson Phillips

## What is it?

A Yelp-Style App that helps people find comfortable places to study, work remotely, or hold meetings in a dining environemnt..

## Timeline

```
(This is all tentitive)

5/4-5/7 - Spend too much focusing on proposal
5/8-5/10 - Build the skeleton (Web-Framework and Database)
5/11-5/12 - Design Basic Website (HTML/CSS/JS)
5/13 - Focus on API (What do I need to make?)
5/14-5/16 - Build and/or Apply APIs
5/17 - Mini Vacation (Block Stairs up to loft and Binge Netflix or Hulu in a blanket-fort)
5/18 - Test ALL THE THINGS
5/19-5/22 - Fine Tune the product.
5/23-5/27 - See if I can add some of the advanced ideas.

**PRESENT...**
```

## ¯\\_(ツ)_/¯

Class Whatever, am I right?

## Features

As a student or remote worker, I want to be able to find locations that are close to home/dorm, comfortable and not crowded, with access to Wi-Fi, light snacks, and power supplies.

As a person seeking locations for business meetings, I want to be able to find locations that are able to handle possibly larger groups of people, possibly have seperate seating areas, and the ability to address specific needs.

As a Restaurant, I want to be able to make myself known to Users, be able to show what we offer, and be able to monitor comments and reviews.

## Data Models ## ((I wish I knew how to draw))

Users types are split into General User and Restaurant as follows:

```
        []      User
                        *Name (First and Last....  is that needed?)
                        *User Name(Email Address)
                        *Password
                        *Email address (Which can be used for Log-In)
        []      Restaurant
                        *Restaurant Name
                        *Address
                        *Phone Number
                        *Hours
                        *Capacity
                        *Website
                        *Price Range
                        *Radio-Buttons to show what we can "provide"
```

Survey Models are as follows :

```
        *Tables/Seating/Standing
        *Power Outlets
        *Noise
        *Food
        *Service
        *Handicap Accessability
        *Bathroom Cleanliness
        *TBD
        *Added Perks
```

## MVP Plan:

```
[x]  Create the framework
[]  Create Website
[x]  Create Database
[x]  Create Fillable Forms
[x]  Create Sign-in Pages
[x]  Find and Create APIs
        []      Research Google Maps API
        []      Research a few other APIs (Forgot their names)
[x]  Create Comments Page
[]  Select appropriate colors, pictures, and Icons for page
[]  Create pseudo-locations or select a handful to test
[]  User Survey for Restaurant
[]  Apply Rating System
[]  Apply Keywords in Search Options and Results
```

## Advanced Plans:

```
[]  Create Curation/Favorites option
[]  Ensure Mobile-Friendliness
[]  Create Roulette option (Picks a restaurant within a distance range)
[]  Add API to show how busy a location is
[]  Add Pop-up alerts
[]  Add a Colorblind option
[]  Have Icons change color based on rating
[]  Add Google/Facebook/LinkedIn Verification?
[]  Add Role Verification? (Have me contact them?  Create Test?)
```

## Thoughts and Maybes

```
[]  Overall Rank (Should that be case by case or auto-cumulative of other scores?)
[]  Should I add Terms and Conditions in the future?
[]  TBD
[]  Create a button/link/whatever that leads to a Location creation page, and hide it if they don't have that checkbox?
[]  Add Tags to assist Search
```
