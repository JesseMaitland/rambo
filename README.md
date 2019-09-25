# Rambo
#### A few helpful tools for creating terminal applications

Rambo is a collection of methods to help with mapping terminal program arguments to python actions / functions

Getting started
`pip install rambo-py`

creating a project
`rambo init project`

This will create a directory called `actions` as well as a file called `rambo.yml` which functions both at the terminal
config file, and mapper configuration

Example `rambo.yml`

```
commands:
  action:
    help: "available options for the rambo action argument"
    choices:
      - init
      - delete
  object:
    help: "available options for the rambo object argument"
    choices:
      - project
      - file
```

Rambo commands follow the pattern of `action -> object` where the action argument will be performed on the 
provided object. in the above example the following combinations are valid
```
init project
init file
delete project
delete file
```

these argument combinations can be mapped to `actions` which are python functions. Rambo will map these valid combinations
to functions of the same name.


## Rambo Decorators

Rambo provides handy decorator methods to access the passed in cmd arguments, 





