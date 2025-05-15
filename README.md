Better Serato USB export. Beats Serato's sync by putting all files in 1 folder (without duplicates) and only copying changed files, unlike Serato's sync which takes forever and creates many duplicate file locations

_Currently designed for Python 3.12+. If you would like backwards compatibility with an older version, please reach out!_

# Installation

```cmd
pip install serato-usb-export
```

# Usage

**NOTE: replaces existing crates on flash drive! (but does not delete existing track files) (TODO: ability to merge with existing)**

**Windows**

```cmd
serato_usb_export --drive E --crate_matcher *house* *techno* --root_crate="Dave USB"
```

**Mac**

```cmd
serato_usb_export --drive "/Volumes/MY_USB/" --crate_matcher *house* *techno* --root_crate="Dave USB"
```

**Linux**

```cmd
serato_usb_export --drive "/media/dave/MY_USB/" --crate_matcher *house* *techno* --root_crate="Dave USB"
```

`root_crate` is 


**Arguments**

_See argument usage:_  `serato_usb_export --help`


`-d, --drive, --drive_dir`

Directory of the destination drive. Example: "E" on Windows

`-c, --crates, --crate_matcher`

Glob or Regex matcher for crate and smartcrate filenames. Example: "\*house\*". Can pass multiple to OR them. To copy all, pass "\*"

`--root_crate`

Not required, but is nice when plugging your drive into another DJ's laptop. Sets all crates to be within this crate on the destination drive

### Contributing / Issues

_This is a wrapper of my [serato-tools](https://github.com/bvandercar-vt/serato-tools) package. Please open issues and contribute there._