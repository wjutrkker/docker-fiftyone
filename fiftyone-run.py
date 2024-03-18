import fiftyone as fo

if __name__ == "__main__":


    print(fo.list_datasets())
    datasets = ["my-dataset", "my-other-dataset"]
    for value in datasets:
        print(value)
        if value in fo.list_datasets():
            dataset=fo.load_dataset(value) 
            dataset.delete() 
    else:
        dataset = fo.Dataset.from_dir(
            dataset_dir="/data/yolo-example",
            dataset_type=fo.types.YOLOv5Dataset,
            split="train",
            name="my-dataset",
            label_field="ground_truth",
        )

        dataset = fo.Dataset.from_dir(
            dataset_dir="/data/yolo-example",
            dataset_type=fo.types.YOLOv5Dataset,
            split="val",
            name="my-other-dataset",
            label_field="ground_truth",
        )

    session = fo.launch_app(dataset, port=5151, address="0.0.0.0")
    dataset.persistent = True

    session.wait()
