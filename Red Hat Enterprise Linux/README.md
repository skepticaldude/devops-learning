# Linux File Management Fundamentals (RHEL)
In this module, I learned how to navigate and manage a Linux file system using the command line.

## 1. Navigation & Inspection

pwd: Print Working Directory—knowing exactly where you are in the file system.

ls: List directory contents.

ls -l: View detailed file information (permissions, owners, size).

ls -a: Show hidden files (those starting with a .).

ls -R: Recursive listing to see files inside subdirectories.

## 2. File & Directory Operations

cd: Change directories to navigate the system.

mkdir: Create new directories.

touch: Create empty files or update timestamps.

cp: Copy files or directories (-r for folders).

mv: Move or rename files and folders.

rm: Remove files (-r for folders). I also learned that rmdir is a safer way to delete only empty directories.

## 3. Links (Aliases)

Hard Links: Create a second name for the same data on the disk.

Symbolic (Soft) Links: Create a shortcut or pointer to another file using ln -s.

## 4. Shell Expansions (Power User Techniques)

Globbing: Use * (multi-char), ? (single-char), and [] (ranges) to select groups of files.

Brace Expansion: Efficiently create or list items like file{1..3}.txt or report_{jan,feb}.log.

Tilde Expansion: Using ~ as a shortcut for the home directory.

Variable Expansion: Storing and using data in variables like $MY_DIR.

Command Substitution: Using the output of one command inside another, such as touch log_$(date +%F).txt.

## 5. Quoting & Protection

Escaping (\): Preventing the shell from interpreting special characters.

Single Quotes (' '): Strong quoting—the shell ignores all special characters inside.

Double Quotes (" "): Weak quoting—allows variables and command substitution while treating most other characters as literal text.
