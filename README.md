# lazylib_preprocessing
Autmatic updating IDv1 and IDv2 tags on mp3-files for LazyLibrarian to allow direct import to Plex

#### Requirements
* [kid3-cli](https://kid3.sourceforge.io/), needs to be added to path
* [LazyLibrarian](https://lazylibrarian.gitlab.io/) duh
* [Plex](https://www.plex.tv/media-server-downloads/), or another media/audiobook streamer
  - I recommend [Audiobooks.bundle](https://github.com/macr0dev/Audiobooks.bundle) to use with Plex

#### What does it do?
* Fix broken IDv tags, cleans up garbage in tags
* Set IDv-tag title as part of total parts
* Set IDv-tag artist as book author
* Set IDv-tag album as book title
* Set IDv-tag track as part number

