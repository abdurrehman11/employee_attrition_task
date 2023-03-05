from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score


class Evaluate:
    def __init__(self, y_true, y_pred_prob, threshold=0.5):
        self.y_true = y_true
        self.y_pred_prob = y_pred_prob
        self.threshold = threshold

    def get_evaluation_metrics(self):
        y_pred = self.y_pred_prob >= self.threshold

        accuracy = accuracy_score(self.y_true, y_pred)
        precision = precision_score(self.y_true, y_pred)
        recall = recall_score(self.y_true, y_pred)
        f1 = f1_score(self.y_true, y_pred)
        roc_auc = roc_auc_score(self.y_true, self.y_pred_prob)

        return {
            "accuracy": accuracy, 
            "precision": precision, 
            "recall": recall, 
            "f1": f1, 
            "roc_auc": roc_auc
        }
