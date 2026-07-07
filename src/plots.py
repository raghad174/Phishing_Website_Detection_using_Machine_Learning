import matplotlib.pyplot as plt
from sklearn.metrics import (
    confusion_matrix,
    ConfusionMatrixDisplay,
    roc_curve,
    auc,
    precision_recall_curve,
    average_precision_score
)


def plot_confusion_matrix(y_true, y_pred, model_name):
    cm = confusion_matrix(y_true, y_pred)

    display = ConfusionMatrixDisplay(confusion_matrix=cm)

    display.plot()

    plt.title(f"{model_name} Confusion Matrix")

    plt.show()


def plot_roc_curve(y_true, model_scores):
    plt.figure(figsize=(9, 7))

    for model_name, scores in model_scores:
        fpr, tpr, _ = roc_curve(y_true, scores)
        roc_auc = auc(fpr, tpr)

        plt.plot(
            fpr,
            tpr,
            label=f"{model_name} (AUC = {roc_auc:.3f})"
        )

    plt.plot([0, 1], [0, 1], linestyle="--", color="black")

    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC Curve Comparison")
    plt.legend(bbox_to_anchor=(1.02, 1), loc="upper left", fontsize=9)
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()


def plot_precision_recall_curve(y_true, model_scores):
    plt.figure(figsize=(9, 7))

    for model_name, scores in model_scores:
        precision, recall, _ = precision_recall_curve(y_true, scores)
        pr_auc = average_precision_score(y_true, scores)

        plt.plot(
            recall,
            precision,
            label=f"{model_name} (AUC = {pr_auc:.3f})"
        )

    plt.xlabel("Recall")
    plt.ylabel("Precision")
    plt.title("Precision-Recall Curve Comparison")
    plt.legend(bbox_to_anchor=(1.02, 1), loc="upper left", fontsize=9)
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()


def plot_threshold_analysis(y_true, model_scores):
    for metric_name in ["Precision", "Recall"]:
        plt.figure(figsize=(8, 6))

        for model_name, scores in model_scores:
            precision, recall, thresholds = precision_recall_curve(
                y_true,
                scores
            )

            if metric_name == "Precision":
                values = precision[:-1]
            else:
                values = recall[:-1]

            plt.plot(
                thresholds,
                values,
                label=model_name
            )

        plt.xlabel("Decision Threshold")
        plt.ylabel(metric_name)
        plt.title(f"{metric_name} vs Decision Threshold")
        plt.legend()
        plt.grid(alpha=0.3)
        plt.tight_layout()
        plt.show()
