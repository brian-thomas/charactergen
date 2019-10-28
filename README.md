# Random D&D Character Generator

By Ramanan Sivaranjan, 2012—
Tweaks by Brian THomas, 2018-


## Introduction

This is a small web application for generating random D&D characters. The
default is to create Basic (Moldvay) D&D characters, but it can generate a
variety of characters based on various systems similar to Basic D&D: Original
D&D, Holmes, etc.

## Supported Systems

- Abstract D&D Character
    - [Little Brown Books][lbb] (1974 Original D&D)
        - [Carcosa][]
        - [Masters of Carcosa!][moc] (my Carcosa game)
        - [Apollyon][]
        - [Pahvelorn][]
        - [Delving Deeper][dd]
    - [Holmes] D&D
    - [Basic][] D&D (Mentzer / Moldvay)
        - [Lamentations of the Flame Princess][lotfp]
- [Danger Time][dangertime]
- [Adventure Game][adventuregame]
- [Fifth Edition][5e] D&D (Incomplete)

You can also generate a list of [NPCs][] and roll [3d6 in order][3d6] or [4d6 drop the lowest][4d6].

## Getting it Running

1. Install Flask (`pip install flask`). 
2. Run `python charactergen/server.py`

## How It Works

This is a Flask web application. `create.py` is the flask app, which does all
the routing. `characterclass.py` contains data and tables about various D&D
systems and that sort of thing. `character.py` is where the magic happens. All
the generators live here. They are assembled by inheriting from more generic
chunks of code, mixing in features as needed. I'm still undecided if this is
the best way to do this or not. The project has sort of grown organically over
time, and I'm not sure I made the best choices. It has allowed me to make
several tweaked generators for friends for their particular house-ruled games,
which has been nice.

The generate for the fifth edition characters works slightly differently. It
takes a runs an incomplete character through a series of processors that add
more and more information to the character. I'm not sure this scheme works that
well either.


[lbb]: http://character.totalpartykill.ca/lbb/
[carcosa]: http://character.totalpartykill.ca/carcosa/
[moc]: http://character.totalpartykill.ca/moc/
[apollyon]: http://character.totalpartykill.ca/apollyon/
[pahvelorn]: http://character.totalpartykill.ca/pahvelorn/
[dd]: http://character.totalpartykill.ca/dd/
[holmes]: http://character.totalpartykill.ca/holmes/
[basic]: http://character.totalpartykill.ca/basic/
[lotfp]: http://character.totalpartykill.ca/lotfp/
[5e]: http://character.totalpartykill.ca/5e/
[dangertime]: http://character.totalpartykill.ca/dangertime/
[adventuregame]: http://character.totalpartykill.ca/adventuregame/
[npcs]: http://character.totalpartykill.ca/npcs/
[3d6]: http://character.totalpartykill.ca/3d6/
[4d6]: http://character.totalpartykill.ca/4d6/
