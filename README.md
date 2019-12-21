# DynamicMenus

[中文README](Chinese.md)

## Features

- Translate words and sentences, and prettily display results, copy results or replace original content with translation.
   ![Translator - Default](screenshots/translator-default.png)

- Open browser, search selected words with customized list of search engines.
   ![Search Online](screenshots/searchonline.png)

- Right-click to open other files in the current directory.
   ![Open files](screenshots/openfiles.png)


## Key binding
- Shortcuts for translating the word next to the cursor or selected sentences.
<kbd>ctrl+shift+y</kbd>


## Advanced

To improve the level of translation results, you should go [HERE](https://ai.youdao.com/) to register and obtain a app-key for youdao dict, then fill them in the Settings file. Youdao will give you the balance of `￥100` first.

You can find a lot about this on the Internet

The folloing image shows a sample of translation with `app-key`, you can see the difference between the above translation(without 'app-key') and it.
![Translator - Enhanced](screenshots/translator.png)


## TODO
- [x] `Preprocess` translation content.
- [x] `Copy` translation results.
- [x] `Replace` original content with translation.
- [ ] Added copy and replace button for `explains`.
- [ ] Create `shortcuts` to copy and replace.
- [ ] Improve the showing of results.
- [ ] Consider to cache translation results.
- [ ] A shortcut to open other files in the current directory;
- [ ] Consider whether these three features should be separated into three separate plug-ins and enhanced.
