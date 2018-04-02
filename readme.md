# Bear to Dropbox Paper Migration Tool

I really liked Bear, but I also sometimes need to access notes on other
computers.  This tool will migrate exported Bear (markdown format)
notes into Paper.

## Install

Install from PyPi:

```
pip install bear-to-paper
```

or from a clone of this repository:

```
pip install .
```

## Instructions

First, you'll need to get a Dropbox access token:

1. Go to https://www.dropbox.com/developers/apps/create.
    1. Select "Dropbox API" as your API selection.
    2. Select "Full Dropbox" as the access level.
    3. Enter a name for your new app -- I chose "Bear to Paper".
2. You'll then be shown the app configuration page.
    1. Click "Generate access token"
    2. Save this token somewhere.  You'll be asked for this again
       when you start the migration process

Then, you can migrate your notes:

```
bear-to-paper /path/to/exported/markdown/file
```

Enter your Dropbox Access Token when asked, and wait for your notes and
their attachments to be uploaded and converted into Paper documents.
