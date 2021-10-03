# Alchemy

Alchemy is a package manager that aims to utilise already-existing package managers (APT/DPKG, RPM/YUM/DNF, pacman, etc.) to create a unified package manager, regardless of Linux distribution. It uses both package managers and set-up scripts to automate installation tasks.

## How does Alchemy work?

Alchemy uses an architecture that is similar to APT- and YUM-based systems. It utilises repositories with specific instructions to install and/or build packages, along with configuring them. However, Alchemy is designed to be distribution-agnostic - meaning that it can be used on any Linux distribution as long as a repository is available for it.

Alchemy "packages" are really just build scripts - similar to the AUR (Arch User Repository) - that install and/or build software. They are not actually packages with binaries, but rather a set of instructions for how to install/build a package. While Alchemy depends on already-existing foundations for installing software, it itself does not depend on a specific foundation. Thus, Alchemy can be used on any Linux distribution, allowing for a unified CLI across all systems.

## How can I contribute?

We're looking for active contributors to help with maintaining the repositories and the command line tool itself. If you're interested in helping out, see [our repository](https://github.com/DanningtonSystems/alchemy) to begin contributing to the project!
