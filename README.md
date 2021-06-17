# Garage Band with OOP

## Links & Resourdes

- [Lab 4 Pull Request]()

## Overview

Create a Garage Band with Object Oriented Programming.

## Feature Tasks and Requirements

Use Python classes to model a Band made up of different kinds of musicians.

Start with Guitarist,Bassist, and Drummer.

Make use of a Musician base class to handle common functionality which particular kinds of musicians will inherit.

### User Acceptance Test

Unit tests will be supplied. Make them pass. Do NOT modify the supplied tests.

#### Band Tests

- A Band instance should have a name attribute which is a string.
- A Band instance should have a members attribute which is a list of instances that inherit from Musician base (or super) class.
- A Band instance should have a play_solos method that asks each member musician to play a solo, in the order they were added to band.
- A Band instance should have appropriate **str** and **repr** methods.
- A Band should have a class method to_list which returns a list of previously created Band instances

#### Musician Subclass Tests

- Each kind of Musician instance should have appropriate **str** and **repr** methods.
- Each kind of Musician instance should have a get_instrument method that returns string.
- Each kind of Musician instance should have a play_solo method that returns string.
