import fiftyone as fo

if __name__ == "__main__":

    dataset = fo.Dataset.from_dir(
        dataset_dir="/data/",
        dataset_type=fo.types.YOLOv5Dataset,
        split="train",
        name="my-dataset-name",
        label_field="ground_truth",
    )

    dataset = fo.Dataset.from_dir(
        dataset_dir="/data/",
        dataset_type=fo.types.YOLOv5Dataset,
        split="val",
        name="my-dataset-2",
        label_field="ground_truth",
    )

    session = fo.launch_app(dataset, port=5151, address="0.0.0.0")
    dataset.persistent = True
    session.wait()
