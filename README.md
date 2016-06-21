This is yet another tool for image annotation based on PyQt4. Check this [video](https://youtu.be/kmqAVtwIE2Y) on how to use.

#### Usage

0. Start: `python annotaMain.py`

1. Load images (click *Open* button), options:
    + **Image**: you can select one or multiple images
    + **Image Folder**: select all the images inside a folder
    + **Video**: not implemented yet, need to label the first frame and then use tracking methods to get continuous annotations in the following frames
    + **Cam**: not implemented yet, save as **Video**

2. Select the task: a task is a group of categories to be annotated in this task, it is specified in *configs/tasks* file.

3. Load label/annotation: if you are continuing from an unfinished annotation task, you should first load the annotation (click *Load Label* button). 

4. Annotate:
    + **select label**: click the row corresponding to the label to be annotated
    + **annotate**: left click and drag a rectange
    + **zoom in/out**: wheel up/down
    + **select rectangle**: left click the edge of a rectangle. *the edge width can be very thin if image has high resolution, you can zoom in first so that it is easier to annotate and select*
    + **remove/redo/undo**: click those buttons to remove/redo/undo
    + **jump to an image**: other than click *prev/next* for iterating images, you can drag the *scroll bar* to jump to the image you are interested

5. Save label/annotation: you can either click *Save Label*, or check *Autosave*. If *Autosave* checked, it will overwrite the old annotation file (if there are change's in current image's annotation) when switch to another image, but this may decrease the responsiveness when switch to another image, so it's better to click *Save Label* by yourself.

6. Saved annotation example:

```csv
image,cateid,tlx,tly,width,height
0004.jpg,1.0,2883.65739439,1566.96084343,1067.43225848,1270.47424999
0004.jpg,1.0,1493.12739197,1622.33593202,907.45978033,1282.77982523
0005.jpg,1.0,278.0,214.0,27.0,41.0
```
