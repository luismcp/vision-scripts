## Project Structure

Both `final-dataset.py` and `separate-images.py` require the same scaffolding to work properly:

```
/Foo
    /data
        /images
            /train
        /labels
            /train
    final-dataset.py
    separate-images.py
```

## Configuration

You only need to set two (or one) variables at the top of each script:

- `DIRS`: the directories names (or name) that contains the images of the scrap pieces and their labels (for example, the dataset exported from CVAT).
- `FINAL_DIR`: the name you want for the output directory.

```python
DIRS = ['data', 'new-data']
FINAL_DIR = 'final'
```

The `INITIAL_DIR` directory must contain the `images` and `labels` subfolders, as shown in the structure above.

The result is a unique directory with all labeled images and their respective labels.