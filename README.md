# Knight

Kenan's Novel Intelligent en(G)lish Helper Tool for Cottage Acquisition Scales for Listening Language & Speech

## Supported Levels (Fifth Edition):

- [ ] Pre-Verbal
- [ ] Pre-Sentence
- [x] Simple Sentence
- [ ] Complex Sentence

## Supported Acquisition Scales

- [ ] Cognition/Play
- [ ] Listening
- [ ] Conversation
- [x] Nouns & Noun Modifiers
- [x] Prepositions & Pronouns
- [x] Verbs & Modals
- [x] Tense & Negation
- [x] Emerging Complexity
- [x] Questions

## Supported Age Ranges

- [x] 24-30 months
- [x] 30-36 months
- [x] 36-42 months
- [x] 42-48 months

## Installation and Usage

1. Download the latest zip file from the [releases tab](https://github.com/KenanTurner/caslls-knight/releases)
2. Unzip the file to a safe location
3. Navigate to the unzipped folder
4. Double click *Knight.exe* to launch the program
5. Windows will warn you against running the program. Click *More info* and then *Run anyway*
6. To exit, type ctrl-c

## Tips

- *TODO* indicates the developer has not yet implemented the feature (likely because the developer doesn't understand CASLLS very well)
- Help mode can be activated by typing *help*
- Right click on *knight.exe* and click *Send to > Desktop* to create a shortcut
- All sessions are stored as *history-YYYY-MM-DD.txt* inside the *knight* folder

## Bugs and issues

If you have any issues or would like to report a bug, notify the developer over email and text
For email, please put *[BUG/ISSUE]* in the subject line and include a zip of all *history-YYYY-MM-DD.txt* and *debug.log*

## Developers

1. Clone the repository
2. Install the required packages
```bash
pip install -r requirements.txt
```
3. Create a distributable with pyinstaller
```bash
pyinstaller ./knight.spec --clean
```

## License

[Mozilla Public License Version 2.0](/LICENSE)