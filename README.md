## Project Structure

Both `final-dataset.py` and `separate-images.py` require the same scaffolding to work properly:

```
/Foo
    /data
        /images
        /labels
    final-dataset.py
    separate-images.py
```

## Configuration

You only need to set two (or one) variables at the top of each script:

- `INITIAL_DIR`: the name of the directory that contains the images of the scrap pieces and their labels (for example, the dataset exported from CVAT).
- `FINAL_DIR`: the name you want for the output directory.

```python
INITIAL_DIR = 'data'
FINAL_DIR = 'final'
```

The `INITIAL_DIR` directory must contain the `images` and `labels` subfolders, as shown in the structure above.
