## Task 2: Work out of a Github repo

Create a Github repo for this homework and check it out to your EC2 where you can work on it. Setup your Github account and EC2 to use key-based authentication (there’s a video I’ll post showing how this is done).

## Task 3: Explore My Little Pony Dataset Properties

We’ll be using the dataset available here: https://www.kaggle.com/liury123/my-little-pony-transcript
For the purpose of this study, we’ll use only clean_dialog.csv and assume that the dataset is perfect.
Using standard command line tools (e.g., head, more, grep) and csvtool, explore the clean_dialog.csv. Use the command line tools to answer the following questions:
-	How big is the dataset? 

    **4.7 mb and 36859 lines**
    
    Commands used:
    ```bash
    ls -lh clean_dialog.csv
    wc -l clean_dialog.csv
    ```

-	What’s the structure of the data? (i.e., what are the field and what are values in them)

    The dataset contains four fields:

    - `title`: title of the episode
    - `writer`: writer of the episode
    - `pony`: character(s) speaking the line
    - `dialog`: spoken dialogue

    Commands used:

    ```bash
    head -n 1 clean_dialog.csv
    csvtool col 1 clean_dialog.csv | head -n 5
    csvtool col 2 clean_dialog.csv | head -n 5
    csvtool col 3 clean_dialog.csv | head -n 5
    csvtool col 4 clean_dialog.csv | head -n 5
    ```
 
-	How many episodes does it cover?

    **197**
    
    Commands used:
    ```bash
    csvtool col 1 clean_dialog.csv | tail -n +2 | sort | uniq | wc -l
    ```

-	During the exploration phase, find at least one aspect of the dataset that is unexpected – meaning that it seems like it could create issues for later analysis.

    **The dialogue was collected using voice recognition software, which may introduce errors by transcribing words as similarly pronounced words with different meanings**

## Task 4: Analyze speaker frequency
    

**Twilight Sparkle: 4749**
**Rarity: 2660**
**Pinkie Pie: 2833**
**Rainbow Dash: 3072**
**Fluttershy: 2109**

Commands used:

```bash
    grep '"name of pony"' clean_dialog.csv | grep -v ',"name of pony","
    csvtool col 3 clean_dialog.csv | grep -xc "name of pony"
```
**First code could contain dialogues match the pattern**

Now calculate the percent of lines that each pony has over the entire dataset (including all characters).
## Task 5: Commit your work


