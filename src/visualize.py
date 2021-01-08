import matplotlib.pyplot as plt


def display_dataset(train_dataset):
    for example, label in train_dataset.take(1):
        print("Texts: ", example.numpy()[:3])
        print()
        print("Labels: ", label.numpy()[:3])


def display_results(test_loss, test_acc, history):
    def plot_graphs(metric):
        plt.plot(history.history[metric])
        plt.plot(history.history["val_" + metric], '')
        plt.xlabel("Epochs")
        plt.ylabel(metric)
        plt.legend([metric, "val_" + metric])

    print("Test Loss: {}".format(test_loss))
    print("Test Accuracy: {}".format(test_acc))

    plt.figure(figsize=(16, 8))

    plt.subplot(1, 2, 1)
    plot_graphs("accuracy")
    plt.ylim(None, 1)

    plt.subplot(1, 2, 2)
    plot_graphs("loss")
    plt.ylim(0, None)
