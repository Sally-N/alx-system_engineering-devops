# 0x0A. Configuration management

## Description
This project is an introduction to Configuration Management, as part of the first year curriculum of Holberton School.
This project contains very basic Puppet manifests.

## Resources
### Read or watch:

 - Intro to Configuration Management
 - Puppet resource type: file (check “Resource types” for all manifest types in the left menu)
 - Puppet’s Declarative Language: Modeling Instead of Scripting
 - Puppet lint
 - Puppet emacs mode

## Requirements
### General
 - All your files will be interpreted on `Ubuntu 20.04 LTS`
 - All your files should end with a new line
 - A `README.md` file at the root of the folder of the project is mandatory
 - Your Puppet manifests must pass `puppet-lint` `version 2.1.1` without any errors
 - Your Puppet manifests must run without error
 - Your Puppet manifests first line must be a comment explaining what the Puppet manifest is about
 - Your Puppet manifests files must end with the extension `.pp`
 
## Table of contents
Files | Description
----- | -----------
[0-create_a_file.pp](./0-create_a_file.pp) | Puppet manifest that creates a file `school` in the `/tmp` directory
[1-install_a_package.pp](./1-install_a_package.pp) | Puppet manifest that installs `flask` `v2.1.0` using `pip3`
[2-execute_a_command.pp](./2-execute_a_command.pp) | Puppet manifest that kills a process named `killmenow`
[killmenow](./killmenow) | Test bash script to kill with manifest `2-execute_a_command.pp`
